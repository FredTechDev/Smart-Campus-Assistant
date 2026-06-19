"""Data preprocessing utilities for ML pipeline"""

from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from ml.src.utils import log_error, log_info, log_warning


class DataPreprocessor:
    """Data preprocessing and cleaning utilities"""

    def __init__(self):
        """Initialize preprocessor"""
        self.standard_scaler = None
        self.minmax_scaler = None
        self.feature_names = None

    @staticmethod
    def check_missing_values(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
        """
        Identify columns with missing values
        
        Args:
            df: Input DataFrame
            threshold: Threshold for missing value percentage
            
        Returns:
            DataFrame with missing value statistics
        """
        missing_stats = pd.DataFrame({
            "column": df.columns,
            "missing_count": df.isnull().sum().values,
            "missing_percentage": (df.isnull().sum().values / len(df) * 100).round(2),
        })
        
        missing_stats = missing_stats.sort_values("missing_percentage", ascending=False)
        
        high_missing = missing_stats[missing_stats["missing_percentage"] > threshold * 100]
        if len(high_missing) > 0:
            log_warning(f"Found {len(high_missing)} columns with >50% missing values")
        
        return missing_stats

    @staticmethod
    def handle_missing_values(
        df: pd.DataFrame,
        strategy: str = "mean",
        columns: Optional[List[str]] = None,
    ) -> pd.DataFrame:
        """
        Handle missing values
        
        Args:
            df: Input DataFrame
            strategy: 'mean', 'median', 'forward_fill', 'backward_fill', or 'drop'
            columns: Specific columns to handle (None = all)
            
        Returns:
            DataFrame with missing values handled
        """
        df_clean = df.copy()
        cols_to_process = columns if columns else df_clean.columns
        
        for col in cols_to_process:
            if col not in df_clean.columns:
                continue
            
            missing_count = df_clean[col].isnull().sum()
            if missing_count == 0:
                continue
            
            if strategy == "mean":
                df_clean[col].fillna(df_clean[col].mean(), inplace=True)
            elif strategy == "median":
                df_clean[col].fillna(df_clean[col].median(), inplace=True)
            elif strategy == "forward_fill":
                df_clean[col].fillna(method="ffill", inplace=True)
            elif strategy == "backward_fill":
                df_clean[col].fillna(method="bfill", inplace=True)
            elif strategy == "drop":
                df_clean = df_clean.dropna(subset=[col])
            
            log_info(f"Filled {missing_count} missing values in '{col}' using {strategy}")
        
        return df_clean

    @staticmethod
    def remove_duplicates(df: pd.DataFrame, subset: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Remove duplicate rows
        
        Args:
            df: Input DataFrame
            subset: Columns to consider for identifying duplicates
            
        Returns:
            DataFrame with duplicates removed
        """
        initial_rows = len(df)
        df_clean = df.drop_duplicates(subset=subset)
        removed_rows = initial_rows - len(df_clean)
        
        if removed_rows > 0:
            log_info(f"Removed {removed_rows} duplicate rows")
        
        return df_clean

    @staticmethod
    def remove_outliers(
        df: pd.DataFrame,
        columns: List[str],
        method: str = "iqr",
        threshold: float = 1.5,
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Remove outliers using IQR or Z-score method
        
        Args:
            df: Input DataFrame
            columns: Columns to check for outliers
            method: 'iqr' or 'zscore'
            threshold: IQR multiplier (1.5) or Z-score threshold (3)
            
        Returns:
            Tuple of (cleaned DataFrame, outliers DataFrame)
        """
        df_clean = df.copy()
        outlier_mask = pd.Series([False] * len(df))
        
        for col in columns:
            if col not in df.columns:
                log_warning(f"Column '{col}' not found")
                continue
            
            if method == "iqr":
                Q1 = df_clean[col].quantile(0.25)
                Q3 = df_clean[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                col_outliers = (df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)
            
            elif method == "zscore":
                z_scores = np.abs((df_clean[col] - df_clean[col].mean()) / df_clean[col].std())
                col_outliers = z_scores > threshold
            
            outlier_mask |= col_outliers
        
        outliers = df_clean[outlier_mask]
        df_clean = df_clean[~outlier_mask]
        
        if len(outliers) > 0:
            log_info(f"Removed {len(outliers)} outlier rows")
        
        return df_clean, outliers

    @staticmethod
    def encode_categorical(
        df: pd.DataFrame,
        columns: List[str],
        method: str = "label",
    ) -> Tuple[pd.DataFrame, dict]:
        """
        Encode categorical variables
        
        Args:
            df: Input DataFrame
            columns: Categorical columns to encode
            method: 'label' for label encoding or 'onehot' for one-hot encoding
            
        Returns:
            Tuple of (encoded DataFrame, encoding mapping)
        """
        df_encoded = df.copy()
        encoding_map = {}
        
        for col in columns:
            if col not in df.columns:
                log_warning(f"Column '{col}' not found")
                continue
            
            if method == "label":
                unique_values = df_encoded[col].unique()
                encoding = {val: idx for idx, val in enumerate(unique_values)}
                df_encoded[col] = df_encoded[col].map(encoding)
                encoding_map[col] = encoding
                log_info(f"Label encoded '{col}' with {len(encoding)} unique values")
            
            elif method == "onehot":
                one_hot = pd.get_dummies(df_encoded[col], prefix=col)
                encoding_map[col] = one_hot.columns.tolist()
                df_encoded = pd.concat([df_encoded, one_hot], axis=1)
                df_encoded = df_encoded.drop(col, axis=1)
                log_info(f"One-hot encoded '{col}' into {len(one_hot.columns)} features")
        
        return df_encoded, encoding_map

    def standardize_features(
        self,
        df: pd.DataFrame,
        columns: Optional[List[str]] = None,
        fit: bool = True,
    ) -> pd.DataFrame:
        """
        Standardize numerical features (zero mean, unit variance)
        
        Args:
            df: Input DataFrame
            columns: Columns to standardize (None = all numeric)
            fit: Whether to fit the scaler
            
        Returns:
            DataFrame with standardized features
        """
        df_scaled = df.copy()
        
        if columns is None:
            columns = df_scaled.select_dtypes(include=[np.number]).columns.tolist()
        
        if fit:
            self.standard_scaler = StandardScaler()
            df_scaled[columns] = self.standard_scaler.fit_transform(df_scaled[columns])
            self.feature_names = columns
            log_info(f"Fitted and standardized {len(columns)} features")
        else:
            if self.standard_scaler is None:
                log_error("Scaler not fitted. Call with fit=True first.")
                return df
            df_scaled[columns] = self.standard_scaler.transform(df_scaled[columns])
            log_info(f"Transformed {len(columns)} features")
        
        return df_scaled

    def normalize_features(
        self,
        df: pd.DataFrame,
        columns: Optional[List[str]] = None,
        fit: bool = True,
        feature_range: Tuple[int, int] = (0, 1),
    ) -> pd.DataFrame:
        """
        Normalize features to a range (default 0-1)
        
        Args:
            df: Input DataFrame
            columns: Columns to normalize (None = all numeric)
            fit: Whether to fit the scaler
            feature_range: Target range
            
        Returns:
            DataFrame with normalized features
        """
        df_scaled = df.copy()
        
        if columns is None:
            columns = df_scaled.select_dtypes(include=[np.number]).columns.tolist()
        
        if fit:
            self.minmax_scaler = MinMaxScaler(feature_range=feature_range)
            df_scaled[columns] = self.minmax_scaler.fit_transform(df_scaled[columns])
            self.feature_names = columns
            log_info(f"Fitted and normalized {len(columns)} features to {feature_range}")
        else:
            if self.minmax_scaler is None:
                log_error("Scaler not fitted. Call with fit=True first.")
                return df
            df_scaled[columns] = self.minmax_scaler.transform(df_scaled[columns])
            log_info(f"Transformed {len(columns)} features")
        
        return df_scaled

    @staticmethod
    def create_features(
        df: pd.DataFrame,
        feature_definitions: dict,
    ) -> pd.DataFrame:
        """
        Create new features from existing ones
        
        Args:
            df: Input DataFrame
            feature_definitions: Dictionary mapping new feature names to functions
                                Example: {'feature_name': lambda row: row['col1'] + row['col2']}
            
        Returns:
            DataFrame with new features
        """
        df_features = df.copy()
        
        for feature_name, func in feature_definitions.items():
            try:
                df_features[feature_name] = df_features.apply(func, axis=1)
                log_info(f"Created feature '{feature_name}'")
            except Exception as e:
                log_error(f"Error creating feature '{feature_name}': {str(e)}")
        
        return df_features

    @staticmethod
    def filter_data(
        df: pd.DataFrame,
        filters: dict,
    ) -> pd.DataFrame:
        """
        Filter data based on conditions
        
        Args:
            df: Input DataFrame
            filters: Dictionary mapping column names to conditions
                    Example: {'age': (18, 65), 'status': ['active', 'pending']}
            
        Returns:
            Filtered DataFrame
        """
        df_filtered = df.copy()
        
        for col, condition in filters.items():
            if col not in df_filtered.columns:
                log_warning(f"Column '{col}' not found for filtering")
                continue
            
            if isinstance(condition, tuple) and len(condition) == 2:
                # Range filter
                df_filtered = df_filtered[
                    (df_filtered[col] >= condition[0]) & (df_filtered[col] <= condition[1])
                ]
            elif isinstance(condition, list):
                # Multiple value filter
                df_filtered = df_filtered[df_filtered[col].isin(condition)]
            else:
                # Single value filter
                df_filtered = df_filtered[df_filtered[col] == condition]
        
        log_info(f"Filtered data from {len(df)} to {len(df_filtered)} rows")
        return df_filtered

    @staticmethod
    def get_data_types(df: pd.DataFrame) -> dict:
        """
        Get detailed data types information
        
        Returns:
            Dictionary with numeric and categorical columns
        """
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        return {
            "numeric": numeric_cols,
            "categorical": categorical_cols,
            "numeric_count": len(numeric_cols),
            "categorical_count": len(categorical_cols),
        }

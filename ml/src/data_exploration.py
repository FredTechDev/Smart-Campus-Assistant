"""Data exploration and analysis utilities"""

from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from ml.src.utils import log_info


class DataExplorer:
    """Explore and analyze data characteristics"""

    @staticmethod
    def basic_statistics(df: pd.DataFrame) -> pd.DataFrame:
        """
        Get basic statistics for numerical columns
        
        Args:
            df: Input DataFrame
            
        Returns:
            DataFrame with statistics
        """
        stats = df.describe(include=[np.number]).T
        log_info("Computed basic statistics")
        return stats

    @staticmethod
    def correlation_analysis(df: pd.DataFrame, numeric_only: bool = True) -> pd.DataFrame:
        """
        Analyze correlations between features
        
        Args:
            df: Input DataFrame
            numeric_only: Only analyze numeric columns
            
        Returns:
            Correlation matrix
        """
        if numeric_only:
            df_numeric = df.select_dtypes(include=[np.number])
        else:
            df_numeric = df
        
        correlation = df_numeric.corr()
        log_info(f"Computed correlation matrix for {len(correlation)} features")
        return correlation

    @staticmethod
    def distribution_analysis(df: pd.DataFrame, column: str) -> Dict:
        """
        Analyze distribution of a column
        
        Args:
            df: Input DataFrame
            column: Column name
            
        Returns:
            Dictionary with distribution info
        """
        if column not in df.columns:
            return {"error": f"Column '{column}' not found"}
        
        data = df[column]
        
        if pd.api.types.is_numeric_dtype(data):
            analysis = {
                "type": "numeric",
                "mean": data.mean(),
                "median": data.median(),
                "std": data.std(),
                "min": data.min(),
                "max": data.max(),
                "q1": data.quantile(0.25),
                "q3": data.quantile(0.75),
                "skewness": data.skew(),
                "kurtosis": data.kurtosis(),
            }
        else:
            analysis = {
                "type": "categorical",
                "unique_values": data.nunique(),
                "top_values": data.value_counts().to_dict(),
            }
        
        log_info(f"Analyzed distribution of '{column}'")
        return analysis

    @staticmethod
    def class_balance_analysis(df: pd.DataFrame, target_column: str) -> Dict:
        """
        Analyze class distribution
        
        Args:
            df: Input DataFrame
            target_column: Target column name
            
        Returns:
            Dictionary with class balance info
        """
        if target_column not in df.columns:
            return {"error": f"Column '{target_column}' not found"}
        
        value_counts = df[target_column].value_counts()
        proportions = (value_counts / len(df) * 100).round(2)
        
        analysis = {
            "counts": value_counts.to_dict(),
            "percentages": proportions.to_dict(),
            "imbalance_ratio": value_counts.max() / value_counts.min(),
        }
        
        log_info(f"Analyzed class balance for '{target_column}'")
        return analysis

    @staticmethod
    def feature_importance_analysis(
        df: pd.DataFrame,
        target_column: str,
        top_n: int = 10,
    ) -> pd.DataFrame:
        """
        Analyze feature importance using variance and correlation
        
        Args:
            df: Input DataFrame
            target_column: Target column name
            top_n: Number of top features to return
            
        Returns:
            DataFrame with feature importance scores
        """
        if target_column not in df.columns:
            return pd.DataFrame()
        
        # Get numeric columns only
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        numeric_cols = [col for col in numeric_cols if col != target_column]
        
        if target_column not in df.select_dtypes(include=[np.number]).columns:
            log_info("Target column is not numeric, using correlation analysis")
            return pd.DataFrame()
        
        # Calculate correlation with target
        correlations = df[numeric_cols].corrwith(df[target_column]).abs().sort_values(ascending=False)
        
        importance = pd.DataFrame({
            "feature": correlations.index,
            "correlation": correlations.values,
        }).head(top_n)
        
        log_info(f"Analyzed feature importance (top {top_n} features)")
        return importance

    @staticmethod
    def missing_pattern_analysis(df: pd.DataFrame) -> Dict:
        """
        Analyze patterns in missing data
        
        Args:
            df: Input DataFrame
            
        Returns:
            Dictionary with missing pattern analysis
        """
        missing_by_column = df.isnull().sum()
        missing_by_row = df.isnull().sum(axis=1)
        
        analysis = {
            "total_missing": missing_by_column.sum(),
            "missing_by_column": missing_by_column.to_dict(),
            "rows_with_missing": (missing_by_row > 0).sum(),
            "most_missing_column": missing_by_column.idxmax() if missing_by_column.max() > 0 else None,
            "missing_percentage": round(missing_by_column.sum() / (len(df) * len(df.columns)) * 100, 2),
        }
        
        log_info("Analyzed missing data patterns")
        return analysis

    @staticmethod
    def generate_summary_report(df: pd.DataFrame) -> str:
        """
        Generate a comprehensive data summary report
        
        Args:
            df: Input DataFrame
            
        Returns:
            Formatted summary report
        """
        report = f"""
        ========== DATA SUMMARY REPORT ==========
        
        Shape: {df.shape[0]} rows × {df.shape[1]} columns
        
        Data Types:
        {df.dtypes.value_counts().to_string()}
        
        Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB
        
        Missing Values:
        {df.isnull().sum().to_string()}
        
        Numeric Columns Statistics:
        {df.describe().to_string()}
        
        =========================================
        """
        
        log_info("Generated summary report")
        return report

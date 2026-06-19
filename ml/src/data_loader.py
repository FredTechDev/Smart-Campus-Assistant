"""Data loading utilities for ML pipeline"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd

from ml.src.utils import log_error, log_info, log_warning


class DataLoader:
    """Load data from various sources"""

    @staticmethod
    def load_csv(filepath: str, **kwargs) -> pd.DataFrame:
        """
        Load data from CSV file
        
        Args:
            filepath: Path to CSV file
            **kwargs: Additional arguments for pd.read_csv
            
        Returns:
            DataFrame containing the data
        """
        try:
            df = pd.read_csv(filepath, **kwargs)
            log_info(f"Loaded {len(df)} rows from {filepath}")
            return df
        except FileNotFoundError:
            log_error(f"File not found: {filepath}")
            raise
        except Exception as e:
            log_error(f"Error loading CSV {filepath}: {str(e)}")
            raise

    @staticmethod
    def load_excel(filepath: str, sheet_name: str = 0, **kwargs) -> pd.DataFrame:
        """
        Load data from Excel file
        
        Args:
            filepath: Path to Excel file
            sheet_name: Sheet name or index
            **kwargs: Additional arguments for pd.read_excel
            
        Returns:
            DataFrame containing the data
        """
        try:
            df = pd.read_excel(filepath, sheet_name=sheet_name, **kwargs)
            log_info(f"Loaded {len(df)} rows from sheet '{sheet_name}' in {filepath}")
            return df
        except FileNotFoundError:
            log_error(f"File not found: {filepath}")
            raise
        except Exception as e:
            log_error(f"Error loading Excel {filepath}: {str(e)}")
            raise

    @staticmethod
    def load_json(filepath: str) -> Any:
        """
        Load data from JSON file
        
        Args:
            filepath: Path to JSON file
            
        Returns:
            Loaded data
        """
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
            log_info(f"Loaded JSON data from {filepath}")
            return data
        except FileNotFoundError:
            log_error(f"File not found: {filepath}")
            raise
        except Exception as e:
            log_error(f"Error loading JSON {filepath}: {str(e)}")
            raise

    @staticmethod
    def load_multiple_csvs(directory: str, pattern: str = "*.csv") -> Dict[str, pd.DataFrame]:
        """
        Load multiple CSV files from a directory
        
        Args:
            directory: Directory containing CSV files
            pattern: File pattern to match
            
        Returns:
            Dictionary mapping filename to DataFrame
        """
        try:
            data = {}
            dir_path = Path(directory)
            
            if not dir_path.exists():
                log_warning(f"Directory not found: {directory}")
                return data
            
            for file_path in dir_path.glob(pattern):
                try:
                    df = pd.read_csv(file_path)
                    data[file_path.stem] = df
                    log_info(f"Loaded {len(df)} rows from {file_path.name}")
                except Exception as e:
                    log_warning(f"Error loading {file_path.name}: {str(e)}")
            
            return data
        except Exception as e:
            log_error(f"Error loading CSVs from {directory}: {str(e)}")
            raise

    @staticmethod
    def save_csv(df: pd.DataFrame, filepath: str, index: bool = False) -> None:
        """
        Save DataFrame to CSV file
        
        Args:
            df: DataFrame to save
            filepath: Output file path
            index: Whether to save index
        """
        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(filepath, index=index)
            log_info(f"Saved {len(df)} rows to {filepath}")
        except Exception as e:
            log_error(f"Error saving CSV to {filepath}: {str(e)}")
            raise

    @staticmethod
    def save_json(data: Any, filepath: str, indent: int = 2) -> None:
        """
        Save data to JSON file
        
        Args:
            data: Data to save
            filepath: Output file path
            indent: JSON indentation
        """
        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, "w") as f:
                json.dump(data, f, indent=indent)
            log_info(f"Saved JSON data to {filepath}")
        except Exception as e:
            log_error(f"Error saving JSON to {filepath}: {str(e)}")
            raise

    @staticmethod
    def get_data_info(df: pd.DataFrame) -> Dict[str, Any]:
        """
        Get summary information about a DataFrame
        
        Args:
            df: Input DataFrame
            
        Returns:
            Dictionary with data information
        """
        return {
            "shape": df.shape,
            "columns": list(df.columns),
            "dtypes": df.dtypes.to_dict(),
            "null_counts": df.isnull().sum().to_dict(),
            "memory_usage": str(df.memory_usage(deep=True).sum() / 1024**2) + " MB",
        }

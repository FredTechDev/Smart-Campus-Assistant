"""Utility functions for ML pipeline"""

import logging
import random
from datetime import datetime
from pathlib import Path

import numpy as np

# Configure logging
LOG_DIR = Path("ml/logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / f"ml_pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


def set_random_seed(seed: int = 42) -> None:
    """
    Set random seed for reproducibility
    
    Args:
        seed: Random seed value
    """
    np.random.seed(seed)
    random.seed(seed)
    log_info(f"Random seed set to {seed}")


def log_info(message: str) -> None:
    """Log info message"""
    logger.info(message)


def log_warning(message: str) -> None:
    """Log warning message"""
    logger.warning(message)


def log_error(message: str) -> None:
    """Log error message"""
    logger.error(message)


def ensure_directory(path: str) -> None:
    """
    Ensure directory exists
    
    Args:
        path: Directory path
    """
    Path(path).mkdir(parents=True, exist_ok=True)
    log_info(f"Directory ensured: {path}")


def get_data_path(filename: str, data_type: str = "raw") -> str:
    """
    Get full path for data file
    
    Args:
        filename: File name
        data_type: 'raw' or 'processed'
        
    Returns:
        Full file path
    """
    base_path = Path(f"ml/data/{data_type}")
    base_path.mkdir(parents=True, exist_ok=True)
    return str(base_path / filename)

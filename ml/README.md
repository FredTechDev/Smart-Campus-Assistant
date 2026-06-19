# ML Pipeline - Smart Campus Assistant

This directory contains the machine learning pipeline for the Smart Campus Assistant project.

## Directory Structure

```
ml/
├── src/                          # ML pipeline source code
│   ├── __init__.py
│   ├── utils.py                 # Utility functions and logging
│   ├── data_loader.py           # Data loading utilities
│   ├── preprocessor.py          # Data preprocessing and cleaning
│   ├── sample_data_generator.py # Generate sample data
│   └── data_exploration.py      # Data analysis and exploration
├── notebooks/                    # Jupyter notebooks
│   ├── 00_setup.ipynb           # Environment setup
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
├── data/
│   ├── raw/                     # Raw data files
│   └── processed/               # Processed data files
├── models/                       # Trained models
├── logs/                         # Pipeline logs
├── requirements.txt             # Python dependencies
└── README.md
```

## Features

### Data Loading (`src/data_loader.py`)
- Load CSV, Excel, and JSON files
- Load multiple CSVs from a directory
- Save processed data
- Get data information summaries

### Data Preprocessing (`src/preprocessor.py`)
- Check and handle missing values
- Remove duplicates
- Remove outliers (IQR and Z-score methods)
- Encode categorical variables (label and one-hot encoding)
- Standardize and normalize features
- Create new features
- Filter data based on conditions

### Data Exploration (`src/data_exploration.py`)
- Basic statistics
- Correlation analysis
- Distribution analysis
- Class balance analysis
- Feature importance analysis
- Missing data pattern analysis
- Generate summary reports

### Sample Data Generator (`src/sample_data_generator.py`)
- Generate realistic student data
- Generate attendance records
- Generate grade data
- Generate performance features
- Generate complete datasets

### Utilities (`src/utils.py`)
- Random seed setting for reproducibility
- Logging configuration
- Directory management

## Quick Start

### 1. Install Dependencies

```bash
cd ml
pip install -r requirements.txt
```

### 2. Run Setup Notebook

```bash
jupyter notebook notebooks/00_setup.ipynb
```

This will:
- Set up the environment
- Create necessary directories
- Generate sample data

### 3. Explore Data

```bash
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```

### 4. Preprocess Data

```bash
jupyter notebook notebooks/02_data_preprocessing.ipynb
```

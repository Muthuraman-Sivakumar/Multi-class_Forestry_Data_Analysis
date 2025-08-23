# Multi-class Forestry Prediction
**Created by:** Muthuraman Sivakumar  
**Date:** August 2025

## About the Project
The project aims to build a classification model that accurately predicts the forest type of a forestry area (Aspen, Krummholz, etc.).

The project uses the UCI Forest Covertypes dataset, please see the "References" section

## File Structure

    ├── README.md                               # This file
    ├── DATA_DICTIONARY.md                      # Explains dataset features
    ├── PROJECT_NOTES.md                        # archive of notes throughout the project
    ├── Jupyter Notebooks                       
        └── EDA                                 
            └── 1_summary.md                    # key EDA moments
            └── 2_visualizations                # Organized storage of all visuals
            └── 3_class_distributions.ipynb     # determining class distributions
            └── 4_multivar_plots.ipynb          # visually comparing feature plots across classes
            └── 5_pearson_correlations.ipynb    # correlations between features by class
            └── cover_type.csv                  # CSV used for Data Wrangler
            └── helper.py                       # helper class to retrieve dataset, split dataset, visualize plots
        └── Preprocessing (TBD)                       
            └── 1_summary.md                    # (TBD) key Preprocessing moments
            └── 2_class_balancing.ipynb         # (TBD) Balance classes within dataset before training
            └── helper.py                       # (TBD)
        └── Training (TBD)
            └── TBD                             # (TBD) Model Training
    ├── requirements.txt
    ├── .gitignore


# Dataset Overview

    ├── 581012 observations
    ├── 55 features    
        └── 54 input features                
            └── 10 numerical
            └── 44 binary
        └── 1 output feature (forest type)
            └── 7 classes (7 types of forests)

# Extra Details
More details on features found in "Data Dictionary.md" file ([link](DATA_DICTIONARY.md))   
Thought process behind project is found in "Project Notes.md" file ([link](PROJECT_NOTES.md))

# References
- Blackard, Jock. "Covertype." UCI Machine Learning Repository, 1998, https://doi.org/10.24432/C50K5N.

- Copyright Jock A. Blackard and Colorado State University

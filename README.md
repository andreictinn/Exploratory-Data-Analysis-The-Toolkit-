# Exploratory Data Analysis Toolkit 

Welcome to the Exploratory Data Analysis (EDA) Toolkit! These tools have been designed specifically for analyzing and visualizing financial data. This repository houses a collection of python scripts to be used accordingly with your project's specifications and dataset needs. Thus, the purpose of this toolkit is to aid others with data analysis tasks through a versatile and modular set of scripts.

## Table of Contents

1. [Understanding the Project](#understanding-the-project)
2. [Files and Descriptions](#files-and-descriptions)
3. [Usage](#usage)
4. [EDA Toolkit Application - an example](#eda-toolkit-application---an-example)
5. [Visual Code Library Requirements](#visual-code-library-requirements)
6. [License](#license)

## What You'll Learn

By exploring this toolkit, you will:

- Understand financial data analysis techniques
- Learn how to extract, clean, manipulate, visualize, and analyze financial loans data
- Gain insights into modular and versatile script usage for specific data analysis needs

## Understanding the Project
The core focus of this toolkit revolves around the exploration and interpretation of financial loans data. This project includes the essentials scripts for data extraction, cleaning, manipulation, visualization and analysis. Whether you are an analyst, data scientist, or a finance professional, this toolkit provides the resources needed to glean meaningful information from loan datasets.

## Files and Descriptions 

This toolset is modular which means that each of the following python scripts can be used separately as they perform unique functions. Based on your project needs, use these tools to help you glean information from your data.  


- **calculating_future_loss.py**: Script to calculate the projected loss of loans - in this instance they are marked with a 'Charged Off' label in the dataset. 

- **calculating_loss.py**: Script to calculate the percentage of charged off loans historically and the total amount paid towards these loans before being charged off.

- **calculating_possible_loss.py**: Script to calculate the loss in revenue loans marked as 'Charged Off' would have generated if they had finished their term. Visualizes the projected loss over the remaining term.

- **correlation_heatmap.py**: Script to generate a correlation heatmap for numerical columns in the dataset, it is a useful tool in data cleaning to potentially remove redundant columns for a cleaner data analysis.
      - **Ensure you are not removing key columns from your data** - 

- **data_transform.py**: Module containing class and functions for essential data cleaning. 

- **data_visualization.py**: Module with basic data exploration script. 

- **date_convertor.py**: Script to convert date columns to a consistent format.

- **df_extractor.py**: Script to extract database from Amazon AWS servers. 

- **df_outlier_removal.py**: Script to remove outliers from the DataFrame through an interquartile range (IQR) analysis.

- **df_skew_checker.py**: Script to visualise data skewn in numerical columns. 
  
-**indicators_for_loss.py**: Script to analyze indicators that might contribute to loans not being paid off, comparing loans already charged off with those that could potentially change to 'Charged Off'.

- **loan_recovery_calculator.py**: Script to calculate and visualise the percentage of loans recovered against investor funding and total amount funded.

- **null_remover.py**: Script to handle Null values and potentially drop unsatisfactory columns.

- **visualiser_plotter.py**: Module containing class and functions for visualizing data.

### Usage 
To use these scripts, follow the instructions provided in each script's docstrings. 
Each script in this toolkit can be utilized independently, providing flexibility based on specific data analysis needs. Consult the docstrings within each script for comprehensive instructions on usage and any additional details.


##### EDA Toolkit Application - an example: 

1. **df_extractor.py** - Extracting your database. Ensure yaml file is updated to include login credentials for your project.
2. **data_visualization.py** - First look at your data. Spend some time to understand what your data looks like and what data types you are working with.
3. **visualiser_plotter.py** - Creates essential data visualization class using matplotlib and seaborn. 
4. **data_transform.py** - First data cleaning script with essential functions for handling missing data. 
3. **date_convertor.py** - In case dataframe is inconsistent with date and time, apply the script to achieve consistency. 
4. **null_remover.py** - If considerable amount of data is missing, it is worth considering removing incomplete columns. Determine what percentage constitutes your limit for Null values and proceed with their removal. The default used here is 60%.  
5. **df_skew_checker.py** - Analyse dataframe skew. It is important to note that data skew can be acceptable based on the nature of the project and the type of the data itself. Define your own skew limits before future data manipulation. 
6. **df_outlier_removal.py** - IQR analysis to pinpoint and remove outliers from the dataframe, will potentially impact data skew considerably.
7. **correlation_heatmap.py** - Visualise columns' correlations and consider removal based extreme figures to reduce redundancy in data analysis.

-- The following scripts are examples of data analysis commands for data querying, personalise or adapt as needed for other operations --
   
9. **calculating_loss.py**   
10. **calculating_future_loss.py**
11. **calculating_possible_loss.py**
12. **indicators_for_loss.py**
13. **loan_recovery_calculator.py**

    
#### Visual Code Library Requirements:   
Make sure to have the required dependencies installed
- pandas 
- matplotlib
- seaborn


# Exploratory Data Analysis Toolkit 

Welcome to the Exploratory Data Analysis (EDA) Toolkit designed specifically for analyzing and visualizing loan data. This repository houses a collection of powerful tools that cater to the intricacies of loan datasets. Our goal is to empower users with a versatile set of scripts, each meticulously crafted to fulfill distinct data analysis requirements.

## Understanding the Project
The core focus of this toolkit revolves around the exploration and interpretation of loan data. This project undertakes a comprehensive journey through various facets of data handling, ranging from cleaning to intricate analyses, and ultimately visualizing insights into loan performance. Whether you are an analyst, data scientist, or a finance professional, this toolkit provides the resources needed to glean meaningful information from loan datasets.

## Files and Descriptions

- **calculating_future_loss.py**: Script to calculate the projected loss of loans marked as Charged Off.

- **calculating_loss.py**: Script to calculate the percentage of charged off loans historically and the total amount paid towards these loans before being charged off.

- **calculating_possible_loss.py**: Script to calculate the loss in revenue loans marked as Charged Off would have generated if they had finished their term. Visualizes the projected loss over the remaining term.

- **correlation_heatmap.py**: Script to generate a correlation heatmap for numerical columns in the cleaned DataFrame.

- **data_transform.py**: Module containing functions for transforming the DataFrame, including handling null values and dropping columns.

- **data_visualization.py**: Module with functions for visualizing data using seaborn and matplotlib.

- **date_convertor.py**: Script to convert date columns to a consistent format.

- **df_extractor.py**: Script to extract a subset of users for analysis.

- **df_outlier_removal.py**: Script to remove outliers from the DataFrame.

- **df_skew_checker.py**: Script to check and handle skewness in numerical columns.
  
-**indicators_for_loss.py**: Script to analyze indicators that might contribute to loans not being paid off, comparing loans already charged off with those that could potentially change to charged off.

- **loan_recovery_calculator.py**loan_recovery_calculator.py: Script to calculate the percentage of loans recovered against investor funding and total amount funded. Visualizes the results on appropriate graphs.

- **null_remover.py**: Script to remove rows with null values in specific columns.

- **visualiser_plotter.py**: Module containing classes and functions for visualizing data, including null distribution plots and boxplots.

### Usage 
To use these scripts, follow the instructions provided in each script's docstrings. 
Each script in this toolkit can be utilized independently, providing flexibility based on specific data analysis needs. Consult the docstrings within each script for comprehensive instructions on usage and any additional detail



#### Visual Code Library Requirements:   
Make sure to have the required dependencies installed
- pandas 
- matplotlib
- seaborn


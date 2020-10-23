# Table of Contents
___
### Reports
<!-- - [Factors Influencing Homesale Prices in King County Area](./notebooks/reports/index.ipynb)
- [Presentation](./reports/King_County_Home_Sales.pdf) -->

### Exploratory Notebooks
<!-- - [Data Cleanup and Exploration](./notebooks/exploratory/notebooks/EDA.ipynb)
- [Influence of Waterfront and Porches on Homesale Price](./notebooks/exploratory/eda/andrew_PR_EDA.ipynb) -->

# Introduction
___
The following is our findings of our analysis of over 3000 customers from SyriaTel. Through data cleaning and analysis various machine learning models were build to predict customer churn. Due to the business nature of this analysis, our process aims to create a model which minimizes false negatives. In other words, beyond genreal acuracy, want to avoid predicting a customer will stay when they will end up leaving. 

# Influences
___

## Feature Correlations
<img src = ./reports/imageses/Feature_corr.png width= 400px>
There were several factors acting as strong predictors of customer churn. These have high correlations with customer churn and are expected to be used in the model.

## Feature Importances
<img src = ./reports/imageses/Feature_importance.png width= 400px>
Using what is known as an "Extra Trees" model, we cerated predictions for customer churn. As expected, 2 of our model's top 5 predictors are related to the high correlations seen between our predictors and customer churn.

## Confusion Matrix
<img src = ./reports/imageses/et_confusion_matrix.png width= 400px>
This is a visualization of our model's predictions. We see along the main diagonal our model's correct predictions. In the top left the number of customers our model correctly predicted would stay. In the bottom right is the number correctly predicted to churn.
The models errors can be seen along the off diagonal. The top right is the number of customers predicted to churn when they stayed with SyriaTel, and the bottom left predicted to stay when they churned.
It is the bottom left number (known as a type II error) that this model seeks to minimize. Oour aim is to efficiently identify customers at risk of leaving, and flag for intervention if possible.





# Appendix
### Repository Navigation
___
Below visualizes the structure of this repository.
```python

project3_ChurnModeling
(Project Folder)
    |
    *README.md (Current file. Markdown file Containing Information on Project Purpose, Process, and Findings)
    |
    |       
    ├ data (Folder Containing Reference Data)
    |    |
    |    └ churn_data.csv (CSV file containing SyriaTel customer churn data)
    |
    |
    ├ notebooks (Folder Containing Notebooks Used as Basis of Analysis)
    |    |
    |    ├ EDA.ipynb (Jupyter Notebook containing data exploration process, initial model development, and creation of visualizations)
    |    |
    |    └ images (Folder containing images created by .ipynb files)
    |
    |
    └ report (Folder Containing Finalized Notebooks, Presentation PDF, and Visualizations)
         |
         ├ index.ipynb (Jupyter Notebook calling functions from report_functions.py that import and clean data. Further functions are called that create model and visualizations)
         |
         ├ index_functions.py (Python Textfile containing functions called in report.ipynb)
         |
         └ images (Folder containing all images created by report.ipynb used in final presentation)
    
```

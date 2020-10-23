# Table of Contents
___
### Reports
<!-- - [Factors Influencing Homesale Prices in King County Area](./notebooks/reports/index.ipynb)
- [Presentation](./reports/King_County_Home_Sales.pdf) -->

### Exploratory Notebooks
<!-- - [Data Cleanup](./notebooks/exploratory/notebooks/EDA.ipynb)
- [Influence of Waterfront and Porches on Homesale Price](./notebooks/exploratory/eda/andrew_PR_EDA.ipynb)
- [Influence of Traffic Noise on Homesale Price](./notebooks/exploratory/eda/sam_traffic_noise.ipynb)
- [Map Visualizations and Location of Housing by Price](./notebooks/exploratory/eda/sam_mapping.ipynb) -->

# Introduction
___
The following is our findings of our analysis of over 3000 customers from SyriaTel.

# Influences
___



<img src = ./reports/figures/presence_nuisance.png width= 400px>


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

import pandas as pd
import numpy as np

from imblearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.model_selection import GridSearchCV
from imblearn.over_sampling import SMOTE

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score

from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

def confusion_matrix_info(model, X_test, y_test, save_path=None):
    '''
    Creates a confusion matrix for a given model

    Parameters
    ----------
    model: an estimator

    X_test: testing dataset

    y_test: training dataset

    Returns
    -------
    A confusion matrix of given model
    '''
    fig, axes = plt.subplots(figsize=(10,5))

    axes.set_title("Model Validation")
    x_tick_marks = ['Predicted to Stay', 'Predicted to Churn']
    y_tick_marks = ['Stayed', 'Churned']
    
    plot_confusion_matrix(model, X_test, y_test, ax=axes, cmap='prism', display_labels=y_tick_marks)

    plt.xticks([0,1], x_tick_marks)
    axes.set_xlabel('')
    axes.set_ylabel('')

    SMALL_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12
    plt.rc('font', size=SMALL_SIZE)          
    plt.rc('axes', titlesize=SMALL_SIZE)     
    plt.rc('axes', labelsize=MEDIUM_SIZE)    
    plt.rc('xtick', labelsize=SMALL_SIZE)   
    plt.rc('ytick', labelsize=SMALL_SIZE)   
    plt.rc('legend', fontsize=SMALL_SIZE)   
    plt.rc('figure', titlesize=BIGGER_SIZE)
    
    plt.tight_layout()
    confusion_matrix = plt.show()

    if save_path:
        plt.savefig(save_path, transparent=True)

    return confusion_matrix, fig


def load_clean_data(df):
    '''
    Uses a dictionary to turn True/False and Yes/No to 0's and 1's

    Parameters
    ----------
    df: Pandas DataFrame

    Returns
    -------
    Data set with True/False and Yes/No changed to 0's and 1's
    '''
        
    
    churn_dict = {False: 0, True: 1},
    yes_no_dict = {'no': 0, 'yes': 1},
    df['churn'].replace(churn_dict, inplace=True),
    df['international plan'].replace(yes_no_dict, inplace=True),
    df['voice mail plan'].replace(yes_no_dict, inplace=True)

    return df


def create_plot_of_feature_importances(coeff_dict, top_num=10, figsize=(7, 6), title='Feature Importances', xlabel='Feature', ylabel='Correlation Percentage', append_title='', prepend_title='', width=0.8, xrot=0, bar_colors=None, percent=None, save_path=None):
    ''' 
    Inputs: 
    
    model: A trained ensemble model instance
    X: a dataframe of the features used to train the model
    '''
    dict_keys = [key for key in coeff_dict.keys()]
    dict_values = [abs(value) for value in coeff_dict.values()]
    
    coeff_dict = {dict_keys[x]: dict_values[x] for x in range(len(dict_values))}
    coeff_dict = dict(list(coeff_dict.items())[:])
    features_and_importances = zip(coeff_dict.keys(), coeff_dict.values())
    features_and_importances = sorted(features_and_importances, key = lambda x: x[1], reverse=True)
    
    features = [i[0].title() for i in features_and_importances[1:top_num+1]]
    print(features)
    importances = [abs(i[1])*100 for i in features_and_importances[1:top_num+1]]
    print(importances)
    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=figsize)
#     width = .35
    plt.bar(features, importances, width=width, color=bar_colors)
    if percent:
        ax.yaxis.set_major_formatter(PercentFormatter())
#     plt.gca().invert_yaxis()
    title = ' '.join([prepend_title, title, append_title])
    plt.title(title)
    plt.xlabel('Feature', fontsize=13)
    plt.ylabel(ylabel, fontsize=13)
    plt.xticks(rotation=xrot)
    plt.axis('tight')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, transparent=True)    












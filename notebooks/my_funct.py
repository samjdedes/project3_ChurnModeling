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

def def confusion_matrix_info(model, X_test, y_test):
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

    plot_confusion_matrix(model, X_test, y_test, ax=axes, cmap='prism', display_labels=y_tick_marks);

    fig, axes = plt.subplots(figsize=(10,5));

    axes.set_title("Model Validation");
    x_tick_marks = ['Predicted to Stay', 'Predicted to Churn'];
    y_tick_marks = ['Stayed', 'Churned'];

    plt.xticks([0,1], x_tick_marks);
    axes.set_xlabel('');
    axes.set_ylabel('');

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

    return confusion_matrix

















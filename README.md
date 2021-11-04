# Customer Segmentation for Arvato Financial Services

In this project, supervised and unsupervised machine learning algorithms are used to analyze demographical datasets of a general population as well as of customers of a German mail-order company. The project has three major steps: the customer segmentation report, the supervised learning model, and the Kaggle Competition.

1. **Customer Segmentation Report**: use unsupervised learning methods to analyze attributes of established customers and the general population in order to create customer segments.
2. **Supervised Learning Model**: use dataset with attributes from targets of a mail order campaign and the previous segmentation analysis to build a machine learning model that predicts whether or not each individual will respond to the campaign.
3. **Kaggle Competition**: use the developed supervised model to make predictions on the campaign data as part of a Kaggle Competition.

This is one of Udacity’s capstone project for the Data Science Nanodegree program. The data is provided by Bertelsmann Arvato Analytics.

The complete project report can be found in [this Medium post](https://medium.com/@thuytrinht4/customer-segmentation-for-arvato-financial-services-4cec6745a20d).

## Installation
To run the Jupyter notebooks and python scripts, you will need a standard installation of Anaconda with Python 3.6.x

Additional libraries needed:
- sklearn

## Data
The data used for this project not publicly available. It was provided only to those participating in the "in class" competition.

## Project Structures

### Data Exploration
- exploration/Data Exploration.ipynb - Data exploration and preprocessing
- exploration/clean_data.py - Python script for cleaning population and customer data
- exploration/utils - module contains all common functions used in others modules

### Customer Segmentation
- segmentation/Customer Segmentation Report.ipynb - Analysis of customers
- segmentation/clean_data.py - Python script for cleaning the segmentation data
- segmentation/utils - module contains all common functions used in others modules
- segmenation/fit_clustering.py - File containing clustering pipeline function. This can also be used as a standlone script.

### Marketing Predictions
- supervised/Supervised Learning.ipynb - Classification using supervised learning techniques
- supervised/clean_data - Python script for cleaning classification data
- supervised/utils - module contains all common functions used in others modules
- supervised/preprocess.py - Python file for preprocessing functions

## Instructions
From the directory containing this README.md, run the following commands:

### Customer Segmentation
1. Clean population and customer data

  <pre>python exploration/clean_data.py [data_dir]/Udacity_AZDIAS_052018.csv [data_dir]/Udacity_CUSTOMERS_052018.csv [data_dir]/merged_data_clean.pkl</pre>

2. Clean mailout_train dataset

  <pre>python segmentation/clean_data.py [data_dir]/Udacity_MAILOUT_052018_TRAIN.csv [data_dir]/mailout_train_clean.pkl</pre>

3. Run the Customer Segmentation Report notebook

### Marketing predictions
1. Clean the mailout_test data

  <pre>python supervised/clean_data.py [data_dir]/Udacity_MAILOUT_052018_TEST.csv [data_dir]/mailout_test_clean.pkl</pre>

2. Run the Supervised Learning notebook


## Prediction Results
Model | Local score |Kaggle Score
--- | --- | ---
Random Forest Classifier | 0.5916 | 0.6023
AdaBoost | 0.76524 | 0.79327
Gradient Boost | 0.76238 | 0.79791


## Acknowledgments

Credit to Udacity and Bertelsmann/Arvato for providing this fun and challenging project!

Other useful source of references:
 + [https://github.com/mkeisenbach/arvato](https://github.com/mkeisenbach/arvato)
 + [https://github.com/djirmgard/arvato-udacity-project](https://github.com/djirmgard/arvato-udacity-project)

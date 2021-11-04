# Customer Segmentation for Arvato Financial Services

In this project, supervised and unsupervised machine learning algorithms are used to analyze demographical datasets of a general population as well as of customers of a German mail-order company. The goal of the project is twofold:

1. Cluster the datasets into groups to find out characteristics of existing customers and differences to general population
2. Develop a forecasting model to predict and identify prospective customer response for a marketing campaign

This is one of Udacity’s capstone project for the Data Science Nanodegree program. The data is provided by Arvato Financial Services, a Bertelsmann subsidiary.

The complete project report can be found in [this Medium post](https://medium.com/@thuytrinht4/customer-segmentation-for-arvato-financial-services-4cec6745a20d).

## Installation
To run the Jupyter notebooks and python scripts, you will need a standard installation of Anaconda with Python 3.6.x

Additional libraries needed:
- sklearn

## Data
The data used for this project not publicly available. It was provided only to those participating in the "in class" competition.

## Files
- features.csv - data dictionary
- Arvato Report.pdf - Analysis report
- Arvato Project Workbook - Jupyter notebook with all parts

### Data Exploration
- exploration/Data Exploration.ipynb - Data exploration and preprocessing
- exploration/clean_data.py - Python script for cleaning population and customer data
- exploration/utils - module contains all common functions used in others modules

### Customer Segmentation
- segmentation/Customer Segmentation Report.ipynb - Analysis of customers
- segmentation/Mailout.ipynb - Analysis of mailout data using clustering model
- segmentation/clean_data.py - Python script for cleaning the segmentation data
- segmenation/fit_clustering.py - File containing clustering pipeline function. This can also be used as a standlone script.

### Marketing Predictions
- supervised/Supervised Learning Using Ensemble Methods.ipynb - Classification using ensemble methods
- supervised/Supervised Learning Using Keras.ipynb - Classification using a neural network
- supervised/clean_data - Python script for cleaning classification data
- supervised/preprocess.py - Python file for preprocessing functions

## Instructions
From the directory containing this README.md, run the following commands:

### Customer Segmentation
1. Clean population and customer data

  <pre>python exploration/clean_data.py [data_dir]/Udacity_AZDIAS_052018.csv [data_dir]/Udacity_CUSTOMERS_052018.csv [data_dir]/merged_data_clean.pkl</pre>

2. Fit clustering algorithms to the merged dataset, using parameters: n_pca=164, n_clusters = 10

  <pre>python segmentation/fit_clustering.py [data_dir]/data_merged_clean.pkl 164 10 [result_dir]/clust_model.pkl</pre>


4. Clean mailout_train dataset

  <pre>python segmentation/clean_data.py data/Udacity_MAILOUT_052018_TRAIN.csv data/mailout_train_clean.pkl</pre>

5. Run the Customer Segmentation Report notebook

### Marketing predictions
1. Clean the training and test data
- From the supervised directory, run:
  <pre>python clean_data.py [data_dir]/Udacity_MAILOUT_052018_TRAIN.csv mailout_train_clean.csv</pre>

- From the supervised directory,
  <pre>run: python clean_data.py [data_dir]/Udacity_MAILOUT_052018_TEST.csv mailout_test_clean.csv</pre>

2. Run the Supervised Learning Using Ensemble Methods notebook

## Results
The detailed analysis of the results can be read in [this Medium post](https://medium.com/@thuytrinht4/customer-segmentation-for-arvato-financial-services-4cec6745a20d).

### Customer segmentation
- One group was found to be more likely to be customers: These individuals were more religious, older and savers.
- Two groups were found to be less likely to be customers: 1) Individuals with low purchasing activity and wealth (also younger) and 2) Individuals from areas with low population density and were less cultural minded/religiousness

### Marketing predictions
The final model had an auc_roc score of 0.76294 and a Kaggle score of 0.80143 (https://www.kaggle.com/c/udacity-arvato-identify-customers/leaderboard).

Model | Local score |Kaggle Score
--- | --- | ---
Gradient Boost | 0.76524 | 0.79327
AdaBoost | 0.76238 | 0.79791
LightGBM (final) | 0.76294 | 0.80143


## Acknowledgments

Credit to Udacity and Bertelsmann/Arvato for providing this fun and challenging project!

Other useful source of references:
 + [https://github.com/mkeisenbach/arvato](https://github.com/mkeisenbach/arvato)
 + [https://github.com/djirmgard/arvato-udacity-project](https://github.com/djirmgard/arvato-udacity-project)

# -*- coding: utf-8 -*-
import distutils.msvccompiler
import sys
import time

from utils import *
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def create_column_transformer(binary_cols, categorical_cols, numerical_cols):
    '''This function deals designated columns and imputes missing data.
    Args:
    df: demographic dataframe
    returns: none
    '''

    # Transform-impute Pipeline
    # Categorical
    categorical_pipeline = Pipeline([
        ('bin_impute', SimpleImputer(missing_values=np.nan, strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Binary
    binary_pipeline = Pipeline([('bin_impute', SimpleImputer(missing_values=np.nan, strategy='most_frequent'))])

    # Numerical
    numerical_pipeline = Pipeline([
        ('num_impute', SimpleImputer(missing_values=np.nan, strategy='median')),
        ('num_scale', StandardScaler())
    ])

    # Combined pipeline
    transformers = [('binary', binary_pipeline, binary_cols),
                    ('categorical', categorical_pipeline, categorical_cols),
                    ('numerical', numerical_pipeline, numerical_cols)]
    column_transformer = ColumnTransformer(transformers=transformers)

    return column_transformer


def build_cluster_pipeline(pca_components, kmeans_clusters):
    '''Creates a pipeline for doing KMeans clustering

    Args:
        pca_components (int): number of pca components
        kmeans_clusters (int): number of clusters

    Returns:
        pipeline (sklearn.pipeline.Pipeline)
    '''

    column_transformer = create_column_transformer(binary_cols, categorical_cols, numerical_cols)

    # Create cluster pipeline
    cluster_pipeline = Pipeline([
        ('transform', column_transformer),
        ('reduce', PCA(n_components=pca_components)),
        ('cluster', KMeans(n_clusters=kmeans_clusters, init='k-means++'))
    ])

    return cluster_pipeline


if __name__ == '__main__':
    '''Fits a clustering model and saves pipeline to a pickle file
    with name 'clust_model' + str(n_clusters) + '.pkl'

    Args:
        cleandata_filepath (str): filepath of cleaned data
        pca_n (int): number of pca components        
        n_clusters (int): number of clusters
        cluster_model_filepath (str): filepath of fitted model
    '''

    cleandata_filepath, pca_n, n_clusters, cluster_model_filepath = sys.argv[1:]
    pca_n = int(pca_n)
    n_clusters = int(n_clusters)

    print('Loading data...')
    if cleandata_filepath[len(cleandata_filepath)-3:] == 'csv':
        clean_df = pd.read_csv(cleandata_filepath)
    elif cleandata_filepath[len(cleandata_filepath)-3:] == 'pkl':
        clean_df = pickle.load(open(cleandata_filepath, "rb"))
    else:
        print('Invalid datatype, please input .csv or .pkl file')

    print('Building model...')
    model = build_cluster_pipeline(pca_n, n_clusters)

    print('Fitting model...')
    # if 'TYPE' in clean_df.columns:
    #     label = clean_df['TYPE']
    # elif 'RESPONSE' in clean_df.columns:
    #     label = clean_df['RESPONSE']

    start_time = time.time()
    print(f"--- Start time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))} ---")

    # Fit cluster pipeline
    # model.fit(clean_df)
    features = binary_cols + categorical_cols + numerical_cols
    model.fit(clean_df[features].sample(frac=0.8))

    train_time = time.time() - start_time
    print("--- Training time: %s minutes ---" % (train_time / 60))


    print('Saving model...')
    f = open(cluster_model_filepath, 'wb')
    joblib.dump(model, f)
    print(f'Saved model to {cluster_model_filepath}')


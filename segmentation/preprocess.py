# -*- coding: utf-8 -*-

from utils import *
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer


def column_transformer(binary_cols, numerical_cols, categorical_cols):
    '''
    Args:
        binary_cols: list of binary columns
        numerical_cols: list of numerical columns
        categorical_cols: list of categorical columns

    Returns:
        column_transformer (sklearn.compose.ColumnTransformer)
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

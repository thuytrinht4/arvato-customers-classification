import sys
from utils import *


def clean_data(df):
 """This function is used to clean dataset after merging"""

 # fix the mixed datatype message
 df = format_mixed_types(df)

 # drop duplicate
 print('--DROP DUPLICATE--')
 (nrow, ncol) = df.shape
 df.drop_duplicates(keep='last', inplace=True)
 print(f'Drop {df.shape[0] - nrow} duplicated rows, Number of rows after drop: {df.shape[0]}')

 # investigate and deal with missing values
 print('--MISSING VALUES--')
 # encoding for the unknown values of each column of dataset
 attributes_values, _ = load_attributes_info()
 dict_of_unknown_names = make_dict_for_unknown_attributes(attributes_values)
 replace_unknown_with_nan(df, dict_of_unknown_names)

 # missing rates of columns
 missing = df.isnull().sum().sort_values(ascending=False) / nrow
 cols_missing_30pect = list(missing[missing > 0.3].index)
 print(f'There are {len(cols_missing_30pect)} attributes with more than 30% values missing, /n'
       f'  {round(len(cols_missing_30pect) / ncol, 1) * 100}% of total attributes')
 print(f'Cols to drop: {cols_missing_30pect}')

 # find columns with identifier or columns with one value with more than 95% of total population
 drop_identifier_cols = identifier_to_drop(df)
 print(f'There are {len(drop_identifier_cols)} columns with identifier or columns with one value with more than '
       f'95% of total population')

 # append to drop cols
 drop_cols = list(set(cols_missing_30pect + drop_identifier_cols))
 print("{} columns will be dropped from the dataset: {}".format(len(drop_cols), drop_cols))

 df.drop(columns=drop_cols, inplace=True)
 print(f'Dropped {df.shape[1] - ncol} columns, Number of columns after drop: {df.shape[1]}')

 # missing rows
 df_null_rows = df.isnull().sum(axis=1)
 drop_missing_rows = list(df_null_rows[df_null_rows > 84].index)
 print(f'There are {len(drop_missing_rows)} rows with more than 84 attributes missing')

 # drop missing rows
 nrow = df.shape[0]
 df.drop(labels=drop_missing_rows, axis=0, inplace=True)
 print(f'Dropped {nrow - df.shape[0]} rows, Number of rows after drop: {df.shape[0]}')

 # feature transformation
 print('--CLEAN CATEGORICAL VARIABLES--')
 # transform datetime variable into Year and Month, + drop variables with too many values
 df, _ = clean_categorical(df)
 # drop unused columns
 designated_cols = binary_cols + categorical_cols + numerical_cols
 if 'TYPE' in df.columns:
    designated_cols = designated_cols + ['TYPE']
 df = df[designated_cols]
 print(f'Dropped {df.shape[1] - ncol} columns, Number of columns after drop: {df.shape[1]}')

 return df


def main():
 if len(sys.argv) == 4:
    general_filepath, customers_filepath, database_filepath = sys.argv[1:]

    print('Loading data...\n    AZDIAS: {}\n    CUSTOMERS: {}'
          .format(general_filepath, customers_filepath))
    df = load_data_2sets(general_filepath, customers_filepath)

    print('Cleaning data...')
    df = clean_data(df)

    print('Saving data...\n    DATABASE: {}'.format(database_filepath))
    save_data(df, database_filepath)

    print('Cleaned data saved to database!')

 else:
      print('Please provide the filepaths of the messages and categories ' \
            'datasets as the first and second argument respectively, as ' \
            'well as the filepath of the database to save the cleaned data ' \
            'to as the third argument. \n\nExample: python clean_data.py ' \
            'Udacity_AZDIAS_052018.csv Udacity_CUSTOMERS_052018.csv ' \
            'data_merged_clean.db')


if __name__ == '__main__':
 main()
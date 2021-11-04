import sys
from utils import *



def clean_data(df):
    """This function is used to clean dataset after merging"""

    # fix the mixed datatype message
    df = format_mixed_types(df)

    # investigate and deal with missing values
    (nrow, ncol) = df.shape
    print('--MISSING VALUES--')
    # encoding for the unknown values of each column of dataset
    attributes_values, _ = load_attributes_info()
    dict_of_unknown_names = make_dict_for_unknown_attributes(attributes_values)
    replace_unknown_with_nan(df, dict_of_unknown_names)

    # feature transformation
    print('--FEATURE TRANSFORMATION--')
    # transform datetime variable into Year and Month, + drop variables with too many values
    df = clean_categorical(df)
    # drop unused columns
    designated_cols = binary_cols + categorical_cols + numerical_cols
    df = df[designated_cols]
    print(f'Dropped {df.shape[1] - ncol} columns, Number of columns after drop: {df.shape[1]}')

    return df



def main():

    if len(sys.argv) == 3:
        data_merged_clean_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    DATA_MERGED_CLEAN: {}\n'
              .format(data_merged_clean_filepath))
        filetype = data_merged_clean_filepath[len(data_merged_clean_filepath)-3:]
        if filetype == 'csv':
            df = pd.read_csv(data_merged_clean_filepath)
        elif filetype == 'pkl':
            df = load_data_pkl(data_merged_clean_filepath)

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
              'Udacity_MAILOUT_052018_TRAIN.csv' \
              'mailout_train_clean.csv')


if __name__ == '__main__':
    main()
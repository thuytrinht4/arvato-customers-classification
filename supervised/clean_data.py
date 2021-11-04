import sys
from utils import *



def clean_data(df):
    """This function is used to clean dataset after merging"""

    # fix the mixed datatype message
    df = format_mixed_types(df)

    # investigate and deal with missing values
    print('--MISSING VALUES--')
    # encoding for the unknown values of each column of dataset
    attributes_values, _ = load_attributes_info()
    dict_of_unknown_names = make_dict_for_unknown_attributes(attributes_values)
    replace_unknown_with_nan(df, dict_of_unknown_names)

    # feature transformation
    print('--FEATURE TRANSFORMATION--')
    # transform datetime variable into Year and Month, + drop variables with too many values
    df = clean_categorical(df)

    all_cols = ['LNR'] + binary_cols + categorical_cols + numerical_cols
    df = df[all_cols]


    return df



def main():

    if len(sys.argv) == 3:
        mailout_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MAIOUT_TEST: {}\n'
              .format(mailout_filepath))
        df = pd.read_csv(mailout_filepath)

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
              'Udacity_MAILOUT_052018_TEST.csv' \
              'mailout_test_clean.csv')


if __name__ == '__main__':
    main()
# import libraries
import pandas as pd
import numpy as np
from datetime import datetime
import pickle


# Constant
DATA_ATTRIBUTES_VALUES_PATH = 'data/DIAS Attributes - Values 2017.xlsx'
DATA_ATTRIBUTES_DESCRIPTION_PATH = 'data/DIAS Information Levels - Attributes 2017.xlsx'
COLUMNS_WITH_MIXED_TYPES = ['CAMEO_DEUG_2015', 'CAMEO_INTL_2015', 'CAMEO_DEU_2015']


# columns by datatype
binary_cols = ['DSL_FLAG', 'GREEN_AVANTGARDE', 'HH_DELTA_FLAG', 'KBA05_SEG6', 'KONSUMZELLE', 'SOHO_KZ',
               'UNGLEICHENN_FLAG', 'VERS_TYP', 'ANREDE_KZ']

categorical_cols = ['OST_WEST_KZ']

numerical_cols = ['ZABEOTYP', 'KBA13_SEG_UTILITIES', 'AKT_DAT_KL', 'D19_VERSI_DATUM', 'D19_GESAMT_ONLINE_DATUM',
                  'KBA13_KMH_180', 'KBA13_MOTOR', 'KBA13_KRSAQUOT', 'KBA13_KRSHERST_BMW_BENZ', 'D19_DROGERIEARTIKEL',
                  'KKK', 'KBA05_KRSHERST1', 'KBA13_BAUMAX', 'KBA05_SEG2', 'KBA05_SEG9', 'D19_BANKEN_GROSS',
                  'D19_VERSAND_DATUM', 'D19_VOLLSORTIMENT', 'FINANZ_UNAUFFAELLIGER', 'KBA13_SITZE_4', 'D19_LEBENSMITTEL',
                  'KBA13_PEUGEOT', 'KBA13_HERST_FORD_OPEL', 'KBA13_HALTER_50', 'KBA13_CCM_1800', 'KBA13_BJ_2004',
                  'KBA05_ANTG3', 'GEBAEUDETYP', 'KBA13_SEG_SPORTWAGEN', 'KBA13_KRSZUL_NEU', 'KBA05_KW1', 'D19_HANDWERK',
                  'KBA13_CCM_1200', 'KBA13_KW_40', 'KBA13_MAZDA', 'CAMEO_DEUG_2015', 'SEMIO_VERT', 'KBA05_KRSZUL',
                  'SHOPPER_TYP', 'KBA05_SEG5', 'ANZ_TITEL', 'KBA13_SEG_KOMPAKTKLASSE', 'D19_BANKEN_DIREKT', 'UMFELD_ALT',
                  'KBA13_RENAULT', 'D19_BUCH_CD', 'KBA13_CCM_0_1400', 'KBA13_SEG_MITTELKLASSE', 'KBA13_FORD', 'VK_DISTANZ',
                  'KBA13_BJ_2009', 'KBA13_KMH_140_210', 'KBA13_CCM_3001', 'KBA13_HALTER_45', 'LP_FAMILIE_FEIN',
                  'KBA13_BJ_2000', 'KBA05_MAXHERST', 'CJT_TYP_1', 'GEMEINDETYP', 'D19_BANKEN_REST', 'KBA13_KW_30',
                  'KBA13_OPEL', 'HEALTH_TYP', 'KBA13_KMH_211', 'D19_TELKO_ANZ_24', 'FINANZ_MINIMALIST', 'KBA05_HERST2',
                  'KBA13_HALTER_30', 'KBA05_KRSHERST2', 'KBA13_FAB_ASIEN', 'KBA13_TOYOTA', 'CJT_TYP_3',
                  'KBA13_SEG_KLEINWAGEN', 'KBA05_MODTEMP', 'KBA13_VORB_1', 'SEMIO_RAT', 'KBA05_FRAU', 'KBA13_VORB_3',
                  'KBA13_CCM_1600', 'VK_DHT4A', 'KBA13_KW_70', 'D19_TECHNIK', 'KBA13_KW_120', 'D19_BEKLEIDUNG_GEH',
                  'SEMIO_KAEM', 'KBA05_MOD4', 'KBA13_SEG_MINIWAGEN', 'PLZ8_ANTG4', 'KBA13_HERST_EUROPA', 'KBA13_ANTG3',
                  'KBA05_KRSVAN', 'KBA05_ALTER2', 'D19_VERSAND_REST', 'D19_HAUS_DEKO', 'VHN', 'KBA05_HERST1',
                  'KBA05_MOD2', 'D19_TELKO_OFFLINE_DATUM', 'KBA05_SEG10', 'KBA13_CCM_1500', 'KBA13_HALTER_25',
                  'KBA13_KW_90', 'D19_KONSUMTYP', 'KBA13_CCM_2000', 'KBA13_SEG_GELAENDEWAGEN', 'KBA13_HERST_AUDI_VW',
                  'RETOURTYP_BK_S', 'KBA13_CCM_1000', 'ARBEIT', 'KBA13_HALTER_35', 'SEMIO_ERL', 'KBA05_MOD8',
                  'D19_VERSICHERUNGEN', 'SEMIO_LUST', 'ANZ_HAUSHALTE_AKTIV', 'KBA13_VORB_1_2', 'RELAT_AB',
                  'KBA13_KMH_251', 'KBA13_VORB_0', 'KBA13_SEG_KLEINST', 'MOBI_REGIO', 'KBA13_SITZE_5', 'D19_ENERGIE',
                  'KBA13_SEG_WOHNMOBILE', 'D19_VERSI_ANZ_12', 'RT_KEIN_ANREIZ', 'KBA05_KRSKLEIN', 'D19_TELKO_DATUM',
                  'PLZ8_ANTG2', 'CJT_TYP_6', 'KBA13_GBZ', 'KBA05_ALTER1', 'KBA05_CCM3', 'WOHNDAUER_2008', 'D19_KOSMETIK',
                  'KBA13_ANTG2', 'KBA13_AUDI', 'FINANZ_HAUSBAUER', 'ANZ_HH_TITEL', 'KBA05_ZUL2', 'D19_SOZIALES',
                  'W_KEIT_KIND_HH',
 'KBA05_CCM2',
 'KBA13_KRSSEG_KLEIN',
 'D19_TELKO_MOBILE',
 'KBA13_FIAT',
 'KBA13_KMH_110',
 'KBA13_HALTER_40',
 'KBA05_MAXAH',
 'ALTERSKATEGORIE_GROB',
 'KBA13_HALTER_55',
 'VHA',
 'D19_REISEN',
 'KBA05_ANHANG',
 'MIN_GEBAEUDEJAHR',
 'KBA13_KMH_210',
 'KBA13_SEG_SONSTIGE',
 'KBA13_SITZE_6',
 'KBA13_HHZ',
 'D19_TELKO_REST',
 'KBA13_HALTER_20',
 'KBA05_SEG4',
 'KBA13_KRSSEG_OBER',
 'D19_BANKEN_ONLINE_DATUM',
 'GFK_URLAUBERTYP',
 'KBA05_MAXSEG',
 'D19_WEIN_FEINKOST',
 'GEBAEUDETYP_RASTER',
 'KBA13_KW_60',
 'D19_GESAMT_ONLINE_QUOTE_12',
 'FINANZ_ANLEGER',
 'KBA05_MOTOR',
 'D19_VERSI_ONLINE_QUOTE_12',
 'KBA05_KRSAQUOT',
 'BALLRAUM',
 'EINGEZOGENAM_HH_JAHR',
 'ANZ_PERSONEN',
 'KBA05_MOTRAD',
 'HH_EINKOMMEN_SCORE',
 'MOBI_RASTER',
 'KBA13_ALTERHALTER_60',
 'KBA13_HERST_BMW_BENZ',
 'KBA13_VW',
 'KBA05_ALTER4',
 'KBA05_MOD1',
 'CJT_TYP_4',
 'KBA13_CCM_1401_2500',
 'KBA13_KMH_0_140',
 'KBA13_BMW',
 'KBA13_NISSAN',
 'KBA13_ALTERHALTER_45',
 'KBA13_FAB_SONSTIGE',
 'KBA13_VORB_2',
 'KBA13_CCM_2501',
 'D19_RATGEBER',
 'D19_VERSAND_OFFLINE_DATUM',
 'KBA13_MERCEDES',
 'CJT_TYP_5',
 'ANZ_KINDER',
 'KBA05_VORB1',
 'D19_BANKEN_ANZ_12',
 'INNENSTADT',
 'D19_GESAMT_ANZ_12',
 'KBA13_BJ_2008',
 'KBA13_KW_61_120',
 'KBA13_HALTER_65',
 'LP_STATUS_FEIN',
 'RT_UEBERGROESSE',
 'D19_TELKO_ONLINE_QUOTE_12',
 'KBA13_CCM_2500',
 'SEMIO_KRIT',
 'KBA13_KMH_140',
 'KBA13_BJ_2006',
 'KBA13_SEG_GROSSRAUMVANS',
 'SEMIO_DOM',
 'KBA13_CCM_1400',
 'KBA13_ALTERHALTER_61',
 'D19_GESAMT_OFFLINE_DATUM',
 'D19_GESAMT_DATUM',
 'D19_SCHUHE',
 'ONLINE_AFFINITAET',
 'NATIONALITAET_KZ',
 'D19_BILDUNG',
 'SEMIO_PFLICHT',
 'KBA05_ANTG1',
 'RT_SCHNAEPPCHEN',
 'CJT_KATALOGNUTZER',
 'KBA13_SEG_OBEREMITTELKLASSE',
 'D19_BANKEN_ANZ_24',
 'KBA13_ANTG4',
 'KBA05_MAXBJ',
 'KBA05_GBZ',
 'KBA13_BJ_1999',
 'KBA13_KW_80',
 'UMFELD_JUNG',
 'REGIOTYP',
 'KBA05_HERST3',
 'KBA05_DIESEL',
 'FIRMENDICHTE',
 'KBA13_KW_0_60',
 'KBA05_SEG1',
 'ALTERSKATEGORIE_FEIN',
 'KBA05_AUTOQUOT',
 'D19_BEKLEIDUNG_REST',
 'KBA05_HERST5',
 'KBA05_VORB2',
 'SEMIO_TRADV',
 'KBA05_SEG8',
 'D19_SAMMELARTIKEL',
 'D19_BANKEN_ONLINE_QUOTE_12',
 'SEMIO_KULT',
 'KBA13_KW_110',
 'KONSUMNAEHE',
 'D19_SONSTIGE',
 'WOHNLAGE',
 'D19_NAHRUNGSERGAENZUNG',
 'SEMIO_MAT',
 'KBA13_AUTOQUOTE',
 'KBA13_SEG_MINIVANS',
 'KBA13_SEG_VAN',
 'SEMIO_REL',
 'KBA13_KW_121',
 'KBA05_CCM1',
 'KBA13_CCM_3000',
 'KBA05_VORB0',
 'KBA05_ZUL4',
 'KBA05_SEG7',
 'EINGEFUEGT_AM_MONTH',
 'KBA05_ZUL3',
 'VK_ZG11',
 'D19_LOTTO',
 'D19_FREIZEIT',
 'KBA13_HERST_ASIEN',
 'SEMIO_SOZ',
 'KBA05_HERSTTEMP',
 'FINANZTYP',
 'KBA13_KRSHERST_AUDI_VW',
 'KBA13_HALTER_60',
 'D19_VERSI_ANZ_24',
 'KBA05_HERST4',
 'KBA05_ALTER3',
 'KBA13_KW_50',
 'KBA05_KW3',
 'EWDICHTE',
 'KBA05_SEG3',
 'D19_BANKEN_DATUM',
 'FINANZ_SPARER',
 'KBA13_SEG_OBERKLASSE',
 'KBA05_MOD3',
 'KBA13_ANTG1',
 'KBA13_ANZAHL_PKW',
 'STRUKTURTYP',
 'KBA05_KRSOBER',
 'KBA13_KRSHERST_FORD_OPEL',
 'KBA05_CCM4',
 'KBA13_KRSSEG_VAN',
 'D19_KONSUMTYP_MAX',
 'D19_BIO_OEKO',
 'FINANZ_VORSORGER',
 'KBA13_ALTERHALTER_30',
 'KBA05_MAXVORB',
 'D19_KINDERARTIKEL',
 'KBA05_KW2',
 'KBA05_ZUL1',
 'KBA05_ANTG2',
 'KBA05_ANTG4',
 'CJT_GESAMTTYP',
 'SEMIO_FAM',
 'VERDICHTUNGSRAUM']


# Preprocessed
drop_missing_30perc = ['ALTER_KIND4', 'TITEL_KZ', 'ALTER_KIND3', 'ALTER_KIND2', 'ALTER_KIND1', 'AGER_TYP', 'EXTSEL992',
                       'KK_KUNDENTYP', 'KBA05_BAUMAX', 'GEBURTSJAHR', 'ALTER_HH']

drop_identifier = ['LNR']

drop_one_value_only = ['D19_BANKEN_LOKAL', 'D19_BANKEN_OFFLINE_DATUM', 'D19_DIGIT_SERV', 'D19_GARTEN', 'D19_TELKO_ANZ_12',
                'D19_TELKO_ONLINE_DATUM', 'D19_TIERARTIKEL', 'D19_VERSI_OFFLINE_DATUM', 'D19_VERSI_ONLINE_DATUM']

drop_high_correlation = ['KBA05_BAUMAX', 'LP_LEBENSPHASE_FEIN', 'D19_TELKO_ANZ_12', 'PLZ8_GBZ', 'LP_STATUS_GROB',
                   'LP_FAMILIE_GROB', 'KBA13_KMH_250', 'LP_LEBENSPHASE_GROB', 'EXTSEL992', 'ORTSGR_KLS9',
                   'KK_KUNDENTYP', 'D19_VERSAND_ANZ_24', 'D19_DIGIT_SERV', 'CJT_TYP_2', 'D19_VERSAND_ONLINE_DATUM',
                   'D19_BANKEN_OFFLINE_DATUM', 'ALTER_KIND2', 'LNR', 'ALTER_KIND4', 'KBA13_HALTER_66']

drop_cols = drop_missing_30perc + drop_identifier + drop_one_value_only + drop_high_correlation



def load_data_2sets(general_filepath, customers_filepath):
    """This function used to load dataset from the given 2 links of categories & messages"""
    # load gerenal dataset
    general = pd.read_csv(general_filepath)

    # load customer dataset
    customers = pd.read_csv(customers_filepath)

    # merging datasets
    general['TYPE'] = 'general'
    customers['TYPE'] = 'customer'

    df = pd.concat([general, customers.drop(columns=['CUSTOMER_GROUP', 'ONLINE_PURCHASE', 'PRODUCT_GROUP'])])

    return df


def load_data_pkl(data_filepath):
    """This function used to load dataset from the given 2 links of categories & messages"""
    # load mailout dataset
    df = pickle.load(open(data_filepath, "rb"))

    return df


def save_data(df, database_filepath):
    """This function help to save dataframe to database"""
    df.to_pickle(database_filepath)


def format_mixed_types(df, cols_mixed_types=COLUMNS_WITH_MIXED_TYPES):
    '''This function is created for formating improper
    values in columns CAMEO_DEUG_2015 and CAMEO_INTL_2015.
    Args:
    df: demographics dataframe
    returns: transformed dataframe
    '''

    if set(cols_mixed_types).issubset(df.columns):
        for col in cols_mixed_types:
            print(col)
            df[col] = df[col].replace({'X': np.nan, 'XX': np.nan})
            try:
                df[col] = df[col].astype(float)
            except ValueError:
                continue
            print(df[col].unique())

    return df


def load_attributes_info(attribute_value_filepath=DATA_ATTRIBUTES_VALUES_PATH, attribute_desc_filepath=DATA_ATTRIBUTES_DESCRIPTION_PATH):
    attributes_values = pd.read_excel(attribute_value_filepath, header=1)
    attribuets_desc = pd.read_excel(attribute_desc_filepath, header=1)

    attribuets_desc.drop(columns=['Unnamed: 0'], inplace=True)
    attributes_values.drop(columns=['Unnamed: 0'], inplace=True)

    # fill the missing values
    attributes_values['Attribute'] = attributes_values['Attribute'].ffill()
    attributes_values['Description'] = attributes_values['Description'].ffill()

    return attributes_values, attribuets_desc


def make_dict_for_unknown_attributes(attributes_values):
    '''This dictionary stores the encoding values of the unknowns for each column of the dataset'''
    dict_of_unknown_names = {}
    # missing values that have the word 'unknown' in attribtute_values description
    for i, row in attributes_values.iterrows():
        if "unknown" in str(row['Meaning']):
            dict_of_unknown_names[row['Attribute']] = [int(num) for num in str(row['Value']).split(', ')]

    # additional missing values that do not have words 'unknown' in description
    additional_missing_values = {'KBA05_MODTEMP': [6.0], 'LP_FAMILIE_FEIN': [0.0], 'LP_FAMILIE_GROB': [0.0],
                                 'LP_LEBENSPHASE_FEIN': [0.0], 'LP_LEBENSPHASE_GROB': [0.0], 'ORTSGR_KLS9': [0.0],
                                 'GEBURTSJAHR': [0]}
    dict_of_unknown_names.update(additional_missing_values)

    return dict_of_unknown_names


def replace_unknown_with_nan(df, dictionary):
    '''This function accept a dataframe which is
    going to be check for the missing values according
    to the dictionary and if such exists it will be replaced with numpy.nan.
    Args:
    df: demographics dataframe
    dictionary: dictionary which contains encodings for unknown values for each column of the dataset
    returns: none
    '''
    for key, value in dictionary.items():
#         print(key, value)
        if key in df.columns:
            for i in range(0, len(value)):
                df.loc[df[key] == value[i], key] = np.nan


def identifier_to_drop(df):
    nrow = df.shape[0]
    cols_to_drop = []

    for col in df.columns:
        # check if column has more than 95% of values are uniques
        nunique_rate = df[col].nunique() / nrow
        if nunique_rate > 0.95:
            cols_to_drop.append(col)
            print(f'{col} has {round(nunique_rate, 2) * 100}% values are unique')

        # check if column has more than 95% of values belongs to only 1 categories
        mode_count = df[col].value_counts().values[0]
        mode_freq = mode_count / nrow
        if mode_freq > 0.95:
            cols_to_drop.append(col)
            print(f'{col} has {round(mode_freq, 2) * 100}% values belongs to categoy {df[col].value_counts().index[0]}')

    return cols_to_drop


def corr_to_drop(df):
    # Create correlation matrix for just Features to determine different models to test
    corr_matrix = df.corr().abs().round(2)

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

    # Find features with correlation greater than 0.90
    cols_to_drop = [column for column in upper.columns if any(upper[column] > 0.90)]

    return cols_to_drop


def clean_categorical(df, cols_drop = []):
    '''This function deals designated columns and imputes missing data.
    Args:
    df: demographic dataframe
    returns: none
    '''

    categorical_cols = list(df.select_dtypes(['object']).columns)

    for col in categorical_cols:
        # Convert columns 'EINGEFUEGT_AM'
        if col == 'EINGEFUEGT_AM':
            df['EINGEFUEGT_AM_MONTH'] = df['EINGEFUEGT_AM'].apply(
                lambda x: np.nan if str(x) == 'nan' else datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S').month)

            if col not in cols_drop:
                cols_drop.append(col)

        else:
            # drop columns have too many categorical values
            n_unique = df[col].dropna().nunique()
            if n_unique > 20:
                if col not in cols_drop:
                    cols_drop.append(col)

    df.drop(columns=cols_drop, inplace=True)

    return df, cols_drop


def get_columns_by_type(df):
    # Categorical
    categorical_cols = list(df.select_dtypes(['object']).columns)

    # Binary
    num_cols = df.select_dtypes(['float64', 'int64']).columns
    binary_cols = []
    for col in num_cols:
        n_unique = df[col].dropna().nunique()
        if n_unique == 2:
            binary_cols.append(col)

    # Numerical
    numerical_cols = list(set(df.columns) - set(binary_cols) - set(categorical_cols))

    return binary_cols, categorical_cols, numerical_cols


import pandas as pd
import re

class QualtricsData:

    def __init__(self, data_csv):

        self.data_csv = data_csv
        self.df_raw = self._read_raw_data()
        self.df_proc = self.df_raw.copy()

        self.var_codebook = None
        self.value_codebook = None
        self.attention_dict = None

    def _read_raw_data(self):
        '''
        This function reads in a qualtrics datafile and removes incomplete entries.
        It also removes the two erroneous rows at the top of the file.
        :return:
        '''
        df = pd.read_csv(self.data_csv)
        df = df.loc[df['Finished'] == 'TRUE', :].reset_index()
        return df

    def _set_var_codebook(self, var_codebook_csv):
        '''
        Take a variable codebook csv, convert to a dictionary format, and save as attribute
        e.g. {'variable1_qualtrics_name': 'new1_variable_name', 'variable2_qualtrics_name': 'new2_variable_name', ...}
        :param var_codebook_csv:
        :return:
        '''
        var_codebook_df = pd.read_csv(var_codebook_csv)
        self.var_codebook = "fill in with variable codebook dict"

    def _set_value_codebook(self, value_codebook_csv):
        '''
        Take a value codebook csv, convert to nested dictionary format, and save as attribute
        e.g:
         {'variable_1':
            {'qualtrics_option_1': new_numeric_option_1, 'qualtrics_option_2': new_numeric_option_2, ...},
         'variable_2':
            {'qualtrics_option_1': new_numeric_option_1, 'qualtrics_option_2': new_numeric_option_2, ...}
         }
        :param value_codebook_csv:
        :return:
        '''
        value_codebook_df = pd.read_csv(value_codebook_csv)
        value_codebook_re_dict = self.__dictify_nested_df(value_codebook_df)
        self.value_codebook = {}
        for column_regex, value_dict in value_codebook_re_dict.items():
            column_regex_matches = [col_name for col_name in self.df_proc.columns if re.search(column_regex, col_name)]
            for col_match in column_regex_matches:
                self.value_codebook[col_match] = value_dict

    def rename_vars(self, var_codebook_csv):
        '''
        Rename variable columns based on var_codebook
        :param var_codebook_csv:
        :return:
        '''
        self._set_var_codebook(var_codebook_csv)
        # some code
        self.df_proc = "fill in with preprocessed dataframe"
        return self.df_proc

    def recode_values(self, value_codebook_csv):
        '''
        Recode values of different variables based on value_codebook
        :param value_codebook_csv:
        :return:
        '''
        self._set_value_codebook(value_codebook_csv)
        # some code
        self.df_proc = "fill in with preprocessed dataframe"
        return self.df_proc

    def remove_attention_fails(self, attention_dict):
        '''
        Remove rows where the participant failed an attention check
        :param attention_dict: attention check dictionary of the form {'column_name_1': 'passing_answer', 'column_name_2': 'passing_answer'}
        :return:
        '''
        self.attention_dict = attention_dict
        # some code
        self.df_proc = "fill in with preprocessed dataframe"
        return self.df_proc

    @staticmethod
    def __dictify_nested_df(df):
        d = {}
        for row in df.values:
            here = d
            for elem in row[:-2]:
                if elem not in here:
                    here[elem] = {}
                here = here[elem]
            here[row[-2]] = row[-1]
        return d



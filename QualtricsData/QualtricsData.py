
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
        This function reads in a qualtrics datafile and removes the two erroneous rows at the top of the file.
        :return:
        '''
        df = pd.read_csv(self.data_csv)
        df['Finished'] = df['Finished'].str.lower()
        df = df.loc[df['Finished'].isin(['true', 'false'])].reset_index(drop=True)
        return df

    def _set_var_codebook(self, var_codebook_csv):
        '''
        Take a variable codebook csv, convert to a dictionary format, and save as attribute
        e.g. {'variable1_qualtrics_name': 'new1_variable_name', 'variable2_qualtrics_name': 'new2_variable_name', ...}
        :param var_codebook_csv:
        :return:
        '''
        var_codebook_df = pd.read_csv(var_codebook_csv)
        self.var_codebook = self.__dictify_df(var_codebook_df)


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
        for column_name in self.df_proc.columns:
            if column_name in self.var_codebook:
                self.df_proc = self.df_proc.rename(columns={column_name: self.var_codebook[column_name]})

    def recode_values(self, value_codebook_csv):
        '''
        Recode values of different variables based on value_codebook
        :param value_codebook_csv:
        :return:
        '''
        self._set_value_codebook(value_codebook_csv)
        self.df_proc = self.df_proc.replace(self.value_codebook)

    def filter_rows(self, attention_dict):
        '''
        Remove rows based on response e.g. where the participant failed an attention check
        :param attention_dict: dictionary of the form {'column_name_1': 'passing_answer', 'column_name_2': 'passing_answer'}
        :return:
        '''
        # TODO: accept other formats of attention dict
        self.attention_dict = attention_dict
        for column_name, passing_answer in attention_dict.items():
            if isinstance(passing_answer, list):
                df = self.df_proc.loc[self.df_proc[column_name].isin(passing_answer)]
            else:
                df = self.df_proc.loc[self.df_proc[column_name]==passing_answer]
        self.df_proc = df.reset_index(drop=True)
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

    @staticmethod
    def __dictify_df(df):
        # TODO: combine with nested df function
        d = {}
        for row in df.values:
            d[row[-2]] = row[-1]
        return d



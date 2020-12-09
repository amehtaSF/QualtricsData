
import pandas as pd

class QualtricsData:

    def __init__(self, data_csv):

        self.df_raw = pd.read_csv(data_csv) # raw dataframe
        self.df_proc = None # preprocessed dataframe

        self.var_codebook = None
        self.value_codebook = None
        self.attention_dict = None

    def _set_var_codebook(self, var_codebook_csv):
        '''
        Take a variable codebook csv, convert to a dictionary format, and save as attribute
        e.g. {'variable1_qualtrics_name': 'new1_variable_name', 'variable2_qualtrics_name': 'new2_variable_name', ...}
        :param var_codebook_csv:
        :return:
        '''
        var_codebook_df = pd.read_csv(var_codebook_csv)
        self.var_codebook = "fill in"

    def _set_value_codebook(self, value_codebook_csv):
        '''
        Take a value codebook csv, convert to nested dictionary format, and save as attribute
        e.g:
         {'variable_1_name':
            {'qualtrics_option_1': new_numeric_option_1, 'qualtrics_option_2': new_numeric_option_2, ...},
         'variable_2_name':
            {'qualtrics_option_1': new_numeric_option_1, 'qualtrics_option_2': new_numeric_option_2, ...}
         }
        :param value_codebook_csv:
        :return:
        '''
        value_codebook_df = pd.read_csv(value_codebook_csv)
        self.value_codebook = "fill in"

    def rename_vars(self, var_codebook_csv):
        '''
        Rename variable columns based on var_codebook
        :param var_codebook_csv:
        :return:
        '''
        self._set_var_codebook(var_codebook_csv)
        # fill in

    def recode_values(self, value_codebook_csv):
        '''
        Recode values of different variables based on value_codebook
        :param value_codebook_csv:
        :return:
        '''
        self._set_value_codebook(value_codebook_csv)
        # fill in

    def remove_attention_fails(self, attention_dict):
        '''
        Remove rows where the participant failed an attention check
        :param attention_dict: attention check dictionary of the form {'column_name_1': 'passing_answer', 'column_name_2': 'passing_answer'}
        :return:
        '''
        self.attention_dict = attention_dict
        # fill in


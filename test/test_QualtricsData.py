from QualtricsData import QualtricsData
from pprint import pprint
import pandas as pd

test_datafile_path = '../data/raw/example_data_file.csv'
test_value_codebook_path = '../data/codebook/example_value_codebook.csv'
test_var_codebook_path = '../data/codebook/example_var_codebook.csv'

qd = QualtricsData(test_datafile_path)

def rename_recode():
    qd.rename_vars(test_var_codebook_path)
    qd.recode_values(test_value_codebook_path)

def test_rename_vars():
    qd.rename_vars(test_var_codebook_path)

def test__set_value_codebook():
    qd.rename_vars(test_var_codebook_path)
    qd._set_value_codebook(test_value_codebook_path)

def test_recode_values():
    qd.rename_vars(test_var_codebook_path)
    qd.recode_values(test_value_codebook_path)

def test_filter_values():
    rename_recode()
    qd.filter_rows({'difficulty_2': 3})

if __name__ == '__main__':
    # test_recode_values()
    print(qd.df_proc.shape)
    test_filter_values()
    print(qd.df_proc['difficulty_2'])
    print(qd.df_proc.shape)
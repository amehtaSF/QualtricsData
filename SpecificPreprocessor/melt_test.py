import pandas as pd
from src.QualtricsData.QualtricsData import QualtricsData
from pprint import pprint

test_datafile_path = '../data/example_data_file.csv'
test_value_codebook_path = '../data/example_value_codebook.csv'
test_var_codebook_path = '../data/example_var_codebook.csv'

qd = QualtricsData(test_datafile_path)
qd.rename_vars(test_var_codebook_path)  # variable names need to be renamed to match with value codebook)
qd._set_value_codebook(test_value_codebook_path)
qd.recode_values(test_value_codebook_path)
df_raw = qd.df_proc

# pprint(df_raw.columns)
df_2 = df_raw[['pid', 'situation_1', 'situation_2', 'situation_3', 'situation_4',
         'rethink_1', 'rethink_2', 'rethink_3', 'rethink_4']].copy()

df_2 = pd.wide_to_long(df_2, stubnames=["situation", "rethink"], i="pid", j="situation_num", sep="_")
pprint(df_2)

# combine situation num and pid into doc id
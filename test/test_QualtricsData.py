from src.QualtricsData.QualtricsData import QualtricsData
from pprint import pprint

test_datafile_path = '../data/example_data_file.csv'
test_value_codebook_path = '../data/example_value_codebook.csv'
test_var_codebook_path = ''

qd = QualtricsData(test_datafile_path)

def test__set_value_codebook():
    qd.rename_vars(test_var_codebook_path) # variable names need to be renamed to match with value codebook)
    qd._set_value_codebook(test_value_codebook_path)
    pprint(qd.value_codebook)

if __name__ == '__main__':
    test__set_value_codebook()
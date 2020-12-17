from src.QualtricsData.QualtricsData import QualtricsData
import regex as re
import pandas as pd
test_datafile_path = '../data/example_data_file.csv'
test_value_codebook_path = '../data/example_value_codebook.csv'
test_var_codebook_path = '../data/example_var_codebook.csv'

qd = QualtricsData(test_datafile_path)

situation_pattern = '^situation_.*'
rethink_pattern = '^rethink_.*'
difficulty_pattern = '^difficulty_.*'
pos_pre_pattern = '^pos_pre_.*'
neg_pre_pattern = '^neg_pre_.*'
pos_post_pattern = '^pos_post_.*'
neg_post_pattern = '^neg_post_.*'

def one_col_for_one_participant_from_qualt_df(qualt_df, re_pattern, sel_name):
    init_df = pd.DataFrame()
    final_df = pd.DataFrame()
    for col_name in qualt_df:
        if re.search(re_pattern, col_name):
            init_df[col_name] = qd.df_proc[col_name]
    proc_init_df = init_df.T
    proc_init_df.index = proc_init_df.index.map(lambda x: str(x)[-1])
    for col in (proc_init_df):

        new_df = pd.concat([final_df, proc_init_df[col]], ignore_index=False, sort=False)

        final_df = new_df
    final_df.rename(columns={0: sel_name}, inplace=True)
    return final_df

def preprocessing():
    qd.rename_vars(test_var_codebook_path)  # variable names need to be renamed to match with value codebook)
    qd._set_value_codebook(test_value_codebook_path)
    qd.recode_values(test_value_codebook_path)
    df = qd.df_proc
    situation_df = one_col_for_one_participant_from_qualt_df(df, situation_pattern, 'situation')
    situation_df['situation_num'] = situation_df.index
    rethink_df = one_col_for_one_participant_from_qualt_df(df, rethink_pattern, 'rethink')
    difficulty_df = one_col_for_one_participant_from_qualt_df(df, difficulty_pattern, 'difficulty')
    pos_pre_df = one_col_for_one_participant_from_qualt_df(df, pos_pre_pattern, 'pos_pre')
    neg_pre_df = one_col_for_one_participant_from_qualt_df(df, neg_pre_pattern, 'neg_pre')
    pos_post_df = one_col_for_one_participant_from_qualt_df(df, pos_post_pattern, 'pos_post')
    neg_post_df = one_col_for_one_participant_from_qualt_df(df, neg_post_pattern, 'neg_post')
    combined_df = pd.concat([situation_df, rethink_df, difficulty_df, pos_pre_df, neg_pre_df, pos_post_df, neg_post_df], axis=1)
    #combined_df['pid'] =qd.df_proc['pid']
    #print(combined_df['situation_num'].max())
    #num_pid_repetitions = int(combined_df['situation_num'].max()) # finding how many times each entry of pid needs to be replicated so pid for each row of processed df can be added
    #pid_df = pd.DataFrame()
    #pid_df['pid'] = None
    #for pid in qd.df_proc['pid']:
     #   pid_df['pid'] = pid


    #print(pid_df)

if __name__ == '__main__':
    preprocessing()
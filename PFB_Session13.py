# Dataframes
# Columns
# Records
# Joins
# Merging
# External Files


orskl_dict_st = {
    'student_id' : [1001, 1002, 1003, 1004, 1005],
    'name' : ['Student 1 ', 'Student 2', 'Student 3', 'Student 4', 'Student 5']
}

orskl_dict_loc = {
    'student_id' : [1001, 1002, 1003, 1004, 1005],
    'location': ['INDIA', 'USA', 'UAE', 'UK', 'JAPAN']
}


orskl_dict_enroll = {
    'student_id' : [1001, 1004],
    'course' : ['PFB', 'DSS']
}

import pandas as pd
orskl_df_st = pd.DataFrame(orskl_dict_st)
orskl_df_loc = pd.DataFrame(orskl_dict_loc)
orskl_df_enroll = pd.DataFrame(orskl_dict_enroll)


# Get locations & names of all the students
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge
orskl_df_st_loc = orskl_df_st.merge(orskl_df_loc, how='inner', on='student_id')

orskl_df1 = pd.DataFrame({'COVID_cases': [10, 20, 30, 40 , 50], 'country': ['USA', 'INDIA', 'UK', 'UAE', 'JAPAN']})
orskl_df2 = pd.DataFrame({'COVID_cases': [40, 50, 60], 'states': ['AP', 'TS', 'TN']})
orskl_df_inner = orskl_df1.merge(orskl_df2, how='inner', on='COVID_cases')
orskl_df_left = orskl_df1.merge(orskl_df2, how='left', on='COVID_cases')
orskl_df_left = orskl_df2.merge(orskl_df1, how='left', on='COVID_cases')
orskl_df_right = orskl_df1.merge(orskl_df2, how='right', on='COVID_cases')
orskl_df_right = orskl_df1.merge(orskl_df2, how='left', on='COVID_cases')
orskl_df_outer = orskl_df1.merge(orskl_df2, how='outer', on='COVID_cases')

# Get locations, names & courses purchased
orskl_df_st_loc_enroll = orskl_df_st_loc.merge(orskl_df_enroll, how='left', on='student_id')

orskl_df_st_loc_enroll.to_csv("OutputFile.txt")
orskl_df_st_loc_enroll.to_csv("OutputFile.txt", index=False)
orskl_df_st_loc_enroll.to_csv("OutputFile.txt", index=False, sep='+')


import pandas as pd
orskl_df = pd.read_csv("OutputFile.txt", sep='+')
orskl_df1 = pd.DataFrame({'COVID_cases': [10, 20, 30, 40 , 50], 'country': ['USA', 'INDIA', 'UK', 'UAE', 'JAPAN']})
orskl_df2 = pd.DataFrame({'COVID_cases': [40, 50, 60], 'states': ['AP', 'TS', 'TN']})

orskl_concat = pd.concat([orskl_df1, orskl_df2], axis=0, sort=False)


import pandas as pd

orskl_dict_student = {
    'student_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'student_name': ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5', 'Student 6', 'Student 7',
                     'Student 8', 'Student 9', 'Student 10']
}

orskl_dict_location = {
    'student_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'student_location': ['India', 'India', 'India', 'USA', 'USA', 'UAE', 'UAE',
                     'UK', 'UK', 'India']
}

orskl_dict_enrollment = {
    'student_id': [1001, 1003, 1004, 1007, 1008, 1010],
    'course': ['PFB', 'PFB', 'PFB', 'DSS', 'DSS', 'PFB'],
    'enrollment_date': ['2019-04-20', '2019-04-12', '2019-04-20', '2019-03-12', '2019-03-02', '2019-04-15']
}


orskl_df_student = pd.DataFrame(orskl_dict_student)
orskl_df_location = pd.DataFrame(orskl_dict_location)
orskl_df_enrollment = pd.DataFrame(orskl_dict_enrollment)


# Get locations of each student
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge
orskl_df_student_location  = orskl_df_student.merge(orskl_df_location, how='inner',
                                                    on='student_id')

orskl_df_student_location_enrollment = orskl_df_student_location.merge(orskl_df_enrollment,
                                                                       how='left',
                                                                       on='student_id')
orskl_df2
orskl_df_student_location_enrollment.to_csv('OutputFile.txt', index=False, sep='|')

orskl_df2 = pd.read_csv('OutputFile.txt', sep='|')

# rows
orskl_df_concat = pd.concat([orskl_df_student, orskl_df_location], axis=0, sort=False)
# columns
orskl_df_concat = pd.concat([orskl_df_student, orskl_df_location], axis=1)

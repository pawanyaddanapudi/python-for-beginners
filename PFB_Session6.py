############# DICTIONARIES / KEY-VALUE / JSON ################

Orskl_dict = {'name': 'OrSkl',  'course': 'Python for Beginners', 'duration': 30, 'purpose': 'Training',
              'name': 'ORSKL2'}
orskl_list = ['OrSkl','Python for Beginners',30, 'Training']
# { key : value, ...}
orskl_list[1]
Orskl_dict['name']
Orskl_dict['course']
Orskl_dict['duration']

orsk_dict = {'name': 'OrSkl',  'course': 'Python for Beginners', 'duration': 30, 'purpose': 'Training'}

# Length of dictionaries
len(Orskl_dict)

# Read dictionary data
Orskl_dict['name']
Orskl_dict['purpose']

# Delete element in Dict
del Orskl_dict['course']
Orskl_dict

# Add new element in Dict
Orskl_dict['course'] = 'Python for Beginners'
Orskl_dict
Orskl_dict.pop('name')
Orskl_dict
Orskl_dict['name'] = 'OrSkl'
Orskl_dict
Orskl_dict['topics'] = 15
Orskl_dict

# Nested dictionaries
orskl_dict2 = {
'name': 'OrSkl',  'course': 'Python for Beginners', 'duration': 30, 'purpose': 'Training',
    'Contents': {
        'chapter1' : 'Introduction',
        'Topics1' : "What is Python, Why Python, ..",
        'Chapter2' : 'Setup',
        'Topic2' : 'Pycharm, Jupyter, Terminal, Anaconda, Spyder'
    }
}
orskl_dict2['Contents']['Topic2']

Orskl_dict2 = {'name': 'OrSkl', 'purpose': 'Training', 'course': 'Python for Beginners', 'duration': 30,
               'Contents': {
                   'chapter1': 'Introduction',
                   'Topics1': 'What is python, Why Python, ..',
                   'chapter2': 'Setup',
                   'topics2': 'Anaconda, spyder, pycharm, terminal'
               },
               'students': 100
               }
Orskl_dict2['Contents']
Orskl_dict2['Contents']['chapter2']

# Adding list into Dictionary
Orskl_dict['student_names'] = ['Student1', 'Student2', 'Student3', 'Student4']
Orskl_dict
Orskl_dict['student_names']
Orskl_dict['student_names'][0]
Orskl_dict['student_names'][3]

# Likewise you can add dict into list
Orskl_dict_list = [10, 20, 30, {'name': 'OrSkl', 'purpose': 'Training'}]
Orskl_dict_list[0]
Orskl_dict_list[3]
Orskl_dict_list[3]['purpose']

############# SETS ################
orskl_set = {'a', 'b', 'c', 'd'}
orskl_set[0]
# orskl_set[0]
orskl_set.add('e')
orskl_set

# cannot have duplicates
orskl_set.add('b')
orskl_set

# set shuffles values when there is a change to the elements
# You cannot access each element of set
len(orskl_set)

############# TUPLES ################
orskl_tuple = ('a', 'b', 'c')
orskl_tuple[0]
orskl_tuple[0:2]
orskl_tuple[::-1]
# Immutable object, cannot add or remove any element inside the tuple
# You cannot add or remove element in tuple
orskl_tuple.add('e')
Orskl_dict_list = Orskl_dict_list + ["Key"]

del orskl_tuple

############# DataFrames/Tables ################
import pandas as pd
# pip3 install pandas

orskl_dict3 = {'students': ['Student1', 'Student2', 'Student3', 'Student4'],
               'Location': ['India', 'USA', 'Canada', 'UAE']}
orskl_dict4 = {'students': ['Student1', 'Student2', 'Student3', 'Student4'],
               'Location': ['India', 'USA', 'Canada','']}

orskl_df2 = pd.DataFrame(orskl_dict4)
orskl_df = pd.DataFrame(orskl_dict3)
orskl_df2
orskl_df

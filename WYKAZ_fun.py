#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:26:16 2019

@author: michak
"""

#%% SEARCH AND DISPLAY RESULTS
def end_program():
    print('Program finished.')
    import sys
    sys.exit()
    
    
def load_database(excel_spreadsheet):
    import pandas as pd
    
    print('Loading database ...')
    xl = pd.ExcelFile(excel_spreadsheet)

    print('Ready !')        
    return xl


def prepare_dict(xl, sheetName, nameCol, pointsCol):

    # format: choose rows and columns 
    d = {'df': xl.parse(skiprows=[0,1], 
                        sheet_name=sheetName, 
                        usecols=[nameCol, pointsCol]),
         'sheetName': sheetName,
         'name': nameCol,
         'points': pointsCol}

    return d



def select_journals_or_conferences(d_jour, d_conf):
    '''
    Input:
    d_jour, d_conf   
        Prepared excel sheets in the form of two dictionaries with keys:
        - 'df'      - data frame with journals/conferencers
        - 'name'    - name of the column in the data frame df which contains 
                      names of journals / conferences
        - 'points'  - name of the column in the data frame df which contains 
                      points of journals / conferences
    d_jour contains data of journals
    d_conf contains data of conferences
    
    Output:
    Returns dictionary d with keys:
        - 'df'      - data frame with journals/conferencers
        - 'name'    - name of the column in the data frame df which contains 
                      names of journals / conferences
        - 'points'  - name of the column in the data frame df which contains 
                      points of journals / conferences
    '''
    # Choose conferences or journals
    print('Choose: ')
    print('1 - Journals')
    print('2 - Conferences ')
    print('0 - EXIT ')   
    
    correct_input = 0
    while(not(correct_input)):
        input1= input()
        if(input1 == '0'):
            correct_input = 1
            end_program()
        elif(input1 == '1'):
            print('Chosen JOURNALS !')
            d = d_jour
            correct_input = 1
        elif(input1 == '2'):
            print('Chosen CONFERENCES !')
            d = d_conf
            correct_input = 1
        else:
            print('Wrong choice ! Try again')
            
    return d




def input_limits():
    '''
    Output:
    MIN , MAX - lower and upper inclusive points values to limit the scope of 
                the search
    KEYS - of keywords to search in database
    correct_input - 0 if the input is incorrect, 1 if the input is correct
    '''
    MIN = 0
    MAX = 0
    KEYS = []
    
    print('Minimum points : ')
    input_min = input()
    print('Maximum points : ')
    input_max = input()
    print('(OPTIONAL) Partial name OR single keywords (separate with ; ) : ')
    input_keys = input()
    # suggested keywords:
    #  - neuro, neural, neuroscience, eeg, brain, cogni, bioinformatics
    
    try:
        MIN = int(input_min)
        MAX = int(input_max)
        KEYS = input_keys.split(";")
        if len(KEYS)>1 :
            KEYS = [s.replace(" ", "") for s in KEYS] 
        
        print(KEYS)
        
        correct_input = 1
    except:
        correct_input = 0
        print('Incorrect input! Try again !')

    return MIN, MAX, KEYS, correct_input




def search_data(d, MIN, MAX, KEYS):
    '''
    d - dictionary with keys:
        - 'df'      - data frame with journals/conferencers
        - 'name'    - name of the column in the data frame df which contains 
                      names of journals / conferences
        - 'points'  - name of the column in the data frame df which contains 
                      points of journals / conferences
    MIN , MAX - lower and upper inclusive points values to limit the scope of 
                the search
    KEYS - of keywords to search in names df column  
    
    Output:
        result - sorted dataframe with journal / conferences names matching 
                 MIN, MAX and KEYS
    '''
    import numpy as np
    
    
    # (points <= MAX) AND (point >= MIN) AND (KEY 1 OR KEY 2 OR ... KEY N)
    idx = (d['df'][d['points']] >= MIN) & (d['df'][d['points']] <= MAX )
    df_filt = d['df'][idx]
    #rows1 = test[conf_pointsCol]
    
    rowList = []
    for k in KEYS:
        x = list(np.flatnonzero(df_filt[d['name']].str.contains(k, case=False)))
        rowList += x
        
    # remove repeats
    rowList = list(set(rowList))
    
    #print(rowList)
    
    # display results
    result = df_filt.iloc[rowList]
    result = result.sort_values(by=d['points'], ascending=False)

    return result



def display_result(result):
#    print(result.to_string())
    import pandas as pd
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None, 'display.max_colwidth', -1):  # more options can be specified also
        print(result)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:25:59 2019

@author: michak


Search conferences or journals by name/keywords and filter by range of points.
Suggested keywords:
    - signal processing
    - networks
    - cereb
    - brain
    - neuro
    - eeg
    - electrophysiology
    - cognit
    
"""

#%%
from WYKAZ_fun import *

#%%

file = 'WYKAZ CZASOPISM 2019 USTAWA 2_0_WG_DYSCYPLINY.xlsx'

xl = load_database(file)

jour_sheetName = 'Czasopisma'
jour_nameCol = 'Tytuł 1' 
jour_pointsCol = 'Punkty'
conf_sheetName = 'Konferencje'
conf_nameCol = 'Tytuł konferencji' 
conf_pointsCol = 'Liczba punktów'

d_jour = prepare_dict(xl, jour_sheetName, jour_nameCol, jour_pointsCol)
d_conf = prepare_dict(xl, conf_sheetName, conf_nameCol, conf_pointsCol)


#%%

finish = 0
while(not(finish)):
    print('Choose: ')
    print('1 - Search')
    print('0 - EXIT ')  
    
    input1= input()
    if(input1 == '0'):
        finish = 1
        end_program()
    elif(input1 == '1'):
        print('Let\'s search !')
        d = select_journals_or_conferences(d_jour, d_conf)
        MIN, MAX, KEYS, correct_input = input_limits()
        result = search_data(d, MIN, MAX, KEYS)
        display_result(result)
    else:
        print('Wrong choice ! Try again')



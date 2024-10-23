#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 01:30:17 2017

@author: Enek0RS
"""

# Trainning Speed Numeric Keyboard - TSNK_C Console Mode version 

import os
import random
import time
import pandas as pd
import matplotlib.pylab as plt

nList = ['0','1','2','3','4','5','6','7','8','9']
listOfEntrys = []
correctInputs = []
counter = 0
answer = ''

for n in range(100):
    n = ''
    for i in range(10):
        n += random.choice(nList)
    listOfEntrys.append(n)
    
correctInputsTarget = len(listOfEntrys)

input('Press Enter to Start when you are Ready...')
timeStart = time.time()

while len(correctInputs) < correctInputsTarget:
    os.system('clear')
    while answer != listOfEntrys[counter]:
        answer = input(str(listOfEntrys[counter]) + '          #  ' + str(len(correctInputs)) + '/' + str(correctInputsTarget) + '\n\n\n')
    correctInputs.append(answer)
    counter += 1

eTime = time.time() - timeStart
eTimeMin = int(str(eTime / 60).split('.')[0])
eTimeSec = int(str(eTime % 60).split('.')[0])

print('Entrys Recorded: ' + str(len(correctInputs)) + '  ' + 'Time: ' + str(eTimeMin) + ':' + str(eTimeSec))

date_time = time.strftime('%d/%m/%Y %X')
strData = date_time + ',' + str(len(correctInputs)) + ',' + str(eTime) + '\n'

with open('tsnk_c_sessions.txt', 'a+') as f:
    f.write(strData)

with open('tsnk_c_sessions.txt', 'r') as original: data = original.read()
with open('tsnk_c_w_columns.txt', 'w') as modified:
    modified.write('Date,Entrys,Elapsed Time\n' + data)

tsnk_sessions_plotting_data = pd.read_csv('tsnk_c_w_columns.txt')
progression = list(tsnk_sessions_plotting_data['Elapsed Time'])

os.remove('tsnk_c_w_columns.txt')

#plt.ylim(min(progression) - 30, max(progression) + 30)
plt.xlabel('Trainning Sessions')
plt.ylabel('Time Elapsed Records (Seconds)')
plt.gca().invert_yaxis()
plt.title('TSNK Progression (100 Inputs)')
plt.plot(progression,'ko-')
plt.show()
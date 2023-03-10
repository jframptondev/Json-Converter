import sys
import os
import pandas as pd
from pandas import json_normalize
from pathlib import Path
import json

cont = True
while (cont is True):
    JsonName = input("Enter the Json name (without .json extension!): ")
    print (str(JsonName)+".json is this correct?")
    S = input("y/n : ")
    if S == 'y':
        print ("Processing Please Wait. . .")
        cont = False

p = Path('r',os.getcwd()+'\\'+JsonName+'.json')

with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())
    df = json_normalize(data)
    df.to_csv(os.getcwd()+'\\'+JsonName+'.csv', index=False, encoding='utf-8')



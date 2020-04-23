import os
import json

os.chdir("..")

with open("WeekTest.json") as jsons:
    data = json.load(jsons)

columnKey = ['date', 'name', 'score']

tablesKey = '|{0}|{1}|{2}|\n|---|---|---|\n'.format(columnKey[0], columnKey[1], columnKey[2])

for _date,val in data["WeekTest"].items():
    for _kid,_score in val.items():
        tablesKey += '|{0}|{1}|{2}|\n'.format(_date, _kid,_score)

with open('WeekTestScore.md', 'w') as f:
    f.write(tablesKey)

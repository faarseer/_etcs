import os
import json

os.chdir("..")

with open("WeekTest.json") as jsons:
    data = json.load(jsons)

columnKey = ['Date', 'Grade', 'Range','Name', 'Score']

tablesKey = '|{0}|{1}|{2}|{3}|{4}|\n|---|---|---|---|---|\n'.format(columnKey[0], columnKey[1], columnKey[2], columnKey[3], columnKey[4])

for _date,testlist in sorted(data["WeekTest"].items()):
    for test in testlist:
        _grade = test["Grade"]
        _range = test["Range"]
        for _name,_score in test["Score"].items() :
            tablesKey += '|{0}|{1}|{2}|{3}|{4}|\n'.format(_date, _grade, _range, _name,_score)

with open('WeekTestScore.md', 'w') as f:
    f.write(tablesKey)

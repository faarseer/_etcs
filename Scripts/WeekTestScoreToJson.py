import os
import json

#-*-coding: utf-8 -*-

os.chdir("..")

with open('WeekTest.json') as jsons:
    data = json.load(jsons)
    print(data["WeekTest"])

while True:
    print("date : (ex:200101) , if input Done, end.")
    date = input()
    if date == "Done":
        break
    print("\nname : ")
    name = input()
    print("\nscore : ")
    score = input()
    
    row = {date : {name : score}}
    print(row)
    
    if date in data["WeekTest"]:
        data["WeekTest"][date].update(list(row.values())[0])
        print("Update :  "+date)
        print(data["WeekTest"][date])

    else:
        data["WeekTest"].update(row)
        print("Make scores at new date : " + date)
        print(data["WeekTest"][date])

print("save? True or False")
save = input()
if(save == "True"):
    with open('WeekTest.json', 'w') as output:
        json.dump(data, output, ensure_ascii = False)

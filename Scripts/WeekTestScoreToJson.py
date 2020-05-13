import os
import json

#-*-coding: utf-8 -*-

os.chdir("..")

with open('WeekTest.json') as jsons:
    data = json.load(jsons)
    print(data["WeekTest"])

while True:
    print("need date,grade,range change or Done?: True or Done")
    change = input()
    if change == "Done":
        break
    if change == "True":
        print("date : (ex:200101) , if input Done, end.")
        date = input()
        if date == "Done":
            break
        print("Grade: , possible range : 중1, 중2")
        grade = input()
        print("Range:")
        _range = input()
    
    print("\nname : ")
    name = input()
    print("\nscore : ")
    score = input()
    
    row = {
            date : 
            [
                {
                    "Grade": grade,
                    "Range": _range,
                    "Score":
                    {
                        name : score
                    }
                }
            ]
        }
    print("new data: ")
    print(row)
    if date in data["WeekTest"] :
        isGR = False;
        for test in data["WeekTest"][date] :
            print(test)
            if (test["Grade"] == grade) and (test["Range"] == _range) :
                isGR = True
                if name in test["Score"] :
                    print("already exists : ")
                    print(test)
                    print("\nreplace True or False?")
                    replace = input()
                    if eval(replace) :
                        test["Score"][name] = score
                    if not eval(replace) :
                        test["Score"][name+" 1"] = score
                else :
                    test["Score"][name] = score
        
        if not isGR:
            data["WeekTest"][date].append(row[date][0])            

        print("Update :  "+date)
        print(data["WeekTest"][date])

    else:
        data["WeekTest"].update(row)
        print("Make test score at new date : " + date)
        print(data["WeekTest"][date])

print("save? True or False")
save = input()
if save == "True":
    with open('WeekTest.json', 'w') as output:
        json.dump(data, output, ensure_ascii = False, indent = 4, sort_keys = True)

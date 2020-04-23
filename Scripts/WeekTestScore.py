import pandas as pd
import numpy as np
import os

os.chdir("..")

df = pd.DataFrame(columns = ["name","date","score"])

while True:

    print("what is your name:")
    name = input()
    if name == "Done":
        break
    print("\ndate:(ex:200101)")
    date = input()
    print("\nscore: ")
    score = input()

    row = pd.DataFrame({"name":name, "date":date, "score":score}, index = [name])

    df = df.append(row)
    print(df)

excelname = "{}.xlsx".format(date)

if os.path.exists("{}.xlsx".format(date)) :
    _df = pd.read_excel(excelname, sheet_name = "Sheet1")
    _df = _df.append(df)    
    writer = pd.ExcelWriter("{}.xlsx".format(date), engine = "xlsxwriter")
    _df.to_excel(writer, sheet_name = "Sheet1", index = False)
    writer.save()

else : 
    writer = pd.ExcelWriter("{}.xlsx".format(date), engine = "xlsxwriter")
    df.to_excel(writer, sheet_name = "Sheet1", index = False)
    writer.save()

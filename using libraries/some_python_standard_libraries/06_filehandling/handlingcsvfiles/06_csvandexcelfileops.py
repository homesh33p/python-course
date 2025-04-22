import pandas as pd
import pathlib
from openpyxl import load_workbook

#reading csv file
# csvdata = pd.read_csv("samplecsvfile.csv")
# print(type(csvdata))
# headers = list(csvdata.columns)
# print(headers)
# print(csvdata)

# print("\n")

# accessing data:
# print(csvdata["Name"])
# print(csvdata["Name"][0])
# print(csvdata.loc[0,:])
# print(csvdata.iloc[0,:])
# print(csvdata.iloc[[0,3]])

'''
To print a specific row we have couple of pandas method

    loc - It only gets label i.e column name or Features
    iloc - Here i stands for integer, actually row number
    ix - It is a mix of label as well as integer

How to use for specific row

    loc

df.loc[row,column]

For first row and all column

df.loc[0,:]

For first row and some specific column

df.loc[0,'column_name']

    iloc

For first row and all column

df.iloc[0,:]

For first row and some specific column i.e first three cols

df.iloc[0,0:3]
'''

# #Modifiying a dataframe and saving to file:
# #lets say i want to add a new column: medal
# csvdata.loc[:,"Medal"] = ["Gold","Gold","Silver","Gold"]
# print(csvdata)

#Saving to file:
# csvdata.to_csv("modifiedcsvfile.csv")

#Reading excel files:
sampleExcelPath = pathlib.Path(r"sampleExlfile.xlsx")
sampleexcel = pd.ExcelFile(sampleExcelPath)
olympics = sampleexcel.parse('olympics')
mohalla = sampleexcel.parse("Mohalla")
print(olympics)
print(mohalla)
#
# #This is also loaded as dataframe, can do processing as dataframes allow
#
#Saving to a excel file:
olympics.to_excel("olympics.xlsx")
#
# #However if we just want to save to the same workbook as source excel file, use following
# #saving to the same excel file and add a new sheet:
#
book = load_workbook(sampleExcelPath)
writer = pd.ExcelWriter(sampleExcelPath, engine = 'openpyxl')
writer.book = book

#create a blank data frame and save to workbook
blankdf = pd.DataFrame()
blankdf.to_excel(writer, sheet_name = 'Colony')

# Save and close
writer.save()
writer.close()
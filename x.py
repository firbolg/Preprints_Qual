import csv
import pandas as pd
import os

directory = r'C:\Users\levi\source\repos\Preprints_Qual\Preprints_Qual'

for csv_file in os.scandir(directory):
    if csv_file.path.endswith(".csv"):
        df = pd.read_csv(csv_file)
        for column in df:
            code_category = df.loc[:, str(column)]
            not_nan = pd.notna(code_category)
            count = not_nan.values
            print(str(column) + ": " + str(sum(count)))
    else:
        continue 





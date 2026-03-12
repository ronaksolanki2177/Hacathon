import pandas as pd
from tabulate import tabulate

df = pd.read_csv("scholarships_dataset_1000.csv")

table = tabulate(df, headers="keys", tablefmt="grid", showindex=False)

with open("scholarships_table.txt", "w", encoding="utf-8") as f:
    f.write(table)
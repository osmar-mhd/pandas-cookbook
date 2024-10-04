# Getting started tutorials
import pandas as pd

# pandas data table representation

df = pd.DataFrame(
    {
        "Name":[
            "Braund, Mr. Owen Harris",
            "Allen, Mr William Henrry",
            "Bonnell, Miss. ELizabeth",
        ],
        "Age":[22, 35, 58],
        "Sex":["male","male","female"],
    }
)
print(df)

#I´m just interested in working with the data in the column Age

print(df["Age"])

# When selecting column of pandas DataFrame. the result is panda Series

# I want to know the maximum Age of the passengers
print(df["Age"].max())
import pandas as pd

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

# The describe method provides a quick overview of the numerical data in DataFrame
print(df.describe())
# You can create a Series from scratch as well:

import pandas as pd

ages = pd.Series([22,35,58], name = "Age")

print(ages)

# I want to know the maximum Age of the passengers
print(ages.max())

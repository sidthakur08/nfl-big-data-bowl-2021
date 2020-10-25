import pandas as pd
from tqdm import tqdm

num = [i for i in range(1,18)]
weeks = [f'data/week{n}.csv' for n in num]

print("Appending dataframes...")
total_df = []
for w in tqdm(weeks):
    total_df.append(weeks)

data = pd.concat(total_df).reset_index(drop=True)
print("Saving Dataframe...")
data.to_csv('data/all_tracking.csv',index=False)
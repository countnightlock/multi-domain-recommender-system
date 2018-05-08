import itertools
import ast
import numpy as np
import pandas as pd
from regression import get_coefficients

# Get theta and X
X = pd.read_csv("comb_regr_data_final.csv", sep=",")
theta = get_coefficients()
# theta = [[ 1, -0.01,  0.03390613, -0.00082851 ]]
y_pred = []


# Get names for reference
df = pd.read_csv("./datasets/content/small_combined_final.csv", usecols=["title"])

def get_title_from_id(idx):
    return df.iloc[idx]["title"]


# Make intermediate df to store id-pairs and similarities
pairs_and_simil = pd.DataFrame(data={
    "id_pair": X["id_pair"],
    "overall_simil": X["overall_simil"]
})

# Since data exists in batches of 1000 with the same idx1
batch_size = 1000

for i in range(11):
    # For all items in subset, idx1 is the same
    subset = pairs_and_simil[i * batch_size : (i+1) * batch_size]
    # print(subset.info())

    simils = np.asarray(subset["overall_simil"])

    # Go from first-last to tenth-last, in reverse
    indices = np.argsort(simils)[-1:-10:-1]

    print("Items similar to %s:" % (get_title_from_id(i)))
    for idx in indices:
        print("%4d - %s" % (idx, get_title_from_id(idx)))

    print("*" * 50)

X.to_csv("comb_regr_data_final.csv", index = False) 
import pandas as pd
import matplotlib.pyplot as plt

# load Excel dataset
df = pd.read_excel("Mantamonis_contamination.xlsx")

# count values in Preliminary Verdict column
counts = df["Preliminary Verdict:"].value_counts()

# create bar chart
counts.plot(kind="bar", figsize=(8,6))
plt.title("Preliminary Verdict Classification Counts")
plt.ylabel("Frequency")
plt.xlabel("Classification")

# save figure
plt.savefig("preliminary_classification.png", dpi=300, bbox_inches="tight")

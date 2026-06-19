# 1_SkinCancer_EDAandAnalysis_AbdulRahman.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from Skincancer_Analysis_Functions_AbdulRahman import chisq_res

#Load cleaned datasets
skc_df = pd.read_excel("cleaned_skc.xlsx")
skc_df_cc = pd.read_excel("cleaned_skc_cc.xlsx")

#POC variable
#White = White
#Everyone else = POC
skc_df["POC"] = np.where(
    skc_df["Racial Identity"] == "White",
    "White",
    "POC"
)

skc_df_cc["POC"] = np.where(
    skc_df_cc["Racial Identity"] == "White",
    "White",
    "POC"
)

print(skc_df["POC"].value_counts())
print(skc_df_cc["POC"].value_counts())

#---------------------------------------------------
#Research Question 1
#Is the average number of primary malignancies
#significantly different between POC and White patients?
#---------------------------------------------------

#Summary stats
rq1_stats = skc_df.groupby("POC")["num_primary_malignancies"].agg(
    ["mean", "std", "median", "max", "count"]
)

print("\nSummary Statistics")
print(rq1_stats)

# Extra professor-friendly outputs
print("\nDescribe Output")
print(skc_df.groupby("POC")["num_primary_malignancies"].describe())

print("\nMedian Output")
print(skc_df.groupby("POC")["num_primary_malignancies"].median())

# Boxplot
plt.figure(figsize=(8,5))

plt.boxplot(
    [
        skc_df.loc[skc_df["POC"] == "POC", "num_primary_malignancies"],
        skc_df.loc[skc_df["POC"] == "White", "num_primary_malignancies"]
    ],
    tick_labels=["POC", "White"]
)

plt.title("Number of Primary Malignancies by Race Group")
plt.xlabel("Race Group")
plt.ylabel("Number of Primary Malignancies")
plt.tight_layout()
plt.show()

#Independent t-test
poc_vals = skc_df.loc[
    skc_df["POC"] == "POC",
    "num_primary_malignancies"
]

white_vals = skc_df.loc[
    skc_df["POC"] == "White",
    "num_primary_malignancies"
]

t_stat, p_val = stats.ttest_ind(
    poc_vals,
    white_vals,
    equal_var=False
)

print("\nT-test Results")
print("T statistic:", t_stat)
print("P-value:", p_val)

#Difference in means
mean_diff = poc_vals.mean() - white_vals.mean()

#95% Confidence Interval
se = np.sqrt(
    (poc_vals.var(ddof=1) / len(poc_vals)) +
    (white_vals.var(ddof=1) / len(white_vals))
)

lower = mean_diff - 1.96 * se
upper = mean_diff + 1.96 * se

print("Difference in Means:", mean_diff)
print("95% CI:", (lower, upper))

#Research Question 2
#Chi-square analyses
#Test 1
print("\n--------------------------------")
print("Chi-square Test 1")
print("Race vs Tumor Location Risk")
print("--------------------------------")

chi2_1, p_1, dof_1, expected_1, table_1 = chisq_res(
    skc_df["M1_Location_risk"],
    skc_df["POC"]
)

print("\nChi-square Statistic:", chi2_1)
print("P-value:", p_1)
print("Degrees of Freedom:", dof_1)

#Test 2
print("\n--------------------------------")
print("Chi-square Test 2")
print("Race vs Cancer Type")
print("--------------------------------")

chi2_2, p_2, dof_2, expected_2, table_2 = chisq_res(
    skc_df["cancer_type"],
    skc_df["POC"]
)

print("\nChi-square Statistic:", chi2_2)
print("P-value:", p_2)
print("Degrees of Freedom:", dof_2)
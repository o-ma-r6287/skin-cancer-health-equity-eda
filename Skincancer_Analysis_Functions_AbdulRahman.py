#--------------------------------------------------------
# This file creates functions for analyses
#--------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import chi2_contingency
skc = pd.read_excel("cleaned_skc.xlsx")
skc_cc = pd.read_excel("cleaned_skc_cc.xlsx")

#---------------------------------------------------------------------------
#Linear Regression Function (Example)
#---------------------------------------------------------------------------

#def linreg(y, predictors, cat_predictors, df):
    #df[cat_predictors] = df[cat_predictors].astype("category")
    #formula = f"{y} ~ {"+".join(predictors)} "
    #lin_reg_model = ols(formula, data = df).fit()
    #print(lin_reg_model.summary())
    #return lin_reg_model

#Example of calling the function to run several linear regressions
#ttd_race = linreg(y = "m1_time_to_diagnosis",predictors = ["POC"], cat_predictors = ["POC"], df=skc_cc)
#num_malig_race = linreg(y = "num_primary_malignancies", predictors = ["POC", "Gender"], cat_predictors = ["POC", "Gender"], df = skc)
import pandas as pd
import numpy as np

skc_df = pd.read_excel("cleaned_skc.xlsx")
skc_df_cc = pd.read_excel("cleaned_skc_cc.xlsx")

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
#You create a chi-square function
#def chisq_res(resp_var, group_var)
def chisq_res(resp_var, group_var):

    #Print the counts for each variable
    print("\nResponse Variable Counts:")
    print(resp_var.value_counts())
    print("\nGroup Variable Counts:")
    print(group_var.value_counts())

    #Create contingency table to show both variables
    table = pd.crosstab(group_var, resp_var)

    #Chi-square test
    chi2, p, dof, expected = chi2_contingency(table)

    #Table
    print("\nContingency Table:")
    print(table)

    #Expected counts
    print("\nExpected Counts:")
    print(expected)

    return chi2, p, dof, expected, table


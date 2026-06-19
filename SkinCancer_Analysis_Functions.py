#--------------------------------------------------------
# This file creates functions for analyses
#--------------------------------------------------------
import pandas as pd
import numpy as np

from statsmodels.formula.api import ols
import statsmodels.api as sm
from scipy import stats
from statsmodels.formula.api import logit
from scipy.stats import chi2_contingency
skc = pd.read_excel("cleaned_skc.xlsx")
skc_cc = pd.read_excel("cleaned_skc_cc.xlsx")

#---------------------------------------------------------------------------
#Linear Regression Function (Example)
#---------------------------------------------------------------------------
def linreg(y, predictors, cat_predictors, df):
    df[cat_predictors] = df[cat_predictors].astype("category")
    formula = f"{y} ~ {"+".join(predictors)} "
    lin_reg_model = ols(formula, data = df).fit()
    print(lin_reg_model.summary())
    return lin_reg_model

#Example of calling the function to run several linear regressions
ttd_race = linreg(y = "m1_time_to_diagnosis",predictors = ["POC"], cat_predictors = ["POC"], df=skc_cc)
num_malig_race = linreg(y = "num_primary_malignancies", predictors = ["POC", "Gender"], cat_predictors = ["POC", "Gender"], df = skc)

#You create a chi-square function
#def chisq_res(resp_var, group_var)

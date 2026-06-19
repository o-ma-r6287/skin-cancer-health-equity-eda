# 0_SkinCancer_cleaning_ABDULRAHMAN.py
import pandas as pd
import numpy as np

#Load raw skin cancer dataset
df = pd.read_excel("skin_cancer-1.xlsx")

#COPY of OG df for cleaning
skc_df = df.copy()

#Recode categorical variables using dictionary of dictionaries
cat_maps = {
    "Racial Identity": {
        "Black or African American": "Black",
        "Black": "Black",
        "black": "Black",
        "Caucasian": "White",
        "White": "White",
        "Hispanic": "Other",
        "hispanic ": "Other",
        "Asian": "Other",
        "Other": "Other"
    },
    "Gender": {
        "M": "Male",
        "F": "Female"
    },

    "immuno_none": {
        1: "Not immunocompromised",
        0: "Immunocompromised"
    },

    "M1_Location_risk": {
        "Area H": "High Risk",
        "Area M": "Medium Risk",
        "Area L": "Low Risk"
    }
}

skc_df = skc_df.replace(cat_maps)

#Recode prior skin cancer into 0/1 integer variable
skc_df["prior_skin_cancer"] = skc_df["prior_skin_cancer"].replace({
    "No": 0,
    "Yes": 1
})

skc_df["prior_skin_cancer"] = skc_df["prior_skin_cancer"].astype(int)

#Binary of cancer variables

skc_df["num_cancers_binary"] = np.where(
    skc_df["num_primary_malignancies"] > 1,
    "More than one cancer",
    "One cancer"
)

#Complete dataset
#Only drop rows where m1_time_to_diagnosis is missing
skc_df_cc = skc_df.dropna(subset=["m1_time_to_diagnosis"])


# Save cleaned datasets in excel
skc_df.to_excel("cleaned_skc.xlsx", index=False)
skc_df_cc.to_excel("cleaned_skc_cc.xlsx", index=False)


#Final Check to make sure everything works
print("Original dataset shape:", df.shape)
print("Cleaned dataset shape:", skc_df.shape)
print("Complete case dataset shape:", skc_df_cc.shape)

print("\nRace categories:")
print(skc_df["Racial Identity"].value_counts())

print("\nGender categories:")
print(skc_df["Gender"].value_counts())

print("\nImmunocompromised categories:")
print(skc_df["immuno_none"].value_counts())

print("\nLocation risk categories:")
print(skc_df["M1_Location_risk"].value_counts())

print("\nPrior skin cancer categories:")
print(skc_df["prior_skin_cancer"].value_counts())

print("\nNumber of cancers binary:")
print(skc_df["num_cancers_binary"].value_counts())

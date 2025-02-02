import pandas as pd
import scipy.stats as stats

# Load the CSV file
df = pd.read_csv("google_analytics_data.csv")

# Ensure transactionRevenue is numeric and replace NaNs with 0 (users who did not convert)
df["transactionRevenue"] = pd.to_numeric(df["transactionRevenue"], errors="coerce").fillna(0)

# Separate groups
group_A = df[df["test_A_B"] == "A"]["transactionRevenue"]
group_B = df[df["test_A_B"] == "B"]["transactionRevenue"]

# Perform T-Test (hypothesis: Group B has a higher conversion rate than Group A)
t_stat, p_value = stats.ttest_ind(group_B, group_A, equal_var=False)

# Display results
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

# Interpretation of the p-value
alpha = 0.05
if p_value < alpha:
    print("Conclusion: There is statistical evidence that paid traffic converts more than organic traffic (Reject H0).")
else:
    print("Conclusion: There is not enough evidence to conclude that paid traffic converts more than organic traffic (Fail to reject H0).")

import pandas as pd
import scipy.stats as stats

# Load the CSV file
df = pd.read_csv("google_analytics_data.csv")

# Ensure transactionRevenue is numeric and replace NaNs with 0 (users who did not convert)
df["transactionRevenue"] = pd.to_numeric(df["transactionRevenue"], errors="coerce").fillna(0)

# Separate groups based on device category
group_A = df[df["test_device_type"] == "A"]["transactionRevenue"]
group_B = df[df["test_device_type"] == "B"]["transactionRevenue"]

# Perform T-Test (hypothesis: Group B (desktop) has a higher conversion rate than Group A (mobile))
t_stat, p_value = stats.ttest_ind(group_B, group_A, equal_var=False)

# Display results
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

# Interpretation of the p-value
alpha = 0.05
if p_value < alpha:
    print("Conclusion: Desktop users convert more than mobile users (Reject H0).")
else:
    print("Conclusion: There is no significant difference in conversion between desktop and mobile users (Fail to reject H0).")

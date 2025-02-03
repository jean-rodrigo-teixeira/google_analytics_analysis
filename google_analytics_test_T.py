import os
import pandas as pd
import scipy.stats as stats

# Get CSV file path from environment variable
csv_path = os.getenv("google_analytics_csv")

# Check if the environment variable is set
if not csv_path:
    raise ValueError("Error: The environment variable 'google_analytics_csv' is not set or is empty.")

# Check if the file exists
if not os.path.isfile(csv_path):
    raise FileNotFoundError(f"Error: The file '{csv_path}' was not found.")

# Load the CSV file
df = pd.read_csv(csv_path)

# Ensure transactionRevenue is numeric and replace NaNs with 0
df["transactionRevenue"] = pd.to_numeric(df["transactionRevenue"], errors="coerce").fillna(0)

# Count the number of samples in each group
count_A = df[df["test_device_type"] == "A"].shape[0]  # Mobile
count_B = df[df["test_device_type"] == "B"].shape[0]  # Desktop

# Determine the minimum sample size to balance the groups
min_sample_size = min(count_A, count_B)

# Balance the groups using random sampling
group_A_balanced = df[df["test_device_type"] == "A"].sample(n=min_sample_size, random_state=42)
group_B_balanced = df[df["test_device_type"] == "B"].sample(n=min_sample_size, random_state=42)

# Extract transaction revenue for balanced groups
revenue_A = group_A_balanced["transactionRevenue"]
revenue_B = group_B_balanced["transactionRevenue"]

# Perform T-Test (hypothesis: Desktop users convert more than mobile users)
t_stat, p_value = stats.ttest_ind(revenue_B, revenue_A, equal_var=False)

# Display results
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

# Interpret the p-value
alpha = 0.05
if p_value < alpha:
    print("Conclusion: Desktop users convert more than mobile users (Reject H0).")
else:
    print("Conclusion: No significant difference in conversion between desktop and mobile users (Fail to reject H0).")

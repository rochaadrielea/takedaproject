import pandas as pd
import numpy as np

# Define the number of rows for mock data
num_rows = 100

# Generate mock data
np.random.seed(42)  # Ensure reproducibility
data = {
    "Process_ID": [f"P-{i:03d}" for i in range(1, num_rows + 1)],
    "Step": np.random.choice(["Cutting", "Welding", "Assembly", "Painting", "Packaging"], size=num_rows),
    "Duration": np.round(np.random.uniform(5, 60, size=num_rows), 2),  # Duration in minutes
    "Defect_Rate": np.round(np.random.uniform(0.01, 0.15, size=num_rows), 4),  # Defect rate between 1% and 15%
    "Production_Yield": np.round(np.random.uniform(85, 99, size=num_rows), 2)  # Yield between 85% and 99%
}

# Create a DataFrame
mock_df = pd.DataFrame(data)

# Save to CSV file
mock_df.to_csv("manufacturing_data.csv", index=False)

# Display the first few rows of the DataFrame
print(mock_df.head())

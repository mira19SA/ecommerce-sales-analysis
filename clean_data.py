import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
# Read data
df = pd.read_csv("sales.csv")
# Before cleaning
print("Before cleaning:", df.shape)
# Cleaning
df = df.dropna()
df = df.drop_duplicates()
# After cleaning
print("After cleaning:", df.shape)
# Save cleaned data
df.to_csv("cleaned_sales.csv", index=False)
print("Data cleaned and saved")
# Analysis
total_sales = df["Sales"].sum()
avg_profit = df["Profit"].mean()
print("Total Sales:", total_sales)
print("Average Profit:", avg_profit)
# Sales by region
sales_by_region = df.groupby("Region")["Sales"].sum()
print(sales_by_region)
# Save to database
conn = sqlite3.connect("sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
conn.close()
# Visualization
sales_by_region.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig("sales_chart.png")
plt.show()

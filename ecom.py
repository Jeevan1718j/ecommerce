import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"/content/Ecommerce_Delivery_Analytics_New.csv")

# Convert Order Date & Time to datetime format
df['Order Date & Time'] = pd.to_datetime(df['Order Date & Time'], errors='coerce')

# Extract Year, Month, and Weekday
df['Year'] = df['Order Date & Time'].dt.year
df['Month'] = df['Order Date & Time'].dt.month
df['Weekday'] = df['Order Date & Time'].dt.day_name()

# ------------------ Unique Orders & Highest Multiple Orders ------------------
customer_order_counts = df.groupby("Customer ID")["Order ID"].nunique()
highest_orders = customer_order_counts.max()
customers_with_10_plus_orders = (customer_order_counts > 10).sum()

print(f"Highest multiple orders by a single user: {highest_orders}")
print(f"Total users with more than 10 orders: {customers_with_10_plus_orders}")

# ------------------ Platform-wise Order Analysis ------------------
platform_sales = df.groupby("Platform")["Order ID"].nunique().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=platform_sales.index, y=platform_sales.values, palette="viridis")
plt.xlabel("E-commerce Platform")
plt.ylabel("Unique Orders")
plt.title("Unique Sales Across Platforms")
plt.xticks(rotation=45)
plt.ylim(32000,35000)
plt.yticks(range(32000,35000,100))
plt.show()

# ------------------ Best and Worst Performing Platforms ------------------
best_platform = platform_sales.idxmax()
worst_platform = platform_sales.idxmin()

print(f"Best performing platform: {best_platform}")
print(f"Least performing platform: {worst_platform}")

# ------------------ Top 10 Highest & Bottom 5 Lowest Rated Products ------------------
product_ratings = df.groupby("Product Category")["Service Rating"].mean().sort_values(ascending=False)

print("Top 10 highest-rated products:")
print(product_ratings.head(10))

print("Bottom 5 lowest-rated products:")
print(product_ratings.tail(5))

# ------------------ Order Status Analysis (Delivered, Cancelled, Delayed) ------------------
if "Delivery Delay" in df.columns:
    delivery_status_counts = df["Delivery Delay"].value_counts(normalize=True) * 100

    plt.figure(figsize=(8, 5))
    sns.barplot(x=delivery_status_counts.index, y=delivery_status_counts.values, palette="coolwarm")
    plt.title("Order Status Analysis")
    plt.xlabel("Order Status")
    plt.ylabel("Percentage (%)")
    plt.show()

    print("Order Status Analysis (Percentage):")
    print(delivery_status_counts)
else:
    print("Column 'Delivery Delay' not found in dataset!")
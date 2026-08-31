import pandas as pd


data = {
    "product": [
        "Laptop",
        "Mouse",
        "Notebook",
        "Pen",
        "Phone",
        "Eraser"
    ],

    "category": [
        "Electronics",
        "Electronics",
        "Stationery",
        "Stationery",
        "Electronics",
        "Stationery"
    ],

    "quantity": [5, 20, 50, 100, 8, 30],

    "price": [50000, 500, 40, 10, 30000, 15]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


df["total_sales"] = df["quantity"] * df["price"]

print("\nDataFrame with Total Sales:")
print(df)



category_summary = df.groupby("category").agg(
    total_quantity=("quantity", "sum"),
    average_price=("price", "mean"),
    number_of_products=("product", "count"),
    total_sales=("total_sales", "sum")
)

print("\nCategory Summary:")
print(category_summary)



highest_sales_category = category_summary["total_sales"].idxmax()

print("\nCategory with Highest Total Sales:")
print(highest_sales_category)


sorted_products = df.sort_values(
    "total_sales",
    ascending=False
)

print("\nProducts Sorted by Total Sales:")
print(sorted_products)
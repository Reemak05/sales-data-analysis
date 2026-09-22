import pandas as pd

df=pd.read_csv("data/sales.csv")

df["revenue"] = df["price"] * df["quantity"]

#Basic information
print("----DATA INFORAMTION----")
print("First 5 rows: ", df.head())
print("Rows: ",df.shape[0])
print("Columns: ", df.shape[1])


#Sales analysis
print("\n---SALES ANALYSIS---")

total_revenue = df["revenue"].sum()
average_price = df["price"].mean()

print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Price: ${average_price:.2f}")


#Best Selling Product
product_sales = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
best_product = product_sales.idxmax()
print("Best Selling Products is :{best_product}")


#Revenue by City and city with highest revenue
print("---Revenue by City---")
revenue_by_city = (df.groupby("city")["revenue"].sum().sort_values(ascending=False))
print(revenue_by_city)
best_city = revenue_by_city.idxmax()
print("Citywith highest revenue:", best_city )


#Revenue by Category
print("---Revenue by Category---")
revenue_by_category = (df.groupby("category")["revenue"].sum().sort_values(ascending=False))
print(revenue_by_category)


#Most Expensive Product
most_expensive = df.loc[df["price"].idxmax()]
print("\n---Most Expensive Product---")
print("product: ", most_expensive["product"])
print("price: $", most_expensive["price"])


#Most Cheapest Product
most_cheapest = df.loc[df["price"].idxmin()]
print("\n---Most Cheapest Product---")
print("product: ", most_cheapest["product"])
print("price: $", most_cheapest["price"])


#Total Quantity Sold
total_quantity = df["quantity"].sum()
print("---Total Quantity Sold---")
print(total_quantity)


#Product with Price >100
expensive_product = df[df["price"]>100]
print("\n---Product with Price > 100---")
print(expensive_product)

#Final Summary
print("------------------------------------")
print("------SALES ANALYSIS SUMMARY--------")
print("------------------------------------")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Price: ${average_price:.2f}")
print(f"Best Selling Products is :{best_product}")
print(f"Citywith highest revenue:", best_city )
print("Most expensive Product: ", most_expensive["product"])
print("Most Cheaped Product: ", most_cheapest["product"])


    


import csv

sales =[]

with open("data/sales.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = float(row["price"])
        row["quantity"] = int(row["quantity"])

        row["revenue"] = row["price"] * row["quantity"]

        sales.append(row)

print(sales)

total_revenue = sum(row["revenue"] for row in sales)
print("Total Revenue:", total_revenue)

number_of_order = len(sales)
print("Number of Orders:", number_of_order)

average_order = total_revenue / number_of_order
print("Average Order Value:", round(average_order,2))

product_quantity = {}

for row in sales:
    product = row["product"]
    quantity=row["quantity"]
    if product not in product_quantity:
        product_quantity[product] = 0
    product_quantity[product] += quantity

best_product = max(
    product_quantity,
    key = product_quantity.get
)

print("Best-Selling Product:", best_product)
print("Units Sold:", product_quantity[best_product])

city_revenue = {}

for row in sales:
    city = row["city"]
    revenue = row["revenue"]

    if city not in city_revenue:
        city_revenue[city] = 0

    city_revenue +=revenue

print("\nRevenue by City:")

for city, revenue in city_revenue.items():
    print(city, ":", round(revenue,2))




import csv

def load_sales(filename):
    sales = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["price"] = float(row["price"])
            row["quantity"] = int(row["quantity"])
            row["revenue"] = row["price"] * row["quantity"]

            sales.append(row)

    return sales


def calculate_total_revenue(sales):
    return sum(row["revenue"] for mow in sales)

def fint_best_product(sales):
    product_quantity = {}

    for row in sales:
        product = row["product"]
        quantity=row["quantity"]
        if product not in product_quantity:
           product_quantity[product] = 0
        product_quantity[product] += quantity

    return max(
      product_quantity,
      key = product_quantity.get
    )

def main():
    sales = load_sales("data/sales.csv")

    total_revenue = calculate_total_revenue(sales)
    best_product = fint_best_product(sales)

    print("===SALES ANALYZER===")
    print(f"Total Revenue: ${total_revenue:2f}")
    print(f"Best-Selling Product: {best_product}")

if __name__ == "__main__":
    main()


    


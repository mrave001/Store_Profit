
# Problem Statement
""" St. Bernard Corner store sells products in 3 different counties, the taxes in Miami-Date county
is 6%, in Broward is 7% and in palm beach is 8%. The Product is described by the brand name, 
product name and the cost price. St. Bernard marks up the product price by 25% in Miami Dade county,
and 30% each in palm beach and Broward county. If they sold 100 of one product in each of the 3 
counties, what is their total profit if the cost price of the product is $30. Implement using
object-oriented design and principles."""

class Products:
    
    def __init__(self, productname, brandname, costprice):
        self.productname = productname
        self.brandname = brandname
        self.costprice = costprice

    def profit(self, numofproducts, countyrate, markup):
        # St Bernard cost: (num of inventory products * cost price) + inventory taxes 
        cost = (numofproducts * self.costprice) + ((numofproducts * self.costprice) * countyrate)
        productprice = (self.costprice * markup)
        
        # St Bernard revenue: (num of inventory products * product price) + customer sales taxes
        revenue = (numofproducts * productprice) + ((numofproducts * productprice) * countyrate)
        
        # profit = revenue - cost
        return revenue - cost

# Test Example 
productname = input("Enter a Product name: ") 
brandname = input("Enter a Brand name: ")
miami = Products(productname, brandname, 30)
broward = Products(productname, brandname, 30)
palmbeach = Products(productname, brandname, 30)
miami_profit = miami.profit(100, 0.06, 1.25)
broward_profit = broward.profit(100, 0.07, 1.30)
palmbeach_profit = palmbeach.profit(100, 0.08, 1.30)

print(f"The total profit for {productname} {brandname} in Miami-Dade is {miami_profit} dollars")
print(f"The total profit for {productname} {brandname} in Broward is {broward_profit} dollars")
print(f"The total profit for {productname} {brandname} in Palm beach is {palmbeach_profit} dollars")

profits = [miami_profit, broward_profit, palmbeach_profit]
sum = 0
for x in profits:
    sum = sum + x
print(f"Total profit is in all three counties is {sum} dollars")



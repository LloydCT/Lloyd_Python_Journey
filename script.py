lovely_loveseat_description = """Lovely Loveseat. Tufted 
polyester blend on wood. 
32 inches high x 40 inches 
wide x 30 inches deep. Red 
or white."""

lovely_loveseat_price = 254.00

stylish_settee_description = """Stylesh Settee. Faux 
leather on birch. 29.50 
inches high x 54.75 inches 
wide x 28 inches deep.
Black."""

stylish_settee_price = 180.50

luxurious_lamp_description = """Luxurious Lamp. Glass and 
iron. 36 inches tall.
Brown with cream shade."""

luxurious_lamp_price = 52.15

# Sales tax is 8.8%
sales_tax = .088

# The first customer ever, they did not purchase anything yet. 
customer_one_total = 0

# Description of the items my first customer purchases.
customer_one_itemization = ""

# Customer purchased one of our lovely loveseats
customer_one_total += lovely_loveseat_price

# Adding item description
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
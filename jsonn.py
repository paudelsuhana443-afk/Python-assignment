# Parse a JSON file representing product details (name,price,quantity) and display the details in tabular form.
import json

products=[
    {
        "name":"Pen",
        "price":20,
        "quantity":2
    },
    {
      "name":"Copy",
      "price":100,
      "quantity":3
    },
    {
      "name":"Whiteboard",
      "price":500,
      "quantity":5
    }
]

with open("products.json","w") as file:
    json.dump(products,file)

print("JSON file created successfully..")

with open("products.json","r")as file:
    data=json.load(file)

print(f"{'Name':<15}{'Price':<10}{'Quantity':<15}")
for item in data:
    print( f"{item['name']:<15}{item['price']:<10}{item['quantity']:<10}")
    

print("Suhana Paudel")

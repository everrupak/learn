customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True,
    }
print(customer)
print(customer["name"])
print(customer.get("name"))
print(customer.get('birthdate'))
print(customer.get("birthdate","Jan 1, 1980"))
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1, 1980"
print(customer)
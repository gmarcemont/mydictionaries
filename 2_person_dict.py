person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# name of second child
print(person.get["children"][1])

# name of cat
print(type(person["pets"]))

# use a loop to list each child
for i in person["children"]:
    print(i)

# type of pet: dog name: Fiao
for i, j in person["pets"].items():
    print(f"Type of pet: {i} name of pet: {j}")

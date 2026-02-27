info = {
    "name" : "Bhagya Patel", #str
    "city" : "Unjha", #str
    "qualification": "Btech",
    "age" : 20, # int
    "salary": 10.5, # float
    "married": False, # Bool
    "favourites" : ["Learning", "movies", 18]
}

print("I live in",info["city"])
print(info.get.__doc__)
print("I love ", info.get("favourites","Not Found"))

info.update({"University": "Ganpat University"})

print(dir(info))


for key,value in info.items():
    print(key,value)
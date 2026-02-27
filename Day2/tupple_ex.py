# Tuple banane ka 1la tareeka
cloud_tuple = ("aws", "azure", "gcp", "aws")

print(type(cloud_tuple))
print(cloud_tuple)

# indexing allowed
print("First Cloud:", cloud_tuple[0])
print("Last Cloud:", cloud_tuple[-1])

#Tuple is Immutable
# cloud_tuple[0] = "ibm"   # ERROR

print("Length of tuple is:", len(cloud_tuple))

print(dir(cloud_tuple))
print(cloud_tuple.count.__doc__)

# iterate tuple
for cloud in cloud_tuple:
    if cloud == "aws":
        print(f"{cloud} Market Leader")
    elif cloud == "azure":
        print(f"{cloud} Microsoft Cloud")
    else:
        print(f"{cloud} Other Cloud")
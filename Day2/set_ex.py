# first technique to create set
cloud_set = {"aws", "azure", "gcp", "aws", "ibm"}

print(type(cloud_set))
print(cloud_set)   # duplicate "aws" automatically removed

# second technique to create set
numbers = set([1, 2, 3, 4, 2, 1])
print(numbers)   # duplicates are removed

# add element
cloud_set.add("alibaba")
print(cloud_set)

# remove element
cloud_set.remove("ibm")
print(cloud_set)

print("Length of set is:", len(cloud_set))

print(dir(cloud_set))
print(cloud_set.add.__doc__)
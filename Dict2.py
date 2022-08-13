data = {"A": 10,"B": 20,"C": 30,"D": 40,"E": 40,"D":50,51: "F"}
# if there are duplicate keys 10,20... then there is updated / last value
# data of duplicate is allow
#heterogenous

print("Data is: ",data)
print("Type is: ",type(data))
print("Length is: ",len(data))

#print("Index ",data[1])  we cannot access index

print(data["A"])

#for i in range(len(data)):  #indexing cannot do.

for i in data:
	print(i,data[i])


data = {"Even" : [2,4,6,8],"Odd" : [1,3,5,7],"Other" : [11.5,4.5]}

print(data["Even"][0])  #2 ASA ACCORDING INDEX

for keys in data:
	print(keys)
	for i in data[keys]:
		#print(keys[i])  o d d   e v e n   o t h e r
		print(i) # 2 4 6 8 1 3 5 7 11.5  4.5

print("Data NEW")

for keys in data:
	print(keys,end = " ")
	for i in range(len(data[keys])):
		print(data[keys][i],end = " ")
	print(" ")
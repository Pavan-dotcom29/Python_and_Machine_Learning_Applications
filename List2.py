'''Program : Accept list and show output by using Iterative loops.
   1. list
   2. indexed
   3. sequential
   4. Data is mutable
   5. list is mutable
   6. Duplicates are allowed
   7. Hetrogenous'''

Data = [11,21,51,121]

print("Data using while loop")
i = 0

while(i<len(Data)):
	print(Data[i])
	i = i+1

print("Data using for loop")

for i in range(len(Data)):
	print(Data[i])
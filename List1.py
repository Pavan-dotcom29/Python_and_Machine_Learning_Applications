'''1. list
   2. indexed
   3. sequential
   4. Data is mutable
   5. list is mutable
   6. Duplicates are allowed
   7. Hetrogenous'''

Data = [11,21,51,121,5.15]   #list
print("Actual Data is :  ",Data)
print("Data Type is:   ",type(Data))
print("Data Type len:  ",len(Data))

print("Data from 0th index:  ",Data[0])
print("Data from 3rd index:  ",Data[3])

Data[0] = 12  
print("New Data is:  ",Data[0])

Data.append(151)  #insert at last
print("New data is ::  ",Data)

Data.insert(4,3.14)
Data.insert(3,50)
Data.insert(2,51)   #duplicate allowed
print(Data)
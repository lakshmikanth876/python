num = [2,5,6,1,8,7,27,12]
name = ["donkey","monkey","apple","biscuit"]
#num.extend(name)#it appends 2nd list to the 1st list 
print(num)
print(name)
num.sort()#sort function is to sort the elements in the list
print(num)
name.sort()
print(name)
num.append(23)#it appends element in last position
print(num)
num.insert(1,253)#it appends element in the index value wich is declared by the user
print(num)
num.remove(253)#it removes the particular element which is mentioned in the function
print(num)
print(num.index(23))
num.pop(8)#it removes the element based on the index value here it wont bother about original value
print(8)
print(num.count(8))#this function is used to count the count the elements upto the element which is mentioned in the function
num.clear()#this function is used to clear the entire data in the list
print(num)
name1 = name.copy()#this is used to copy the entire vales in the list
print(name1)
'''Given a list iterates it and counts the occurrence of each element and create a dictionary to show the count
of each element
original list[11,45,8,11,23,45,45,89]
printing count of each item[11:2,45:3,8:1,23:2,89:1]'''
list1=[]
n=int(input("Enter the number of elements:"))
for i in  range(0,n):
    list1.append(int(input(f"Enter the {i+1}th element: ")))
print("The original list is:",list1)
frequency={}
for num in list1:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1   
print("Count of numbers: ",frequency)             

     
    
'''Program to create two lists with even numbers and odd numbers from a given list'''
even=[]
odd=[]
list1=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    list1.append(int(input(f"Enter the {i+1}th element:")))

for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("the even list is",even)
print("the odd list is",odd)                
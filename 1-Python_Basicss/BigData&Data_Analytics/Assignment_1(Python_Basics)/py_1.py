''' Write a program to make an unordered symmetric list then reverse,sort the elements of the given list in
ascending and descending'''

num =[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    num.append(int(input(f"Enter the {i+1} th element: ")))
num.reverse()
print("the reversed list is:",num)   
num.sort() 
print("the sorted list is:",num) 
num.sort()
print("the ascending list is:",num)       
num.sort(reverse=True)
print("the descending list is:",num)    
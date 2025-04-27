'''Create a list of month names and print the last 3 characters short names of this month list'''
month_names=[]
short_month_names=[]
n=int(input("Enter the numbers of months:"))
for i in range(0,n):
    month_names.append(input("Enter the month name:"))
for i in month_names:
        short_month_names.append(i[0:3])
print(short_month_names)        
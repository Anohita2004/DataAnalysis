'''Create a program to find out the count of vowels and consonants of given string'''

str1=input("enter the string")
vowel=0
consonant=0
for i in str1:
    if i=='a' or i=='e'or i=='i' or i=='o' or i=='a' or i=='u'or i=='A' or i=='E'or i=='I' or i=='O'or i=='U':
        vowel+=1
    else:
        consonant+=1
print(f"the number of vowels are:{vowel} and the number of consonants are {consonant}")            
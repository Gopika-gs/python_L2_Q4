from collections import Counter
string = input("Enter the string : ")
print ("Repeated character in the string : ")
for i in string:
    count = Counter(string)
print(count)


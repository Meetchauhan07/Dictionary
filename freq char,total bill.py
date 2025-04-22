#dictionary containing frequency of each character occurring in the string.
s = input("Enter string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
'''
output:
Enter string: meet
{'m': 1, 'e': 2, 't': 1}
'''
#Two dictionaries compute the total bill.
price = {"apple": 25, "banana": 20, "milk": 100}
quantity = {"apple": 1, "banana": 4, "milk": 2}
total = 0
for item in quantity:
    total += price.get(item, 0) * quantity[item]
print("Total Bill:", total)
'''
output:
Total Bill: 305
'''

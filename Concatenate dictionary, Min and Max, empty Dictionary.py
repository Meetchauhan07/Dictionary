#concatenate Dictionary
d1 = {"a": 'ram'}
d2 = {"b": 'jeet'}
d3 = {"c": 'dwij'}
d4 = {**d1, **d2, **d3}
print(d4)
'''
output:
{'a': 'ram', 'b': 'jeet', 'c': 'dwij'}
'''
#check whether a dictionary is empty or not.
d = {}
print("Empty" if not d else "Not Empty")
'''
output:
Empty
'''
#Create a dictionary with dept no, employee roll no. and salary.find min and max.
data = {"HR": [50000, 1000], "IT": [250000, 25800, 92000], "Sales": [20000]}
for dept in data:
    print(dept, "Min:", min(data[dept]), "Max:", max(data[dept]))
'''
output:
HR Min: 1000 Max: 50000
IT Min: 25800 Max: 250000
Sales Min: 20000 Max: 20000
'''

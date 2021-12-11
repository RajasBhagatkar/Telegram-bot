import math

x = float(0.123)
y = int(2)
# print((x * y))
string = '61,160.33'

string = string.replace(',','')
# print(math.floor(string))
string = float(string)
print(type(string))

import re

# match a password that is 8 char long and ends with number 8

pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
string = 'Lucian'
pattern2 = re.compile(r'[A-Za-z0-9#$%@]{8,}\d')
password = 'yhsnckdj5463#8'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)

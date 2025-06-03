# Enter your code here
s=input()
count_hyphen = s.count('-')
new_str='-'*count_hyphen + s.replace('-', ' ')
print(new_str)
print("count of extra spaces")
count_spaces=new_str.count(' ')
new_str=new_str.replace('     ',' ')
print(new_str)
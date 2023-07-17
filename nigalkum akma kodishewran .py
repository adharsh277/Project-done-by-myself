lst = ['what is capital of India', 'a. delhi', 'b. mumbai', 'c. chennai', 'd. kolkata', 'a']

d=lst[0:5]
for i in d:
  print(i)
b = input('choose correct option: ')
if b==lst[5]:
  print('correct answer')
else:
  print('wrong answer')

import time
t= time.strftime('%h:%M:%s')
hour=int(time.strftime('%H'))
hour=int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<12):
  print("good morning")
elif(hour>=12 and hour<17):
  print("good afternoon")
if(hour>=17 and hour<0):
  print("good night")

from random import randint

#make an empty list
l = []

#generate a list of 50 random numbers between 0 and 100 and appends to the list
for i in range(50):
  x = randint(0,100)
  l.append(x)
#print the random number list
print(l)

#create a function that finds the minimum number in random number list
def find_minimum(l):
  #set minimum number to 0, the highest possible number
  mini_num = 100
  for i in l:
    #check the numbers in r and compares to mini_num
    #if i is larger than mini_num, replace mini_num with i
    if(i < mini_num):
      mini_num = i
  #returns the minimum value
  return mini_num

#print minimum number
#call the function
print("Minimum number in the list:", find_minimum(l))

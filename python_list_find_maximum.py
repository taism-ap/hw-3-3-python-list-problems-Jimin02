from random import randint

#make an empty list
l=[]

#generate a list of 50 random numbers between 0 and 100 and appends to the list
for i in range(50):
  x = randint(0,100)
  l.append(x)
#print the random number list
print(l)

#create a function that finds the maximum number in random number list
def find_maximum(l):
  #set maximum number to 0, the lowest possible number
  max_num = 0
  for i in l:
    #check the numbers in r and compares to max_num
    #if i is larger than max_num, replace max_num with i
    if(i > max_num):
      max_num = i
  #returns the maximum value
  return max_num

#print maximum number
#call the function
print("Maximum number in the list:", find_maximum(l))

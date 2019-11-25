from random import randint

#make an empty list
l = []

#generate a list of 50 random numbers between 0 and 100 and appends to the list
for i in range(50):
  x = randint(0,100)
  l.append(x)
#print the random number list
print(l)

#take in a integer value from the user
input_num = int(input("Put a number between 0 and 100 you want to set: "))

#create a function that take in some integer value and place all of the elements which are smaller on one side of the list, leaving the larger elements on the other
def partition(l,input_num):
  #make an empty list that has smaller numbers than the user's input
  smaller = []
  #make an empty list that has larger numbers than the user's input
  larger = []
  #make an empty list that will have list partitioned
  result = []
  
  #goes through the numbers in the list l
  for i in l:
    #if i is smaller than the user's input, append it to smaller
    if (i < input_num):
      smaller.append(i)
    #if i is larger than the user's input, append it to larger
    elif (i > input_num):
      larger.append(i)
  
  #add smaller list and larger list to result list
  result = smaller + larger
  #return result list
  return result

#call the fuction and partitioned list to result
result = partition(l,input_num)
#print result
print(result)

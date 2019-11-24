from random import randint

#make an empty list
l = []

#generate a list of 50 random numbers between 0 and 100 and appends to the list
for i in range(50):
  x = randint(0,100)
  l.append(x)
#print the random number list
print(l)

#create a function to find the number in the list
def find_number(l):
  #count the number of times an integer appears
  count = 0
  #add a count each time the user's input integer in the list
  for i in l:
    if(i == num):
      count += 1
  #return resulting count
  return count

#recive number from user and check how many times that number is in the list
num = int(input("Put a number between 0 to 100 you want to search: "))

#call the function
count = find_number(l)
#print count
print(count)

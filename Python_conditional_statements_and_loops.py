
# coding: utf-8

# In[ ]:

###Python conditional statements and loops [44 exercises
####https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php


# In[ ]:

##1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
for i in range(1500,1700,1):
    if i%7==0 and i%5==0:
        print(i)


# In[ ]:

#2Write a Python program to convert temperatures to and from celsius, fahrenheit. 
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
#Expected Output : 
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius 

CF=input("Enter F or C:")
T=input("Enter the  temp:")
if CF.upper()=='C':
    tp=int(T)/5*9+32
    print(str(tp)+"in Fahrenheit")
elif CF.upper()=='F':
    tp=(int(T)-32)/9*5
    print(str(tp)+"in Celsius")
          
          
      


# In[1]:

#3. Write a Python program to guess a number between 1 to 9. 
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
#on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random
guess=0
while guess !=1:
    K=random.randint(1,9)
    user=input ("take a guess 1 to 9:") 
    if user != K:        
        continue
    else:
        print("Well guessed!")
        guess=1
    


# In[16]:

#44. Write a Python program to construct the following pattern, using a nested for loop.
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*
Mys=''
for i in range(1,9):
    Mys+='*'
    print(Mys)
for i in range(9,1,-1):
    print(Mys[0:i])
    


# In[22]:

#5. Write a Python program that accepts a word from the user and reverse it. 
Wd=input("give me a word:")
MV=''
Jl=len(Wd)-1
for i in range(Jl,-1,-1):
    MV+=Wd[i]
print(MV)


# In[29]:

#6. Write a Python program to count the number of even and odd numbers from a series of numbers. 
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#Expected Output : 
#Number of even numbers : 5
#Number of odd numbers : 4

numbers=(1,2,3,4,5,6,7,8,9)
JD=len(numbers)+1
Even=""
Odd=""
for i in range(1,JD,1):
    if numbers[i-1]%2==0:
        Even+=str(numbers[i-1])+" "
    else:
        Odd+=str(numbers[i-1])+" "
        

print("Number od even number:"+str(Even))
print("Number od odd number:"+str(Odd))


# In[ ]:

#7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]



# coding: utf-8

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[87]:

print([x for x in range(2000,3201) if (x%7 ==0 and x%5 != 0)])


# Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

# In[94]:

def fact(num):
    prod = 1
    for i in range(1,num+1):
        prod = prod*i
    print(prod)        
    
fact(0)    


# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# In[102]:

def gdict(num):
    dict={}
    for i in range(1,num+1):
        dict[i] = i**i     
    print(dict)   
    
gdict(8)


# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# In[107]:

def seq(*args):
    print(list(args))
    print(tuple(args))
    
seq(2,3,4,5,6)    


# Define a class which has at least two methods:
# getString: to get a string from console input printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# In[118]:

class Strng():
    def __init__(self):
        self.s=''
    def getString(self):
        self.s = input('Pleae enter a string')
    
    def printString(self):
        print(self.s)


# In[120]:

obj = Strng()
obj.getString()
obj.printString()


# In[ ]:




# In[ ]:




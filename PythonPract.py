
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


# Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in 
# a comma-separated sequence.
# Example: 100,150,180
# The output of the program should be: 18,22,24

# In[126]:

def fun(C=50,H=30,*args):
    lst = [round(((2*x*C)/H)**(0.5)) for x in args]
    print(lst)

fun(50,30,100,150,180)    


# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,..,Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

# num1 = 3
# num2 = 5
# lst = [list(map(lambda x:x*i,list(range(0,5)))) for i in range(0,num1)]
# print(lst)

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world
# 

# In[171]:

def ssort(*arg):
    list(arg).sort()
    print(lst)

ssort('without','hello','bag','world')


# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# In[7]:

def cap(*arg):
    print(arg)
     
cap('Hello world \n Practice makes perfect')    


# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# In[7]:

def fun():
    sent = 'hello world and practice makes perfect and hello world again' #input('Enter the sentence')
    lstsent = list(set(sent.split(' ')))
    lstsent.sort()
    snt = " ".join(lstsent)
    print(snt)
    
fun()    


# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# In[18]:

def fun(*args):
    l = ['1' if x%5 ==0 else '0' for x in args]
    snt ="".join(l)
    print(snt)

fun(100,11,1010,1001)


# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[24]:

def fun():
    l = [x for x in range(1000,3001) if x%2 == 0]
    print(l)
        
#fun()    


# Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: hello world! 123 
# Then, the output should be: LETTERS 10 DIGITS 3

# In[44]:

def fun(strg):
    l=[1 for x in strg.replace(' ','') if x.isnumeric()]
   # print(f'LETTERS {len(strg.replace(' ','')}))
    print(f'DIGITS {sum(l)}')
    
fun('hello world! 123')


# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# In[48]:

def fun(strng):
    upp = [1 for x in strng if x.isupper()]
    print(upp)
fun('Hello world!')


# In[45]:

l = [2,4,2,5,7,2,1]
print(l.count(2))


# In[ ]:

---------------------


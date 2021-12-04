# Why python is called a scripting language? comment line
# python reads the code line by line and gives the output line by line
# Why python is dynamic??
# there is no need to mention the data type.
##It doesn't know about the type of the variable until the code is run.
# So declaration is of no use and the type of the variable is determined only
# during runtime.
print(2)
print(0.002)
# ()=parenthesis
print('pune')
print("hello pune")
print('2')
print(type('2'))
print(type(2))
print('2'+'2')
print(type('pune'))
print('I live in pune')
#Boolean value (True,False) (1,0)
#Numbers
#float,integer
#type function will give the data type of variable.
print(100)
print(0.000000056)
#working with numbers
#Addition
#add 2 integers
#there is no need to declare data type of 2 numbers.
print(3+2)
print(5+5.56)
#Subtraction
print(3-2)
print(3-2.5)
#Multiplication
print(3*5)
print(10*10)
print(6*6.6)
#Division
print(10/2)
print(45/6)
print(77/3)
print(22/3)
#floor division //
#it will cut out the demimal part ,it will take only the integer part of answer
print(10//2)
print(45//6) #7
print(77//3) #25
print(22//3)
#Modulus operator %
#it will be remainder
print(10 % 3) #1
print(10 % 2) #0
print(99 % 5) #4
#Inbuilt functions for numbers
#1.abs()
#it will give u the absolute (positive) value
print(abs(5)) #5
print(-5) #-5
print(abs(-5)) #5
#2.max()
#it will give you the maximum number
print(max(12,56,100))
print(max(100,23,545,12))
print(max(1,2,3))
#3.min()
#it will give you the minimum number
print(min(10,56,100))
print(min(100,23,545,2))
#4.round()
print(round(3.6))
print(round(3.2101))
print(round(3.526334))
print(round(3.211893001))
print(round(7.77556))
#5.floor()
#it will remove the decimal part and only gives the integer part
from math import *#* means all
print(floor(3.6)) #3
print(floor(3.2101)) #3
print(floor(7.77556)) #7
#6.ceil()
#it will give you the next number
print(ceil(3.6)) #4
print(ceil(3.2101)) #4
print(ceil(5.526334)) #6
# floor and ceil for negative numbers
#for negative numbers,floor will work as ceil and ceil will work as floor
print(floor(-2.11456789)) #-
print(floor(-3.6)) #-4
print(floor(-3.2101)) #-4
print(floor(-3.526334)) #-4
print(floor(-3.211893001)) #-4
print(floor(-7.77556)) #-8
print(ceil(-3.6)) #-3
print(ceil(-3.2101)) #-3
print(ceil(-5.526334)) #-5
print(ceil(-3.211893001)) #-3
print(ceil(-10.8956)) #-10
#7.pow()
print(pow(3,2))# 3^2 base=3,power=2
print(pow(2,2))# 2^2
print(pow(2,10))# 2^10
print(pow(3,10))
#8.sqrt()
print(sqrt(25))
print(sqrt(456)

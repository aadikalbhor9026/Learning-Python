# if condition 
#  code block 
# var = 10 
# if var % 2 == 0:
#       print("number is Faaaaaaaa")




#if else stmt

# a = 10 
# if a > 9:
#       print("a is greater than 9")
# elif a == 9:
#       print("a is equal to 9")
# else:
#       print('a is less than 9')




# positive and negative num using if elif and else
# num = int( input ("enter number []"))
# print(num)

# if num>0:
#       print("positive number")
# elif num < 0:
#       print("negative number")
# elif num == 0:
#       print("number is zero !!")
# else:
#       print("invalid number !!")





# program to give 2 no.from user 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     print(a, "is greater")
# elif b > a:
#     print(b, "is greater")
# else:
#     print("Both numbers are equal")



# Reverse a string in Python
# tup=(1,2,3,4,5,6)
# print(tup)
# print(tup[::-1])

# for i in range(1,5,2):
# start=int(input("enter start no"))
# end=int(input("enter end no"))
# sum=0
# for i in range(start,end):
#     sum= sum + i

# print(sum)
# sum=0
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     sum+=i
# print(sum)


# Add two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Sum =", a + b)


# Way Too Long Words
# word = input("Rajaisraj: ")
# if len(word) > 10:
#     print(word[0] + str(len(word) - 2) + word[-1])
# else:
#     print(word)




# Elephant
# n = int(input("Enter number of elephants: "))
# if n == 1:
#     print("1 elephant")
# elif n == 2:
#     print("2 elephants")
# else:
#     print(n, "elephants")



# Is your horseshoe on the other hoof
# a = int(input("Enter first horseshoe : "))
# b = int(input("Enter second horseshoe : "))
# c = int(input("Enter third horseshoe : "))
# d = int(input("Enter fourth horseshoe : "))
# e = int(input("Enter fifth horseshoe : "))
# colors = {a, b, c, d, e}
# print(5 - len(colors))

# Wrong Subtraction
# n, k = map(int, input().split())
# for n in range(k):
#         if n % 10 == 0:
#             n //= 10
#         else:
#             n -= 1
# print(n)



# Odd One Out
# t=int(input())
# for n in range(t):
#   a, b, c = map(int, input("enter three numbers: ").split())
#   if a == b:
#     print(c)
#   elif a == c:
#     print(b)
#   else:
#     print(a)


# sqaure The first line contains a single integer t



# list for unique list
# l1=[1,2,3,4,5,6,7,8,8,9,9,10,1,2,3]
# unique=[]
# for i in l1:.
#     if i not in unique:
#         unique.append(i)
# print(unique)


# l1=[1,2,3,4,5,6,7,8,8,9,9,10,1,2,3]
# a=set(l1)
# print(a)

# Bit++
# t=int(input())
# x=0
# for i in range(t):
#     s=input()
#     if s[1]=='+':
#         x+=1
#     else:
#         x-=1
# print(x)



# list = [12,33,54,61]

# largest = second = 0
# for i in list:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second:
#         second = i
# print(second)



# list = [2,3,4,1,2,4,2,7,2,8,9]

# count = 0

# for i in list:
#     if i == 2:
#         count += 1

# print("Count of 2s:", count)



# n = int(input("Enter the number of rows: "))  
# for i in range(n, 0, -1):
#     print(" "* (n - i) + "* " * i)
    
# code for print even numbers from 1 to 100
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i) 

# functions in Python

# def greet():
#     print("hellow world")
# greet()   

# def wellcome():
#     print("wellcome")
# wellcome()

# function with parameter and without return value.
# def greet(name="ak"):
#    print("hello",name)
# greet("ak47")
# greet()


# def get_number():
#    return 264
# num=get_number()
# print (num)

# # lambda function
# lambda argument : expression
# add = lambda a , b : a + b 
# print(add(5,3))

# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     return n * fact(n-1)
# print(fact(6))


# exception handling in python
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# c = a*b;
# print("a*b = ",c) #other code:
# print("Hi I am other part of the program")
  

# try and catch block in python
# a = int(input("Enter a:"))
# b = int(input("Enter b:")) 
# try:
#   c = a*b; 
# except:
#    print("can't divide by zero") 
# else:
#    print("a*b = %d"%c)

# def employee(fname,Iname="shinde"):
#       print("fname,Iname")
# employee("aaditya","kalbhor")

# Simple Input and Output Example
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}!")
# print(f"You are {age} years old.")
# print("Welcome to Learning Python!")
# employee("aaditya")

# def name():
#  print("hello world")
# name()

# def name(fname):
#     print(fname)
# name("aaditya")

# def name(*fname):
#     print(fname)
# name("aaditya","kalbhor")

# def name(fname="ajay"):
#     print(fname)
# name ("aaditya")
# name()    

# def my_function(child3,child2,child1):
#    print("the youngest child is " +child3)
# my_function (child1="aaditya",child2="kalbhor",child3="shinde")


# def arithmetic(x):
#    return 5*x
# print(arithmetic(3))


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a >= b :
#     print("True")
# else:
#     print("False")

# for i in range(10):
#     print(i)

# while loop in python
# i = 1
# while i <= 10:
#     print ("i am boss")
#     i += 1

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1
# print("done")

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# multiplaction table using while loop
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 25, 81, 100)

# x =int (input("Enter a number: "))
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#         print("found at index", i)
#     else:
#         print("not found")
#     i += 1

# i = 1
# while i <= 10:
#     print(i)
#     if i == 5:
#      break
#     i += 1
# print("done")

# str = "hello world"
# for char in str:
#     print(char)

# nums = [1,4,9,16,25,36,49,64,81,100,49]
# x = int(input("Enter a number: "))

# index = 0
# for el in nums:
#     if (el == x):
#         print("found at index", index)
#         break
#     index += 1

# start stop step in range function
# for i in range(10):   
#     print(i)

# for i in range(2, 10):    
#     print(i)

# for i in range(2, 10, 2):
#     print(i)

# printing even no.
# for i in range(2, 101, 2):
#     print(i)

# # printing odd no.
# for i in range(1, 101, 2):
#     print(i)

# function and function calling in python
# def cal_sum(a,b):
#     sum  = a+b
#     print(sum)
#     return sum

# cal_sum(10,20)


# cal_sum(30,40)


# cal_sum(50,60)

# def cal_sum(a,b):
#     return a + b

# sum = cal_sum(6269,206489) 
# print(sum)

# def print_hello():
#     print("hello")

# print_hello()

# # calculating the avg of 3 numbers using function   
# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     return avg

# avg = calc_avg(10,20,30)
# print("Average:", avg)

# cities = ["pune", "mumbai", "delhi", "bangalore"]
# heroes = ["ironman", "spiderman", "batman", "thor"]

# print(heroes[0], end=" ")

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
#     print()

# print_list(cities)
# print_list(heroes)

# INR TO USD converter USING FUNCTION
# def conveter(usd_val):
#     inr_val = usd_val * 82.74
#     print(usd_val, "USD =", inr_val, "INR")

# conveter(73)

# def check_number(num):
#     if num % 2 == 0:
#         print(num, "is EVEN")
#     else:
#         print(num, "is ODD")

# num = int(input("Enter a number: "))
# check_number(num)

# def show(n):
#     if(n==0):
#         return
#     print(n) 
#     show(n-1)

# show(3)

# def cal_sum(n):
#     if n == 0:
#         return 0
#     print(n)
#     return cal_sum(n-1) + n

# sum = cal_sum(5)
# print("Sum:", sum)  

def print_list(list, idx):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx +1)

fruits = ["apple", "banana", "cherry", "date"]
print_list(fruits, 0)
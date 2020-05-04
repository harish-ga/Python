# Author: Harish
# Purpose: To finish the first assignment given by Ineuron on 1 May 2020
# Date: 5/3/2020

# 1.
# Install Jupyter notebook and run the first program and share the screenshot of the output.
# This task1:1 was run in jupyter ; Other tasks were run in PyCharm
# But copying the code used in jupyter below in pycharm as well as only one file is going to be uploaded onto github
try:
    user_input = input("enter a string")
    if not user_input:
        raise ValueError('empty string!!!! Hence using default string!! Author: Harish \n')
except ValueError as err:
    print(err)
    user_input = "Result \n 1.Install Jupyter notebook and run the first program and share the screenshot of the output."

print(user_input)


# 2.
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

task1_2_list = []
# since we want from 2000 to 3200
for i in range(2000,3201,1):
    if i % 5 != 0 and i % 7 == 0:
        # converting the integer to string because we want to print the list of numbers without [] and comma separated
        task1_2_list.append(str(i))
else:
    print("All values from 2000 to 3200 (both included) are traversed and the numbers divisible by 7"
          " but not a multiple of 5 are:\n",
          ', '.join(task1_2_list))  # used join function with comma separator to print the

# PyDev console: starting.
# Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
# runfile('/PycharmProjects/ineuron_assign1_hg/assign1.py',
# wdir='/PycharmProjects/ineuron_assign1_hg')
# All values from 2000 to 3200 (both included) are traversed and the numbers divisible by 7 but not a multiple of 5 are:
#  2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156,
#  2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324,
#  2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492,
#  2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653,
#  2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821,
#  2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989,
#  2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157,
#  3164, 3171, 3178, 3192, 3199

# 3.
# Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

user_input_fname = input("Enter the First name")
user_input_lname = input("Enter the Last name")
# Since i didn't understand what exactly was being asked  printing all three results
print('Same Order and reverse string:', user_input_fname[::-1], user_input_lname[::-1], sep=' ')
print('Reverse Order and reverse string:', user_input_fname[::-1], user_input_lname[::-1], sep=' ')
print('Reverse Order and same string:', user_input_lname, user_input_fname, sep=' ')

# Enter the First name>? Hello
# Enter the Last name>? World
# Same Order and reverse string: olleH dlroW
# Reverse Order and reverse string: olleH dlroW
# Reverse Order and same string: World Hello

# 4.
# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3
import math

try:
    user_input_dia = int(input("Enter the Diameter of the spehere in cm: "))
except ValueError:
    user_input_dia = 12
vol = (4/3) * math.pi * pow(user_input_dia / 2, 3)

print("Volume of a spehere with diameter ", user_input_dia, " cm is : ", round(vol, 3), sep='')

# The user didn't enter any value and hence it took the default value of 12
# Enter the Diameter of the spehere in cm: >?
# Volume of a spehere with diameter 12 cm is : 904.779

# Task 2:
# 1.
# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list

inp_seqn = input("enter a seq of numbers sep by a comma")
print(inp_seqn)
str_list = list(inp_seqn.split(','))
int_list = [int(i) for i in str_list]
print(int_list)

# enter a seq of numbers sep by a comma>? 3,4,5,9,6,8
# 3,4,5,9,6,8
# [3, 4, 5, 9, 6, 8]


# 2.
# Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

asterix_list = ["*"]
count = 2
for j in range(10):
    for i in asterix_list:
        if j <= 5:
            print(j*i)
        else:
            print((j-count)*i)
            count += 2

# 3.
# Write a Python program to reverse a word after accepting the input from the user.

user_word = input("Enter a word")
print(user_word[::-1])

# Enter a word>? TeSt
# tSeT

# Enter a word>? AcadGild
# dliGdacA


# 4.
# Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens

# WE, THE PEOPLE OF INDIA,
#       having solemnly resolved to constitute India into a SOVEREIGN, !
#           SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#            and to secure to all its citizens
print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN, ! "
      "\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")

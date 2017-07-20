#Given: Positive integers n≤40n≤40 and k≤5k≤5.

#Return: The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each generation,
#every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).


import sys

n = input("Please input the value of n \n")
k = input("Please input the value of k \n")

#initiate the arrary to be all 0s
f_array =[0]*(n+1)
f_array[1] = 1
f_array[2] = 1

def getFn(n):
    if n == 1:
        return f_array[1]
    elif n == 2:
        return f_array[2]
    elif f_array[n]>0:
        return f_array[n]
    elif f_array[n-1]>0 and f_array[n-2]>0:
        f_array[n] = f_array[n-1] + f_array[n-2]*k
        return f_array[n]
    else:
        return getFn(n-1) + getFn(n-2)*k

print getFn(n)
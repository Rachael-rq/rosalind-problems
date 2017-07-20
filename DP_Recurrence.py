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
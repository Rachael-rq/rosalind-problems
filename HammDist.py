#Problem
#Given two strings s and t of equal length, the Hamming distance between s and t,
# denoted dH(s,t)dH(s,t), is the number of corresponding symbols that differ in ss and tt
#author: Ruqian
#Date Aug 2017
def hamDis(s,t):
    return sum(1 for x,y in zip(s, t) if x != y)



fileS = open('/Users/ruqianlyu/Documents/rosalind/rosalind_hamm.txt','r')
s = file.readlines(fileS)
print(hamDis(s[0],s[1]))
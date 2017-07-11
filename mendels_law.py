#Given 3 positve integers, k,m,n representing a population containing k+m+n organisms. k individuals are homozygous dominant for a factor
#,m are heterozygous, n are homozygous recessive

#Return the probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying
#the dominant phenotype. Assume that any two organisms can mate


k = 29.0
m = 25.0
n = 21.0

total = k + m + n

prob = (m*n + n*(n-1) + m*(m-1)/4)/(total*(total-1))

print 1 - prob
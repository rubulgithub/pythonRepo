from functools import reduce

nums=[3,4,6,12,21,6,7,13]
evens=list(filter(lambda n:n%2==0,nums))
double=list(map(lambda n:n*3,evens))
print(double)
sum=reduce(lambda a,b:a+b,double)
print(sum)

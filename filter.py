
def is_even(n):
    return n%2==0

nums=[3,4,6,12,21,6,7,13]
evens=list(filter(is_even,nums))
print(evens)
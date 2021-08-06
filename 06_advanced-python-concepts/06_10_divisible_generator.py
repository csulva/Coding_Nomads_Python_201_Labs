# Create a Generator that loops over the given range and prints out only
# the items that are divisible by 1111.

nums = range(1, 1000000)
loop = (num for num in nums if num % 1111 == 0)
print(loop) #OUTPUT <generator object <genexpr> at 0x10528e890>

x = list(loop)
print(x)
print(len(x)) #OUTPUT 900
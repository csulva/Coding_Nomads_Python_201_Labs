# Adapt your Generator expression from the previous exercise:
# Don't print anything, and run a floor division by 1111 on it.
# What numbers do you get?

nums = range(1, 1000000)
loop = (num for num in nums if num // 1111 == 0)
print(list(loop))
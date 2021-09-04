# Go to https://stackoverflow.com/questions/tagged/python?tab=Newest
# and look through some of the newest questions tagged with "Python".

# Pick one of the questions that includes a code snippet and try to get
# it working in your local environment.

# Use your debugger to attempt to solve the challenge that the user ran into.
# If you can solve it, post your solution as an answer to the question.


a=[11,0,40,5,1, 1, 14, 14, 15, 14]
i=0
while i<len(a):
    key=i
    j=i+1
    while j<len(a):
        if a[key]>a[j]:
            key=j
        j+=1
    a[i],a[key]=a[key],a[i]
    i+=1
print(a)
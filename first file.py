def show(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*show(n-1)

print(show(999))
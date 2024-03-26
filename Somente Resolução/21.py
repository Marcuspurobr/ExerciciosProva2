
def subsSTR(x,k):
    ln=[]
    x=str(x)
    t=len(x)//k
    r=len(x)%k
    for d in range(t):
        ln.append(x[k*d:(k*d)+k])
    if r!=0:
        ln.append(x[(len(x))-r-1:(len(x))-1])
    return ln
print(subsSTR('marcusmarcus',2))
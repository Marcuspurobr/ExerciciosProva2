def MergeTwoLists(l1,l2):
    l3=[]
    p1=0
    p2=0
    while p1!=len(l1) or p2!=len(l2):
        if p1==len(l1):
            l3.append(l2[p2])
            p2+=1
        elif p2==len(l2):
            l3.append(l1[p1])
            p1+=1
        elif l1[p1]<=l2[p2]:
            l3.append(l1[p1])
            p1+=1
        elif l2[p2]<l1[p1]:
            l3.append(l2[p2])
            p2+=1
    return l3
l1 = [0,2,5,8]
l2 = [1,2,3,4,5,6,7]
print(MergeTwoLists(l1,l2))

        
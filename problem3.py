def freq(stri,chri):
    count = 0
    for i in stri:
        if i == chri:
            count += 1
    return count
def myfun(stri):
    cha = set(stri)
    for i in cha:
        ans = freq(stri,i)
        if ans>1:
            print(str(i)+ " : " + str(ans) + " times")
    
arr = [int(x) for x in input().split()]
myfun(arr)

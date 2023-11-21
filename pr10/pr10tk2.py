

a =[12,66,234,789,11]
def dd(a):
    b=[]
    while a > 0:
        b.append(a % 10)
        a = a // 10
    b.reverse()
    return(b)
def create_full_sorted_lst(l):
    l.sort(reverse = True)
    return list(map(dd,l))
a = create_full_sorted_lst(a)
# print(a)
b =[] 
for i in a:
    b+=i
print(b)
def one_num(lst):
    num = 0
    for i in range(len(lst)):
        num = num * 10 + lst[i]
    return num
print(one_num(b))
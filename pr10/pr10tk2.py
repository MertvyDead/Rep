

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
c= 0
for i in a:
    b+=i
print(b)
for i in b:
    c+= b[i] ^ 10^(len(b)-i)
print(c)

# a = [95,96,94]
# def create_one_num(mas):
#     one_num = 0
#     for i in mas:
#             one_num *= 10 ** len(i)
#             one_num += mas[i]
#     return one_num
# c = create_one_num([[9, 1], [9, 0], [8, 6], [8, 5], [7]])
# print(c)
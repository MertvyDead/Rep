import random
bitmap =[{'r':random.randint(0,255),'g':random.randint(0,255),'b':random.randint(0,255)} for i in range(20000)]
# print(bitmap)
r = sorted(bitmap, key= lambda x:(x['r']))
g=sorted(bitmap, key= lambda x:(x['g']))

b=sorted(bitmap, key= lambda x:(x['b']))
print(r[0]['r'],g[0]['g'],b[0]['b'])
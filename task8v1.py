l=[1,2,1,1,1,1,2,2,1,1,2]

def cnt(g):
    d = {'1':0, '2':0}
    for i in g:
        if g[i] == 2:
            d["2"]+=1
        else:
    
            d['1']+=1
    return (d)
print(cnt(l))
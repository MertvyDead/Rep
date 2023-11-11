def Datadict (Data):
    y, m, d = Data.split(' ')
    data_dict= {'Year':y, 'month':m, 'day':d}
    return data_dict
data = '2001 9 11'
dd=Datadict(data)
print(dd)

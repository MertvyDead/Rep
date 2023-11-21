import names as n
import random as rd
def gen(number_of_ppl):
    a=[]
    for i in range(number_of_ppl):
        ag =rd.randint(18,60)
        nm=n.get_full_name()
        ds=rd.randrange(1000,5000,200)
        en=rd.choices(["Yes","No"])
        we=rd.randrange(0, 10)
        st=rd.choices(["Python","Other"])
        ppl ={'Name': nm,'Age':ag,'Desired salary':ds, 'English': en, 'Work exp.': we, 'Stack':st}
        a.append(ppl)
        # ppl ={'Name': n.get_full_name(),'Age':rd.randint(18,60),'Desired salary':rd.randrange(1000,5000,200), 'English': rd.choice["Yes","No"], 'Work exp.': rd.choice["0","1-3","3+"], 'Stack':rd.choice["Python","Other"]}
        # a = a.append(ppl)
    return a
def best_worker(lst_of_ppl, age , eng, money, exp1, exp2, stack):
    for i in range(len(lst_of_ppl)):
            rating = 0
            
            if lst_of_ppl[i]['Age'] in range(18, age):
                rating +=1
            if lst_of_ppl[i]['English'] == [eng]:
                rating += 1
            if lst_of_ppl[i]['Desired salary'] <= money:
                rating += 1
            if lst_of_ppl[i]['Work exp.'] in range(exp1,exp2):
                rating += 1
            if lst_of_ppl[i]['Stack'] == [stack]:
                rating += 1
             
            lst_of_ppl[i]['Rating'] = rating
    return lst_of_ppl
c = gen(10)
lutch = best_worker(c,33, "Yes", 5000,1, 5 ,"Python")
lutch = sorted(lutch, key= lambda x : x['Rating'], reverse=True)
# print(lutch[:2])
print(f'{lutch[0]}\n{lutch[1]}\n{lutch[2]}')


        

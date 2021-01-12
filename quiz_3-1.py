# Author Emanuel Mark Gjoka (AMDG) 1/12/2021

younglings = ['Petro', 'Katooni', 'Byph', 'Ganodi', 'Zatt', 'Gungi']
race = ['Human', 'Tholothian', 'Ithorian', 'Rodian', 'Nautolan', 'Wookie']

def ydprmtrs(name, race):
    hmn = [name[0] + ', ' + race[0]]
    thlthn = [name[1] + ', ' + race[1]]
    thrn = [name[2] + ', ' + race[2]]
    rdn = [name[3] + ', ' + race[3]]
    ntln = [name[4] +  ', ' + race[4]]
    wk = [name[5] + ', ' + race[5]]
    l_st = [hmn] + [thlthn] + [thrn] + [rdn] + [ntln] + [wk]
    print(l_st)

print(ydprmtrs(younglings, race))

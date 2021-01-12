# Author: Emanuel Mark Gjoka (AMDG) 1/12/2021

ledger = [['Sebulba', 100, 200, 400], ['Skywalker', 500, 100, 20000], ['Reeso', 200, 700, 100]]

def ldgrsplttr(x):
    for index, value in enumerate(x):
        nml_st = [(x[0][0] + ', ') + (x[1][0] + ', ') + (x[2][0])]
        btl_st = [100, 200, 400, 500, 100, 20000, 200, 700, 100]
        nwldgr = [nml_st] + [btl_st]
        print(nwldgr)


print(ldgrsplttr(ledger))

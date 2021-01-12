# Author: Emanuel Mark Gjoka (AMDG) 1/12/2021

import random

qstnnr = input('Need a new clone? ("Y" or "N") ')

if qstnnr == 'Y':
    nmbr = int(random.randrange(0, 9999))
    if nmbr < 10:
        nmbr == "000" + str(nmbr)
    elif nmbr < 100:
        nmbr == "00" + str(nmbr)
    elif nmbr < 1000:
        nmbr == "0" + str(nmbr)
    clone = "CT-" + str(nmbr)
    print('New clone name: ' + str(clone))
elif qstnnr == 'N':
    print('No more new clones')
else:
    print('Error.')

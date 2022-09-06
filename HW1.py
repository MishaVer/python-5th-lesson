print ('Hello World')

import random
conf = 2021
human = -1
choose = 1
while conf > 0:
    if choose == 1:
        human = -1
        while human > 28 or human < 0:
            human = int(input())
        conf = conf - human
        choose = 0
        print(conf)
    if choose == 0:
        if conf <=28:
            conf = 0
        else:
            comp = random.randint(1,28)
            conf = conf - comp
        choose = 1
        print("комп забрал",comp )
        print(conf)
import random as ra

from demo import *


data = demo.data

score = 0

s = ''

def dec(c):
    global count, s
    s = ''
    count += 1
    s = 'compare ' + str(count) + ":" + " "\
        + data[c]['Name'] + "," + " "+ data[c]['Description'] + "," + " "+ data[c]['Country']
    return s

while True:

    lis = [0,1,2,3]
    l = ra.choice(lis)
    lis.remove(l)
    z = ra.choice(lis)

    count = 0

    a = dec(l)
    t = l

    b = dec(z)
    t1 = z
    print(a)

    print('''
     _____ _____ 
    |  |  |   __|
    |  |  |__   |
     \___/|_____|
    ''')
    print(b)

    f = int(input("who has more followers(1/2):"))

    if f == 1:
        if data[t]['Followers'] > data[t1]['Followers']:
            score += 1
            print(f"You are right. you scored {score}")
            pass

        else:
            print(f"You lost. your score is {score}")
            break
    elif(f == 2):
        if data[t1]['Followers'] > data[t]['Followers']:
            score += 1
            print(f"You are right. you scored {score}")
            pass

        else:
            print(f"You lost. your score is {score}")
            break
    else:
        break
    print("------------------------------------")

print()
print("/*** Thank you for Playing ***/")

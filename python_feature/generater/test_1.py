#Date:2018/5/6
#Author:dylan_xi
#Desc: exercise for generator 

#starting with a1 through z1 , then a2 through z2, and so on  

def generator_alphanumeric():
    a ,  b = 0 , 1
    while True:
        yield chr(ord('a')+a) + str(b)
        a = a + 1
        if a >= 26:
            a = 0
            b = b +1
        if b > 10:
            return

for a in generator_alphanumeric():
    print(a)
#Date:2018/5/10
#Author:dylan_xi
#Desc: learn how to use zip

l = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']

k =  zip(l[:-1] , l[1:])
print(list(k))
# def calctime(curlon):
# 	shangValue=int(curlon//15)
# 	yuValue=float(curlon%15)
# 	if yuValue<=7.5 and yuValue>-7.5:
# 		return shangValue
# 	else:
# 		if yuValue<=-7.5:
# 			return shangValue-1
# 		else:
# 			return shangValue+1


# print(calctime(22.5))
# print('08'>'17')
# print(int('08'))


# list=[]
# i=0
# a=0
# j=0

# for i in range(90):
# 	for j in range(180):
# 		list.append([i,i+1,j,j+1,0])
# a=[80,110]
# print(len(list))
# print(list2)

# while i != 90:
# 	j=0
# 	while j !=180:
# 		list.append([i,i+5,j,j+5,0])
# 		j+=5
# 	i+=5

# # print (list)

# for i in range(len(list)):
# 	if (a[0]>=list[i][0] and a[0]<list[i][1]) and (a[1]>=list[i][2] and a[1]<list[i][3]):
# 		list[i][4]+=1
# 		print(list[i])
from timeit import timeit
import sqlite3
import time
import redis
r=redis.Redis(host='localhost',port=6379,decode_responses=True)
r.set('name','test')
print(r['name'])
print(r.get('name'))

# db=sqlite3.connect('1.db')
# cu=db.cursor()
# data=cu.execute('select * from all_month')
# data2=[]
# i=0
# for row in data:
# 	data2.append(row)
# 	r.set(i,list(row))
# 	i+=1
# db.commit()
# db.close()
print(r.get(1))
print(r.get(1)[0:10])



# t=timeit("print('test')",'print("start")',number=1000)

# print(t)
# print('start')
# print(t2)
# db=sqlite3.connect('1.db')
# cu=db.cursor()

# start=time.time()

# for i in range(100):

# 	cu.execute('select * from all_month')


# end=time.time()

# test2=timeit("cu.execute('select * from all_month');","import sqlite3;db=sqlite3.connect('1.db');cu=db.cursor()",number=100)
# test1=timeit("data","from __main__ import data",number=100)

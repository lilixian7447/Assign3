#!/usr/bin/env python3
from flask import Flask

import os
import csv
from flask import render_template
from flask import request
import sqlite3
from timeit import timeit
import redis

app = Flask(__name__)

# print(os.getenv("PORT"))
port = int(os.getenv("PORT", 5000))
print(port)
r=redis.Redis(host='localhost',port=6379,decode_responses=True)
db=sqlite3.connect('1.db')
cu=db.cursor()
data=cu.execute('select * from all_month')
data2=[]
i=0
for row in data:
	data2.append(row)
	r.set(i,str(row))
db.commit()
db.close()



@app.route('/choose')
def choose():
	# db=sqlite3.connect('1.db')
	# cu=db.cursor()
	# data=cu.execute('select * from all_month')
	list=[]
	for row in data2:
		# print(row[4])
		if row[4]==None:
			pass
		else:
			if float(row[4])>5.0:
				list.append(row)



	return render_template('earchquake.html',data=list)





@app.route('/createtable')
def createtable():
	tablename=request.args.get('tabelname')
	if tablename:
		time11=timeit("cu.execute('CREATE Table %s(Id NOT NULL)');"%tablename,"import sqlite3;db=sqlite3.connect('1.db');cu=db.cursor();",number=1)
		print(time11)
		return render_template('tabletime.html',time11=time11)
	else:
		return render_template('tabletime.html')

@app.route('/searchtable')
def searchtable():
	list = []
	number=request.args.get('number')
	depth=request.args.get('depth')
	redis_num=request.args.get('redis_num')
	mag=request.args.get('mag')
	if number and redis_num:
		number = int(number)
		depth = 0.0
		time2=timeit("cu.execute('SELECT * FROM all_month WHERE depth>=%d');"%depth,"import sqlite3;db=sqlite3.connect('1.db');cu=db.cursor();",number=number)
		number2=int(redis_num)
		time3=timeit("r.get(1)","import redis;r=redis.Redis(host='localhost',port=6379,decode_responses=True);",number=number2)
		return render_template('tabletime.html',time2=time2,number=number,time3=time3,number2=number2)

	if number and depth and redis_num and mag:
		number=int(number)
		depth=float(depth)
		time2=timeit("cu.execute('SELECT * FROM all_month WHERE depth>=%d AND mag>=%d');"%depth%mag,"import sqlite3;db=sqlite3.connect('1.db');cu=db.cursor();",number=number)
		number2=int(redis_num)
		time3=timeit("r.get(1)","import redis;r=redis.Redis(host='localhost',port=6379,decode_responses=True);",number=number2)
		for row in data2:
			if row[5] == None:
				pass
			else:
				if float(row[3]) < depth and float(row[3]) < mag :
					list.append(row)
					print(list)

		return render_template('tabletime.html',time2=time2,number=number,time3=time3,number2=number2,data=list)
	else:
		return render_template('tabletime.html')


@app.route('/',methods=['POST','GET'])
def input():
	return render_template('form.html')
	






if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port,debug=True)

import mysql.connector

config = {
  'user': 'root',
  'password': '12345',
  'host': '127.0.0.1',
  'database': 'api3',
  'raise_on_warnings': True,
  'use_pure': False,
}

class MySQL():
	def __init__(self,table):
		self.table=table
	def all(self):
		cnx=mysql.connector.connect(**config)
		mycursor=cnx.cursor()
		query="""select * from {};""".format(self.table)
		mycursor.execute(query)
		data=mycursor.fetchall()
		columns=[i[0] for i in mycursor.description]
		mycursor.close()
		cnx.close()
		return [dict(zip(columns, i)) for i in data]
	def post(self,query):
		cnx = mysql.connector.connect(**config)
		mycursor = cnx.cursor()
		mycursor.execute(query)
		cnx.commit()
		mycursor.close()
		cnx.close()
	def put(self,query):
		cnx = mysql.connector.connect(**config)
		mycursor = cnx.cursor()
		mycursor.execute(query)
		cnx.commit()
		mycursor.close()
		cnx.close()
	def delete(self,id):
		cnx = mysql.connector.connect(**config)
		mycursor = cnx.cursor()
		query = """Delete from {} where id={};""".format(self.table,id)
		mycursor.execute(query)
		cnx.commit()
		mycursor.close()
		cnx.close()
	def get(self,id):
		cnx = mysql.connector.connect(**config)
		mycursor = cnx.cursor()
		query = """select * from {} where id={};""".format(self.table,id)
		mycursor.execute(query)
		data = mycursor.fetchone()
		if(not data):
			return
		columns = [i[0] for i in mycursor.description]
		mycursor.close()
		cnx.close()
		return dict(zip(columns, data))

from configparser import ConfigParser
import mysql.connector

class DB:
	def __init__(self):
		db_config = self.read_db_config()


		try:
			self.cnx = mysql.connector.connect(
				user=db_config['user'],
				password=db_config['password'],
				db=db_config['database'],
				host=db_config['host'],
				port=db_config['port']

			)

		except mysql.connector.Error as e:
			print(e)

		print('*** Connection Established ***')

	def insertRow(self, *args):
		# Creating a query for later execution using .prepare()
		cursor = self.cnx.cursor(prepared=True)
		prepared_sql ="""
			INSERT INTO users (username,email,password)
			VALUES (?,?,?)
			"""
		cursor.execute(prepared_sql, args)

		self.cnx.commit()

	def select_all_rows(self):
		cursor = self.cnx.cursor()
		cursor.execute("select * from users")
		rows = cursor.fetchall()

		# print(rows)
		return rows

	def authenticate(self, user_name, password):
		# create a cursor for the connection
		cur = self.cnx.cursor()

		# prepare SQL query:
		query = f"""
			SELECT * FROM users
				WHERE username='{user_name}'
				AND `password`='{password}'
		"""
		# execute the query
		cur.execute(query)

		# we are only interested if 1 or 0 rows are returned
		res = cur.fetchone()

		# do something with the result
		if(res):
			return True
		else:
			return False

	def read_db_config(self,file_name='config.ini', section='mysql'):

		# create parser and read the configuration file
		parser = ConfigParser()
		parser.read(file_name)


		db_config = {}
		if parser.has_section(section):
			items = parser.items(section)
			for item in items:
				db_config[item[0]] = item[1]
		else:
			raise Exception(f'{section} not found in the {filename} file')

		return db_config


if __name__ == '__main__':
	db = DB()
	db.select_all_rows()

	# db.insertRow('Asen', 'asen@abv.com', 'asen123')

	# # let's use some hard-coded values for test:
	# user_name = 'Maria'
	# password = 'maria123'

	# auth = db.authenticate(user_name=user_name, password=password)

	# if auth:
	# 	print('Loged in')
	# else:
	# 	print('Problem')


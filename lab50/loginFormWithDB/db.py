import mysql.connector

class DB:
	def __init__(self, user, password, db, host="localhost", port=3306):
		try:
			self.cnx = mysql.connector.connect(
				user=user,
				password=password,
				db=db,
				host=host,
				port=port
			)

		except mysql.connector.Error as e:
			print(e)

		print('*** Connection Established ***')


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



if __name__ == '__main__':
	db = DB('test', 'test1234','pyqtDemos')

	# let's use some hard-coded values for test:
	user_name = 'Maria'
	password = 'maria123'

	db.authenticate(user_name=user_name, password=password)




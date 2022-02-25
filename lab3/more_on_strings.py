# ------------------------------ strings basics ------------------------------ #
# # single-line strings
# print( '1' )
# print( "1" )

# # multiline strings
# print( '''1''')
# print( """1""")

# print('''1
# 2''')

# print( ' multi line 1 \
# line 2')

# res1 = 234+3243+43+435+43+43+3443+43
# res2 = 234+3243+43+435\
# 	   +43+43+3443+43
# print(res1,res2)


# ----------------------------- escape sequences ----------------------------- #
# "a\b"
# print("aa\b")
# print("a\na")
# print("a\ta")
# print("a	a")
# print("a    a")
# print("a\u12afa")
# print("aኯa")

# # immutable == непроменяем
# x = 1
# x = 5
# x = 6


# RAM:
#     73243843 => 0001 (1)
#    x:73243849=> 0101 (5)


# --------------------------- f-strings and format --------------------------- #
# user_name = 'aDa ByroN'
# user_name = user_name.capitalize()

# print( 'Hello, user_name !' )

# msg1 = 'Hello, ' + user_name + ' !'
# msg2 = f'Hello, {user_name} !'
# msg3 = 'Hello, {} !'.format(user_name)
# print( msg1 )
# print( msg2 )
# print( msg3 )

# 'Hello, user_name !'

user_name = 'Ada  Byron'
msg1 = "{} - {}".format(user_name, 23)
msg2 = "{} - {}".format('Ivan Ivanov', 23)
msg3 = "%-30s - %d" % ('Ivan Ivanov', 23)
msg4 = "%-30s - %d" % ('Ada ', 23)
print(msg1)
print(msg2)
print(msg3)
print(msg4)









# --------------- Форматиране на стрингове чрез използване на % -------------- #

# formated_str1 = '%-10d-%10s' % (6,'bananas')
# formated_str2 = '%-10d-%10s' % (646743,'apple')

# formated_str3 = '{:<10d}-{:>10s}'.format(6,'bananas')
# formated_str4 = '{1:<10s}-{0:>10d}'.format(6,'bananas')

# print(formated_str1)
# print(formated_str2)
# print(formated_str3)
# print(formated_str4)



# ----------------------- f-strings vs .format strings ----------------------- #
user_name = 'byron'
# msg = 'Hello, Ada !'

msg = 'Hello, {} !'.format(user_name)
print(msg)

msg2 = f'Hello, {user_name.capitalize()} !'
print(msg2)



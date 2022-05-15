l = ['a',1,'b','c',34]

# l_new = []
# for el in l:
# 	l_new.append(str(el))

l_new = [ str(el) for el in l ]

row = ','.join(l_new)
print(row)
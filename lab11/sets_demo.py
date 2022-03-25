# l = [1,2,2]

# d = {
# 	'a': 1,
# 	'b': 2,
# 	'c': 2
# }

# s = {1,2,2}

# print(l)
# print(d)
# print(s)

# s = set(range(5))
# print(s)

# ------------------------------- set use case: ------------------------------ #
# from l1 create another list - l2, with unique l1 values

# l1 = [1,2,2]
# l2 = list(set(l1))
# print(l2[-1])


# -------------------------- set elements operations ------------------------- #
## add:
# s = {1,2,3}
# s.add(4)
# s.add(4)
# s.add(4)
# s.add(4)
# print(s)

# # update:
# s = {1,2,3}
# s.update([4,5,6])
# print(s)

# # discard:
# s = {1,2,3}
# s.discard(5)
# print(s)

## remove:
# s = {1,2,3}
# s.remove(5)
# print(s)

# # clear
# s = {1,2,3}
# s.clear()
# print(s)


# ------------------------------ set operations ------------------------------ #
# # обединяване на два множества:
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# print(s1 | s2)
# print(s1.union(s2))
# print(s2.union(s1))
# s_union = {1,2,3,45,6,7,8}

# # сечение на два множества:
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# print(s1 & s2)
# print(s1.intersection(s2))
# print(s2.intersection(s1))

## разлика между множества:
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# print(s1 - s2)
# print(s2 - s1)
# print(s1.difference(s2))
# print(s2.difference(s1))

# сравняване на два множества:
# s1 = {1,2,3,4,5}
# s2 = {4,5}

# print( s1>s2 )

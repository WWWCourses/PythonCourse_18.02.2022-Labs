age = 29
sex = "M"
marry = "Y"

print("Age: {}".format(age))
print("SEX? (M or F): {}".format(sex))
print("MARRIED? (Y or N): {}".format(marry))

if sex == "F" and 20 <= age <= 60:
    print("Urban areas only")
elif sex == "M" and 20 <= age <= 40:
    print("You can work anywhere")
elif sex == "M" and 40 < age <= 60:
    print("Urban areas only")
else:
    print("ERROR")

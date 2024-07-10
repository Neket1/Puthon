#___________________________________________кортеж
immutable_var = ([1, 4, 2], 0, True, "string")
print(immutable_var)# кортеж не изменяимый в отличии от списка
immutable_var[0][0] = 53
print(immutable_var)
#___________________________________________список
mutable_list = [0,4,12,4,2,4,6,2]
print(mutable_list)
mutable_list[0] = 9999
print(mutable_list)
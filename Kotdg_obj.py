immutable_var = 1, 23, 54, True, "string"
print(immutable_var)# кортеж не изменяимый в отличии от списка
mutable_list = ([1, 4, 2], 0) # но если сделать так он будет изменяемый
print(mutable_list)
mutable_list[0][0] = 53
print(mutable_list)
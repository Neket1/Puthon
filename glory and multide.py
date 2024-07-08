my_dict ={"Имя" : "Олег", "Год рождения": 2000}
print(my_dict)
my_dict ={"Имя" : "Олег", "Год рождения": 2000}
print(my_dict.get("Имя"))
print(my_dict.get("Фамилия"))
my_dict["Имя"] = "максим"
my_dict["Имя_2"] = "Денис"
print(my_dict)
my_dict.__delitem__("Имя")# не уверен что так это надо сделать
print(my_dict)
#______________________________________________________
my_set = {1, 3, 4, 3, 5, 2, 7, "что-то тут должно быть", True, }
print(my_set)
my_set.add(10)
my_set.add("бу")
print(my_set)
my_set.remove("что-то тут должно быть")
print(my_set)
my_dict = {"Roma": 2002, "Misha": 1998, "Anton": 2006}
print(my_dict)
print(my_dict.get("Misha"))
print(my_dict.get("Denis", "такой ключ не найден"))
my_dict.update({"Katya": 2000,
                "Masha": 1986})
print(my_dict.pop("Misha"))
print(my_dict.items())

my_set ={112, 3.14, "name", 112, 2}
print(my_set)
my_set.add(56.43)
my_set.discard(112)
print(my_set)
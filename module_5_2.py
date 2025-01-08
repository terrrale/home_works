class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f"Название: {self.name}, количество этажей: {self.number_of_floors}")

    def go_to(self, new_floor):
        for i in range(1, self.number_of_floors + 1):

            if 1 <= i <= new_floor:
                print(i)
            else:
                continue
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

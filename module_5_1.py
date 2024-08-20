class House:
	def __init__(self, name, number_of_floors):
		self.number_of_floors = number_of_floors
		print(f'Название - {name}')
		print(f'Кол-во этажей - {number_of_floors}')

	def go_to(self, new_floor):
		if new_floor > self.number_of_floors:
			print('Такого этажа не существует')
		elif new_floor <= 0:
			print('Такого этажа не существует')
		else:
			print(f'Вы приехали на {new_floor} этаж')

result = House(input('Введите название: '), int(input('Введите кол-во этажей: ')))
result.go_to(int(input('Введите желаемый этаж: ')))
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name (self):
        full_name = self.name + ' ' + self.surname
        return full_name
    def get_total_income (self):
        total_income = self._Worker__income["wage"] + self._Worker__income['bonus']
        return total_income
a = Position ('Иван', 'Иванов', 'Электрик', 15000, 5000)
print(a.get_full_name())
print(a.get_total_income())
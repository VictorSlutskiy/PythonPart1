class Worker:
    name = "Андрей"
    surname = "Бодров"
    position = "Team lead"
    _income = {"wage": 1500, "bonus": 500}


class Position(Worker):
    def get_full_name(self):
        print(self.name, " ", self.surname)

    def get_total_income(self):
        sum = self._income["wage"] + self._income["bonus"]
        print(sum, "$")


a = Position()
a.get_full_name()
a.get_total_income()

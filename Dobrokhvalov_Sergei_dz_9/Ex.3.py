class Worker:
    def __init__(self, info):
        self.name = info[0]
        self.surname = info[1]
        self.position = info[2]
        self._income = {'wage': int(info[3]), 'bonus': int(info[4])}


class Position(Worker):
    def get_full_name(self):
        return ' '.join((self.name, self.surname))

    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]


worker_info = [["Ivan", "Ivanov", None, 30000, 10000], ["Andrey", "Andreev", None, 34000, 16000]]
worker_1 = Position(worker_info[0])
worker_2 = Position(worker_info[1])
print(worker_1.get_full_name(), worker_1.get_total_income())
print(worker_2.get_full_name(), worker_2.get_total_income())

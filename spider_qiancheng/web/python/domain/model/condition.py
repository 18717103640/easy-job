class Condition:
    def __init__(self, condition, res_count, total_count, id=None, created_time=None, updated_time=None):
        self.id = id
        self.condition = condition
        self.res_count = res_count
        self.total_count = total_count
        self.created_time = created_time
        self.updated_time = updated_time

    def print_self(self):
        print_str = f"{self.id} {self.condition} {self.res_count} {self.total_count} {self.created_time} {self.updated_time}"
        print(print_str.title())


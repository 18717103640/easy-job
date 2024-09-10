class ConditionFail:
    def __init__(self, condition,retry_times,id=None,created_time=None,updated_time=None):
        self.id = id
        self.condition = condition
        self.retry_times = retry_times

        self.created_time = created_time
        self.updated_time = updated_time

    def print_self(self):
        print_str = f"{self.id} {self.condition} {self.retry_times}  {self.created_time} {self.updated_time}"
        print(print_str.title())
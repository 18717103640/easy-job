class TaskFail:
    def __init__(self, task_id, condition, current_page, retry_time,
                 id=None, created_time=None, updated_time=None):
        self.id = id
        self.task_id = task_id
        self.condition = condition
        self.current_page = current_page

        self.retry_time = retry_time
        self.created_time = created_time
        self.updated_time = updated_time

    def print_self(self):
        print_str = (f"{self.id} {self.task_id} {self.condition} {self.current_page} {self.retry_time}"
                     f"{self.created_time} {self.updated_time}")
        print(print_str.title())
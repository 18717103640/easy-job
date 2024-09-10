class Task:
    def __init__(self, task_id, condition, status, current_page, page,
                 order,
                 id=None, created_time=None,updated_time=None):
        self.id = id
        self.task_id = task_id
        self.condition = condition
        self.status = status
        self.current_page = current_page

        self.page = page
        self.order = order
        self.created_time = created_time
        self.updated_time = updated_time

    def print_self(self):
        print_str = (f"{self.id} {self.task_id} {self.condition} {self.status} {self.current_page} "
                     f"{self.page} {self.order} {self.created_time} {self.updated_time}")
        print(print_str.title())

class RequestLog:
    def __init__(self, platform, task_id, user_id, condition, url, ip, source_data,
                 id=None, created_time=None,updated_time=None):

        self.platform = platform
        self.task_id = task_id
        self.user_id = user_id
        self.condition = condition
        self.url = url

        self.ip = ip
        self.source_data = source_data

        self.id = id
        self.created_time = created_time
        self.updated_time = updated_time

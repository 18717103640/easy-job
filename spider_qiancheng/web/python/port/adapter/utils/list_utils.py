class ListUtils:
    @staticmethod
    def list_to_string(list):
        if list == None:
            return None
        if len(list) == 0:
            return None
        return '，'.join([str(i) for i in list])

    @staticmethod
    def list_dict_to_string(list, key_name):
        if list == None:
            return None
        if len(list) == 0:
            return None
        return ', '.join([item[key_name] for item in list])

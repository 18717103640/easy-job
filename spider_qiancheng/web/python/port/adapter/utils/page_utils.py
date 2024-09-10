class PageUtils:
    @staticmethod
    def get_page_num(total_count, pagesize):
        # 处理没有数据的特殊情况
        if total_count == 0:
            return 0
        elif total_count % pagesize == 0:
            return total_count // pagesize
        else:
            return total_count // pagesize + 1

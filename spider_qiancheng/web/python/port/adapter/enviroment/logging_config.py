import logging
from logging.handlers import RotatingFileHandler
import colorlog


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # 禁用日志传播

    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    )

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # 设置 formatter
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 创建文件处理器
    file_handler = RotatingFileHandler('easy_job.log', maxBytes=1024 * 1024 * 5, backupCount=5, encoding='utf-8',
                                       mode='a')
    # file_handler = logging.FileHandler(log_file, encoding='utf-8', mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

logger = setup_logger()


if __name__ == '__main__':
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')
    # 写入日志
    logger.info('实际请求 real_url: https://www.lagou.com/wn/zhaopin?fromSearch=true&kd=Java&city=南京')
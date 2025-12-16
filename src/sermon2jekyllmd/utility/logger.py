import logging

def setup_logger(log_file):
    """設置日誌記錄器。"""
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def write_to_log(message):
    """寫入訊息到日誌。"""
    logging.info(message)

def write_level_log(message, level):
    """寫入訊息到日誌。"""
    if level is None or level == '' or level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    else:
        logging.warning("Unsupported log level")

# 設置日誌記錄器
# log_file_path = "my_log.txt"
# setup_logger(log_file_path)
#
# # 寫入日誌
# log_message_info = "This is an informational message."
# log_message_error = "This is an error message."
#
# write_to_log(log_message_info)
# write_to_log(log_message_error, level=logging.ERROR)

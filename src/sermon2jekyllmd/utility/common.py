import datetime
import os
import re


def get_latest_file(directory):
    # 檢查目錄是否存在
    if not os.path.isdir(directory):
        raise ValueError(f"Directory {directory} does not exist")

    # 獲取目錄下的所有文件
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        raise ValueError(f"No files found in directory {directory}")

    # 找到最新的文件
    latest_file = max(files, key=os.path.getmtime)

    return latest_file


def get_latest_docx_file(directory):
    # 檢查目錄是否存在
    if not os.path.isdir(directory):
        raise ValueError(f"Directory {directory} does not exist")

    # 獲取目錄下所有的 .docx 文件
    docx_files = [os.path.join(directory, f) for f in os.listdir(directory) if
                  f.endswith('.docx') and os.path.isfile(os.path.join(directory, f))]

    if not docx_files:
        raise ValueError(f"No .docx files found in directory {directory}")

    # 找到最新的 .docx 文件
    latest_docx_file = max(docx_files, key=os.path.getmtime)

    return latest_docx_file

def get_current_week_of_year():
    # 獲取當前日期
    today = datetime.date.today()

    # 獲取今年的第一天
    first_day_of_year = datetime.date(today.year, 1, 1)

    # 計算當前日期是今年的第幾天
    day_of_year = (today - first_day_of_year).days + 1

    # 計算當前日期是今年的第幾周
    week_of_year = (day_of_year - 1) // 7 + 1

    return week_of_year


def get_current_week_of_year_iso():
    # 獲取當前日期
    today = datetime.date.today()

    # 使用isocalendar()方法獲取ISO週數
    year, week_of_year, weekday = today.isocalendar()

    return week_of_year

def get_year_as_string():

    return str(datetime.datetime.today().year)

def is_null_or_empty_or_whitespace(s):
    # 檢查字串是否為 None
    if s is None:
        return True
    # 使用正則表達式檢查字串是否為空值、全部都是空格、\r或空行
    if re.match(r'^\s*$', s):
        return True
    return False

def remove_spaces_and_newlines(text):
    # 使用正則表達式替換所有空格和分行符號
    cleaned_text = re.sub(r'[\s\n\r]+', '', text)
    return cleaned_text


def remove_extra_spaces(s):
    # 分割字串為單詞列表，同時保留頭尾的空格
    parts = s.split()
    # 過濾掉空白部分，僅保留單詞
    filtered_parts = [part for part in parts if part]
    # 使用單一空格連接單詞列表，並加回頭尾的空格
    result = ''.join(filtered_parts)
    if s.startswith(' '):
        result = ' ' + result
    if s.endswith(' '):
        result = result + ' '
    return result

def replace_line_breaks(text):
    # 將所有的'\n'替換成'\n\n'
    return text.replace('\n', '\n\n')

def is_underlined(text):
    """
    判斷字串是否被 <u> 標籤包圍
    :param text: 要檢查的字串
    :return: 如果被 <u> 標籤包圍則返回 True，否則返回 False
    """
    pattern = r'^<u>.*<\/u>$'
    return bool(re.match(pattern, text))


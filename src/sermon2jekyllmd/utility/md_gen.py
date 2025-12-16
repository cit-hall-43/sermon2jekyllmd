import re
import os
import datetime
from . import common

def gen_paragraph(text):
    markdown_text = []
    pattern = r'^(?:創|出|利|民|申|書|士|得|撒上|撒下|王上|王下|代上|代下|拉|尼|斯|伯|詩|箴|傳|歌|賽|耶|哀|結|但|何|珥|摩|俄|拿|彌|鴻|哈|番|該|亞|瑪|太|可|路|約|徒|羅|林前|林後|加|弗|腓|西|帖前|帖後|提前|提後|多|門|希|來|雅|彼前|彼後|約壹|約貳|約參|猶|啟)\s*\d+:\d+(?:-\d+)?'
    line = text.split('\n')
    markdown_text.append("### " + line.pop(0) + "\n\n")
    for l in line:
        matches = re.findall(pattern, l)
        # 找出所有符合模式的聖經引用
        if (len(matches) > 0):
            markdown_text.append("> " + l + "\n\n")
        else:
            #segments = re.split(r'[\\s|\\r|\\n]+', l)
            segments = l.split()
            if len(segments) > 1:
                segments[0] = f"**{segments[0]}** "
                markdown_text.append(''.join(segments) + "\n\n")
            else:
                markdown_text.append(l + "\n\n")

    return ''.join(markdown_text)

def gen_html_underline_from_cell(cell):
    for para in cell.paragraphs:
        for run in para.runs:
            # if run.bold:
            #     bold_text = remove_extra_spaces(run.text)
            #     if not is_null_or_empty_or_whitespace(bold_text):
            #         # 將有粗體的文字替換為markdown ** 語法
            #         bold_mrakdown = f"**{bold_text}**"
            #         # 替換原始文字
            #         run.text = bold_mrakdown
            if run.underline:
                if not common.is_underlined(run.text):
                    underlined_text = run.text
                    # 將有底線的文字替換為<u>語法
                    underlined_html = f"<u>{underlined_text}</u>"
                    # 替換原始文字
                    run.text = underlined_html

    return cell.text

def write_header(file_path):
    # 獲取今天的日期
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    current_year = datetime.date.today().year
    # 獲取當前日期
    today = datetime.date.today()
    # 使用isocalendar()方法獲取ISO週數
    _, week_of_year, _ = today.isocalendar()
    current_week_of_year = str(week_of_year)
    # Header 訊息
    header = f"""---
title: "{current_year}第{current_week_of_year}週導讀卡"
date: "{today_date}"
thumbnail: "/assets/img/thumbnail/"
tags:
bookmark: true
---
"""

    # 將 header 訊息寫入 Markdown 檔案
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(header)
        file.write("\n\n")
        file.close()

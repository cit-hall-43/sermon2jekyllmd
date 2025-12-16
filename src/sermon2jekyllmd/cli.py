from pathlib import Path
from utility import parser, logger, md_gen, common
import os

def get_file_paths(file_name):
    """
    根據輸入的文件名生成各種路徑。
    :param file_name: 文件名
    :return: 文件的路徑 (docx, md, log)
    """
    
    # cli.py 的實際檔案位置
    CURRENT_FILE = Path(__file__).resolve()

    # src/sermon2jekyll/cli.py
    # ↑ 往上三層 = 專案根目錄
    PROJECT_ROOT = CURRENT_FILE.parents[2]

    docx_file_path = PROJECT_ROOT / "docs" / f"{file_name}.docx"
    md_file_path = PROJECT_ROOT / "docs" / f"{file_name}.md"
    log_file_path = PROJECT_ROOT / "logs" / f"{file_name}.txt"
    return docx_file_path, md_file_path, log_file_path

def handle_null_input():
    """
    處理文件名為空的情況，獲取最新的docx文件並生成相應的路徑。
    :return: 文件的路徑 (docx, md, log)
    """

    # cli.py 的實際檔案位置
    CURRENT_FILE = Path(__file__).resolve()

    # src/sermon2jekyll/cli.py
    # ↑ 往上三層 = 專案根目錄
    PROJECT_ROOT = CURRENT_FILE.parents[2]

    print("Null INPUT, Set the last file as INPUT!")
    docx_file_path = common.get_latest_docx_file(os.path.join(PROJECT_ROOT, "docs"))
    print("The last file is:", docx_file_path)
    md_file_path = PROJECT_ROOT / "docs" / f"{common.get_year_as_string()}第{common.get_current_week_of_year_iso()}週導讀卡.md"
    file_name_with_extension = os.path.basename(docx_file_path)
    log_file_path = PROJECT_ROOT / "logs" / f"{os.path.splitext(file_name_with_extension)[0]}.txt"
    return docx_file_path, md_file_path, log_file_path

def main():
    file_name = input("Enter the docx name: ")
    # cli.py 的實際檔案位置
    CURRENT_FILE = Path(__file__).resolve()

    # src/sermon2jekyll/cli.py
    # ↑ 往上三層 = 專案根目錄
    PROJECT_ROOT = CURRENT_FILE.parents[2]

    if file_name:
        if os.path.isfile(PROJECT_ROOT / "docs" / f"{file_name}.docx"):
            docx_file_path, md_file_path, log_file_path = get_file_paths(file_name)
        else:
            raise ValueError(f"File name {file_name} does not exist")
    else:
        docx_file_path, md_file_path, log_file_path = handle_null_input()

    logger.setup_logger(log_file_path)

    table_data = parser.read_doc_table(docx_file_path)

    weekdays = ['週一', '週二', '週三', '週四', '週五', '週六']
    weekday_titles = []
    weekday_contents = []
    title = ''

    if len(table_data[0]) == 7:
        title, weekday_titles, weekday_contents = parser.parse_table_length_7(table_data)
        logger.write_to_log(title)
    elif len(table_data[0]) == 4:
        title, weekday_titles, weekday_contents = parser.parse_table_length_4(table_data)
        logger.write_to_log(title)
    elif len(table_data[0]) == 11:
        title, weekday_titles, weekday_contents = parser.parse_table_length_11(table_data)
        logger.write_to_log(title)
    elif len(table_data[0]) == 12:
        title, weekday_titles, weekday_contents = parser.parse_table_length_12(table_data)
        logger.write_to_log(title)
    else:
        logger.write_level_log(f'File format error: {len(table_data[0])}', 'error')
        exit(f'File format error: {len(table_data[0])}')

    md_gen.write_header(md_file_path)
    with open(md_file_path, 'a', encoding='utf-8') as mkfile:
        mkfile.write(f"# {title}\n\n")
        mkfile.write(f"___\n\n")
        for i in range(6):
            mkfile.write(f"## {weekdays[i]}\n\n")
            mkfile.write(md_gen.gen_paragraph(weekday_contents[i]))
            mkfile.write(f"___\n\n")

if __name__ == "__main__":
    main()

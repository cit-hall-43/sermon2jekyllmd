# sermon2jekyllmd

## Overview
`sermon2jekyllmd` converts `.docx` sermon guide files into Jekyll-compatible Markdown files for weekly devotionals. It reads a structured Word table, extracts titles and weekday content, applies markdown formatting, and writes both the `.md` output and a `.txt` log.

## Requirements
- Python 3.13+
- Dependencies in `requirements.txt` or `pyproject.toml`
  - `python-docx`
  - `pytest` for tests

## Installation
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Or use Poetry:
   ```sh
   poetry install
   ```

## Usage
1. Put your source `.docx` file into the `docs/` directory.
2. Run the converter:
   ```sh
   python src/sermon2jekyllmd/cli.py
   ```
   Or, if installed with Poetry:
   ```sh
   poetry run sermon2jekyllmd
   ```
3. When prompted, enter the base filename of the `.docx` file (without `.docx`).
4. If you press Enter without typing a filename, the script uses the latest `.docx` in `docs/` and generates a Markdown file named with the current year/week.

## Output
- Markdown output is written to `docs/` with a `.md` extension.
- Log output is written to `logs/` with a `.txt` extension.
- If the filename is empty, the log file uses the latest `.docx` basename, while the Markdown filename is generated from the current ISO week and year.

## Supported Table Formats
The CLI supports `.docx` tables with these column layouts:
- 7 columns
- 4 columns
- 11 columns
- 12 columns
- 14 columns (treated as 12-column format)

## Formatting Conventions
- Scripture references are written as Markdown blockquotes
- The first word of each paragraph is bolded
- Underlined text in `.docx` is converted to HTML-style `<u>...</u>` inside Markdown
- Output files include a front matter header with date, title, thumbnail, and bookmark metadata

## Project Structure
- `src/sermon2jekyllmd/cli.py`: Main CLI entrypoint and file-path handling
- `src/sermon2jekyllmd/utility/parser.py`: Reads `.docx` tables and parses supported table structures
- `src/sermon2jekyllmd/utility/md_gen.py`: Generates Markdown text and handles underline formatting
- `src/sermon2jekyllmd/utility/logger.py`: Sets up log output
- `src/sermon2jekyllmd/utility/common.py`: File/date utilities and text helpers
- `docs/`: Source `.docx` files and generated Markdown files
- `logs/`: Conversion logs

## Notes
- The script raises an error if a supplied file name does not exist in `docs/`.
- Only supported table formats are accepted; unsupported tables stop execution with a logged error.

## References
- Main entrypoint: `src/sermon2jekyllmd/cli.py`
- Utility modules: `src/sermon2jekyllmd/utility/`
- Package script: `poetry run sermon2jekyllmd`

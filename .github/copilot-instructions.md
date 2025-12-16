# Copilot Instructions for sermon2jekyllmd

## Project Overview
This project converts .docx sermon guide files into Jekyll-compatible Markdown files for weekly devotionals. The main workflow is orchestrated by `src/sermon2jekyllmd/cli.py`, which interacts with utility modules for parsing, logging, and Markdown generation.

## Key Components
- **CLI Entrypoint:** `src/sermon2jekyllmd/cli.py` handles user input, file path resolution, and coordinates the conversion process.
- **Utilities:**
  - `parser.py`: Reads and parses .docx tables, dispatches to different parsing functions based on table structure.
  - `md_gen.py`: Generates Markdown content, including special formatting for scripture references and underlined text.
  - `logger.py`: Handles logging to a file, with support for different log levels.
  - `common.py`: Provides helpers for file discovery, date/week calculations, and string utilities.
- **Input/Output:**
  - Input: `.docx` files in `docs/`
  - Output: Markdown files in `docs/`, logs in `logs/`

## Developer Workflows
- **Run Conversion:**
  - Execute `cli.py` (e.g., `python src/sermon2jekyllmd/cli.py`) and enter the base name of a `.docx` file (without extension) in `docs/`.
  - If no name is entered, the latest `.docx` in `docs/` is used automatically.
- **File Naming:**
  - Output Markdown and log files are named based on the input file or current week/year if input is empty.
- **Table Parsing:**
  - Table structure in `.docx` determines which parser function is used (`parse_table_length_7`, `parse_table_length_4`, etc.).
  - Only certain table formats are supported; errors are logged and halt execution if format is unrecognized.

## Project Conventions
- **Chinese Naming:** Many variables, comments, and file names use Chinese for clarity with the target audience.
- **Markdown Output:** Scripture references are blockquoted, and the first word of each paragraph is bolded.
- **Underlined Text:** Underlined text in `.docx` is converted to `<u>...</u>` in Markdown.
- **Logging:** All major steps and errors are logged to a file in `logs/`.

## Extending/Modifying
- Add new table parsing logic in `parser.py` if new formats are needed.
- Update `md_gen.py` for changes in Markdown formatting rules.
- Use `common.py` for date/week/file utilities to ensure consistency.

## References
- See `src/sermon2jekyllmd/cli.py` for the main workflow.
- See `src/sermon2jekyllmd/utility/` for utility modules and parsing logic.
- Input/output examples: `docs/`, `logs/`.

---
For questions about project-specific conventions or unclear patterns, consult the code in `src/sermon2jekyllmd/` and this file. Please update this document if you introduce new workflows or conventions.

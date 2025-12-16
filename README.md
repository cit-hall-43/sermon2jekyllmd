# sermon2jekyllmd

## Overview
This project converts `.docx` sermon guide files into Jekyll-compatible Markdown files for weekly devotionals. It is designed to automate the workflow for generating weekly devotional content from structured Word documents.

## Features
- Converts `.docx` tables to Markdown with special formatting for scripture references and underlined text
- Supports multiple table formats (7, 4, 11, 12 columns)
- Automatically names output files based on input or current week/year
- Logs all major steps and errors

## Project Structure
- `src/sermon2jekyllmd/cli.py`: Main CLI entrypoint; coordinates the conversion process
- `src/sermon2jekyllmd/utility/`: Utility modules for parsing, Markdown generation, logging, and common helpers
	- `parser.py`: Table parsing logic for different formats
	- `md_gen.py`: Markdown formatting and underlined text handling
	- `logger.py`: Logging utilities
	- `common.py`: File/date helpers and string utilities
- `docs/`: Input `.docx` files and output Markdown files
- `logs/`: Log files for each conversion

## Usage
1. Place your `.docx` sermon guide in the `docs/` directory.
2. Run the CLI:
	 ```sh
	 python src/sermon2jekyllmd/cli.py
	 ```
3. Enter the base name of your `.docx` file (without extension) when prompted. If left blank, the latest `.docx` in `docs/` is used.
4. The converted Markdown will be saved in `docs/`, and a log file will be created in `logs/`.

## Conventions
- Variable names, comments, and some file names use Chinese for clarity with the target audience
- Scripture references are blockquoted in Markdown; the first word of each paragraph is bolded
- Underlined text in `.docx` is converted to `<u>...</u>` in Markdown
- Only certain table formats are supported; errors are logged and halt execution if format is unrecognized

## Extending
- Add new table parsing logic in `parser.py` for new formats
- Update `md_gen.py` for changes in Markdown formatting rules
- Use helpers in `common.py` for consistent file/date handling

## References
- See `.github/copilot-instructions.md` for AI agent and contributor guidelines
- Key files: `src/sermon2jekyllmd/cli.py`, `src/sermon2jekyllmd/utility/`

---
For questions about project-specific conventions or unclear patterns, consult the code in `src/sermon2jekyllmd/` and `.github/copilot-instructions.md`.

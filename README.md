
# _Skillz.sh_

Skillz is a command-line application to manage and track your programming skills. It allows you to add, update, delete, and view your skill levels for various programming languages in an interactive and user-friendly way.

### Features

- **Add Skills**: Add a new programming language and its skill level.
- **Update Skills**: Update the skill level of an existing programming language.
- **Delete Skills**: Remove a programming language from the database.
- **View Skills**: Display a dashboard of all programming languages and their skill levels.
- **Clear All Data**: Delete all records from the database.
- **Interactive Command-Line Interface**: Easy-to-use CLI with colored output for better readability.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pythonicforge/Skillz.sh.git
   cd Skillz.sh
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

### Commands

- `add <language> <skill-level>`: Add a new programming language with a skill level (0-100).
- `update <language> <skill-level>`: Update the skill level of an existing programming language.
- `delete <language>`: Delete a programming language from the database.
- `deleteall`: Clear all data from the database.
- `show`: Display the skill chart.
- `clear`: Clear the terminal screen.
- `bye`: Exit the application.

### Example Usage

```bash
Welcome to Skillz! Type 'help' to list commands.

(sh) add Python 80
[INFO] Python added at skill level 80

(sh) show
DASHBOARD
Python          | ████████████-------- | 80/100

(sh) update Python 90
[INFO] Python updated to 90

(sh) delete Python
[INFO] Python deleted

(sh) bye
Bye 👋
```

### Dependencies

- Python 3.12
- `sqlite3`: Built-in Python library for database management.
- `termcolor`: For colored terminal output.

Install `termcolor` using:
```bash
pip install termcolor
```

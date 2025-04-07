import os
import sys
import cmd
import sqlite3
import builtins
from termcolor import colored
from typing import Optional, Literal

class Skillz(cmd.Cmd):
    os.system('clear')
    intro = "Welcome to Skillz! Type 'help' to list commands."
    prompt = "\n\n(sh) "

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout) 
        self.conn = sqlite3.connect('skillz.db')
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS skills (
                language TEXT PRIMARY KEY,
                skill_level INTEGER
            )
        ''')
        self.conn.commit()

    def do_show(self, arg:str) -> None:
        """Shows the skill chart."""
        self.cursor.execute("SELECT * FROM skills")
        rows = self.cursor.fetchall()
        self.print("DASHBOARD\n", "light_blue")
        for lang, skill in rows:
            self.print(f"{lang:<15} | {self.bar(skill)} \t {skill}/100", "white")

    def do_add(self, arg:str) -> None:
        """Add a new language and it's respective skill level: add <lang> <skill-level>"""
        try:
            language, skillLevel = arg.split()
            skillLevel = int(skillLevel)
            language = language.capitalize()
            if not (0 <= skillLevel <= 100):
                raise ValueError("Skill level should be between 0 and 100.")
            self.cursor.execute("INSERT INTO skills (language, skill_level) VALUES (?, ?)", (language, skillLevel))
            self.conn.commit()
            self.print(f"[INFO] {language} added at skill level {skillLevel}\n", "light_green")
        except sqlite3.IntegrityError:
            self.print(f"[ERROR] {language} already exists. Use `update` to modify.\n", "red")
        except Exception as e:
            self.print(f"[ERROR] {e}\n", "red")

    def do_update(self, arg:str) -> None:
        """Update an existing and it's respective skill level: update <lang> <skill-level>"""
        try:
            language, skillLevel = arg.split()
            skillLevel = int(skillLevel)
            language = language.capitalize()
            if not (0 <= skillLevel <= 100):
                raise ValueError("Skill level should be between 0 and 100.")
            self.cursor.execute("UPDATE skills SET skill_level = ? WHERE language = ?", (skillLevel, language))
            if self.cursor.rowcount == 0:
                raise ValueError(f"{language} doesn't exist. Use `add` instead.")
            self.conn.commit()
            self.print(f"[INFO] {language} updated to {skillLevel}\n", "light_green")
        except Exception as e:
            self.print(f"[ERROR] {e}\n", "red")

    def do_delete(self, arg: str) -> None:
        """
        Deletes a programming language from the skills database, handling errors and providing feedback.
        """
        try:
            language = arg.capitalize()
            self.cursor.execute("DELETE FROM skills WHERE language = ?", (language,))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                raise ValueError(f"{language} doesn't exist. Use `add` instead.")
            self.print(f"[INFO] {language} deleted\n", "light_green")
        except Exception as e:
            self.print(f"[ERROR] {e}\n", "red")

    def do_deleteall(self, arg: str) -> None:
        """Deletes all records from the skills table."""
        try:
            self.cursor.execute("DELETE FROM skills")
            self.conn.commit()
            self.print(f"[INFO] All data cleared.\n", "light_green")
        except Exception as e:
            self.print(f"[ERROR] {e}\n", "red")

    def do_clear(self, arg:str) -> None:
        os.system('clear')

    def do_bye(self, arg:str) -> None:
        """Exits the program."""
        self.print(f'Bye 👋\n',"light_cyan")
        sys.exit(0)

    def print(self, text:str, color:Optional[Literal['black', 'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'light_grey', 'dark_grey', 'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan', 'white']]) -> None:
        """Modified print function that prints text with colors"""
        builtins.print(colored(text, color))

    def bar(self, value: int, maxVal: int = 100, barLength: int = 20) -> str:
        """Generates a bar for the skill level of the languages"""
        filledLength = int((value / maxVal) * barLength)
        bar = "█" * filledLength + "-" * (barLength - filledLength)
        return f"{bar} |"

if __name__ == '__main__':
    try:
        Skillz().cmdloop()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt! Shutting down Skillz...")
        sys.exit(0)
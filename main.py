import os
import sys
import cmd
import builtins
from termcolor import colored
from typing import Optional, Literal

class Skillz(cmd.Cmd):
    os.system('clear')
    intro = "Welcome to Skillz! Type 'help' to list commands."
    prompt = "(sh) "

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout) 

    def do_show(self, arg:str) -> None:
        """Shows the skill chart."""
        self.print("DASHBOARD\n", "light_blue")

    def do_add(self, arg:str) -> None:
        """Add a new language and it's respective skill level: add <lang> <skill-level>"""
        try:
            language, skillLevel = arg.split()
            self.print(f'[INFO] {language} added at a skill level of {skillLevel}\n',"light_green")
        except ValueError as e:
            self.print(f"[ERROR] {e}\n", "red")

    def do_update(self, arg:str) -> None:
        """Update an existing and it's respective skill level: update <lang> <skill-level>"""
        try:
            language, skillLevel = arg.split()
            self.print(f'[INFO] {language} updated at a skill level of {skillLevel}\n',"light_green")
        except ValueError as e:
            self.print(f"[ERROR] {e}\n", "red")

    def do_bye(self, arg:str) -> None:
        """Exits the program."""
        self.print(f'Bye 👋\n',"light_cyan")
        sys.exit(0)

    def print(self, text:str, color:Optional[Literal['black', 'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'light_grey', 'dark_grey', 'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan', 'white']]) -> None:
        """Modified print function that prints text with colors"""
        builtins.print(colored(text, color))

if __name__ == '__main__':
    try:
        Skillz().cmdloop()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt! Shutting down Skillz...")
        sys.exit(0)
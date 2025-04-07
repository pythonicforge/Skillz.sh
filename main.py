import os
import cmd
from typing import Optional
import sys

class Skillz(cmd.Cmd):
    os.system('clear')
    intro = "Welcome to Skillz! Type 'help' to list commands."
    prompt = "(sh) "

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout) 

    def do_show(self, arg:str) -> None:
        """Shows the skill chart."""
        pass

    def do_add(self, arg:str) -> None:
        """Add a new language and it's respective skill level: add <lang> <skill-level>"""
        pass

    def do_update(self, arg:str) -> None:
        """Update an existing and it's respective skill level: update <lang> <skill-level>"""
        pass

    def do_bye(self, arg:str) -> None:
        """Exits the program."""
        pass

if __name__ == '__main__':
    try:
        Skillz().cmdloop()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt! Shutting down Skillz...")
        sys.exit(0)
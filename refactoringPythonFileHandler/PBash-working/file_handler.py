from __future__ import print_function
import sys
import re
from validator import Validator
from file_reader import *

class FileHandler:
    def __init__(self, new_validator):
        self.validator = new_validator

    def open(self, file_path):
        if re.search(r'\.csv$', file_path):
            return self.csv_dict_reader(file_path)
        elif re.search(r'\.txt$', file_path):
            return self.txt_dict_reader(file_path)
        elif re.search(r'\.xlsx$', file_path):
            result = self.excel_reader(file_path)
            if result and self.validator.check_data_set(result):
                return result
            else:
                print("There were no valid entries in the file", file=sys.stderr)
                return False
        else:
            print('Invalid file extension', file=sys.stderr)
            return False

    # Tim
    @staticmethod
    def open_rules():
        try:
            file = open('rules.txt', "r")
        except FileNotFoundError:
            print('Cannot find rules.txt', file=sys.stderr)
            return False
        rules = {}
        for line in file:
            if len(line.split("=")) == 2:
                key = line.split("=")[0]
                value = line.split("=")[1]
                value = value.rstrip('\n')
                rules[key] = value
            else:
                print('The file was in an invalid format', file=sys.stderr)
                return False
        return rules

    # Tim
    def set_rules(self):
        self.validator.set_rules(self.open_rules())

    # Rosemary
    @staticmethod
    def open_help(help_command):

        try:
            file = open("help.txt", "r")
            for line in file:
                if len(line.split("=")) == 2:
                    entries = line.split("=")
                    if help_command == entries[0]:
                        return entries[1].rstrip('\n')
                else:
                    print("Invalid help file format!")
        except FileNotFoundError:
            print('The help file was not found', file=sys.stderr)
        return "No such command."



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=1)

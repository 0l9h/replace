from colorama import init
from colorama import Fore, Back, Style
init()

class Replacement():
    i = 0
    def __init__(self, what_to_replace, replace_for):
        self.what_to_replace = what_to_replace
        self.replace_for = replace_for
        self.new_string = ''


    """".replace() WITH YOUR HANDS"""
    def InputReplace(self, old_string):
        self.old_string = old_string
        while Replacement.i < len(self.old_string):

            #   if any interval in old_string == what_to_replace
            if self.old_string[(Replacement.i) : (Replacement.i+len(self.what_to_replace))] == self.what_to_replace: 
                self.new_string += self.replace_for                             #   change it to replace_for
                Replacement.i += (len(self.what_to_replace)-1)             #   skip next values
            else:
                self.new_string += self.old_string[Replacement.i]          #   else: add char old_string[i] to new_string
            Replacement.i+=1
        print(Replacement.i)
        print(self.new_string)
        print(Fore.GREEN+Style.BRIGHT+'Succesful')

    """change another file"""
    def OutsideReplace(self, file_name):
        self.new_text = ''
        self.file_name = file_name
        with open(self.file_name, 'r') as read_file:
            reading = read_file.read()

        while Replacement.i < len(reading):
            #   if any interval in reading == what_to_replace
            if reading[(Replacement.i) : (Replacement.i+len(self.what_to_replace))] == self.what_to_replace: 
                self.new_text += self.replace_for                             #   change it to replace_for
                Replacement.i += (len(self.what_to_replace)-1)             #   skip next values
            else:
                self.new_text += reading[Replacement.i]          #   else: add char old_string[i] to new_string
            Replacement.i+=1
        
        with open(self.file_name, 'w') as write_to_file:
            write_to_file.write(self.new_text)

        print(Fore.GREEN+Style.BRIGHT+'Succesful')


choice = input('Print "input" if you want to change string inside program.\n\
Print "outside" if you want to change another file:\n\
Print "exit" to stop executing:\n')


if choice == 'input':
    old_string = input('Input string:\n')
    what_to_replace = input('Input chars you need to replace:\n')
    replace_for = input('Input replacement chars:\n')
    getClass = Replacement(what_to_replace, replace_for)
    getClass.InputReplace(old_string)

elif choice == 'outside':
    file_name = input('Print name of file you want to change:\n')
    what_to_replace = input('Input chars you need to replace:\n')
    replace_for = input('Input replacement chars:\n')
    getClass = Replacement(what_to_replace, replace_for)
    getClass.OutsideReplace(file_name)


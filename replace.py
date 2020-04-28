
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
        print(self.new_string)



choice = input('Print "input" if you want to change string inside program.\n\
Print "outside" if you want to change another file:\n\
Print "exit" to stop executing:\n')

if choice != 'exit':
    what_to_replace = input('Input chars you need to replace:\n')
    replace_for = input('Input replacement chars:\n')
    getClass = Replacement(what_to_replace, replace_for)

if choice == 'input':
    old_string = input('Input string:\n')
    getClass.InputReplace(old_string)

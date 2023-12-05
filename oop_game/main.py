# Project Definition

# Build an escape room game
## Room contains several objects
## Players need a code to escape
## Objects provide clues about the code

### Each item can be look at, smelled, or touched
### Each sense provides new information
### Players discern information based on interaction

### Game components
# GameObject
# Room
# Game

# Declared GameObject class
class GameObject:
    name = ""
    appearance = ""
    feel = ""
    smell = ""

# Initialized that sets up the fields of a class
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell
        
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"
      
    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"
      
    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"
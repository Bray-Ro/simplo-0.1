# uses python3
from random import *
from termcolor import colored
variable_names = []
variable_values = []
variables = -1
value = 0
print_var = None
def new_command():
    global print_var
    global variables
    global value
    global variable_values
    global variable_names
    command = input("skyscript 2 >")
    if command[:4] == "ling":
       
        variables += 1
        value = command.replace(command[:12], '')
        
        command = command.replace(command[:4], '')
        command = command.split()
        var_length = len(command)
        
        variable_names.insert(variables, command[0])
        print(command)
        print("var names: " + str(variable_names))

        variable_values.insert(variables, value)
        print(colored("Variable " + variable_names[variables] + " has been made with a value of " + value, "green"))
    if command[:5] == "echo ":
        command = command.replace(command[:4], '')
        print(command)
    if command[:10] == "echo_var: ":
        command = command.replace(command[:10], '')
        command = variable_names.index(command)
        value = variable_values[command]
        print(value)    
    if command[5] == "add: ":
        command = command.replace(command[:5, ''])
        
        problem = command.split(' ')
        value1 = problem[0]
        value2 = problem[2]
        value1 = int(value1)
        value2 = int(value2)
        print(str(problem))
        command = str(value1 + value2)
        print(command)
    new_command()
new_command()

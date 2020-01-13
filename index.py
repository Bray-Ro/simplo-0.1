# uses python3

import os
from random import *
import psutil
from termcolor import colored
program = []
variable_names = []
variable_values = []
variables = -1
value = 0
print_var = None
print(colored("**** Skyscript v2 ****", "green"))
print(psutil.virtual_memory())
print()
def new_command():
    global program
    global print_var
    global variables
    global value
    global variable_values
    global variable_names
   
    command = input("Mac Skyscript V2 >")
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
    if command[:9] == "echo_var ":
        command = command.replace(command[:9], '')
        command = variable_names.index(command)
        value = variable_values[command]
        print(value)    
    if command == "new_program":
        print(colored("Creating a new program...", "green"))
        program = []
        lines = 0
        running_line = -1
        line_running = None
        def run(running_line):
            
            running_line += 1
            if running_line == lines:
                print("program completed")
            else:
                line_running = program[lines]
                if  program[:5] == "echo ":
                    command = command.replace(command[:4], '')
                    print(command)
        def new_line(lines):
            
            lines += 1
            
            line = input("> ")
            program.insert(lines, str(line))
            new_line(lines)
        new_line(lines)
    new_command()
new_command()

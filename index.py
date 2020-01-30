#!/usr/bin/env python
# work on ling command next
# simplo transpiler version 0.1 BETA by Rohan Samra-O'Neill
import sys
for arg in sys.argv:
    with open(arg) as file:
        goto_repeat = 0
        goto_on = 0
        variable_names = []
        variable_values = []
        variables = -1
        value = None
        prog = file.read()
        prog = prog.split(';')
        
        running_line = 0
        line_running = None
        def new_line():
            global goto_on
            global goto_repeat
            global value
            global prog
            global running_line
            global line_running
            global variables
            global variable_values
            global variable_names
            # set the variable line_running to the line that is running
            line_running = prog[running_line]
            if line_running[:1] == '#':
                running_line += 1
                new_line()
            if  line_running[:5] == 'echo ':
                
                line_running = line_running.replace(line_running[:5], '')
                
                print(line_running)
                
                if running_line == len(prog):
                    print("program completed")
                else:
                    running_line += 1
                    new_line()
                    # WORK ON NEXT
            if line_running[:5] == "goto ":
                line_running = line_running.replace(line_running[:5], '')
                
                line_running = line_running.replace(line_running[2:], '')
                if goto_repeat == 0:
                  goto_repeat = line_running[1:]
                  goto_on = 0
                goto_on += 1
                
                running_line = line_running
                running_line = int(float(running_line))
                if goto_on == 300:
                  print("program completed")
                else:
                  
                  new_line()
            if line_running[:5] == "ling ":
                variables += 1
                value = line_running.replace(line_running[:12], '')
                
            
                line_running = line_running.replace(line_running[:4], '')
                line_running = line_running.split()
                var_length = len(line_running)
            
                variable_names.insert(variables, line_running[0])
                
               

                variable_values.insert(variables, value)
                running_line += 1
                if running_line == len(prog):
                    print("program completed")
            
                else:
                    
                    new_line()
            line_running = str(line_running)
            if line_running[:9] == "echo_var ":
                line_running = line_running.replace(line_running[:9], '')
                if line_running in variable_names:
                  line_running = variable_names.index(line_running)
                  value = variable_values[line_running]
                  print(value)  
                  running_line += 1
                  if running_line == len(prog):
                      print("program completed")
                  else:
                      
                      new_line()
                else:
                  print("Reference error on line " + str(running_line + 1) + " unknown variable name")
        new_line()
                    






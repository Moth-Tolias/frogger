#goal: a functional frogger
#sub-goal: a mutable string array

import time
OUTLINES=""
LINES = ["","0010000001","0000000101","0000100000","0010100100","0010001010",""]
j=0

def moveline(line_to_edit): #prints the line moved down a bit
    NEWSTR ="" #output
    #print(line_to_edit)#debug
    i = 1#offset
    for char in line_to_edit:#check each character
        if line_to_edit.rfind("1",i,i+1) != -1: #if the next char is 1
            NEWSTR += "1" #move it
        else:
            NEWSTR += "0" #don't move it
        
        i += 1
    return(NEWSTR)

#main loop
while 1:
    OUTLINES += moveline(LINES[j]) #add the output
    LINES[j] = moveline(LINES[j]) #change the array
    OUTLINES += "\n" #add a new line
    j += 1 #next line
    if j > 6:
        j = 0 #reset
        print(OUTLINES) #print the output for this cycle
        OUTLINES = "" #cleanse the output
        time.sleep(0.5) #wait a bit


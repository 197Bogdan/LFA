 lambda-NFA class that checks if a string is valid for given machine ( through method lambdanfa.isValidString(string) ) <br>
 implies functionality for NFA/DFA input

lambda-NFA object can be created through constructor input <br>
Arguments:  <br>
>node_count - integer, number of nodes/states  <br>
transitions - list of tuples of format (node1, node2, letter)      example: (1, 2, 'b'), (0, 2, 'a')  // use '#' for 'lambda'<br>
entry_state - integer, represents entry node  <br>
fstates - list of integers, represents exit nodes <br>

lambda-NFA object can also be created by file input. Note: {variable} means the content of the variable <br>
Syntax: <br>
>{node_count}, {transition_count}        // integers  <br>
{transition_count} lines, each representing a transition    // line format: {node1}, {node2}, {letter}  <br>
{entry_state}   // integer  <br>
{finalstates_count} {final_state1} {final_state2} ..... {last_final_state}    // integers <br>


Example of both methods of creating objects can be found in main.py / lambdaNFA.txt

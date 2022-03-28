class lambdaNFA:
    def __init__(self, node_count=0, transitions=None, entry_state=-1, fstates=None):
        if transitions is None:
            transitions = []
        if fstates is None:
            fstates = []

        self.node_count = node_count
        self.nodes = []
        self.createNodes(node_count)

        self.fstates = []
        self.fstate_count = 0
        self.setFinalStates(fstates)

        self.transition_count = 0
        self.transitions = []
        self.addTransitions(transitions)

        self.entry_state = entry_state

        self.solution = False
        self.last_string = [0]*node_count
        self.route = []

    def resetNodes(self):
        self.nodes.clear()

    def createNodes(self, node_count):
        for _ in range(node_count):
            self.nodes.append([False, []])

    def resetFinalStates(self):
        for node in self.nodes:
            node[0] = False
        self.fstate_count = 0

    def setFinalStates(self, fstates):
        self.resetFinalStates()
        for fs in fstates:
            self.nodes[fs][0] = True
        self.fstate_count = len(fstates)
        self.fstates = fstates

    def addTransitions(self, transitions):
        for t in transitions:
            self.nodes[t[0]][1].append((t[1], t[2]))
        self.transition_count += len(transitions)
        self.transitions.extend(transitions)

    def ResetTransitions(self):
        for node in self.nodes:
            node[1].clear()
        self.transition_count = 0

    def print_info(self):
        print(f"Nodes[{self.node_count}]: {self.nodes}")
        print(f"Transitions[{self.transition_count}]: {self.transitions}")
        print(f"Entry state: {self.entry_state}")
        print(f"Final states[{self.fstate_count}]: {self.fstates}")

    def isValidString(self, string, node=None):
        if node is None:
            node = self.entry_state
        self.route.clear()
        self.last_string = [0]*self.node_count
        self.solution = False
        return self.__isValidString_recursive(string, node)

    def __isValidString_recursive(self, string, node):
        self.route.append(node)
        if string == "":       # if empty string + final state
            if self.nodes[node][0]:
                self.solution = True
                return True

        for t in self.nodes[node][1]:
            if t[1] == '#':
                if not self.last_string[node] == string:    # if not lambda loop
                    self.last_string[node] = string
                    self.__isValidString_recursive(string, t[0])    # lambda transition to next node
                    self.last_string[node] = 0
                else:
                    self.route.pop()
                    return
            if self.solution:
                return True

            if string:
                if t[1] == string[0]:
                    self.__isValidString_recursive(string[1:], t[0])    # letter transition to next node
                if self.solution:
                    return True
        self.route.pop()
        return False


def createNFAfromFile(file_in):
    node_count, transition_count = [int(x) for x in file_in.readline().split()]
    transitions = []
    for _ in range(transition_count):
        line = file_in.readline().strip().split()
        transitions.append((int(line[0]), int(line[1]), line[2]))
    entry_state = int(file_in.readline())
    final_states = [int(x) for x in file_in.readline().strip().split()[1:]]
    nfa = lambdaNFA(node_count, transitions, entry_state,  final_states)
    return nfa


m = lambdaNFA(4, [(0, 1, 'a'), (0, 1, 'b')], 0, [0, 3])         # NFA by constructor
m.addTransitions([(1, 2, 'c'), (2, 3, 'd')])
m.print_info()
print()
print(m.isValidString("acd"))
print(m.isValidString("ccd"))
print(m.isValidString(""))
m.resetFinalStates()
print(m.isValidString("acd"))
print()
print()


f_in = open("lambdaNFA.txt", 'r')
n = createNFAfromFile(f_in)             # NFA by file input
n.print_info()
print()

nr_cuvinte = int(f_in.readline())
cuvinte = []
for i in range(nr_cuvinte):
    cuvinte.append(f_in.readline().strip())
    if cuvinte[-1] == "#":      # empty string notation
        cuvinte[-1] = ""
    print(f"String: {cuvinte[-1]}")
    if n.isValidString(cuvinte[-1]):
        print("Valid")
    else:
        print("Invalid")
    print(n.route)
    print()

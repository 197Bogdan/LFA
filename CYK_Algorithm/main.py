class CFGrammar:
    def __init__(self, productions_strings):
        self.productions_strings = productions_strings
        self.productions = dict()
        for production in productions_strings:
            left_side, right_side = production.split('->')
            for part in right_side.split('|'):
                part = part.replace(" ", "")
                try:
                    self.productions[part].append(left_side.strip())
                except KeyError:
                    self.productions[part] = [left_side.strip()]

    def CYK(self, word):
        CYK_matrix = [0]    # index matrix lines from 1
        word_size = len(word)

        CYK_matrix.append([])       # particular case, first line of the matrix
        CYK_matrix[1].append(0)     # index columns from 1
        for letter in word:
            CYK_matrix[1].append(self.productions[letter])

        for substring_size in range(2, word_size + 1):      # for every line
            CYK_matrix.append([])
            CYK_matrix[substring_size].append(0)    # add line to matrix, indexed from 1
            for substring_start in range(1, word_size - substring_size + 2):    # for every column/cell
                substr_size_split1 = 1
                substr_size_split2 = substring_size - 1
                matrix_cell = set()
                while substr_size_split1 < substring_size:   # for every way the size can be split in sum of two
                    for str1 in CYK_matrix[substring_size-substr_size_split2][substring_start]:
                        for str2 in CYK_matrix[substring_size-substr_size_split1][substring_start + substr_size_split1]:
                            try:
                                for element in self.productions[str1+str2]:  # cartesian product of the sets, converted to the nonterminal they can be obtained from
                                    matrix_cell.add(element)
                            except KeyError:
                                pass

                    substr_size_split1 += 1
                    substr_size_split2 -= 1
                CYK_matrix[substring_size].append(list(matrix_cell))
        if 'S' in CYK_matrix[word_size][1]:
            return True
        return False


productions = ["S -> S  H1 | D H2  | SS | H2 H1 | H1 H2",
               "H1 -> b",
               "B -> H2S",
               "H2 -> a",
               "D -> H1 S"]
# this CFG is equivalent to  S -> aSb | bSa | SS | ab | ba
# which generates any word with number of a's equal to number of b's
# grammar converted to CNF using https://cyberzhg.github.io/toolbox/cfg2cnf
cfg = CFGrammar(productions)
print(cfg.productions)      # shows the set of terminals from which the key can be obtained

if cfg.CYK("ab"):
    print("Accepted")
else:
    print("Denied")

if cfg.CYK("abbba"):
    print("Accepted")
else:
    print("Denied")

if cfg.CYK("bbaaaabb"):
    print("Accepted")
else:
    print("Denied")

if cfg.CYK("bbbabaaababbaa"):
    print("Accepted")
else:
    print("Denied")

if cfg.CYK("aababa"):
    print("Accepted")
else:
    print("Denied")

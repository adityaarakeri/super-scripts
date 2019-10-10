import re
# Integer number represent priority of pattern 
BASE_PATTERN_LABELS = ['a-z', 'A-Z', '0-9' ]
OPTIONAL = tuple('?')
CHOICE = tuple('|')

def enclose(s):
    return '[' + s + ']'

PATTERNS_DICT = {}
for i in range(1, len(BASE_PATTERN_LABELS)+1):
    PATTERNS_DICT.update({(i,l) : re.compile(enclose(l)) for l in BASE_PATTERN_LABELS })


# Assign pattern to a single letter from base patterns if it can be assigned
def generate_pattern_from_letter(letter):
    for label, pattern in sorted(PATTERNS_DICT.items()):
        if label[0] == 1 and re.match(pattern, letter):
            return enclose(label[1])    
    return letter

# Convert contiguous list of same letter/pattern to plus notation and return the new list         
def contiguous_to_plus(lst):
    for l in range(1, len(lst)//2 + 1):
        i = 0
        while i < len(lst) :
            j = i + l
            while j < len(lst) and lst[j:j+l] == lst[i:i+l]:
                j += l
            if j > i+l :
                newElement = '(' + ''.join(lst[i:i+l]) + ')+'
                del lst[i+1:j]
                lst[i] = newElement
            i += 1
    return lst

# Note give as exp1 the bigger term
def get_bigger(exp1, exp2):
    i = 0
    j = 0
    while i < len(exp1) and j < len(exp2) :
        if exp1[i] == exp2[j]:
            i += 1
            j += 1
        else:
            j = 0
            while i < len(exp1) and exp1[i] != CHOICE:
                i += 1
            try :                
                if exp1[i] == CHOICE:
                    i += 1
            except:
                pass
                
    if j == len(exp2) :
        if i == len(exp1) or exp1[i] == OPTIONAL or exp1[i] == CHOICE  :
            return exp1
        else:
            #TODO: Now that exp2 is exausted make rest of exp1 optional
            #For now just returning as a choice by combining with or operator
            return exp1 + [CHOICE] + exp2
    elif i == len(exp1):
        #we are assuming exp2 will not have OPTIONAL OR CHOICE
        return exp1 + [CHOICE] + exp2
    else :
        raise Exception ('Any one of the striing should have been exausted')
    
            


def union(exp1, exp2):
    if exp1 == exp2 :
        return exp1
    elif len(exp1) == 0:
        if exp2[-1] != OPTIONAL:
            exp2.append(OPTIONAL)
        return exp2
    elif len(exp2) == 0:
        if exp1[-1] != OPTIONAL:
            exp1.append(OPTIONAL)
        return exp1
    else:
        return get_bigger(exp1, exp2)

def raw_string(s):
    if isinstance(s, str):
        s = s.encode('string-escape')
    elif isinstance(s, unicode):
        s = s.encode('unicode-escape')
    return s

def concat (lst):
    START = '^'
    END = '$'

    res = START

    for el in lst :
        if isinstance(el, str):
            res += el
        elif isinstance (el, list):
            #TODO: Put parantheses on each OR block
            elstr = ''
            firstOpt = True
            firstCh = True
            for subel in el:
                if isinstance(subel, str):
                    elstr += subel
                elif subel == CHOICE:
                    if firstCh:
                        elstr = '(' + elstr
                        firstCh = False
                    elstr += ')' + CHOICE[0] + '('
                elif subel == OPTIONAL :
                    if firstOpt and firstCh:
                        elstr = '(' + elstr
                        firstOpt = False
                    elif not firstCh:
                        firstOpt = False
                    elstr += ')' + OPTIONAL[0]
                else:
                    raise TypeError('Not handled type {}'.format(subel))
            if not firstCh:
                elstr += ')'
            res += '(' + elstr + ')'
        else:
            pass
    res = res + END
    return raw_string(res)
    


        

    
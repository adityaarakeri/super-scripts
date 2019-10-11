## Overview
* Problem Statement
* Design Thoughts
* System Requirements
* Getting Started

## Problem Statement
Give a list of strings, generate a loose regex that pass all these strings and the strings that follow the similar pattern.

## Design Thoughts
As the problem statement states that strings with similar pattrens should pass
but the similarities may be of different kind and may also sometimes depend on the context to which the strings are from.

So we will be grouping letters to basic regex classes which are as follows:
* [a-z]
* [0-9]
* [A-Z]

But this way we won't be able to find common substrings, to resolve that issue,
we first find common stems in all the string of a user defined length and then classify.

Finally we merge all the intermediate regex forms of all the strings.


## System Requirements
*Python(2/3)

## Getting Started
Navigate to the root directory of the repo . Then run the following bash command to install library
```bash
pip install .
```

Now you can convert a list of strings to regex as follows

```bash
>>> from makere import Makere
>>> ob = Makere(['ak123', 'ak23', 'ak45'])
>>> ob.make()
'^(([a-z])+([0-9])+)$'
```
You can also convert a file containing a list of strings to regex as follows:

```bash
>>> ob2 = Makere(r'test_file.txt') #Absolute location of testfile is needed
>>> ob2.make()
'^http((s)?)://www.lifewire.com/((([a-z])+-)+([a-z])+)-google-((([0-9])+)|(([a-z])+-([0-9])+))$'
```
Contents of test_file can be found in the test folder of this library.







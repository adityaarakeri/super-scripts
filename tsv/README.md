# Tab Separated Values
## Usage:

There are 2 ways to use this script.

You can `cat` a file to it and as the argument of this script, a space separated list of column numbers you want to print.

```
cat /tmp/your.tsv | tsv/print_columns.sh 1 2 4
cat /tmp/your.tsv | tsv/print_columns.sh
```

Or you can redirect the content of the file to shell's stdin by using `<`

```
tsv/print_columns.sh  < /tmp/your.tsv
tsv/print_columns.sh 1 2 4 < /tmp/your.tsv
```


### Requirements
Awk
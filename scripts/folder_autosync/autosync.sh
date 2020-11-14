fswatch -o $1 | xargs -n1 -I{} rsync -r -a --delete $1 $2:$3

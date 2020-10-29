#!/usr/bin/env bash

SPIN='-\|/'

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NOCOLOR='\033[0m'

# Go build can be changed here.
GOBUILD='env GOOS=linux go build -ldflags="-d -s -w -X main.minversion=`date -u +.%Y%m%d.%H%M%S`" -tags netgo -installsuffix netgo -o'

printf "> Clean bin\\r"
rm -rf bin/
echo -e "${GREEN}✓ Clean ./bin${NOCOLOR}"

for path in "$@"; do
    for f in $(find $path/* -maxdepth 0 -type d); do
        dest="bin${f#"$path"}"
        src=$f/*.go

        eval $GOBUILD $dest $src &
        pid=$! ## PID of last command

        function stop() {
            echo -e "${RED}✕ Exited: compiling $f${NOCOLOR}"
            kill $pid 2>/dev/null
        }

        # If this script is killed, kill 'go build':
        trap stop EXIT

        i=0

        # While 'go build' is running:
        while kill -0 $pid 2>/dev/null; do
            i=$(((i + 1) % 4))
            printf "> Compiling %s: %s\\r" $f ${SPIN:$i:1}
            sleep .1
        done

        echo -e "${GREEN}✓ Compiled $f ... DONE${NOCOLOR}"
    done
done

# Disable the trap on a normal exit:
trap - EXIT

echo -e "${GREEN}✓ All compiled${NOCOLOR}"
echo -e "${YELLOW}⌛ Elapsed: $(($SECONDS / 3600))hrs $((($SECONDS / 60) % 60))min $(($SECONDS % 60))sec${NOCOLOR}"
exit 0

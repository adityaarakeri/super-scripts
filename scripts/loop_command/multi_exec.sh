#!/bin/bash

COMMAND=${1}
LOOPS=${2}

if [[ -z "${LOOPS}" || ! "${LOOPS}" =~ ^[0-9]+$ ]]; then
    LOOPS=5
fi

for (( i = 1; i <= ${LOOPS}; i++ )); do
	echo -n "#${i}: "
	COMMAND_RESPONSE=$(${COMMAND})

    echo ${COMMAND_RESPONSE}
done
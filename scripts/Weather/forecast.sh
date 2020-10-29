#!/bin/bash

CITY="${1}"

# Make sure to have your default city here
if [[ -z "${CITY}" ]]; then
	CITY="Düsseldorf"
fi

# Special thanks to the service itself!
curl http://v2.wttr.in/${CITY}
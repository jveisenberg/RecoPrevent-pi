#!/bin/bash
#
# start the RecoPrev Application
#
#SERVICE="python3 recoprev_v2_02.py"
SERVICE="python3 recoprev_v3_00.py"
if ps -C "$SERVICE" >/dev/null
then
    echo "$SERVICE is running"
    exit 1
else
    cd /home/pi/dev/recoprev
    DISPLAY=:0.0 $SERVICE &
fi



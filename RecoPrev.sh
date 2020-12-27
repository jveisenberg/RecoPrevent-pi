#!/bin/bash
#
# start the RecoPrev Application
#
#SERVICE="python3 recoprev_v2_02.py"
SERVICE="python3 recoprev_v4_00.py"
if ps -C "$SERVICE" >/dev/null
then
    echo "$SERVICE is running"
    exit 1
else
    cd /home/alpha/develop/jve/RecoPrevent-pi
    DISPLAY=:0.0 $SERVICE &
fi

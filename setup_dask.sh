#!/bin/bash

IP=192.168.2.10
NUM_WORKERS=3
PORT=8786

is_dask=$(screen -ls | grep dask_scheduler)
if [[ -z "$is_dask" ]]; then
    screen -d -m -S dask_scheduler bash -c "dask-scheduler --host $IP --port $PORT"
    sleep 2s #arbitrary
    for i in $(seq 1 $NUM_WORKERS); do
        screen -d -m -S dask_worker_$i bash -c "dask-worker $IP:$PORT"
    done
else
    echo "You already have a dask-scheduler running."
fi;

#!/bin/bash

shutdown_screen(){
    screen -S $1 -p 0 -X stuff $'\003'
    screen -S $1 -p 0 -X stuff "y$(printf \\r)"
}

shutdown_screen dask_scheduler

NUM_WORKERS=$(screen -ls | grep dask | wc -l)
for i in $(seq 1 $NUM_WORKERS); do
    shutdown_screen dask_worker_$i
done;

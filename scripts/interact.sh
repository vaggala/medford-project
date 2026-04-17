#!/bin/bash

# config as needed

function f_interact() {
    Nodes=$1
    cpus=$2
    TIME=$3
    salloc --time=$TIME --nodes=$Nodes --ntasks-per-node=$cpus -pice-cpu --mem=0
}

NODES=1
CPUS=24
TIME="10:00:00"

f_interact $NODES $CPUS $TIME

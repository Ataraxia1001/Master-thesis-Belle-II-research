#!/bin/bash
source /cvmfs/belle.cern.ch/tools/b2setup release-05-01-25
basf2 /afs/desy.de/user/j/jjjy213/htcondor/Steering_combined.py $1 $2

#!/usr/bin/env python

################
### Includes ###
################

# Command Line Parsing
import argparse

# Platform Detection
import platform

# Creating Files / Path Checks
import os

#################
### Functions ###
#################

# Determines platform being run
# Exits program if platform is not supported
def os_check():
    plat = platform.system()
    if(plat == "Darwin"):
        return plat
#    elif(plat == "Windows"):
#        release = platform.release()
#        if(release == "10"):
#            return release
#        elif(release == "7"):
#            return release
    else:
        print "Platform not supported"
        exit(1)

# Run all the things
def robbery(os):
    print os
    return;

##############################
### Command Line Arguments ###
##############################

argparser = argparse.ArgumentParser(description='Looter script, collects juicy data for malicious use.')
argparser.add_argument('-a','--all', action='store_true', help='perform all collections')
args = argparser.parse_args()

####################
### Main Program ###
####################

# Calls platform information function
plat = os_check()

# Argument tree for appropriate functionality
if args.all:
    robbery(plat)
        
# End Program
exit(0)
    












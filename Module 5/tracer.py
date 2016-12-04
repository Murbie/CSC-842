# Author - Kyle Murbach
# CSC-842-D30
# tracer.py

################
### Includes ###
################

# Command Line Parsing
import argparse

# Scapy
import pcapy
from scapy.all import *

# Sockets
import socket


##############################
### Command Line Arguments ###
##############################

argparser = argparse.ArgumentParser(description='TCP SYN Tracer Script')
argparser.add_argument('-i','--ip', action='store', dest='ip', help='specify the ip address to trace (IPv4)')
argparser.add_argument('-t','--target', action='store', dest='target', help='specify the hostname to trace')
args = argparser.parse_args()

#################
### Functions ###
#################
def main():
	# Checks to make sure that only one argument is provided
	if (args.ip and args.target):
		print "Specify one argument or the other, not both!"
		exit(3)
	# Checks to make sure that an argument is provided
	if (not args.ip and not args.target):
	    print "Specify an IP address or hostname to trace using either -i or -t"
	    exit(2)

	# Obtains the IP address of the hostname if specified
	if args.target:
		# Prints target hostname and attempts to resolve the hostname
		print "Target hostname is:", args.target
		destination = socket.gethostbyname(args.target)
	else:
		destination = args.ip

	# Prints target IP address
	print "Target IP is:", destination

	# SCAPY packet generation / sending
	# sr is a scapy function that sends/receives packets
	# IP is a scapy function that allows you to craft a packet
	# dst contains destination ip
	# ttl contains TTL range to go through, or a single value
	# Randshort randomizes the id used for packets sent
	# TCP flag is raised
	# verbose is turned off to hide packet sending (1/2 for enable levels)
	# inter is the interval at which packets are sent
	# retry is how many times the packet will be resent if timed out
	# timeout is how many seconds it will wait before timing out
	# all results are stored in first variable
	# non responses are stored in the second variable
	res,nores=sr(IP(dst=destination,ttl=(1,20),id=RandShort())/TCP(flags=0x2),verbose=0,inter=1,retry=-2,timeout=3)

	boolean = False
	# loops through results from sr function above
	for res,rcv in res:

		# boolean function to identify if destination is reached
		if boolean == True:
			if args.target:
				print res.ttl, args.target
			return;

		# disassembles results into IP address
		# attempts to resolve hostname, if fails, just prints IP
		# clean up output with python translate function
		try:
			val = [] 
			remove = [',','[',']','\'']
			val = socket.gethostbyaddr(rcv.src)
			ip = str(val[2])
			ip = ip.translate(None,''.join(remove))
			hostname = str(val[0])
			hostname = hostname.translate(None,''.join(remove))
			print res.ttl, ip, hostname

		except:
			print res.ttl, rcv.src	

		# checks to see if payload is SYN ACK (syn ack is received when destination is reached
		if isinstance(rcv.payload,TCP):
			boolean = True

	return;

####################
### Main Program ###
####################

if __name__ == "__main__":
    main()



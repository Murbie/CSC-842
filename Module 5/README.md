#Module 5 - TCP SYN Tracer
##Idea
For my last cycle, I wanted to return to Python and learn more about networking actually use scapy in Python.  I found a project in Josh's spreadsheet that seemed to be an attainable goal, which is shown in the next section below.

##Objective
Corey Steele- Write a TCP SYN tracer that starts with a TTL of 1 and walks the packet to its destination by incrementing the TTL.  This sort of tool can often identify passive/in-line devices that don't show-up on normal traceroute results. Key criteria is the tool should recognize when its reached its destination, and stop; also should stop after 254 hops (or whatever the maximum TTL for the OS is.) 

##Files Overview:
* tracer.py - main script that executes the TCP tracer

##Script Usage & Functionality Walkthrough
Execute the Python Script with the -i flag to trace an IP address.

python trace.py -i <IP ADDRESS>

Execute the Python Script with the -t flag to trace a hostname.

python trace.py -t <HOSTNAME>

##Resources
Scapy in Python - overview / basics
http://www.secdev.org/projects/scapy/doc/usage.html

Scapy in Python - extensive
http://www.secdev.org/projects/scapy/files/scapydoc.pdf

More Scapy Info
https://theitgeekchronicles.files.wordpress.com/2012/05/scapyguide1.pdf

Socket Example
http://staff.washington.edu/jon/python-course/python_traceroute.py

##Future Work
Greppable output, text file format

XML formmatted output

Having more flags for other traceroute activities such as protocol type, etc. (only does TCP right now)

IPv6 Support
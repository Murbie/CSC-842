#Module 1 - looter.py 
##Idea
On the 842 Ideas Spreadsheet, Andrew Kramer suggested the idea of creating an automated looting script that will collect relevant data for someone who gained root access to a box.  This is great for red team exercises where the attacker wants to be able to quickly grab useful files and data before getting booted off the system.

##Purpose
This script will crawl through a box and quickly collect useful information for an attacker.

#Help Screen 
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
#Usage Examples

#Other

#Future Work

#Resources
https://pymotw.com/2/argparse/

http://stackoverflow.com/questions/3718657/how-to-properly-determine-current-script-directory-in-python

http://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python

http://stackoverflow.com/questions/2032403/how-to-create-full-compressed-tar-file-using-python

http://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running

https://docs.python.org/2/library/os.path.html#os.path.basename

http://stackoverflow.com/questions/29065781/how-can-i-get-a-python-program-to-kill-itself-using-a-command-run-through-the-mo


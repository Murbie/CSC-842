#Module 4 - scan.ps1
##Idea
Get some hands on with PowerShell and learn the basics of the language after seeing many examples of PowerShell scripts in other cycles! My objective for this cycle was derived from the spreadsheet that Josh provided, which is shown in the next section below.

##Objective
Buzz Hillestad - This script/tool will detect if there is anti-virus software on the asset in which it is being run. It will then use domain credentials to access the registries of other network assets on the same LAN and attempt to detect if AV is present on those assets as well. As an added bonus it will also decide whether or not the AV is up-to-date on each asset. It will report its information in a text file with each asset's name and yes or no for AV protection and yes or no for up-to-date.

I decided to go a little further as the WMI AntiVirusProduct has a lot more information than just status of the AV.

Output consists of:

ComputerName

AV Product state (hex value)

AV State (enabled/disabled)

AV Updated? (up-to-date / out-of-date)

AV Product name

GUID

AV Executable Path

AV Reporting Executable Path

Timestamp

##Files Overview:
* scan.ps1 - main script that performs the scanning

##Script Usage & Functionality Walkthrough
Execute the PowerShell Script without any arguments and the localhost machine will be scanned.

./scan.ps1

##Resources
Microsoft SecurityCenter2
http://neophob.com/2010/03/wmi-query-windows-securitycenter2/

StackOverflow
http://stackoverflow.com/questions/33649043/powershell-how-to-get-antivirus-product-details

##Future Work
Connect to other computers in the same domain with credentials to be able to extract anti-virus information from each machine.

Be able to detect my own statuses based on the hex value of the product state in the WMI.  Ran into issues and could not figure out how to properly read the hex values.  Will implement this in the next cycle.

https://social.msdn.microsoft.com/Forums/en-US/6501b87e-dda4-4838-93c3-244daa355d7c/wmisecuritycenter2-productstate?forum=vblanguage

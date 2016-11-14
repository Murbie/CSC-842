<#
.SYNOPSIS
A Powershell script to detect the presence of anti-virus software on the system it is being run.
.DESCRIPTION
This script utilizes WMI SecurityCenter\SecurityCenter(2) to retrieve AntiVirus Product information on a machine.
.PARAMETER ComputerName
Names of computers to collect data from. If nothing is listed, the script defaults to the local machine.
.EXAMPLE
./scan.ps1
Gets AntiVirus Product information from local computer
.EXAMPLE
.LINK
https://github.com/Murbie/CSC-842/tree/master/Module%204
#>
[CmdletBinding()]

param(
    [Parameter(ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true)] 
    [string[]] $ComputerName
)

process {
    #Collect anti-virus information of specified system.
    function GetVirusInfo(){

        #Creates a hashtable to hold data
        $hash = @{}

        #obtains hostname of machine
        $hostname = hostname

        #determines the os of the machine
        $os = [system.version](Get-WmiObject win32_operatingsystem -computername $hostname).version

        #all windows vista and above are NT6, all NT5 and below are XP and older
        if($os -ge [system.version]'6.0.0.0'){
            #query the system for antivirus product information
            $av = Get-WmiObject -Namespace root\SecurityCenter2 -Class AntiVirusProduct -ComputerName $hostname -ErrorAction Stop

        }
        else{
            #query the system for antivirus product information
            $av = Get-WmiObject -Namespace root\SecurityCenter -Class AntiVirusProduct -ComputerName $hostname -ErrorAction Stop

        }

        #Obtained from the following website: http://community.kaseya.com/resources/m/knowexch/1020.aspx 
        switch ($av.productState) { 
            "262144" {$defstatus = "Up to date" ;$rtstatus = "Disabled"} 
            "262160" {$defstatus = "Out of date" ;$rtstatus = "Disabled"} 
            "266240" {$defstatus = "Up to date" ;$rtstatus = "Enabled"} 
            "266256" {$defstatus = "Out of date" ;$rtstatus = "Enabled"} 
            "393216" {$defstatus = "Up to date" ;$rtstatus = "Disabled"} 
            "393232" {$defstatus = "Out of date" ;$rtstatus = "Disabled"} 
            "393488" {$defstatus = "Out of date" ;$rtstatus = "Disabled"} 
            "397312" {$defstatus = "Up to date" ;$rtstatus = "Enabled"} 
            "397328" {$defstatus = "Out of date" ;$rtstatus = "Enabled"} 
            "397568" {$defstatus = "Out of date" ;$rtstatus = "Enabled"} 
            default {$defstatus = "Unknown" ;$rtstatus = "Unknown"} 
        }

        #Adds values to hash table
        $hash.ComputerName = $hostname
        $hash.'productstate' = $av.productstate
        $hash.'AV State' = $rtstatus
        $hash.'AV Updated?' = $defstatus
        $hash.Name = $av.displayName
        $hash.'GUID' = $av.instanceguid
        $hash.'Executable' = $av.pathtosignedproductexe
        $hash.'Reporting Executable' = $av.pathtosignedreportingexe
        $hash.'Timestamp' = (Get-Date).ToShortDateString() + " " + ((Get-Date).ToShortTimeString())

        #print out hash info and output to avlog.txt
        $string = $hash | out-string
        write-host $string
        $string | Out-File C:\avlog.txt -Append -Force
    }

    
    # MAIN #
    
    #Collect antivirus information from local system.
    $result = GetVirusInfo
}

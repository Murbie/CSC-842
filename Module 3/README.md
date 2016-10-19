#Module 3 - scanner.pl
##Idea
Create a basic virus scanner that can search and determine the presence of any signature matches in a given directory from a signature file.

##Overview
This Perl script is a basic virus scanner that recursively scans files in a given directory and all of its subdirectories to find signature matches.

This scanner opens the signature file and scanned file in binary using the Find::Slurp module, which has a read\_file function for easy I/O.

http://search.cpan.org/~uri/File-Slurp-9999.19/lib/File/Slurp.pm

Next, the scanner uses the Find::Find module, which has an index function that utilizes the Boyer-Moore Algorithm to find a substring match in .

http://search.cpan.org/~rjbs/perl-5.24.0/ext/File-Find/lib/File/Find.pm

The Boyer-Moore algorithm is regarded as the most efficient string matching algorithm. https://en.wikipedia.org/wiki/Boyer–Moore\_string\_search\_algorithm

If a signature match is found, the script will output a message stating which file matched which signature.

##Files Overview:
* scanner.pl - main script that performs the scanning
* signatures - signature file used to compare against
* Testme directory - contains a virus binary with known signatures
* virus.bin - malware sample obtained from https://www.hybrid-analysis.com/sample/c5d0e8bc13cd08b25157a766889f417a8669651db8497fcd8ad85be8fdc589a4?environmentId=100

##Script Usage & Functionality Walkthrough
Execute the scanner perl script with the specified signature file and directory to scan.

./scanner.pl directory signatures

If an invalid file or directory is provided, the script will error out appropriately.

##Resources
Listed throughout the information above

Perl Documentation
http://perldoc.perl.org
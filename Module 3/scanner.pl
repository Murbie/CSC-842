#!/usr/bin/perl
# Kyle Murbach
# scanner.pl

use strict;
use File::Slurp;
use File::Find;

# Declare Variables
my $dir;
my $sig;
my $str;
my @listing;
my @sigs;
my @strs;
my $match = -1;

# Check to make sure arguments are defined
if(defined $ARGV[0] && defined $ARGV[1]){
	$dir = $ARGV[0];
	$sig = $ARGV[1];
}
else{
	print "Usage:$0 <directory path> <signature file>\n";
	exit 1;
}

# Attempts to open directory handle, errors out if fails
if(!opendir DIR, $dir){
	print "Directory does not exist!\n";
	exit 2;
}

closedir(DIR);

# Attempts to open signature file handle, errors out if fails
@sigs = read_file($ARGV[1], binmode => ':raw');

# Reads in all files and directories of given directory using the find module
# Note that the $File::Find::name pulls up the full path of the current file
# When a file is found, its directory is added to the @listing array
find(
	sub{
		-f $_ and push @listing, $File::Find::name;
		}, $dir
	);

# Opens each of the files in the @listing array in binary mode
# Compares each of the files as a binary string and prints out
# All signature matches
foreach(@listing){
	my $filename = $_;
	$str = read_file($_, binmode => ':raw');

	# converts character by character of the str variable that contains
	# file data into byte by byte array
	my @strs = (unpack "C*",$str);
	my $strbytes;

	# populates $strbytes variable with byte by byte string of entire file
	for(my $i = 0; $i < $#strs; $i++){
		$strbytes.=$strs[$i];
	}

	my $counter = 0;
	foreach(@sigs){
		$counter++;
		$sig = $_;

		# converts character by character of the sig variable that contains
		# file data into byte by byte signature array
		my @sigs = (unpack "C*",$sig);

		my $sigbytes;

		# populates $sigbytes variable with byte by byte string of signature
		for(my $i=0; $i < $#sigs; $i++){
			$sigbytes.=$sigs[$i];
		}

		# index function utilized boyer-moore algorithm to identify substring
		# returns -1 if no match is found in $strbytes when searching for $sigbytes
		my $match = index($strbytes,$sigbytes);
		
		if($match != -1){
			print "The following file: \"$filename\" matches signature #$counter in the signature file.\n";
		}
	}
}
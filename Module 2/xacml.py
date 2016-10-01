#!/usr/bin/python
__author__ = 'Murbie'

import sys, getopt, os.path, getpass, subprocess

#RC4 Encryption
def encrypt():
	r = raw_input("Do you have a file? [y/n]: ")

	while r != "y" and r != "n":
		r = raw_input("Do you have a file? [y/n]: ")

	if r == 'y':
		print("Be aware that the operations will destroy the initial file contents!")
		fname = raw_input("Please enter the filename: ")

		while(not os.path.isfile(fname)):
			fname = raw_input("File cannot be found, please enter an existing file: ")

		fhandle = open(fname, "r")
		msg = fhandle.read()
		fhandle.close()

		key = raw_input("Please enter the key: ")
		nrange = creation(key)
	else:
		msg = raw_input("Please enter your message: ")
		key = raw_input("Please enter the key: ")
		nrange = creation(key)

	generator = prng(nrange)
	ciphertext = []

	for i in msg:
		pt = ord(i)
		ct = pt ^ generator.next()
		ciphertext.append(chr(ct))

	result = ''.join(ciphertext)

	if r == 'y':
		os.remove(fname)
		fhandle = open(fname, "w")
		fhandle.write(result)
		fhandle.close()
	else:
		print 'Ciphertext:', repr(result)

	return

#RC4 Decryption
def decrypt():
	r = raw_input("Do you have a file? [y/n]: ")

	while r != "y" and r != "n":
		r = raw_input("Do you have a file? [y/n]: ")

	if r == 'y':
		print("Be aware that the operations will destroy the initial file contents!")
		fname = raw_input("Please enter the filename: ")

		while(not os.path.isfile(fname)):
			fname = raw_input("File cannot be found, please enter an existing file: ")

		fhandle = open(fname, "r")
		msg = fhandle.read()
		fhandle.close()

		key = raw_input("Please enter the key: ")
		nrange = creation(key)
	else:
		msg = raw_input("Please enter your message: ")
		msg = msg.decode('string_escape')
		key = raw_input("Please enter the key: ")
		nrange = creation(key)

	generator = prng(nrange)
	plaintext = []

	for i in msg:
		ct = ord(i)
		pt = ct ^ generator.next()
		plaintext.append(chr(pt))

	result = ''.join(plaintext)

	if r == 'y':
		os.remove(fname)
		fhandle = open(fname, "w")
		fhandle.write(result)
		fhandle.close()
	else:
		print 'Plaintext:', repr(result)

	return

#Generates a 256 number list based on key for RC4 Encryption/Decryption
def creation(cryptoKey):
	count = 0
	nrange = range(256)

	for i in range(256):
		length = len(cryptoKey)
		count = (int(ord(cryptoKey[i % length])) + nrange[i] + count) % 256
		temp = nrange[i]
		nrange[i] = nrange[count]
		nrange[count] = temp

	return nrange

#Generates values for XORing against based on nrange created during creation function for RC4 Encryption/Decryption
def prng(nrange):
	a = 0
	b = 0
	while True:
		a = (a + 1) % 256
		b = (b + nrange[a]) % 256
		temp = nrange[a]
		nrange[a] = nrange[b]
		nrange[b] = temp
		yield nrange[(nrange[a]+nrange[b]) % 256]

#Tests the username/password with XACML to ensure that the user is authenticated to run the encryption
def encTest(usr,pswd):
	action = "enc"
	filename = "request.xml"
	os.remove(filename)
	fhandle = open(filename, "w")
	var = "<?xml version='1.0' encoding='UTF-8'?><S:Envelope xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\"><S:Body><ns2:getDecision xmlns=\"http://dto.entitlement.identity.carbon.wso2.org/xsd\" xmlns:ns2=\"http://org.apache.axis2/xsd\" xmlns:ns3=\"http://entitlement.identity.carbon.wso2.org/xsd\"><ns2:request><Request xmlns=\"urn:oasis:names:tc:xacml:3.0:core:schema:wd-17\" CombinedDecision=\"false\" ReturnPolicyIdList=\"true\"><Attributes Category=\"urn:oasis:names:tc:xacml:3.0:attribute-category:action\"><Attribute AttributeId=\"urn:oasis:names:tc:xacml:1.0:action:action-id\" IncludeInResult=\"false\"><AttributeValue DataType=\"http://www.w3.org/2001/XMLSchema#string\">" + action + "</AttributeValue></Attribute></Attributes><Attributes Category=\"urn:oasis:names:tc:xacml:1.0:subject-category:access-subject\"><Attribute AttributeId=\"urn:oasis:names:tc:xacml:1.0:subject:subject-id\" IncludeInResult=\"false\"><AttributeValue DataType=\"http://www.w3.org/2001/XMLSchema#string\">" + usr + "</AttributeValue></Attribute></Attributes><Attributes Category=\"urn:oasis:names:tc:xacml:3.0:attribute-category:resource\"><Attribute AttributeId=\"urn:oasis:names:tc:xacml:1.0:resource:resource-id\" IncludeInResult=\"false\"><AttributeValue DataType=\"http://www.w3.org/2001/XMLSchema#string\">RC4</AttributeValue></Attribute></Attributes></Request></ns2:request></ns2:getDecision></S:Body></S:Envelope>"
	fhandle.write(var)
	fhandle.close()
	command = ["./request.sh", usr, pswd, filename]
	p = subprocess.call(command)
	foo = 0
	filename2 = "permit.xml"
	if 'Decision&gt;Permit&lt;/Decision&gt' in open(filename2).read():
		encrypt()
	else:
		print("YOU ARE NOT AUTHORIZED TO DO THIS!")

#Tests the username/password with XACML to ensure that the user is authenticated to run the decryption
def decTest(usr,pswd):
	action = "dec"
	filename = "request.xml"
	os.remove(filename)
	fhandle = open(filename, "w")
	var = "<?xml version='1.0' encoding='UTF-8'?><S:Envelope xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\"><S:Body><ns2:getDecision xmlns=\"http://dto.entitlement.identity.carbon.wso2.org/xsd\" xmlns:ns2=\"http://org.apache.axis2/xsd\" xmlns:ns3=\"http://entitlement.identity.carbon.wso2.org/xsd\"><ns2:request><Request xmlns=\"urn:oasis:names:tc:xacml:3.0:core:schema:wd-17\" CombinedDecision=\"false\" ReturnPolicyIdList=\"true\"><Attributes Category=\"urn:oasis:names:tc:xacml:3.0:attribute-category:action\"><Attribute AttributeId=\"urn:oasis:names:tc:xacml:1.0:action:action-id\" IncludeInResult=\"false\"><AttributeValue DataType=\"http://www.w3.org/2001/XMLSchema#string\">" + action + "</AttributeValue></Attribute></Attributes><Attributes Category=\"urn:oasis:names:tc:xacml:1.0:subject-category:access-subject\"><Attribute AttributeId=\"urn:oasis:names:tc:xacml:1.0:subject:subject-id\" IncludeInResult=\"false\"><AttributeValue DataType=\"http://www.w3.org/2001/XMLSchema#string\">" + usr + "</AttributeValue></Attribute></Attributes><Attributes Category=\"urn:oasis:names:tc:xacml:3.0:attribute-category:resource\"><Attribute AttributeId=\"urn:oasis:names:tc:xacml:1.0:resource:resource-id\" IncludeInResult=\"false\"><AttributeValue DataType=\"http://www.w3.org/2001/XMLSchema#string\">RC4</AttributeValue></Attribute></Attributes></Request></ns2:request></ns2:getDecision></S:Body></S:Envelope>"
	fhandle.write(var)
	fhandle.close()
	command = ["./request.sh", usr, pswd, filename]
	p = subprocess.call(command)
	foo = 0
	filename2 = "permit.xml"
	if 'Decision&gt;Permit&lt;/Decision&gt' in open(filename2).read():
		decrypt()
	else:
		print("YOU ARE NOT AUTHORIZED TO DO THIS!")

# MAIN
# Ensures that an -e or -d argument is given
try: 
	myopts, args = getopt.getopt(sys.argv[1:],"ed")
except getopt.GetoptError:
      print 'xacml.py -e or -d'
      sys.exit(2)

# Asks user for username and password
usr = raw_input("Hello! Please enter your username: ")
pswd = getpass.getpass('Password:')

# Invokes XACML tests
for o, a in myopts:
    if o == '-e':
        encTest(usr,pswd)
    elif o == '-d':
        decTest(usr,pswd)
    else:
        print("Incorrect usage")
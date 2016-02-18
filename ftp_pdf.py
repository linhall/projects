#####################################################
# Python: FTP/PDF Maker
# Date: 2/17/2016
# Author: Lin Hall
# Description: This program pulls .pdf files from an FTP
# site, and then merges each file into one PDF document.
# This program works based on a specific file naming
# convention.
######################################################

import ftplib
import os

# FTP Server Information
server = '10.14.65.5'
username = 'hallle'
password = 'Gucisthebest1'

# FTP Directory
directory = '/temp/scan/'
filenames = '*.pdf'

# Connect to the FTP server
ftp = ftplib.FTP(server)
ftp.login = (username, password)

# Navigate to the appropriate directory
ftp.cwd(directory)

# Set the folders to place the downloaded files
pp_folder = os.path.join(r"c:\--destination--)
fp_folder = os.path.join(r"c:\--destination--)

# Loop through each file and download to the
# designated folder

for fname in ftp.nlst(filenames):
	fhandle = open(fname, 'wb')
	print "Downloading " + fname
	ftp.retrbinary('RETR ' + fname, fhandle.write)
	fhandle.close()
	if 








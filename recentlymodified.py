import os
import datetime

def datetime_to_float(d):
    epoch = datetime.datetime.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds

def float_to_datetime(fl):
    return datetime.datetime.fromtimestamp(fl)

def get_file_time(full_path):
    try:
        mtime = os.stat(full_path).st_mtime
    except:
        return 0
    return mtime

show_files_newer = datetime_to_float(datetime.datetime(2015, 12, 2, 9, 30))

for dirname,subdirs,files in os.walk(".."):
    for fname in files:
        full_path = os.path.join(dirname, fname)
        mtime = get_file_time(full_path)
        if mtime > show_files_newer:
            print full_path + "," + str(float_to_datetime(mtime))



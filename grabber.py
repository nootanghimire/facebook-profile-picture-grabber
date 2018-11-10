#######################################################################
# grabber.py
# coded by: Nootan Ghimire <nootan.ghimire@gmail.com>
# description: Grabs Facebook Profile Pictures..
# Rather than a exploit, it is a service given by fb :D
#######################################################################

import urllib.request
from urllib.error import HTTPError, URLError
import os


# Function that downloads a file
def downloadFile(file_name, file_mode, base_url, out_path=None):
    if out_path is None:
        out_path = os.getcwd();

    # Create the url
    url = base_url + file_name + "/picture"

    # Open the url
    try:
        f = urllib.request.urlopen(url)
        print("downloading ", url)

        # Open our local file for writing
        local_file = open(os.path.join(out_path,file_name+".jpg"), "w" + file_mode)
        local_file.write(f.read())
        local_file.close()
        return 1

    # Handle errors
    except HTTPError as e:
        print("HTTP Error:", e.code, url)
        return 0
    except URLError as e:
        print("URL Error:", e.reason, url)
        return 0
# End Function


# For those of us afraid of infinite loops...
# Function that downloads N files and saves them in the directory out_path
def downloadNFiles(N, out_path=None):
    if out_path is None:
        out_path = os.getcwd();

    profile = 100000425733973
    base_url = 'https://graph.facebook.com/'
    num_worked = 0
    while (num_worked < N):
        s_index = str(profile)
        worked = downloadFile(s_index, "b", base_url, out_path)
        num_worked += worked
        profile = profile + 1


# Main pogram
if __name__=="__main__":
    profile = 100000425733973  # Start From Profile ID

    # Iterate over image range . Infinite Loop :)
    while(1 == 1):
        base_url = 'https://graph.facebook.com/'
        s_index = str(profile)
        file_name = s_index
        # Now download the image. b for binary
        downloadFile(file_name, "b", base_url)
        profile = profile + 1
    # End While Loop
    # End Program

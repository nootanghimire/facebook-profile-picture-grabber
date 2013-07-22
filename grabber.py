#######################################################################
# grabber.py
# coded by: Nootan Ghimire <nootan.ghimire@gmail.com>
# description: Grabs Facebook Profile Pictures..
# Rather than a exploit, it is a service given by fb :D
#######################################################################


#import urllib request
import urllib.request
#import urllib error handling
from urllib.error import HTTPError,URLError

#function that downloads a file
def downloadFile(file_name,file_mode,base_url):
    #create the url
    url = base_url + file_name + "/picture"
   
    # Open the url
    try:
            f = urllib.request.urlopen(url)
            print("downloading ", url)

            # Open our local file for writing
            local_file = open(file_name+".jpg", "w" + file_mode)
            #Write to our local file
            local_file.write(f.read())
            local_file.close()

    #handle errors
    except HTTPError as e:
            print("HTTP Error:",e.code , url)
    except URLError as e:
            print("URL Error:",e.reason , url)

#Function Ends !!
            
profile=100000425733973 #Start From Profile ID          

# Iterate over image range . Infinite Loop :)
while(1==1):   
    base_url ='https://graph.facebook.com/'
    s_index=str(profile)
    file_name =s_index;
    # Now download the image. b for binary
    downloadFile(file_name,"b",base_url)
    profile=profile+1
#End While Loop

# TODO : This program grabs profile pictures by
# bruteforcing the profile id's. So, if a person's
# profile id does not match, instead of returning
# nothing, facebook returns default profile picture
# So it would be good to overcome this,
# by a image manipulating library which deletes those
# default images


#################################################################
#End Program#

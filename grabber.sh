#!/bin/bash

#######################################################################
# grabber.py
# coded by: Avash Mulmi <avashmulmi@gmail.com>
# description: Grabs Facebook Profile Pictures..
# Rather than a exploit, it is a service given by fb :D
#######################################################################

profile=100000425733973 #starting profile
extension=.jpg
function download(){
    url="https://graph.facebook.com/$profile/picture"
    wget $url -O $profile$extension
    profile=$(($profile+1))
}

while true
do
	download
done


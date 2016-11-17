import urllib2
import cookielib
from getpass import getpass
import sys
import os
import traceback
from stat import *

# message = raw_input("Enter text: ")
# number = "8768668885"

def send_msg(message,number="8768668885") :  
    username = "9784830733"
    passwd = "12345"

    message = "+".join(message.split(' '))

 #logging into the sms site
    url ='http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

 #For cookies

    cj= cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

 #Adding header details
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    try:
        usock =opener.open(url, data)
    except IOError:
        print "error"
        #return()

    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
        print "success {}".format(sms_sent_page)
    except IOError:
	print traceback.format_exc()
        print "error"
        #return()
    return 0
i=7
while True :
	print "Try no. : {}".format(str(i))
	try :
		send_msg("Test")
	except :
		print (traceback.format_exc())
	i+=1   	 
    #return ()

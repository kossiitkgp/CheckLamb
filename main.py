import requests
import json
import os
import email_functions


def slack_notification(message):
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "channel": "#email",
        "text": message
    })
    r = requests.post(
        os.environ["SLACK_WEBHOOK_URL"], headers=headers, data=data)

    if r.status_code != 200:
        print("in slack_notification : {}".format(r.status_code))
        print(r.text)

mails = email_functions.reading_mail()
if mails :
    print "Sending mails"
    if len(mails) == 1 :
        header_msg = "Got one new mail"
    else :
        header_msg = "Got {} new mails".format(len(mails))
    slack_notification(header_msg)
    message = ""
    for index, mail in enumerate(mails):
        message = " ```{}. \nFrom : {}\n*Subject* : {}\n*Body* :{}.```\n\n".format(index+1 ,
                                                mail["sender"],
                                                mail["subject"],
                                                mail["body"])
        slack_notification(message)
else :
    print "No new mail"

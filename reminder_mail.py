import sys
import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# process the schedule file
with open('C:/Users/kk/Desktop/email/schedule.txt', 'r') as f:
    read_file=f.readlines()
    file_content=[a.strip().split(' ') for a in read_file] # convert file in list of list
    for i in file_content:
        i.remove('-')
    dates = [' '.join(i[0:3]) for i in file_content] # geting the list of schedule dates
    time = [' '.join(i[3:5]) for i in file_content] # geting the list of schedule times
    class_module = [' '.join(i[5:]) for i in file_content] # geting the list of schedule class module
    lst_of_values= [] # combining time and class module in one list 
    for i in range(len(time)):
        lst=[]
        lst.append(time[i])
        lst.append(class_module[i])
        lst_of_values.append(lst)
    dict_file_content = dict(zip(dates,lst_of_values)) # creating dictionary in which dates act as key and lst of values act as a values
    schedule_date = list(dict_file_content.keys())
    format="%Y %d %B"
    today=datetime.date.today() # checking the weekday of today 
    if today.strftime("%a") in ['Mon','Tue','Wed','Thu']:
        a=f'This is a reminder mail for your class on {dict_file_content[(today+datetime.timedelta(days=1)).strftime(format)][1]} at {(today+datetime.timedelta(days=1)).strftime(format)} {dict_file_content[(today+datetime.timedelta(days=1)).strftime(format)][0]}. Please join the class on time.'
    elif today.strftime("%a") == 'Fri':
        a=f'This is a reminder mail for your class on {dict_file_content[(today+datetime.timedelta(days=3)).strftime(format)][1]} at {(today+datetime.timedelta(days=3)).strftime(format)} {dict_file_content[(today+datetime.timedelta(days=3)).strftime(format)][0]}. Please join the class on time.'

    mail_content = a
    #The mail addresses and password
    sender_address = sys.argv[1] # provided as a system arguments
    sender_pass = sys.argv[2] # provided as a system arguments
    receiver_address = ['rehan@onelearn.io', 'nakkapraneeth23899@gmail.com']
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = ','.join(receiver_address)
    message['Subject'] = 'OneLearn course series reminder'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
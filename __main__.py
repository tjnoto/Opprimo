__author__ = 'n3tn0'
__base__='n3tn0/Opprimo:master'
__baseversion__ = '1.0.2'
__version__='ALPHA'

import smtplib
import sys
import csv
import os

#os.chdir('modules/'+sys.argv[0])
os.chdir(sys.argv[0][:-7])

#Read list of carriers and format a dictionary object to choose email suffix from
with open('carrierdb.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('carrierdb_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        carriers = {rows[0]: rows[1] for rows in reader}

#Make the list of carriers uppercase to avoid conflict with user input
carriers_upper = {}
upper=''
for i in carriers:
    #upper = i.upper()
    carriers_upper[i.upper()] = carriers[i]

#Determine and format the final target address
if sys.argv[2].upper() == 'EMAIL':
    target = sys.argv[1]
else:
    target = sys.argv[1] + '@' + carriers_upper[sys.argv[2].upper()]


amount = sys.argv[3]

#READ FROM TEXT FILE IN FUTURE
user = 'n3tn0.chariot@gmail.com'
password = 'chariottest'
smtpserver = 'smtp.gmail.com:587'

#Get the message to be sent
body = sys.argv[4]

#Prepare message for sending
#header = 'From: %s\n' % 'joe@joe.com'
#header += 'To: %s\n' % ','.join(target_addr)
#message = header + body

#Login to the email server
try:
    server = smtplib.SMTP(smtpserver)
    server.starttls()
except:
    exit()

#Send the message
for i in range(int(amount)+1):
    server.sendmail(user, target, body)

#Write return message
response = open('../../response.txt', 'w')
response.write('Command Complete')

#Cleanup
response.close()
server.quit()
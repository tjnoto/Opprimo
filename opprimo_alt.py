__author__ = 'n3tn0'
__base__='n3tn0/Opprimo:master'
__baseversion__ = '1.0.2'
__version__='BETA'

import smtplib
import sys
import csv
from telapi.telapi import rest

#Read list of carriers and format a dictionary object to choose email suffix from
with open('carrierdb.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('carrierdb_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        carriers = {rows[0]: rows[1] for rows in reader}


#Look up the cellphone number and determine the carrier
account_sid = 'AC4c88908413a68ace1b9b4f05b5576cc0'
auth_token  = '5e3d1e4be9a44f53bf8f2cdffdcac794'
client      = rest.Client(account_sid, auth_token)
account     = client.accounts[client.account_sid]

carrier_details  = account.carrier.create(phone_number = '860-966-7264')
print carrier_details
print "Carrier Lookup Sid: %s" % carrier_details.sid


#Determine and format the final target address
#if sys.argv[].upper() == 'EMAIL':
#    target = sys.argv[1]
#else:
#target = sys.argv[1] + '@' + carriers[CARRIER]

"""
amount = sys.argv[2]

#READ FROM TEXT FILE IN FUTURE
user = 'crush@chariot.ml'
password = 'opprimo'
smtpserver = 'chariot.ml:25'

#Get the message to be sent
body = sys.argv[3]

#Prepare message for sending
#header = 'From: %s\n' % user
#header += 'To: %s\n' % ','.join(target_addr)
#message = header + body
server = smtplib.SMTP(smtpserver)
server.starttls()

#Login to the email server
try:
    server.login(user, password)
except smtplib.SMTPAuthenticationError:
    exit()

#Send the message
for i in range(amount):
    server.sendmail(user, target, body)

#Cleanup
server.quit()
"""
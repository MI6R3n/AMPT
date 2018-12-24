 # Import Modules
import smtplib
import getpass
import subprocess
import string
import socket, httplib
import subprocess
import sys,os
import thread
import time
#import requests
import urllib2
import hashlib 
import base64
from datetime import datetime
from random import *

# Start Codeing

os.system('clear')

def baner():
     print('''
        XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
        XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
        XX   MMMMMy''                                                    ''yMMMMM   XX
        XX   MMMy'                                                          'yMMM   XX
        XX   Mh'                                                              'hM   XX
        XX   -                                                                  -   XX
        XX                                                                          XX
        XX   ::                                                                ::   XX
        XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
        XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
        XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
        XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
        XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
        XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
        XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
        XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
        XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
        XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
        XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
        XX                                oo      oo                                XX
        XX           oM                 oo          oo                 Mo           XX
        XX         oMMo                M              M                oMMo         XX
        XX       +MMMM                 s              s                 MMMM+       XX
        XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
        XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
        XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
        XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
        XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
        XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
        XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
        XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
        XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
        XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
        XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
        XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
        XX   MMMMMMMM-                                                  -MMMMMMMM   XX
        XX   MMMMMMMM                                                    MMMMMMMM   XX
        xx   MMMMMMMMM            #########################             MMMMMMMMM   XX
        XX   MMMMMMMMMy           |Amir Mehrab  Pack Tools|            yMMMMMMMMM   XX
        XX   MMMMMMMMMMy.         #########################          .yMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
        ''')
baner()
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 100)
try : 
    print ""
    slowprint("\n\t\t        [!] Starting Script Please Wite My Ferind [!] ")
    print ''
    time.sleep(2)
    slowprint("\n\t\t           [!] OK Everything is Ready Lest Start [!] ")
    time.sleep(1)
    os.system('clear')

except KeyboardInterrupt :
    print "[!] Oh !! Your Are Presed ctrl + c [!]"
    exit()
#
def menu():
    print ("""

    #     # ####### #        #####  ####### #     # ####### 
    #  #  # #       #       #     # #     # ##   ## #       
    #  #  # #       #       #       #     # # # # # #       
    #  #  # #####   #       #       #     # #  #  # #####   
    #  #  # #       #       #       #     # #     # #       
    #  #  # #       #       #     # #     # #     # #       
    ## ##  ####### #######  #####  ####### #     # ####### 

    MENU :

    1)  Sender Mail
    2)  Genereting Password 
    3)  port Sacaner
    4)  Char Hasher(MD5)
    5)  IP Fuonder
    6)  Banner Grabbing
    7)  Whois 
    8)  Revrse IP Lookup
    9)  DNS Lookup
    10) Hash Encoder(MD5)
    11) SMS Sender
    """)
menu()
def ext():

    ex = raw_input ('\nContinue/Exit->-> ')
    if ex[0] == 'e' :
           print 'Good-bye!!!'
           exit() 
    elif ex[0] == '':
		print 'Good Bye !!'
		exit()
    else:
           os.system('clear')
           baner
           menu()
           scrpt()
def scrpt():
    try:
        def Sender_Mail():
            subprocess.call("clear")

            print('''
                 ____                 _ _   ____                 _           
                / ___|_ __ ___   __ _(_) | / ___|  ___ _ __   __| | ___ _ __ 
               | |  _| '_ ` _ \ / _` | | | \___ \ / _ \ '_ \ / _` |/ _ \ '__|
               | |_| | | | | | | (_| | | |  ___) |  __/ | | | (_| |  __/ |   
                \____|_| |_| |_|\__,_|_|_| |____/ \___|_| |_|\__,_|\___|_|   
             
	     	To use this feature, you must activate the Google Account Limit to this section
		https://myaccount.google.com/data-and-personalization
		And tick the "Web & App Activity" option
	     
            ''')



            try:
                
                sender = raw_input("Enter Your Mail >> ")  

                toaddrs = raw_input("\nEnter Target Mail >> ") 

                message = raw_input("""\nEnter Your Massege : >> 

                """)  

                username = raw_input("\nEnter Your Username(Gmail) >> ")

                password = getpass.getpass("\nEnter Your Password >> ") 
            
                server = smtplib.SMTP("smtp.gmail.com:587") 
                server.starttls() 
                server.login( username , password ) 
                server.sendmail(sender, toaddrs, message) 
                server.quit() 
                print "\n+-+-+-+-+-+-+-+-+-+-+-+"
                print "|S|u|c|c|e|s|s|F|u|l|y|"
                print "+-+-+-+-+-+-+-+-+-+-+-+"
            except socket.error:
                print ''
                
                slowprint("\n\t     [!] Connection Error Please chek Your Connection And Rerun Again [!] \n")
                
                exit()
            except KeyboardInterrupt:
                slowprint("\n\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
                exit()
                print "\n+-+-+-+-+-+-+-+-+-+-+-+"
                print "|S|u|c|c|e|s|s|F|u|l|y|"
                print "+-+-+-+-+-+-+-+-+-+-+-+"
            

                
        def Password_Maker():
            subprocess.call("clear")
            print('''

                         _____         _____ _____                    _             
                        |  __ \ /\    / ____/ ____|                  | |            
                        | |__) /  \   | (___| (___   _ __ ___   __ _ | | _____ _ __ 
                        |  ___/ /\ \   \___ \\___ \ | '_ ` _ \ / _` | |/ / _ \ '__|
                        | |  / ____ \ ____) |___) | | | | | | | (_| |   <  __/ |   
                        |_| /_/    \_\_____/_____/  |_| |_| |_|\__,_|_|\_\___|_|   
                                                                
            ''')

            try:
                select = raw_input("\n\nSelect a char for Join In Password : >> ")

                cahr = string.ascii_letters + string.punctuation + string.digits 

                tarkib =  select + cahr

                password = "".join(choice(tarkib)for x in range(randint(10,20)))

                    
                eneder = (password)

                print("\nThis Is Your Password :>> {}\n" .format(eneder))

                    
                    
                file = open("Password.txt","w+")
                file.write(eneder)
                file.close()
                print "\n+-+-+-+-+-+-+-+-+-+-+-+"
                print "|S|u|c|c|e|s|s|F|u|l|y|"
                print "+-+-+-+-+-+-+-+-+-+-+-+"
            except KeyboardInterrupt:
                slowprint("\n\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
                exit()
                print "\n+-+-+-+-+-+-+-+-+-+-+-+"
                print "|S|u|c|c|e|s|s|F|u|l|y|"
                print "+-+-+-+-+-+-+-+-+-+-+-+"
            
        def port_scaner():
            subprocess.call("clear")
            print('''
            
            _____           _      _____                           
            |  __ \         | |    / ____|                          
            | |__) |__  _ __| |_  | (___   ___ __ _ _ __   ___ _ __ 
            |  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \ / _ \ '__|
            | |  | (_) | |  | |_   ____) | (_| (_| | | | |  __/ |   
            |_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|\___|_|   
                                                                
            ''')

            try:
                dz = raw_input('Enter IP Address >> ')
                port = "http://api.hackertarget.com/nmap/?q=" + dz
                scan = urllib2.urlopen(port).read()
                print (scan)
                

                print "\n+-+-+-+-+-+-+-+-+-+-+-+"
                print "|S|u|c|c|e|s|s|F|u|l|y|"
                print "+-+-+-+-+-+-+-+-+-+-+-+"

            except KeyboardInterrupt:
                slowprint("\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
            
        def sms_sender():
            subprocess.call("clear")
            print('''
            
             _____ __  __  _____    _____                _           
            / ____|  \/  |/ ____|  / ____|              | |          
           | (___ | \  / | (___   | (___   ___ _ __   __| | ___ _ __ 
            \___ \| |\/| |\___ \   \___ \ / _ \ '_ \ / _` |/ _ \ '__|
            ____) | |  | |____) |  ____) |  __/ | | | (_| |  __/ |   
           |_____/|_|  |_|_____/  |_____/ \___|_| |_|\__,_|\___|_|   
                                                                
            ''')
            try:
                print """
                Very important point:

                To use this option, you must register on the site and enter the API in the script
                site >> https://panel.kavenegar.com/Client/Membership/Register
                """
                api = raw_input("Enter Kaveh Negar API >> ")
                ersal = {"receptor": raw_input("Enter Target Number(+98100000) ==> ") , "message": raw_input("Enter Message > ")}
                avab = requests.post(api,data=ersal)
                print(avab)
            except requests.ConnectionError:
                
                slowprint("\n\t     [!] Connection Error Please chek Your Connection And Rerun Again [!] \n")
                
            except KeyboardInterrupt:
                slowprint("\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
            
        def hasher():
            subprocess.call("clear")
            print '''
            
             \  | __ \  ___|   |   |          |               
            |\/ | |   | __ \   |   |  _` |  __| __ \   _ \  __| 
            |   | |   |   ) |  ___ | (   |\__ \ | | |  __/ |    
           _|  _|____/ ____/  _|  _|\__,_|____/_| |_|\___|_|    
            '''
            try:
                iput = raw_input("Enter Your Charcter ==> ")

                md5 = hashlib.md5()

                md5.update(iput)

                print ('This Is Your Hash >> {}') .format(md5.hexdigest()) 
                
                print "\n+-+-+-+-+-+-+-+-+-+-+-+"
                print "|S|u|c|c|e|s|s|F|u|l|y|"
                print "+-+-+-+-+-+-+-+-+-+-+-+"
            except KeyboardInterrupt:
                slowprint("\n\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
            
        def ip_fuonder():
            
            subprocess.call('clear')

            print '''

        |_   _|  __ \  |  ____|                   | |          
          | | | |__) | | |__ _   _  ___  _ __   __| | ___ _ __ 
          | | |  ___/  |  __| | | |/ _ \| '_ \ / _` |/ _ \ '__|
          | |_| |      | |  | |_| | (_) | | | | (_| |  __/ |   
        |_____|_|      |_|   \__,_|\___/|_| |_|\__,_|\___|_|    '''

            try:
                RemoteServer = raw_input("\nEnter Target Domin >> ")

                RemoteServerIP = socket.gethostbyname(RemoteServer)

                print('This is Your Target IP >> {}') .format(RemoteServerIP)
            except socket.error:
                print ''
                
                slowprint("\n\t     [!] Connection Error Please chek Your Connection And Rerun Again [!] \n")
                
            except KeyboardInterrupt:
                slowprint("\n\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
            
        def Banner_Grabbing():

            subprocess.call('clear')

            print'''
            
            ____                              
            |  _ \                             
            | |_) | __ _ _ __  _ __   ___ _ __ 
            |  _ < / _` | '_ \| '_ \ / _ \ '__|
            | |_) | (_| | | | | | | |  __/ |   
            |____/ \__,_|_| |_|_| |_|\___|_| 
                                          _____           _     _     _             
                                         / ____|         | |   | |   (_)            
                                        | |  __ _ __ __ _| |__ | |__  _ _ __   __ _ 
                                        | | |_ | '__/ _` | '_ \| '_ \| | '_ \ / _` |
                                        | |__| | | | (_| | |_) | |_) | | | | | (_| |
                                         \_____|_|  \__,_|_.__/|_.__/|_|_| |_|\__, |
                                                                               __/ |
                                                                              |___/ 

                
            '''
            try:

                print ('\nPlease Enter This [http://target.com]')

                url = raw_input("\nEnter Target >> ")

                server = urllib2.urlopen(url)

                for key, value in server.headers.items():

                    print key+':'+value
            
            except urllib2.URLError:
                print ''
                
                slowprint("\n\n\t     [!] Connection Error Please chek Your Connection And Rerun Again [!] \n")
                
            except ValueError:
                print ''
                
                slowprint("\n\t     [!] Please Enter This [http://target.com] Now run Again [!] \n")
                
            except KeyboardInterrupt:
                slowprint("\n\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
            
        def whois():
            os.system('clear')
            print'''
                __          ___    _  ____ _____  _____ 
                \ \        / / |  | |/ __ \_   _|/ ____|
                 \ \  /\  / /| |__| | |  | || | | (___  
                  \ \/  \/ / |  __  | |  | || |  \___ \ 
                   \  /\  /  | |  | | |__| || |_ ____) |
                    \/  \/   |_|  |_|\____/_____|_____/ 
                                                    
            
            '''  
            try:
                iurl = raw_input('\nEnter IP Address >> ')
                whois = "http://api.hackertarget.com/whois/?q=" + iurl
                e = urllib2.urlopen(whois).read()
                print (e)
                
            except KeyboardInterrupt:
                slowprint("\n\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
            
        def ip_lookup():
            os.system('clear')
            print '''
            
             _____ _____    _                 _                
            |_   _|  __ \  | |               | |               
              | | | |__) | | |     ___   ___ | | ___   _ _ __  
              | | |  ___/  | |    / _ \ / _ \| |/ / | | | '_ \ 
             _| |_| |      | |___| (_) | (_) |   <| |_| | |_) |
            |_____|_|      |______\___/ \___/|_|\_\\__,_| .__/ 
                                                        | |    
                                                        |_|    
            '''
            try:
                url = raw_input('\nEnter IP Address >> ')
                revrse = "http://api.hackertarget.com/reverseiplookup/?q=" + url
                lookup = urllib2.urlopen(revrse).read()
                print (lookup)
                
            except KeyboardInterrupt:
                slowprint("\n\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
            
        def dns_lookup():
            os.system('clear')
            print '''
             _____  _   _  _____   _                 _                
            |  __ \| \ | |/ ____| | |               | |               
            | |  | |  \| | (___   | |     ___   ___ | | ___   _ _ __  
            | |  | | . ` |\___ \  | |    / _ \ / _ \| |/ / | | | '_ \ 
            | |__| | |\  |____) | | |___| (_) | (_) |   <| |_| | |_) |
            |_____/|_| \_|_____/  |______\___/ \___/|_|\_\\__,_| .__/ 
                                                               | |    
            '''
            try:
                url = raw_input('\nEntre Your Domain >> ')
                dns = "http://api.hackertarget.com/dnslookup/?q=" + url
                end = urllib2.urlopen(dns).read()
                print (end)
                

            
            except KeyboardInterrupt:
                    slowprint("\n\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
                    ext()
            
        def encoder():
            os.system("clear")
            print"""
            _   _    _    ____  _   _   _____ _   _  ____ ___  ____  _____ ____  
            | | | |  / \  / ___|| | | | | ____| \ | |/ ___/ _ \|  _ \| ____|  _ \ 
            | |_| | / _ \ \___ \| |_| | |  _| |  \| | |  | | | | | | |  _| | |_) |
            |  _  |/ ___ \ ___) |  _  | | |___| |\  | |__| |_| | |_| | |___|  _ < 
            |_| |_/_/   \_\____/|_| |_| |_____|_| \_|\____\___/|____/|_____|_| \_\
                                                                        
            """
            hsh = raw_input("Enter Your Hash >> ")
            print "\nEncode Is >> ", base64.b64encode(hsh),"\n"
        






        aske = raw_input("\nPlease Enter a Number ==> ")


        if aske == '1' :
            Sender_Mail()
            ext()
            
        elif aske == '2':
            Password_Maker()
            ext()
        elif aske == '3':
            port_scaner()
            ext()
        elif aske == '4':
            hasher()
            ext()
        elif aske == '5':
            ip_fuonder()
            ext()
        elif aske == '6':
            Banner_Grabbing()
            ext()
        elif aske == '7':
            whois()
            ext()
        elif aske == '8':
            ip_lookup()
            ext()
        elif aske == "9":
            dns_lookup()
            ext()
        elif aske == "10":
            encoder()      
            ext()
        elif aske == "11":
            sms_sender()
            ext()
        else:
            os.system('clear')
            
            slowprint("\n\t        [!] Error your Number is Not Match Please Rerun Script  [!] \n")
            
        
            
    except KeyboardInterrupt:
        slowprint("\n\n\t     [!] Oh !! Your Are Presed ctrl + c [!] \n")
        ext()

scrpt()

# End Codeing

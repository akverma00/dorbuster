#This is a directory busting  tool which mainly takes two arguments i.e. url of the target and the wordlist.
#This can be also used for finding files of any any type present in that directory by passing additional parameters.
#More details are available on github.com/ashigup/corobuster

import requests
import sys
#here prCyan,prYellow and prGreen are the functions defined for the printing the text in cyan , yellow and green colour respectively.
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
banner_me='''
             ############   ###############   ##############   
             ############   ###############   ##############   
             ###      ###   ###		###   ###        ###   
             ###       ###  ###		###   ##############   
             ###      	### ###		###   ##############   
	     ###       ###  ###		###   ###   ###        
             ###      ###   ###         ###   ###     ###      
             ############   ###############   ###      ###     
             ############   ###############   ###       ###    '''
aut='''  Arun Kumar Verma (github.com/akverma00)    '''
sep="***************************************************************************************************************************************************"
print("\n\n")
prYellow(sep)
print("\n\n\n\n")
prCyan(banner_me)
print("\n\n\n\n")
prGreen(aut)
prYellow(sep)

wordlist=str(sys.argv[2])
base_url=str(sys.argv[1])
length=len(sys.argv)
#ext=str(sys.argv[3])
#print (ext)
#print (url)
#print (c)

print("")
print("")

stinfo="Starting directory on " + base_url+"   using the wordlist  "+wordlist +" .\n This will show only successful attempts .\n\n"
prYellow(stinfo)
prYellow(sep)
f=open(wordlist,"r")  #opening the wordlist file using given path
for word in f:
  new_url=""
  new_url=base_url+word
  new_url=new_url[:-1]
  #print(s)
  r=requests.get(new_url)
  if r.status_code == 200: #checking whether the requested url is 200 or not
   print (new_url)
   r.close
  for i in range(3,length):
    ext_url=new_url+"."+str(sys.argv[i])
    #print(ext_url)
    r=requests.get(ext_url)   #checking for the file types
    if r.status_code == 200:
      print (ext_url)
      r.close
f.close()


prGreen("\nDirectory Busting is completed")
prYellow(sep)


from selenium import webdriver
import os


print("Welcome , I am your virtual assistant !  \n I can run the following programs for you : \n Run chrome. \n Run vlc. \n Play music \n Run windows media player. \n Run notepad . \n Open gmail  \n Open youtube \n Open Calculator \n Open facebook \n If you wish to quit press'q' .")

while True:
	
	print("chat with me with your requirements : " , end=' ' )

	p = input()

	if(("run" in p) or ("open" in p))  and ("chrome" in p):
	  os.system("chrome")
	
	elif (("dont run" in p) or ("dont open" in p)):
	  print("Only type the program you want to open :")


	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")

	elif(("run" in p) or ("open" in p)) and ('youtube' in p) :
	  driver = webdriver.Chrome()
	  driver.get('https://youtube.com')

	elif(("run" in p) or ("open" in p) or ("send" in p)) and (('gmail' in p) or ('mail' in p )) :
	  driver = webdriver.Chrome()
	  driver.get('https://gmail.com')

	elif(("run" in p) or ("open" in p) ) and (("facebook"in p) or ("fb" in p )) :
	  driver = webdriver.Chrome()
	  driver.get('https://facebook.com')

	elif ("run" in p)  and ("player" in p) and ("media" in p):
	  os.system("wmplayer")
    	
	elif  (("run" in p)or("open" in p)) and("vlc" in p):
    	  os.system("start VLC")
	
	elif  (("run" in p)or("open" in p)) and("calculator" in p):
    	  os.system("calc")
	
	elif  (("play" in p)or("open" in p)) and (("music" in p) or ("song" in p )):
    	  os.system("spotify")
	
	elif  (("exit" in p)  or ("quit" in p) or ("q" in p)):
	  break

	else:
	  print("Sorry!,This command is not supported ") 


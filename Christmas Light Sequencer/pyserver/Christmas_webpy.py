#!/usr/local/bin/python
#import modules
import web
from web import form
import RPi.GPIO as GPIO
import os

#Set board
GPIO.setmode(GPIO.BCM)
#Initialize the pins that have to be controlled
GPIO.setup(26,GPIO.OUT)
GPIO.output(26,False)
GPIO.setup(19,GPIO.OUT)
GPIO.output(19,False)
#used for controlling the appliance
global state
state = False
global state1
state1 = False

#defining the structure
urls = ('/', 'index')
render = web.template.render('templates/')


#buttons used on the webpage
appliances_form = form.Form(
    form.Button("appbtn", value="tree", class_="btntree"),
    form.Button("appbtn", value="Santa", class_="btnSanta"),
    form.Button("appbtn", value="audio", class_="btnaudio")
    )

class index:
        
	def GET(self):
                form = appliances_form()
		return render.index(form,"Raspberry Pi Christmas lights controller")
        def POST(self):
                userData = web.input()

                if userData.appbtn == "tree":
                        global state
			state = not state
			print "tree"
                elif userData.appbtn == "Santa":
                        global state1
			state1 = not state1
                elif userData.appbtn == "audio":
                        os.system("omxplayer -o local song.mp3")
            
                GPIO.output(19,state1)
                GPIO.output(26,state)
                raise web.seeother('/')
if __name__ == '__main__':
        app = web.application(urls,globals())
        app.run()

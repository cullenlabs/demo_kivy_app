#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
#  
#  Copyright 2022 Unknown <cullenlabs@cullenlaabs>

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


# Replace this with your
# current version
#kivy.require('1.11.1')

# Defining a class
class SayHelloApp(App):
	
	# Function that returns
	# the root widget
    
    def build(self):
        self.root = GridLayout()
        self.root.cols = 1
        self.root.size_hint = (0.9, 0.9)
        self.root.pos_hint = {"center_y": 0.5, "center_x": 0.5}
        
        self.root.add_widget(Image(source = "./doctor_strange.png"))
        
        self.greet = Label(text = "Say a spell",
                     font_size = 18,
                    )
                    
        self.root.add_widget(self.greet)
        
        self.entry = TextInput(multiline = False,
                     padding_y = (20, 20),
                     padding_x = (20, 20),
                     size_hint = (0.5, 0.5),
                     font_size = 26
        
        )
        self.root.add_widget(self.entry)
        
        self.say = Button(text = "SAY IT",
                   size_hint = (0.5, 0.5),
                   width = 300,
                   bold = True,
                   background_color = (0, 1, 0, 0.7),
                   background_normal = ""
        )
        self.say.bind(on_press = self.callback)
        self.root.add_widget(self.say)
        
        return self.root
        
        
    def callback(self, instance):
        self.greet.text = "Said: " + self.entry.text
    
    


# Here our class is initialized
# and its run() method is called.
# This initializes and starts
# our Kivy application.
SayHelloApp().run()			


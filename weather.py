#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python program to find current
# weather details of any city
# using openweathermap api

__author__ = "@Kessaras XDA Dev"
__copyright__ = "Copyright (C) 2020 Paul Theodorou"
__license__ = "Public Domain"
__version__ = "3.6"

# import required modules
import requests, json, gi, sys, io

# Enter your API key here
api_key = "e6dbd70742cb26ba58083c87ba5b4c62"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class EntryWindow(Gtk.Window):

    def __init__(self):
        # Create the Gtk.Window
        Gtk.Window.__init__(self, title="Ο καιρός σήμερα ")
        self.set_size_request(300, 200)

        self.timeout_id = None

        # create a Gtk.Dialog
        dialog = Gtk.Dialog()
        dialog.set_title("Ο καιρός σήμερα ")
        dialog.set_size_request(250, 30)
        # Furthermore, the dialog is on top of the parent window
        dialog.set_attached_to(self)
        dialog.set_transient_for(self)

        # create a Gtk input box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # We add the question , hint, for user to know what to type in the box
        question = Gtk.Button()
        question.set_label("Εισάγετε πόλη: ")
        # Make the question visible
        vbox.pack_start(question, False, True, 0)

        # Here we create the box where we answer to the question above
        self.entry = Gtk.Entry()
        # The widget input command
        self.entry.get_text()
        # When we press "enter" it takes us to the results
        self.entry.connect("activate", self.on_click_me_clicked)
        # Make box visible
        vbox.pack_start(self.entry, False, False, 0)

        # Here we create a button which we can click and take us to the results
        button = Gtk.Button.new_with_label("Go")
        button.connect("clicked", self.on_click_me_clicked)
        # Make button visible
        vbox.pack_start(button, False, True, 0)

        self.label = Gtk.Label()
        self.label.get_text()
        vbox.pack_start(self.label, True, True, 0)

    # after pressing "Go", grab text from entry and run num_check() with it, then set label with the result
    def on_click_me_clicked(self, button):
        city_name = self.entry.get_text()
        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + api_key + "&units=metric" + "&lang=el" + "&q=" + city_name
        # get method of requests module
        # return response object
        response = requests.get(complete_url)
        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()
        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        self.label.set_text(city_name)
        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidiy = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]
            # print following values

            label = Gtk.Label()
            self.label.set_text(" Θερμοκρασία (σε βαθμούς κελσίου) = " +
                        str(current_temperature) +
                "\n ατμοσφαιρική πίεση (σε εκτοπασκάλ) = " +
                        str(current_pressure) +
                "\n υγρασία (σε ποσοστό) = " +
                        str(current_humidiy) +
                "\n περιγραφή = " +
                        str(weather_description))
        else:
            label = Gtk.Label()
            self.label.set_text(" Η πόλη δε βρέθηκε ")

win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

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
import requests, json, sys, io
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

class MyWindow(QMainWindow):

    def __init__(self):
        # Create the QMainWindow and the label. Change the window title as you please
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 250, 250)
        self.setWindowTitle("Ο καιρός σήμερα")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Εισάγετε πόλη: ")
        self.label.move(10, 0)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 25)
        self.textbox.resize(210,30)

        # Here we create a button which we can click and take us to the results
        self.button = QtWidgets.QPushButton(self)
        self.button.move(70, 70)
        self.button.setText("OK")
        self.button.clicked.connect(self.on_click_me_clicked)

    	# This is the output print area
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("")
        self.label2.move(100, 100)

        # This is the output print area
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("")
        self.label3.move(10, 140)

    # after pressing "Go", grab text from entry and run num_check() with it, then set label with the result
    def on_click_me_clicked(self, button):
        # Enter your API key here
        api_key = "e6dbd70742cb26ba58083c87ba5b4c62"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        city_name = self.textbox.text()
        # complete_url variable to store
        # complete url address.
    	# Change &lang=el to your language to get the weather results to your language
    	# Delete &units=metric if you do not want to use the metric system
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
        self.label2.setText(city_name)
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

            self.label3.setText(" Θερμοκρασία (σε βαθμούς κελσίου) = " +
                        str(current_temperature) +
                "\n ατμοσφαιρική πίεση (σε εκτοπασκάλ) = " +
                        str(current_pressure) +
                "\n υγρασία (σε ποσοστό) = " +
                        str(current_humidiy) +
                "\n περιγραφή = " +
                        str(weather_description))
            self.label3.adjustSize()
        else:
            self.label3.setText(" Η πόλη δε βρέθηκε ")
            self.label3.adjustSize()

app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
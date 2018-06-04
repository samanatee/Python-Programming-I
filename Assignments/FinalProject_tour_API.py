'''
Created on May 24, 2018

@author: Samantha Hangsan
'''

from tkinter import Tk, Label, Frame, messagebox, Button, RAISED, Entry, END, BOTH, X, BOTTOM
import urllib.request
import json


class Tour:
# instantiated with two US cities
# used to fetch information from the web.

    def __init__ (self, city_1, city_2):
        self.origin_city = city_1
        self.destination_city = city_2

    def distance(self, mode):
        self.mode_of_travel = mode

        # request object
        user_agent = 'Mozilla/5.0'
        headers = {'User-Agent': user_agent}

        parameters = {'origins' : self.origin_city, 'destinations' : self.destination_city, 'mode' : self.mode_of_travel, 'sensor' : False}

        url = 'http://maps.googleapis.com/maps/api/distancematrix/json?'
        data = urllib.parse.urlencode(parameters)

        url = url + data
        request = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(request)
        json_data = response.read().decode()

        try:
            read_json = json.loads(json_data)
            distance = read_json['rows'][0]['elements'][0]['distance']['value']
        except KeyError:
            raise ValueError

        return(distance)

class TourGui(Frame):
    def __init__(self):

        super().__init__()
        self.interface()

    def interface(self):

        self.master.title('Tour')
        self.pack(fill = BOTH, expand = True)

        frame_1 = Frame(self)
        frame_1.pack(fill = None, expand = False, pady = 5)

        frame_2 = Frame(self, borderwidth = 5)
        frame_2.pack(pady = 45)

        self.origin_label = Label(frame_1, font = ('Helvetica', 16), text = 'Origin')
        self.origin_label.pack(padx = 5, pady = 5)

        self.origin_entry = Entry(frame_1, borderwidth = 5, width = 25, font = ('Helvetica', 12))
        self.origin_entry.pack(fill = X, padx = 5)

        self.destination_label = Label(frame_1, font = ('Helvetica', 16), text = 'Destination')
        self.destination_label.pack(padx = 5, pady = 5)

        self.destination_entry = Entry(frame_1, borderwidth = 5, width = 25, font = ('Helvetica', 12))
        self.destination_entry.pack(fill = X, padx = 5)

        self.mode_label = Label(frame_1, font = ('Helvetica', 16), text = 'Mode')
        self.mode_label.pack(padx = 5, pady = 5)

        self.mode_entry = Entry(frame_1, borderwidth = 5, width = 25, font = ('Helvetica', 12))
        self.mode_entry.pack(fill = X, padx = 5)

        self.distance_label = Label(frame_2, font = ('Helvetica', 16), text = 'Distance (m)')
        self.distance_label.pack(padx = 5, pady = 5)

        self.distance_entry = Entry(frame_2, borderwidth = 5, width = 25, font = ('Helvetica', 12))
        self.distance_entry.pack(fill = X, padx = 5)

        self.distance_button = Button(frame_2, text = "Get Distance", font = ('Helvetica', 12), relief = RAISED, borderwidth = 5, command = self.click_command)
        self.distance_button.pack(side = BOTTOM, padx=5, pady=5)

    def click_command(self):

        self.distance = "N/A"

        # clear previous distance result
        self.distance_entry.delete(0, END)

        self.origin = self.origin_entry.get()
        self.destination = self.destination_entry.get()
        self.mode = self.mode_entry.get()

        if self.mode == '':
            self.mode = 'driving'

        mode_error = False

        if (self.mode.lower() != 'driving' and self.mode.lower() !='biking' and self.mode.lower().lower() != 'walking'):
            mode_error = True
            messagebox.showinfo('Error', 'Invalid mode. Valid modes are \'driving\', \'biking\', and \'walking\'.')

        try:
            distance = Tour(self.origin, self.destination).distance(self.mode)

            if not mode_error:
                self.distance = distance


        except ValueError:
            messagebox.showinfo('Error', 'Distance between ' + self.origin + ' and ' + self.destination +' not found.')

        self.distance_entry.insert(END, self.distance)


def main():

    # url, query = search_on_google()
    root = Tk()
    TourGui()
    root.mainloop()

if __name__ == '__main__':
    main()

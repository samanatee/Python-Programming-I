''' Created on May 24, 2018

@author: Samantha Hangsan


'''
from tkinter import Tk, Label, Frame, Button, RAISED, RIDGE, Entry, END, BOTH, X, TOP, BOTTOM

# Create a class called Tour.
# class Tour(TourGui):

# # instantiated with two US cities
# # used to fetch information from the web.

# 	def __init__ (self, city_1, city_2):

# '''
# The constructor takes two strings as arguments, each giving a
# city name and state abbreviation, indicating the origin and destination.  For
# example: Tour(“New York, NewY”, “Los Angeles, CA”)represents a tour that starts
# in New York city and ends in Los Angeles.
# '''

'''
This method takes a
single (optional) argument indicating a mode – one of the strings ‘driving’
(default), ‘biking, or ‘walking’.  It returns the total distance (in meters)
covered by the tour for the indicated mode.  This method is where you will use
urllib functions to get data from the web to find the distances between two
locations in the tour and calculate the total distance.  If a response does
not contain a distance value, the method should raise a ValueError exception.
'''


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
		# request object
		print(self.origin_entry.get())
		print(self.destination_entry.get())
		print(self.mode_entry.get())

		# if (self.mode_entry.get().lower() != 'driving' and self.mode_entry.get().lower() !='biking' and self.mode_entry.get().lower() != 'walking'):
		if (self.mode_entry.get().lower() != 'driving' and != 'biking' and != 'walking'):
			print('invalid')


		# user_agent = 'Mozilla/5.0'
		# headers = {'User-Agent': user_agent}

		# origins = input('Origin: ')
		# destinations = input('Destination: ')
		# sensor = input('Sensor: ')
		# mode = input('Mode: ')

		# value = {'q': search_query}

		# url = 'http://maps.googleapis.com/maps/api/distancematrix/json?'
		# data = urllib.parse.urlencode(value)

		# url = url + 'origins=' + '&destinations=' + '&mode=' + '&sensor=false'
		# req = urllib.request.Request(url, None, headers)
		# response = urllib.request.urlopen(req)
		# html = response.read().decode()



'''

2. onClick
This method is the event handler for the Get Distance Button. When
the button is clicked, the origin, destination and mode fields are read, the
query is made and the distance between the origin and the destination is
displayed. If the user enters an invalid mode, a message box shows up
indicating invalid mode was entered:

If the distance was not found between the origin and the destination, a
message box shows up indicating the distance was not found:
'''






def main():

	# url, query = search_on_google()
	root = Tk()
	tour_application = TourGui()
	#Tour(tour_application)
	root.mainloop()


if __name__ == '__main__':
	main()

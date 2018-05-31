''' Created on May 24, 2018

@author: Samantha Hangsan


'''
from tkinter import Tk, Frame, Button, RAISED, RIDGE, Entry, END

# Create a class called Tour.
class Tour():

# instantiated with two US cities
# used to fetch information from the web.

	def __init__ (self, city_1, city_2):

'''
The constructor takes two strings as arguments, each giving a
city name and state abbreviation, indicating the origin and destination.  For
example: Tour(“New York, NY”, “Los Angeles, CA”)represents a tour that starts
in New York city and ends in Los Angeles.
'''

	def distance(self, mode):

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
		self.title('Tour')

		labels = ['Origin', 'Destination', 'Mode', 'Distance']

'''
The constructor doesn’t take any arguments. The constructor
creates two frames in the window, a top frame and buttom frame. The top frame
contains a  label and an entry widget for the following fields: origin,
destination, and mode. The bottom frame contains a label and text widget for
Distance and a button widget for Get Distnace. The GUI should like the
following:

2. onClick
This method is the event handler for the Get Distance Button. When
the button is clicked, the origin, destination and mode fields are read, the
query is made and the distance between the origin and the destination is
displayed. If the user enters an invalid mode, a message box shows up
indicating invalid mode was entered:

If the distance was not found between the origin and the destination, a
message box shows up indicating the distance was not found:
'''

def search_on_google():
	# request object
	user_agent = 'Mozilla/5.0'
	headers = {'User-Agent': user_agent}

	origins = input('Origin: ')
	destinations = input('Destination: ')
	sensor = input('Sensor: ')
	mode = input('Mode: ')

	value = {'q': search_query}

	url = 'http://maps.googleapis.com/maps/api/distancematrix/json?'
	data = urllib.parse.urlencode(value)

	url = url + data
	req = urllib.request.Request(url, None, headers)
	response = urllib.request.urlopen(req)
	html = response.read().decode()

	return url, html


def main():

	url, query = search_on_google()

	root = Tk()
	TourGui(root)
	root.mainloop()

if __name__ == '__main__':
	main()

''' Created on May 24, 2018

@author: Samantha Hangsan


'''

''' Create a class called Tour.  An instance of this class is to be
instantiated with two US cities, and is used to fetch information from the
web. Specifically, the class must define:

1. __init__
The constructor takes two strings as arguments, each giving a
city name and state abbreviation, indicating the origin and destination.  For
example: Tour(“New York, NY”, “Los Angeles, CA”)represents a tour that starts
in New York city and ends in Los Angeles. 2. distance  This method takes a
single (optional) argument indicating a mode – one of the strings ‘driving’
(default), ‘biking, or ‘walking’.  It returns the total distance (in meters)
covered by the tour for the indicated mode.  This method is where you will use
urllib functions to get data from the web to find the distances between two
locations in the tour and calculate the total distance.  If a response does
not contain a distance value, the method should raise a ValueError exception.
'''

'''
Graphical User Interface Description:  Create a class called TourGui. An
instance of this class is to be instantiated in the main. Specifically the
class must define:

1. __init__ T
he constructor doesn’t take any arguments. The constructor
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



# json convert the python dictionary
# above into a json
import json
import turtle

# urllib.request fetch URLs using
# a variety of different protocols
import urllib.request
import time

# webbrowser provides a high-level interface
# to allow displaying Web-based documents
# to users
import webbrowser

# geocoder takes the data and locate these
# locations in the map
import geocoder

url = &quot;http://api.open-notify.org/astros.json&quot;
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open(&quot;iss.txt&quot;, &quot;w&quot;)
file.write(&quot;There are currently &quot; +
            # prints number of astronauts
        str(result[&quot;number&quot;]) + &quot; astronauts on the ISS: \n\n&quot;)
people = result[&quot;people&quot;]

# prints names of crew
for p in people:
    file.write(p['name'] + &quot; - on board&quot; + &quot;\n&quot;)
# print long and lat
g = geocoder.ip('me')
file.write(&quot;\nYour current lat / long is: &quot; + str(g.latlng))
file.close()
webbrowser.open(&quot;iss.txt&quot;)

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic(&quot;images/map.gif&quot;)
screen.register_shape(&quot;images\iss.gif&quot;)
iss = turtle.Turtle()
iss.shape(&quot;images\iss.gif&quot;)
iss.setheading(45)
iss.penup()

while True:

    # load the current status of the ISS in real-time
    url = &quot;http://api.open-notify.org/iss-now.json&quot;
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result[&quot;iss_position&quot;]
    lat = location['latitude']
    lon = location['longitude']

    # Ouput lon and lat to the terminal
    lat = float(lat)
    lon = float(lon)
    print(&quot;\nLatitude: &quot; + str(lat))
    print(&quot;\nLongitude: &quot; + str(lon))

    # Update the ISS location on the map
    iss.goto(lon, lat)

    # Refresh each 5 seconds
    time.sleep(5)

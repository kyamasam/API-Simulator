import json
import random
import time
import urllib.request

cooler_instances = []

# todo: create interface for creating simulated coolers. the cooler object created here will use data from the database
# todo: allow user to launch the simulator script as a service that runs in the background
# todo: allow user

class Cooler:
    def __init__(self, cooler, humidity, temperature, location_lat, location_long, door_opens):
        cooler_instances.append(self)
        self.cooler = cooler
        self.humidity = humidity
        self.temperature = temperature
        self.location_lat = location_lat
        self.location_long = location_long
        self.door_opens = door_opens


print("\n Welcome to the cooler Simulator \n")
print(''''
 _______  _______  _______  _        _______  _______        _______ _________ _______           _        _______ _________ _______  _______ 
(  ____ \(  ___  )(  ___  )( \      (  ____ \(  ____ )      (  ____ \\__   __/(       )|\     /|( \      (  ___  )\__   __/(  ___  )(  ____ )
| (    \/| (   ) || (   ) || (      | (    \/| (    )|      | (    \/   ) (   | () () || )   ( || (      | (   ) |   ) (   | (   ) || (    )|
| |      | |   | || |   | || |      | (__    | (____)|      | (_____    | |   | || || || |   | || |      | (___) |   | |   | |   | || (____)|
| |      | |   | || |   | || |      |  __)   |     __)      (_____  )   | |   | |(_)| || |   | || |      |  ___  |   | |   | |   | ||     __)
| |      | |   | || |   | || |      | (      | (\ (               ) |   | |   | |   | || |   | || |      | (   ) |   | |   | |   | || (\ (   
| (____/\| (___) || (___) || (____/\| (____/\| ) \ \__      /\____) |___) (___| )   ( || (___) || (____/\| )   ( |   | |   | (___) || ) \ \__
(_______/(_______)(_______)(_______/(_______/|/   \__/      \_______)\_______/|/     \|(_______)(_______/|/     \|   )_(   (_______)|/   \__/
                                                                                                                                             
' ''')

sleep_time = 30
while 1:
    print("\nSleep For ", sleep_time, 'Seconds\n')
    time.sleep(sleep_time)
    # instances of the class
    # this could be automated since we can create dynamic classes in python
    Nairobi = Cooler(1, random.randrange(0, 10), random.randrange(0, 10), "36.8166695", "-1.28333",
                     random.randrange(15, 30))
    Mombasa = Cooler(2, random.randrange(0, 10), random.randrange(0, 10), "39.6635895", "-4.0546598",
                     random.randrange(15, 30))
    Wajiir = Cooler(4, random.randrange(0, 10), random.randrange(0, 10), "40.0573196", "1.7471",
                    random.randrange(15, 30))
    Kisumu = Cooler(5, random.randrange(30, 50), random.randrange(30, 50), "34.7617111", "-0.10221",
                    random.randrange(0, 5))
    Bungoma = Cooler(6, random.randrange(20, 30), random.randrange(30, 50), "34.5605507", "0.5635",
                     random.randrange(0, 5))

    for instance in cooler_instances:
        # cool way of getting the class name
        # print(Obj.__class__.__name__)
        body = {
            "cooler": instance.cooler,
            "humidity": instance.humidity,
            "temperature": instance.temperature,
            "location_lat": instance.location_lat,
            "location_long": instance.location_long,
            "door_opens": instance.door_opens
        }

        destination_url = "http://127.0.0.1:8000/api/cooler_data/"
        request = urllib.request.Request(destination_url)
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        json_data = json.dumps(body)
        json_data_as_bytes = json_data.encode('utf-8')
        request.add_header('Content-Length', len(json_data_as_bytes))
        response = urllib.request.urlopen(request, json_data_as_bytes)

        if response.getcode() == 201:
            print("Success...\n")

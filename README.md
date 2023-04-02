# pi-climate
A project bundle containing the necessary files and instructions to equip a Raspberry Pi Pico to be a humidity, CO2, and temperature sensor.

Case was commissioned by Manos Liolios, aka /u/cgmanuil and https://www.artstation.com/manosl - great modeler, bring him your ideas!

Parts List:
 - Pi Pico W (NOT H)
 - Adafruit SCD-30
 - Dorhea 3007
 - Stemma QT Cable (1)
 - Soldering iron, solder, super glue (or screws that fit the Dorhea fan)
 - a lighter

Other things to consider:
 - The pico will dump data to a local influx database
 - The case is 3D printed

## Directions:

Buy the things

Print the case (or have a friend do it (I’ll be your friend))
Model is also available via: https://www.printables.com/model/440658-pi-pico-w-scd-30-case

Get ready to do microcontroller stuff (we’re gonna test everything pre-solder)

### SOFTWARE:

Plug in the pico, it should show up as a storage device called RPI-PICO or something.

Flash the pico with the .uf2 in the repository (meaning drag the file over). It’s Adafruit’s CircuitPython. You can also just use your favorite search engine to find the most up to date version of the firmware – remember, you want it for the Pico W. Once it’s over, the device will reboot and show up as a storage device named CIRCUITPY.

Drag everything over. Everything in /lib in the repo goes in /lib on the device, code.py and secrets.py should go into the highest directory on the device. It’ll now try to run that code over and over until it fails (which it will).

On a Linux device, use `screen /dev/ttyACM<n> 115200` to interface with the pi using serial. If you’re using Windows, install Linux. If you press enter, you can enter a python console to test importing, running specific functions, whatever; it’s handy. Make sure that the code is running.

Now’s a good time to plug everything in. If you have a breadboard, use it. If you don’t, find a friend to hold everything for you – you’ll want to make sure everything works the way you think it does before soldering anything.

If you’ve done everything right, after a soft reboot it’ll print the sensor data into the serial console. Hooray! If you haven’t, the console output should be pretty specific about what’s wrong. Now is also a good time to test your influxdb.

Now it’s time for hardware.






### HARDWARE:

Cut the connectors and strip the wires (preserving as much length as possible) on a fan and a stemma qt cable – not the end that plugs into the sensor.

Do a test fit for everything. See how the fan fits into the case (it should have the white sticker pointing OUT OF THE CASE – air will flow in the direction the sticker is facing), pull the cables around so you can see how they need to be soldered, put the boards into the case, put the case together.

twist together matching cable colors (red and black) on the fan and stemma cables.

solder everything together – here’s a nice pinout guide: https://learn.adafruit.com/adafruit-scd30/python-circuitpython
though I used pins 3 & 4 for SDA and SCL instead of 1 & 2. If you do 1 & 2, make sure to change the code to reflect that. Red goes to 3v3 and black goes to GND.

Superglue the fan in, put the pico in, plug in the sensor, and put it in the base of the case. The boards should be fine without any kind of adhesive, but you could melt a post with a soldering iron to keep them from rattling if you want. Put the two halves together, then plug it in and test – your influxdb should get sent data nearly immediately after being plugged in. If it doesn’t work, debug with the screen command.

Once everything is confirmed working, use a lighter to melt the case together. Don’t go too overboard or you won’t be able to pull the halves apart.

Plug it in and get yourself some climate data. I visualize mine with Grafana.


Feel free to suggest or contribute to anything here, I have no idea what I’m doing.

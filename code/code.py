import time
import adafruit_scd30
import busio
import board
import wifi
import socketpool
import ssl
import adafruit_requests
import secrets

i2c = None
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool)

while True:
    # SCD-30 has temperamental I2C with clock stretching, datasheet recommends
    # starting at 50KHz
    while not i2c:
        try:
            i2c = busio.I2C(board.GP3, board.GP2, frequency=50000)
            scd = adafruit_scd30.SCD30(i2c)
        except Exception as e:
            print(e)
            time.sleep(2)
            pass

    while not wifi.radio.ipv4_address:
        try:
            wifi.radio.connect(secrets.SSID, secrets.PASS)
        except:
            print("Wi-fi error - retrying. . .")
            time.sleep(2)
            pass
            
    print(f"Wifi Connected with IP: {wifi.radio.ipv4_address}")
    
    if scd.data_available:
        co2 = scd.CO2
        temp = scd.temperature
        humidity = scd.relative_humidity
        payload = f'temperature,room=office value={temp}\nco2,room=office value={co2}\nhumidity,room=office value={humidity}'
        print("-----------------------------------")
        print("CO2:", co2, "PPM")
        print("Temperature:", temp, "degrees C")
        print("Humidity:", humidity, "%%rH")
        requests.post(secrets.URL, data=payload)
    time.sleep(30)

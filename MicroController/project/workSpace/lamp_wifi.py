import network
import socket
from machine import Pin
import time

SSID = "SANGATLUCU"
PASSWORD = "SANGATLUXU"

# LED onboard ESP8266 (D4 / GPIO2) = active LOW
led = Pin(2, Pin.OUT)
led.value(1)  # awal MATI (active LOW)

# LED eksternal (umumnya active HIGH)
led3 = Pin(15, Pin.OUT)  # GPIO15 (D8)
led4 = Pin(13, Pin.OUT)  # GPIO13 (D7)
led3.value(0)  # awal MATI
led4.value(0)  # awal MATI

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(0.5)
            print(".", end="")
    print("\nWiFi connected!")
    ip = wlan.ifconfig()[0]
    print("IP address:", ip)
    return ip

def web_page():
    # status LED onboard (active LOW)
    state  = "ON" if led.value() == 0 else "OFF"

    # status LED eksternal (active HIGH)
    state1 = "ON" if led3.value() == 1 else "OFF"
    state2 = "ON" if led4.value() == 1 else "OFF"

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ESP8266 LED WEB</title>
  <style>
    body {{ font-family: Arial; text-align:center; margin-top:50px; }}
    button {{
      font-size:20px; padding:15px 30px; margin:10px;
      border:none; border-radius:10px; cursor:pointer;
    }}
    .on {{ background:#2ecc71; color:white; }}
    .off {{ background:#e74c3c; color:white; }}
  </style>
</head>
<body>
  <h2>Kontrol LED ESP8266 via Web</h2>
  <p>Status LED_biru: <b>{state}</b></p>
  <p>Status LED_hijau: <b>{state1}</b></p>
  <p>Status LED_kuning: <b>{state2}</b></p>

  <p>
    <a href="/on"><button class="on">LED BIRU ON</button></a>
    <a href="/off"><button class="off">LED BIRU OFF</button></a>
    <br>
    <a href="/pin1_on"><button class="on">LED HIJAU ON</button></a>
    <a href="/pin1_off"><button class="off">LED HIJAU OFF</button></a>
    <br>
    <a href="/pin2_on"><button class="on">LED KUNING ON</button></a>
    <a href="/pin2_off"><button class="off">LED KUNING OFF</button></a>
  </p>
</body>
</html>"""
    return html

ip = connect_wifi()

addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Web server ready. Open browser to:")
print("http://{}/".format(ip))

while True:
    conn = None
    try:
        conn, addr = s.accept()
        request = conn.recv(1024).decode()

        first_line = request.split("\r\n")[0]
        path = first_line.split(" ")[1]

        # LED biru (onboard, active LOW)
        if path == "/on":
            led.value(0)   # nyala
        elif path == "/off":
            led.value(1)   # mati

        # LED hijau (GPIO15, active HIGH)
        elif path == "/pin1_on":
            led3.value(1)
        elif path == "/pin1_off":
            led3.value(0)

        # LED kuning (GPIO13, active HIGH)
        elif path == "/pin2_on":
            led4.value(1)
        elif path == "/pin2_off":
            led4.value(0)

        response = web_page()
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n")
        conn.sendall(response)

    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            conn.close()


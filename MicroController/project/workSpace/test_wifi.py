import network
import socket
from machine import Pin
import time
import errno  # untuk kode error

SSID = "chizui"
PASSWORD = "chizui03"

# LED onboard ESP8266 (D4 / GPIO2) = active LOW
led = Pin(15, Pin.OUT)
led3 = Pin(13, Pin.OUT)  # GPIO15 (D8)
led4 = Pin(12, Pin.OUT)  # GPIO13 (D7)
led.value(0)  # awal MATI (active LOW)
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
    state  = "ON" if led.value() == 1 else "OFF"      
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
  <h2>ESP8266 LED WEB</h2>
  <p>Status LED Hijau: <b>{state}</b></p>
  <p>Status LED Kuning: <b>{state1}</b></p>
  <p>Status LED Merah: <b>{state2}</b></p>

  <p>
    <a href="/on"><button class="on">LED IJO ON</button></a>
    <a href="/off"><button class="off">LED IJO OFF</button></a>
    <br>
    <a href="/pin1_on"><button class="on">LED KUNING ON</button></a>
    <a href="/pin1_off"><button class="off">LED KUNING OFF</button></a>
    <br>
    <a href="/pin2_on"><button class="on">LED MERAH ON</button></a>
    <a href="/pin2_off"><button class="off">LED MERAH OFF</button></a>
  </p>
</body>
</html>"""
    return html


def start_server(preferred_port=80):
    global s
    try:
        s.close()
    except:
        pass

    for port in (preferred_port, 8080):
        try:
            addr = socket.getaddrinfo("0.0.0.0", port)[0][-1]
            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(addr)
            s.listen(1)

            # OPTIONAL: timeout supaya loop bisa jalan walau ga ada client
            s.settimeout(2)

            print("Server listening on port:", port)
            return port
        except OSError as e:
            if e.args and e.args[0] == errno.EADDRINUSE:
                print("Port", port, "in use, trying another port...")
                try:
                    s.close()
                except:
                    pass
                continue
            else:
                raise e

    raise OSError("Cannot bind to port 80 or 8080")


ip = connect_wifi()
PORT = start_server(80)

print("Web server ready. Open browser to:")
print("http://{}:{}/".format(ip, PORT) if PORT != 80 else "http://{}/".format(ip))


while True:
    conn = None
    try:
        try:
            conn, addr = s.accept()
        except OSError as e:
            # kalau timeout (karena settimeout), lanjut loop aja
            time.sleep(0.02)   # biar ga overload
            continue

        try:
            request = conn.recv(1024)
            if not request:
                conn.close()
                time.sleep(0.02)
                continue
            request = request.decode()
        except OSError as e:
            if e.args and e.args[0] == errno.ECONNRESET:
                time.sleep(0.02)
                continue
            else:
                raise e

        first_line = request.split("\r\n")[0]
        path = first_line.split(" ")[1]

        if path == "/on":
            led.value(1)
        elif path == "/off":
            led.value(0)
        elif path == "/pin1_on":
            led3.value(1)
        elif path == "/pin1_off":
            led3.value(0)
        elif path == "/pin2_on":
            led4.value(1)
        elif path == "/pin2_off":
            led4.value(0)

        response = web_page()

        try:
            conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n")
            conn.sendall(response)
        except OSError as e:
            if e.args and e.args[0] == errno.ECONNRESET:
                time.sleep(0.02)
                continue
            else:
                raise e

        # delay setelah melayani 1 request
        time.sleep(0.1)

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            try:
                conn.close()
            except:
                pass

    # delay kecil tiap loop (jaga stabilitas)
    time.sleep(0.02)



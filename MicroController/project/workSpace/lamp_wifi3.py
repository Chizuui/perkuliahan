import network
import socket
from machine import Pin
import time
import errno

# ===== HOTSPOT SETTING =====
AP_SSID = "ESP-LED"
AP_PASSWORD = "12345678"   # minimal 8 char kalau mau WPA2

# LED onboard ESP8266 (D4 / GPIO2) = active LOW
led = Pin(2, Pin.OUT)
led.value(1)  # awal MATI

# LED eksternal (active HIGH)
led3 = Pin(15, Pin.OUT)  # D8 / GPIO15
led4 = Pin(13, Pin.OUT)  # D7 / GPIO13
led3.value(0)
led4.value(0)


def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)

    # authmode=3 -> WPA2-PSK
    ap.config(essid=AP_SSID, password=AP_PASSWORD, authmode=3)

    # tunggu AP beneran aktif
    while ap.active() == False:
        time.sleep(0.2)

    ip = ap.ifconfig()[0]
    print("Hotspot aktif!")
    print("SSID:", AP_SSID)
    print("Password:", AP_PASSWORD)
    print("IP ESP:", ip)
    return ip


def web_page():
    state  = "ON" if led.value() == 0 else "OFF"   # onboard active LOW
    state1 = "ON" if led3.value() == 1 else "OFF"  # eksternal active HIGH
    state2 = "ON" if led4.value() == 1 else "OFF"

    return f"""<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ESP8266 AP LED</title>
  <style>
    body {{ font-family: Arial; text-align:center; margin-top:40px; }}
    button {{
      font-size:20px; padding:12px 24px; margin:6px;
      border:none; border-radius:10px; cursor:pointer;
    }}
    .on {{ background:#2ecc71; color:white; }}
    .off {{ background:#e74c3c; color:white; }}
  </style>
</head>
<body>
  <h2>Kontrol LED via Hotspot ESP8266</h2>
  <p>LED Biru (onboard): <b>{state}</b></p>
  <p>LED Hijau: <b>{state1}</b></p>
  <p>LED Kuning: <b>{state2}</b></p>

  <p>
    <a href="/on"><button class="on">BIRU ON</button></a>
    <a href="/off"><button class="off">BIRU OFF</button></a><br>
    <a href="/pin1_on"><button class="on">HIJAU ON</button></a>
    <a href="/pin1_off"><button class="off">HIJAU OFF</button></a><br>
    <a href="/pin2_on"><button class="on">KUNING ON</button></a>
    <a href="/pin2_off"><button class="off">KUNING OFF</button></a>
  </p>
</body>
</html>"""


def start_server(port=80):
    global s
    try:
        s.close()
    except:
        pass

    addr = socket.getaddrinfo("0.0.0.0", port)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    s.settimeout(2)
    print("Web server listen port:", port)


# ========== MAIN ==========
ip = start_ap()
start_server(80)

print("Buka browser ke:")
print("http://{}/".format(ip))   # biasanya 192.168.4.1

while True:
    conn = None
    try:
        try:
            conn, addr = s.accept()
        except OSError:
            time.sleep(0.02)
            continue

        try:
            req = conn.recv(1024)
            if not req:
                conn.close()
                time.sleep(0.02)
                continue
            req = req.decode()
        except OSError as e:
            if e.args and e.args[0] == errno.ECONNRESET:
                time.sleep(0.02)
                continue
            else:
                raise e

        first = req.split("\r\n")[0]
        path = first.split(" ")[1]

        if path == "/on":
            led.value(0)
        elif path == "/off":
            led.value(1)
        elif path == "/pin1_on":
            led3.value(1)
        elif path == "/pin1_off":
            led3.value(0)
        elif path == "/pin2_on":
            led4.value(1)
        elif path == "/pin2_off":
            led4.value(0)

        html = web_page()
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n")
        conn.sendall(html)

        time.sleep(0.1)

    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            try:
                conn.close()
            except:
                pass

    time.sleep(0.02)


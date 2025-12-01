import gc
import time
import BlynkLib
import machine
import network
from machine import ADC, Pin

# --- KONFIGURASI ---
led = Pin(2, Pin.OUT)

WIFI_SSID = "chizui-desktop"  # Pastikan SSID 2.4GHz
WIFI_PASS = "chizui03"
BLYNK_AUTH = "JtlD6EgQ3A-Q-Qt3iW0gnzug67NAQmP3"

# Variabel Global
pot = ADC(0)
pot_old = 0
pot_now = 0
pot_lock = 0
pot_time = 0
pot_value_old = 0
pot_value = False
pot_next_check = 300


# --- FUNGSI KONEKSI WIFI ---
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Menghubungkan ke WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            time.sleep(1)
            print(".", end="")
    print("\nWiFi Terhubung!")
    print("IP Address:", wlan.ifconfig()[0])


connect_wifi()

# --- INISIALISASI BLYNK ---
# Kita gunakan server blynk.cloud sesuai akun baru
blynk = BlynkLib.Blynk(BLYNK_AUTH, server="blynk.cloud")


# --- FUNGSI LOGIKA ---
def TombolSentuh():
    global pot, pot_old, pot_now, pot_lock, pot_time, pot_value, pot_next_check
    now = time.ticks_ms()
    elapsed = int(now - pot_time)

    if elapsed > pot_next_check:
        pot_value = 0
        pot_old = pot_now
        for x in range(1, 5):
            pot_now = pot.read()
            if abs(pot_now - pot_old) >= 3:
                pot_value = 1
                break
            pot_old = pot_now
            time.sleep(0.01)

        pot_time = time.ticks_ms()
        if pot_value:
            pot_next_check = 500
        else:
            pot_next_check = 10

    return pot_value


gc.collect()

# --- BLYNK HANDLERS (CARA MANUAL) ---


def blynk_disconnected(args):
    print("Blynk disconnected")


def v0_write_handler(value):
    print("Nilai tombol V0: " + str(value[0]))
    if value[0] == "1":
        led.value(0)
        print("LED menyala")
    else:
        led.value(1)
        print("LED mati")


def v1_write_handler(value):
    print("Tombol Sentuh V1 : " + str(value[0]))


def v2_write_handler(value):
    print("Uptime Request V2: " + str(value[0]))


# --- DAFTARKAN HANDLER (BAGIAN REVISI) ---
# Ini yang memperbaiki error "3 arguments"
blynk.on("disconnected", blynk_disconnected)
blynk.on("V0", v0_write_handler)
blynk.on("V1", v1_write_handler)
blynk.on("V2", v2_write_handler)


# --- MAIN LOOP ---
def runLoop():
    global pot_value_old, pot_value

    pot_value = TombolSentuh()
    firstBoot = time.time()
    oldTick = firstBoot

    print("Sistem Siap! Cek App Blynk kamu...")

    while True:
        blynk.run()

        if time.time() > oldTick:
            uptime_sec = time.time() - firstBoot
            blynk.virtual_write(2, uptime_sec)
            oldTick = time.time() + 1

        pot_value = TombolSentuh()
        if pot_value_old != pot_value:
            pot_value_old = pot_value
            print("Status tombol sentuh : " + str(pot_value))
            if pot_value:
                blynk.virtual_write(1, 1)
            else:
                blynk.virtual_write(1, 0)

        gc.collect()


# Jalankan Program
gc.collect()
runLoop()


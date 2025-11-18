import time

from machine import ADC, Pin

ldr = ADC(0)

# 1. Gabungkan semua LED ke dalam satu list
lamp = [
    Pin(15, Pin.OUT),  # led1
    Pin(13, Pin.OUT),  # led2
    Pin(12, Pin.OUT),  # led3
    Pin(14, Pin.OUT),  # led4
    Pin(16, Pin.OUT),  # led5
]

# Threshold LED (contoh)
thresholds = [1024, 900, 700, 500, 300]

while True:
    value = ldr.read()  # 0 - 1023
    print("LDR:", value)

    for i in range(len(lamp)):  # mengambil range dari variable lamp
        # Mengambil led dan threshold menggunakan index 'i'
        led = lamp[i]
        threshold = thresholds[i]

        if value < threshold:  # jika nilai LDR lebih kecil dari threshold
            led.on()  # led menyala
        else:  # jika nilai led lebih besar dari trasehold
            led.off()  # maka led akan mati

    time.sleep_ms(10)


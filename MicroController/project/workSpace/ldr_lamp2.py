from machine import Pin, ADC
import time

ldr = ADC(0)

# menggabungkan menjadi 1 list
lamp = [
    machine.Pin(15, machine.Pin.OUT),  # led1
    machine.Pin(13, machine.Pin.OUT),  # led2
    machine.Pin(12, machine.Pin.OUT),  # led3
    machine.Pin(14, machine.Pin.OUT),  # led4
    machine.Pin(16, machine.Pin.OUT)   # led5
]

# Threshold LED (contoh)
thresholds = [1000, 800, 600, 400, 200]

while True:
    value = ldr.read()    # 0 - 1024
    print("LDR:", value)

    # 3. Loop gabungan untuk cek threshold DAN kendalikan LED
    # zip() akan memasangkan setiap LED dengan threshold-nya
    # (leds[0] dengan thresholds[0], leds[1] dengan thresholds[1], dst.)
    
    for led, threshold in zip(lamp, thresholds):
      # jika value lebih kecil dari trasehold yang dikasih, maka led akan menyala
        if value <= threshold:
            led.on()
      # jika tidak maka akan terjadi sebaliknya
        else:
            led.off()
    
    time.sleep_ms(5)


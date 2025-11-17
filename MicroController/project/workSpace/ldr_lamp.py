from machine import Pin, ADC
import time

ldr = ADC(0)

# LEDs: dari gelap -> terang (D8..D0)
led1 = Pin(15, Pin.OUT)   # D8
led2 = Pin(13, Pin.OUT)   # D7
led3 = Pin(12, Pin.OUT)   # D6
led4 = Pin(14, Pin.OUT)   # D5
led5 = Pin(16, Pin.OUT)   # D0 (merah)

# Threshold LED (contoh)
T1 = 1000
T2 = 800
T3 = 600
T4 = 400
T5 = 200

while True:
    value = ldr.read()     # 0 - 1023
    print("LDR:", value)

    # reset LED
    led1.off(); led2.off(); led3.off(); led4.off(); led5.off()

    # Nyalakan LED sesuai threshold (semakin terang -> lebih banyak LED)
    if value <= T1:
        led1.on()
    if value <= T2:
        led2.on()
    if value <= T3:
        led3.on()
    if value <= T4:
        led4.on()
    if value <= T5:
        led5.on()

    time.sleep_ms(5)   # delay sangat responsif (sesuai diskusi)

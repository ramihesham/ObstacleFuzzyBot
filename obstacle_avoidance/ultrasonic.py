from machine import Pin, utime_pulse_us
import utime

TRIGGER_PIN = 2
ECHO_PIN = 3

# Initialize trigger and echo pins
trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def get_distance():
    # Send a 10us pulse.
    trigger.low()
    utime.sleep_us(5)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()

    # Measure the duration of the incoming pulse
    duration = utime_pulse_us(echo, Pin.HIGH)
    
    # Calculate distance in cm (sound travels at about 343m/s, which is roughly 0.0343cm/us)
    distance = (duration / 2) * 0.0343

    return distance
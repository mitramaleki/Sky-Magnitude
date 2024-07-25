#This code is written by Mitra Maleki
from skyfield.api import load, Topos
from datetime import datetime, timezone
import math

# Load astronomical data and define Sun, Moon, and Earth
ts = load.timescale()
eph = load('de421.bsp')
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

# Set observer location to Iran National Observatory (latitude, longitude)
observer = Topos('35.7963 N', '51.3542 E')

def calculate_moon_phase_and_brightness(date):
    # Convert the given date and time to UTC
    t = ts.utc(date.year, date.month, date.day, date.hour, date.minute)
    observer_location = earth + observer

    # Get apparent positions of the Sun and Moon as seen from the observer's location
    sun_astrometric = observer_location.at(t).observe(sun).apparent()
    moon_astrometric = observer_location.at(t).observe(moon).apparent()

    # Calculate ecliptic longitudes of the Sun and Moon
    _, sun_lon, _ = sun_astrometric.ecliptic_latlon()
    _, moon_lon, _ = moon_astrometric.ecliptic_latlon()

    # Calculate the phase angle between the Moon and the Sun
    phase_angle = (moon_lon.degrees - sun_lon.degrees) % 360
    if phase_angle > 180:
        phase_angle = 360 - phase_angle

    # Calculate the percentage of the Moon's illumination
    illumination = (1 + math.cos(math.radians(phase_angle))) / 2 * 100

    # Determine the moon phase based on the phase angle
    if phase_angle < 1.0 or phase_angle >= 359.0:
        phase_name = "New Moon"
    elif 1.0 <= phase_angle < 89.0:
        phase_name = "Waxing Crescent"
    elif 89.0 <= phase_angle <= 91.0:
        phase_name = "First Quarter"
    elif 91.0 < phase_angle < 179.5:
        phase_name = "Waxing Gibbous"
    elif 179.5 <= phase_angle <= 180.5:
        phase_name = "Full Moon"
    elif 180.5 < phase_angle < 269.5:
        phase_name = "Waning Gibbous"
    elif 269.5 <= phase_angle <= 270.5:
        phase_name = "Last Quarter"
    else:
        phase_name = "Waning Crescent"

    # Calculate sky brightness (simplified model based on moon illumination)
    if phase_name == "New Moon":
        sky_brightness = 22.0  # Dark sky magnitude
    else:
        sky_brightness = 22.0 - (2.5 * math.log10(illumination / 100))

    return phase_angle, phase_name, sky_brightness

# Main function to prompt user for input and display results
def main():
    user_input = input("Enter the date and time (YYYY-MM-DD HH:MM) in UTC: ")
    try:
        date = datetime.strptime(user_input, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
        phase_angle, moon_phase, sky_brightness = calculate_moon_phase_and_brightness(date)
        print(f"Calculated Phase Angle: {phase_angle:.2f} degrees")
        print(f"Calculated Moon Phase: {moon_phase}")
        print(f"Calculated Sky Brightness: {sky_brightness:.2f} mag/arcsec^2")
    except ValueError:
        print("Invalid date format. Please enter the date and time in 'YYYY-MM-DD HH:MM' format.")

if __name__ == "__main__":
    main()

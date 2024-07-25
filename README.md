
# Moon Phase and Sky Brightness Calculator

This Python script calculates the moon phase and sky brightness (sky magnitude) for a given date and time. It uses the Skyfield library to determine the positions of celestial bodies from the observer's location, specifically set to the Iran National Observatory.

## Features

- **Moon Phase Calculation**: Determines the moon phase (e.g., New Moon, Waxing Crescent) based on the phase angle calculated from the Sun and Moon's ecliptic longitudes.
- **Sky Brightness Calculation**: Estimates the sky brightness in magnitudes per square arcsecond (mag/arcsec²), which is a measure of the sky's darkness or brightness, influenced primarily by the moon's illumination.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Skyfield Library**: Install Skyfield for astronomical calculations.
  ```
  pip install skyfield
  ```

## Usage

1. **Clone the Repository**: Download or clone the repository containing this script.
2. **Run the Script**: Execute the script using Python.
   ```
   python moon_phase_calculator.py
   ```
3. **Input Date and Time**: When prompted, enter the desired date and time in the format `YYYY-MM-DD HH:MM` (UTC). The script will output the moon phase, phase angle, and sky brightness.

## Example

```
Enter the date and time (YYYY-MM-DD HH:MM) in UTC: 2024-07-05 22:59
Calculated Phase Angle: 0.53 degrees
Calculated Moon Phase: New Moon
Calculated Sky Brightness: 22.00 mag/arcsec^2
```

## How It Works

1. **Loading Data**: The script loads ephemeris data for the Sun, Moon, and Earth using the Skyfield library.
2. **Observer Location**: The observer's location is set to the Iran National Observatory (35.7963 N, 51.3542 E).
3. **Calculations**:
   - **Phase Angle**: The script calculates the phase angle between the Moon and Sun based on their ecliptic longitudes.
   - **Moon Phase**: The phase angle determines the moon phase (e.g., New Moon, Full Moon).
   - **Sky Brightness**: Based on the moon's illumination, the sky brightness is estimated.

## Important Notes

- The script provides a simplified estimation of sky brightness. For precise measurements, consider using additional atmospheric and local environmental data.
- Ensure the date and time are entered in UTC to maintain accuracy.

## Contributing

If you find bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is for INO Observatory.

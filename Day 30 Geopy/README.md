# Day 30 - Geopy Library

# 📌 Overview

On Day 30, I explored Python’s powerful **geopy library**, which is used for geocoding and location-based operations.

The geopy library allows Python programs to:

* convert place names into coordinates
* retrieve location information
* calculate geographical distances
* work with GPS data

It is widely used in:

* map applications
* delivery systems
* travel platforms
* location tracking
* analytics applications

---

# 📦 Installing Geopy

Install using pip:

```bash id="geo301d"
pip install geopy
```

---

# 🧠 Importing the Library

```python id="geo301e"
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
```

---

# 🌍 What is Geocoding?

Geocoding means converting:

* city names
* addresses
* locations

into:

* latitude
* longitude coordinates

Example:

```text id="geo301f"
Hyderabad → (17.3850, 78.4867)
```

---

# 📍 Creating a Geolocator

Example:

```python id="geo301g"
Nominatim(user_agent="geo_app")
```

This initializes the geolocation service.

---

# 🔍 Getting Location Details

Example:

```python id="geo301h"
geolocator.geocode("Hyderabad")
```

This retrieves:

* full address
* latitude
* longitude

---

# 📏 Calculating Distance

Example:

```python id="geo301i"
geodesic(location1, location2)
```

This calculates geographical distance.

---

# 💻 Complete Example

```python id="geo301j"
from geopy.geocoders import Nominatim

geo = Nominatim(user_agent="app")

location = geo.geocode("Delhi")

print(location.latitude)
```

---

# 🚀 Real-World Uses

Geopy is used in:

* Google Maps-like apps
* food delivery systems
* travel applications
* GPS tracking systems
* logistics platforms

---

# ⚡ Why Geolocation is Important

Location systems help:

* track deliveries
* analyze travel routes
* provide map services
* calculate distances

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how geocoding works
* how Python retrieves location data
* basics of GPS coordinates
* geographical distance calculation

---

# 🚀 Conclusion

The geopy library is a powerful tool for location-based applications.

It helps developers:

* work with maps
* calculate distances
* build GPS-enabled systems

Learning geopy is useful for:

* map applications
* travel systems
* logistics platforms
* analytics projects

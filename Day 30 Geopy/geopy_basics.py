from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# --- initialize geolocator ---
geolocator = Nominatim(user_agent="geo_app")

# --- get location coordinates ---
location = geolocator.geocode("Hyderabad")

print("Location:", location.address)

print("Latitude:", location.latitude)

print("Longitude:", location.longitude)

# --- calculate distance between two places ---
hyderabad = (17.3850, 78.4867)

delhi = (28.7041, 77.1025)

distance = geodesic(hyderabad, delhi).km

print("\nDistance Between Hyderabad and Delhi:")

print(round(distance, 2), "KM")
import requests
import ipapi
import folium
import webbrowser
import os

def get_geolocation():
    try:
        ip_address = requests.get("https://api64.ipify.org?format=json").json()["ip"]

        ip_location = ipapi.location(ip=ip_address, key=None)

        if not ip_location or "error" in ip_location:
            raise Exception("Failed to fetch geolocation data.")

        return {
            "ip": ip_address,
            "latitude": ip_location.get("latitude"),
            "longitude": ip_location.get("longitude"),
            "city": ip_location.get("city"),
            "region": ip_location.get("region"),
            "country": ip_location.get("country_name"),
        }
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Error fetching geolocation data: {e}")
    return None

def display_map(latitude, longitude):
    if latitude is None or longitude is None:
        print("Invalid or Coordinates are None")
        return

    geolocation_map = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup="Your Location").add_to(geolocation_map)
    map_file = "geolocation_map.html"
    geolocation_map.save(map_file)
    print("Map saved as 'geolocation_map.html'.")
    webbrowser.open(f"file://{os.path.realpath(map_file)}")

def main():
    geolocation = get_geolocation()

    if geolocation:
        print(f"IP Address: {geolocation['ip']}")
        print(f"City: {geolocation['city']}, Region: {geolocation['region']}, Country: {geolocation['country']}")
        print(f"Coordinates: {geolocation['latitude']}, {geolocation['longitude']}")
        display_map(geolocation["latitude"], geolocation["longitude"])
    else:
        print("Sorry, could not retrieve geolocation data.")

if __name__ == "__main__":
    main()

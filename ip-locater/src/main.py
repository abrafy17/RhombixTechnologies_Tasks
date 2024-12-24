import requests
import folium
from geopy.geocoders import Nominatim

def get_geolocation():
    try:
        ip_request = requests.get("https://api64.ipify.org?format=json")
        ip_address = ip_request.json()["ip"]
        
        location_request = requests.get(f"https://ipapi.co/{ip_address}/json/")
        location_data = location_request.json()
        if location_request.status_code != 200 or "error" in location_data:
            raise Exception("Unable to fetch geolocation data.")
        
        return {
            "ip": ip_address,
            "latitude" : location_data.get('latitude'),
            "longitude" : location_data.get('longitude'),
            "city" : location_data.get('city'),
            "region" : location_data.get('region'),
            "country" : location_data.get('country_name'),
        }
    except Exception as e:
        print(f"Error {e}")
        return None
    
def display_map(latitude, longitude):
    geolocation_map = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup="Your Location").add_to(geolocation_map)
    geolocation_map.save("geolocation_map.html")
    print(f"Map has been saved.")
    
def main():
    geolocation = get_geolocation()
    if geolocation:
        print(f"IP Address: {geolocation['ip']}") #TODO: Show other infomation
        print(f"City: {geolocation['city']}, Region: {geolocation['region']}, Country: {geolocation['country_name']}")
        print(f"Coordinates: {geolocation['latitude']}, {geolocation['longitude']}")
        
        display_map(geolocation['latitude'], geolocation['longitude'])
        
    else:
        print("Sorry, Could not retrive geolocation data.")
        
if __name__ == "__main__":
    main()
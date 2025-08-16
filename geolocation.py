import requests

def get_user_location():
    try:
        # Using ip-api.com (free service with no API key required for basic usage)
        response = requests.get('http://ip-api.com/json/')
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return data['lat'], data['lon']
        # Fall back to default coordinates if any issues
        print("Could not detect location. Using default coordinates.")
        return 52.52, 13.41
    except Exception as e:
        print(f"Error detecting location: {e}. Using default coordinates.")
        return 52.52, 13.41
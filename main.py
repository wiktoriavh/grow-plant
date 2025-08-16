from weather import hourly_dataframe
import time

keys = {
   "temperature": "temperature_2m",
   "cloud_cover": "cloud_cover",
   "soil_moisture": "soil_moisture_3_to_9cm",
   "soil_temperature": "soil_temperature_6cm",
   "showers": "showers",
   "wind_gusts": "wind_gusts_10m"
}

plant_leaves = 0

def evaluate_temperature(temp):
    if temp > 30:
        return -3
    elif temp > 15:
        return 1
    elif temp < 8:
        return -1
    else:
        return 0

def evaluate_clouds(cover):
    if cover < 40:
        return 2
    elif cover < 70:
        return 1
    else:
        return 0

def evaluate_soil_moisture(moisture):
    if moisture < 0.2:
        return -1
    elif 0.2 <= moisture < 0.4:
        return 1
    elif 0.4 <= moisture < 0.6:
        return 2
    else:
        return -2
    
def evaluate_soil_temperature(temp):
    if 18 <= temp < 24:
        return 2
    elif temp > 30:
        return -2
    elif temp < 10:
        return -3
    else:
      return 0
    
def evaluate_shower(shower):
    if shower > 0.2:
        return -4
    else:
        return 0

def evaluate_wind(gust):
    if gust > 50:
        return -5
    elif gust > 30:
        return -2
    else:
        return 0

print("Plant is growing...")

for index, row in hourly_dataframe.iterrows():
    metrics = row.to_dict()
    date = metrics.pop("date")
    plant_leaves += evaluate_temperature(metrics[keys["temperature"]])
    plant_leaves += evaluate_clouds(metrics[keys["cloud_cover"]])
    plant_leaves += evaluate_soil_moisture(metrics[keys["soil_moisture"]])
    plant_leaves += evaluate_soil_temperature(metrics[keys["soil_temperature"]])
    plant_leaves += evaluate_shower(metrics[keys["showers"]])
    plant_leaves += evaluate_wind(metrics[keys["wind_gusts"]])

    day = index // 24 + 1
    hour = index % 24
    print(f"\rDay: {day} Hour: {hour} | Leaves: {plant_leaves}", end="")
    time.sleep(0.1)


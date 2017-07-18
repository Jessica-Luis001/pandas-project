import pandas

data = pandas.read_csv("weather_year.csv")
print(data)

china = len(data)
print(china)

forest = data.columns
print(forest)

slides = data["EDT"]
print(slides)

giant = data[["EDT", "Mean TemperatureF"]]
print(giant)

cuddly = data.EDT
print(cuddly)

place = data.EDT.head()
print(place)

sky = data.EDT.head(10)
print(sky)

word = data["Mean TemperatureF"].head()
print(word)

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]
print(data)

jason = data.mean_temp.head()
print(jason)

july = data.mean_temp.std()
print(july)

data.mean_temp.hist()
print(data)

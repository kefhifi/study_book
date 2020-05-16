def city_country(city,country,population=""):
    if population:
        return (city + " " + country).title()+ " - " + "population " + population
    else:
        return (city + " " + country).title()

def city_country_1(city,country,population=0):
    if population:
        return (city + " " + country).title()+ " - " + "population " + str(population)
    else:
        return (city + " " + country).title()

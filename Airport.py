class Airport:
    def __init__(self, code, name, city, country, lat, lon, rate) -> None:
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.lat = float(lat)
        self.lon = float(lon)
        self.rate = float(rate)

    def __repr__(self) -> str:
        return f"Airport name: {self.name} in: {self.country} lat: {self.lat} lon: {self.lon} rate: {self.rate}"
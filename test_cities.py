import unittest
from city_function import city_country,city_country_1
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country("santiago","chile"),"Santiago Chile")
    def test_city_country_1(self):
        self.assertEqual(city_country_1("santiago","chile"),"Santiago Chile")
    def test_city_country_population(self):
        self.assertEqual(city_country("santiago", "chile", "5000000"), "Santiago Chile - population 5000000")
    def test_city_country_population_1(self):
        self.assertEqual(city_country_1("santiago", "chile", 5000000), "Santiago Chile - population 5000000")

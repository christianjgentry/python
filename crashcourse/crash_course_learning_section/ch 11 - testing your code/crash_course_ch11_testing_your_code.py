import unittest
from city_countrys import city_country

class DefTests(unittest.TestCase):

	def test_city_countrys(self):
		#does the city_test function work?
		formatted_city_country = city_country("tokyo", "japan")
		self.assertEqual(formatted_city_country, "Tokyo, Japan")

unittest.main() 

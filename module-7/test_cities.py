# Name: Brian Palm
# Date: 10/25/2026
# Assignment: Module 7.2 - Test Cases
# Description: Tests the city_country function using the unittest module.

import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Test that city_country returns the correct City, Country format."""
        formatted_city = city_country("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
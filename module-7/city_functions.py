# Name: Brian Palm
# Date: 10/25/2026
# Assignment: Module 7.2 - Test Cases
# Description: Formats city and country information with optional
# population and language values.

def city_country(city, country, population=None, language=None):
    """Return city and country information with optional population and language."""
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"


print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan", 14000000))
print(city_country("Paris", "France", 2100000, "French"))
from unittest.mock import patch, ANY

@patch('app.requests')
def test_weather_results(self, requests):
    requests.get().json.return_value = {
        'main': { 'temp': 60 }
    }
    result = self.app.get('/weather_results?city=San+Francisco')
    # ... do other verifications on result

    requests.get.assert_called_with(ANY, 
        params={'q': 'San Francisco', 'units': 'Imperial', 'appid': ANY})
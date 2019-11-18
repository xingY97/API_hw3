from app import app
from unittest import TestCase, main
from unittest.mock import patch, ANY



class AppTests(TestCase): 
    """Run tests on the Weather App."""
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 


        
@patch('app.requests')
def test_weather_results(self, requests):
    requests.get().json.return_value = {
        'main': { 'temp': 60 }
    }
    result = self.app.get('/weather_results?city=San+Francisco')
    self.assertEqual(result.status_code, 200)

    requests.get.assert_called_with(ANY, 
        params={'q': 'San Francisco', 'appid': ANY})

if __name__ == '__main__':
    main()
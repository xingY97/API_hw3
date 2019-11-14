def test_weather_results(self):
    result = self.app.get('/weather_results?city=San+Francisco')
    self.assertEqual(result.status_code, 200)

    page_content = result.get_data(as_text=True)
    self.assertIn('It is now 60 degrees Fahrenheit', page_content)
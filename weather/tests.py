from django.test import TestCase, Client
from django.urls import reverse

class WeatherTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_weather_page(self):
        response = self.client.get(reverse('get_weather'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/index.html')

    def test_post_weather_success(self):
        response = self.client.post(reverse('get_weather'), {'city': 'London'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'City')
        self.assertContains(response, 'Temperature')
        self.assertContains(response, 'Humidity')
        self.assertContains(response, 'Wind Speed')
        self.assertContains(response, 'Condition')

    def test_post_weather_empty_city(self):
        response = self.client.post(reverse('get_weather'), {'city': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'City name cannot be empty.')

    def test_post_weather_city_not_found(self):
        response = self.client.post(reverse('get_weather'), {'city': 'InvalidCity'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'City not found.')


# Create your tests here.

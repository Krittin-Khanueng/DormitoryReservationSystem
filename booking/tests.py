from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class TestBooking(TestCase):
	def test_booking_page_view(self):
		response = self.client.get(reverse('booking:booking_page'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'booking/booking_page.html')
		self.assertContains(response, 'Booking')
		self.assertContains(response, 'Booking form')

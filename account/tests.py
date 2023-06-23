from django.test import TestCase

from doctor.models import Doctor


class DoctorTestCase(TestCase):

    def test_animals_can_speak(self):
        expertise = Doctor.objects.get(title="متخصص پوست")
        doctor = Doctor.objects.get(expertise=expertise)
        self.assertEqual(doctor.get_fullname(), 'علی علی زاده', 'full name doesnt match!')
        self.assertTrue(doctor.get_first_visit(), 'doctor does not have an empty visit!')

from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
    def test_bad(self):
        self.assertEqual(1, 2, "bad math")
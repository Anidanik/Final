from django.test import TestCase
from main.models import *


class PublisherTest(TestCase):
    def setUp(self):
        Publisher.objects.create(
        publisher= 'asd',
        count = 2,
        )

    def test_name(self):
        publisher = Publisher.objects.first()

        self.assertEqual(publisher.publisher, 'asd')
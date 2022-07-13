import uuid
from django.test import Client, TestCase

from dolphin import views, models, serializers
from monitor import main


class ClusterManagementTestCase(TestCase):
    def setUp(self):
        self.request_client = Client()

    def test_add_log(self):
        pass

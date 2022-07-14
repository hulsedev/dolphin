import uuid
import json
from django.test import Client, TestCase

from dolphin import views, models, serializers
from monitor import main


class LogTestCase(TestCase):
    def setUp(self):
        self.request_client = Client()

    def test_add_log(self):
        data = main.get_telemetry()
        resp = self.request_client.post(
            "/log/", data=data, content_type="application/json"
        )
        self.assertEqual(resp.status_code, 200)

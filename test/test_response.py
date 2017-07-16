import io

import django
from django.conf import settings
from django.test.client import RequestFactory
from django.test.testcases import TestCase

from ranged_fileresponse import RangedFileResponse


settings.configure( DEBUG=True)
django.setup()

class testResponse(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_ok(self):
        request = self.factory.get(
            '/customer/details', HTTP_RANGE='bytes=512-1023'
        )
        回應 = RangedFileResponse(
            request, io.BytesIO(b'sui2' * 512), content_type='audio/wav'
        )
        self.assertEqual(回應.body, b'sui2' * 128)

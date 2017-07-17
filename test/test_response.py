import io

from django.test.client import RequestFactory
from django.test.testcases import TestCase

from ranged_fileresponse import RangedFileResponse


class testResponse(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_begin(self):
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=0-3'
        )
        回應 = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertContent(回應, b'sui2')

    def test_middle(self):
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=4-9'
        )
        回應 = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertContent(回應, b'khiau2')

    def test_end(self):
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=10-16'
        )
        回應 = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertContent(回應, b'tsiang5')

    def assertContent(self, response, except_response):
        self.assertEqual(list(response.streaming_content)[0], except_response)

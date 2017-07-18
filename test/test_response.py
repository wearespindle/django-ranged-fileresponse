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

    def test_failing(self):
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=17-20'
        )
        回應 = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertEqual(回應.status_code, 416)

    def test_overlapping(self):
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=10-20'
        )
        回應 = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertContent(回應, 'khiau2')

    def assertContent(self, response, except_response):
        self.assertEqual(list(response.streaming_content)[0], except_response)

import io

from django.test.client import RequestFactory
from django.test.testcases import TestCase

from ranged_fileresponse import RangedFileResponse


class ResponseTestCase(TestCase):

    def setUp(self):
        """
        Setup a request factory.
        """
        self.factory = RequestFactory()

    def test_begin(self):
        """
        Test requesting the first bytes.
        """
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=0-3'
        )
        response = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertContent(response, b'sui2')

    def test_middle(self):
        """
        Test requesting bytes in the middle.
        """
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=4-9'
        )
        response = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertContent(response, b'khiau2')

    def test_end(self):
        """
        Test requesting the last bytes.
        """
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=10-16'
        )
        response = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertContent(response, b'tsiang5')

    def test_failing(self):
        """
        Test requesting non existing bytes.
        """
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=17-20'
        )
        response = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertEqual(response.status_code, 416)

    def test_overlapping(self):
        """
        Test requesting to many bytes.
        """
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=10-20'
        )
        response = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertContent(response, b'tsiang5')

    def test_more_one_char(self):
        """
        Test requesting 1 bytes to many.
        """
        request = self.factory.get(
            '/path', HTTP_RANGE='bytes=10-17'
        )
        response = RangedFileResponse(
            request, io.BytesIO(b'sui2khiau2tsiang5'), content_type='audio/wav'
        )
        self.assertContent(response, b'tsiang5')

    def assertContent(self, response, expected_response):
        """
        Function to assert the content of the response to the expected value.

        Args:
            response (FileResponse): The response to check.
            expected_response (str): The string to be expected.
        """
        self.assertEqual(list(response.streaming_content)[0], expected_response)

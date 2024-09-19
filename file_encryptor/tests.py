import os
        
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

class FileUploadTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('upload_and_encrypt')  # Adjust if your URL name is different

    def test_file_upload_and_encryption(self):
        # Prepare a file to upload
        file_content = b'This is a test file content.'
        
        #Added sample file from my local machine to test the scenario
        test_file = SimpleUploadedFile("Desktop/password.txt", file_content, content_type="text/plain")

        # Perform the POST request
        response = self.client.post(self.url, {'file': test_file}, format='multipart')
        # Check if the response is successful
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        

        # Check if the response contains necessary keys
        self.assertIn('message', response_data['data'])
        self.assertIn('encryption_key', response_data['data'])
        self.assertIn('file_path', response_data['data'])

        # Verify the message content
        self.assertEqual(response_data['data']['message'], 'File uploaded and encrypted successfully')

        # Verify if the encrypted file is saved
        file_path = os.path.basename(response_data['data']['file_path'])
        self.assertTrue(file_path.startswith('encrypted_'))

        # Clean up: remove the encrypted file after test
        if os.path.exists(file_path):
            os.remove(file_path)

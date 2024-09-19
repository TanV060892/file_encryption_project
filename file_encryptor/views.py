import os

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from cryptography.fernet import Fernet
from django.conf import settings
from django.views.decorators.http import require_GET

@require_GET
def health_check(request):
    return JsonResponse({'status':True,'data':{
        'health': 'Ok',
        'message': 'Server is up and running'
    }}, status=200)


'''
 * Takes file as input encrypts it using Fernet and save it on server
 * @route POST /api/upload/
 * @returns JSON Object 200 - Ok
 * @returns JSON Object 400 - File Not Uploaded
 * @returns JSON Object 500 - Internal server error
'''

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_and_encrypt_file(request):
    if 'file' not in request.FILES:
        # Return an error response, but without attempting to include the 'request' object
        return JsonResponse({'status':False,'error': {'code':'OTZ400','message':'No file uploaded'}}, status=400)

    file = request.FILES['file']
    
    # Generate a new encryption key
    encryption_key = Fernet.generate_key()
    cipher = Fernet(encryption_key)
    
    # Read file contents
    file_data = file.read()

    # Encrypt the file data
    encrypted_data = cipher.encrypt(file_data)
    
    # Save the encrypted file to the filesystem
    file_path = os.path.join(settings.MEDIA_ROOT, f'encrypted_{file.name}')
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    # Return the encryption key and file path
    return JsonResponse({'status':True,'data':{
        'message': 'File uploaded and encrypted successfully',
        'encryption_key': encryption_key.decode(),
        'file_path': file_path
    }})


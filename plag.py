import os
from dotenv import load_dotenv

import base64
import random

from PyPDF2 import PdfReader

from copyleaks.copyleaks import Copyleaks
from copyleaks.exceptions.command_error import CommandError
from copyleaks.models.submit.document import FileDocument, UrlDocument, OcrFileDocument
from copyleaks.models.submit.properties.scan_properties import ScanProperties
from copyleaks.models.export import *

load_dotenv()

COPYLEAKS_API_KEY = os.getenv('COPYLEAKS_API_KEY')
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')

try:
    auth_token = Copyleaks.login(EMAIL_ADDRESS, COPYLEAKS_API_KEY)
except CommandError as ce:
    response = ce.get_response()
    print(f"An error occurred (HTTP status code {response.status_code}):")
    print(response.content)

print("Logged successfully!\n")



# This example is going to scan a FILE for plagiarism.
# Alternatively, you can scan a URL using the class `UrlDocument`.

with open('/home/mohak/Downloads/Copy of AI_Experiment03.pdf', 'rb') as pdf_file:
    pdf_binary_data = pdf_file.read()

    pdf_reader = PdfReader(pdf_file)
    page = pdf_reader.pages[1]
    page_content = page.extract_text().encode('utf-8')

print("Submitting a new file...")
BASE64_FILE_CONTENT = base64.b64encode(page_content).decode('utf8')  # or read your file and convert it into BASE64 presentation.
FILENAME = "Copy of AI_Experiment03.pdf"
scan_id = random.randint(100, 100000)  # generate a random scan id
file_submission = FileDocument(BASE64_FILE_CONTENT, FILENAME)

# Once the scan completed on Copyleaks servers, we will trigger a webhook that notify you.
# Write your public endpoint server address. If you testing it locally, make sure that this endpoint
# is publicly available.

#CHANGE TO NGROK URL
scan_properties = ScanProperties('https://8350-150-242-205-198.ngrok-free.app/copyleaks/{STATUS}')

#VERY IMPORTANT
scan_properties.set_sandbox(True)  # Turn on sandbox mode. Turn off on production.

scan_properties.set_action(1)


file_submission.set_properties(scan_properties)
Copyleaks.submit_file(auth_token, scan_id, file_submission)  # sending the submission to scanning
print("Send to scanning")
print("You will notify, using your webhook, once the scan was completed.")

# Wait for completion webhook arrival...
# Read more: https://api.copyleaks.com/documentation/v3/webhooks
"""
Question 5
Given the following JSON document:
    ./data.json
• Read in the document from a file
• Find and print:
    o The Payee ID value
    o Any invoices that contain the text “583”
• Change any date/time fields to text in the format ‘%Y-%m-%dT%H:%M:%S’
    o Hint: The format of the date/time fields are integer timestamp. To
    create a datetime object from an integer timestamp, use the following:
    datetime_obj = datetime.datetime.fromtimestamp(integer_timestamp / 1e3)
• Write the json document back out to a new file
    ./output.json
"""

import os

from src.json_helpers import JsonReader, JsonWriter
from src.schemas import Claim
from src.services import ClaimService

file_path = os.path.dirname(__file__) + "/data.json"
reader = JsonReader(file_path)
json_content = reader.read()
claim = Claim(**json_content)  # Validate JSON contract and parse datetime fileds

print(f"Payee ID: {claim.payee.id}")

invoices_containg_583 = ClaimService.find_invoices_containing_583(claim)
print(f"Invoices containing '583': {invoices_containg_583}")

output_file_path = os.path.dirname(__file__) + "/output.json"
JsonWriter(output_file_path).write(claim.model_dump())

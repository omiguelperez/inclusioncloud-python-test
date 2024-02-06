import json

import pytest
from pydantic import BaseModel

from src.json_helpers import JsonReader, JsonWriter
from src.schemas import Claim
from src.services import ClaimService


@pytest.fixture
def input_json_file(tmpdir):
    input_data = {
        "claimId": "99999-100000",
        "payee": {"id": 9999, "role": "Payee"},
        "claimDateTime": 1634860244000,
        "invoiceCount": 7,
        "status": "LoadComplete",
        "invoiceIds": [
            "XXA15839",
            "XXA25829",
            "XXA35832",
            "XXA45830",
            "XXA55831",
            "XXA65833",
            "XXA75834",
        ],
        "jobNumber": 100000,
        "fileName": "XXXXXX20211021235044.xml",
        "fileId": 99999,
        "fileDateTime": 1634860244000,
        "receivedDateTime": 1634922275533,
        "process": "TRANSACT",
        "transmitterId": "XXX",
        "retailerId": "RETAILERID",
        "plantName": "XXX1",
        "totalStoreCount": 2,
        "totalOfferCount": 21,
        "totalRecordCount": 27,
        "totalCouponCount": 166,
        "totalFaceValueAmount": 445.58,
    }

    input_file_path = str(tmpdir.join("input.json"))
    with open(input_file_path, "w") as input_file:
        json.dump(input_data, input_file)

    return input_file_path


@pytest.fixture
def output_json_file(tmpdir):
    return str(tmpdir.join("output.json"))


def test_integration(input_json_file: str, output_json_file: str):
    reader = JsonReader(input_json_file)
    json_content = reader.read()
    claim = Claim(**json_content)  # Validate JSON contract and parse datetime fields

    # Test the claim Payee ID
    assert claim.payee.id == 9999

    # Test find invoices containing '583'
    invoices_containing_583 = ClaimService.find_invoices_containing_583(claim)
    assert invoices_containing_583 == [
        "XXA15839",
        "XXA35832",
        "XXA45830",
        "XXA55831",
        "XXA65833",
        "XXA75834",
    ]

    # Write the claim to the output JSON file
    writer = JsonWriter(output_json_file)
    writer.write(claim.model_dump())

    # Verify the content of the output JSON file
    with open(output_json_file, "r") as output_file:
        output_content = json.load(output_file)
    assert output_content == {
        "claimId": "99999-100000",
        "payee": {"id": 9999, "role": "Payee"},
        "invoiceCount": 7,
        "status": "LoadComplete",
        "invoiceIds": [
            "XXA15839",
            "XXA25829",
            "XXA35832",
            "XXA45830",
            "XXA55831",
            "XXA65833",
            "XXA75834",
        ],
        "jobNumber": 100000,
        "fileName": "XXXXXX20211021235044.xml",
        "fileId": 99999,
        "process": "TRANSACT",
        "transmitterId": "XXX",
        "retailerId": "RETAILERID",
        "plantName": "XXX1",
        "totalStoreCount": 2,
        "totalOfferCount": 21,
        "totalRecordCount": 27,
        "totalCouponCount": 166,
        "totalFaceValueAmount": 445.58,
        "claimDateTime": "2021-10-21T18:50:44",
        "fileDateTime": "2021-10-21T18:50:44",
        "receivedDateTime": "2021-10-22T12:04:35",
    }

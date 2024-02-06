import pytest
from pydantic import ValidationError

from src.schemas import Claim

payload = {
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


def test_claim_valid_payload():
    claim = Claim(**payload)
    assert claim.claimId == "99999-100000"
    assert claim.payee.id == 9999
    assert claim.claimDateTime == "2021-10-21T18:50:44"


def test_claim_invalid_payload():
    invalid_payload = payload.copy()
    del invalid_payload["claimId"]

    with pytest.raises(ValidationError):
        Claim(**invalid_payload)


def test_claim_datetime_conversion():
    timestamp = 1634860244000
    converted_datetime = Claim.parse_datetime(timestamp)
    assert converted_datetime == "2021-10-21T18:50:44"


def test_claim_datetime_invalid_input():
    with pytest.raises(ValueError) as exc_info:
        invalid_timestamp = "invalid_timestamp"
        Claim.parse_datetime(invalid_timestamp)
    assert str(exc_info.value) == "value must be a timestamp"

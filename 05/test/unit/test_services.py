import pytest

from src.schemas import Claim
from src.services import ClaimService


@pytest.fixture
def sample_claim():
    json_data = {
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
    return Claim(**json_data)


def test_find_invoices_containing_583_with_matching_invoices(sample_claim):
    result = ClaimService.find_invoices_containing_583(sample_claim)
    assert isinstance(result, list)
    assert result == [
        "XXA15839",
        "XXA35832",
        "XXA45830",
        "XXA55831",
        "XXA65833",
        "XXA75834",
    ]


def test_find_invoices_containing_583_with_no_matching_invoices(sample_claim: Claim):
    sample_claim.invoiceIds = ["123456", "789000"]
    result = ClaimService.find_invoices_containing_583(sample_claim)
    assert isinstance(result, list)
    assert result == []


def test_find_invoices_containing_583_with_empty_invoice_ids(sample_claim: Claim):
    sample_claim.invoiceIds = []
    result = ClaimService.find_invoices_containing_583(sample_claim)
    assert isinstance(result, list)
    assert result == []

from datetime import datetime

from pydantic import BaseModel, field_validator


class Payee(BaseModel):
    id: int
    role: str


class Claim(BaseModel):
    claimId: str
    payee: Payee
    invoiceCount: int
    status: str
    invoiceIds: list[str]
    jobNumber: int
    fileName: str
    fileId: int
    process: str
    transmitterId: str
    retailerId: str
    plantName: str
    totalStoreCount: int
    totalOfferCount: int
    totalRecordCount: int
    totalCouponCount: int
    totalFaceValueAmount: float
    claimDateTime: str
    fileDateTime: str
    receivedDateTime: str

    @field_validator("claimDateTime", "fileDateTime", "receivedDateTime", mode="before")
    @classmethod
    def parse_datetime(cls, value: int) -> str:
        if type(value) is not int:
            raise ValueError("value must be a timestamp")
        return datetime.fromtimestamp(value / 1e3).strftime("%Y-%m-%dT%H:%M:%S")

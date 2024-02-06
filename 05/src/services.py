from src.schemas import Claim


class ClaimService:
    @classmethod
    def find_invoices_containing_583(cls, claim: Claim) -> list[str]:
        return [invoice for invoice in claim.invoiceIds if "583" in invoice]

# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse"]


class LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse(BaseModel):
    filename: Optional[str] = None
    """Name of LOA document."""
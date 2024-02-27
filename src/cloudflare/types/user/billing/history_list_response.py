# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["HistoryListResponse", "Zone"]


class Zone(BaseModel):
    name: Optional[object] = None


class HistoryListResponse(BaseModel):
    id: str
    """Billing item identifier tag."""

    action: str
    """The billing item action."""

    amount: float
    """The amount associated with this billing item."""

    currency: str
    """The monetary unit in which pricing information is displayed."""

    description: str
    """The billing item description."""

    occurred_at: datetime
    """When the billing item was created."""

    type: str
    """The billing item type."""

    zone: Zone
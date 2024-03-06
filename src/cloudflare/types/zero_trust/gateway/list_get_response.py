# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ListGetResponse"]


class ListGetResponse(BaseModel):
    id: Optional[str] = None
    """API Resource UUID tag."""

    count: Optional[float] = None
    """The number of items in the list."""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the list."""

    name: Optional[str] = None
    """The name of the list."""

    type: Optional[Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]] = None
    """The type of list."""

    updated_at: Optional[datetime] = None
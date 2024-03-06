# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["PriorityQuotaResponse"]


class PriorityQuotaResponse(BaseModel):
    anniversary_date: Optional[datetime] = None
    """Anniversary date is when annual quota limit is refresh"""

    quarter_anniversary_date: Optional[datetime] = None
    """Quater anniversary date is when quota limit is refreshed each quarter"""

    quota: Optional[int] = None
    """Tokens for the quarter"""

    remaining: Optional[int] = None
    """Tokens remaining for the quarter"""
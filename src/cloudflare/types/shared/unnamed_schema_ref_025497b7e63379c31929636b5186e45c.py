# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef025497b7e63379c31929636b5186e45c"]


class UnnamedSchemaRef025497b7e63379c31929636b5186e45c(BaseModel):
    pools: Optional[Dict[str, str]] = None
    """Monitored pool IDs mapped to their respective names."""

    preview_id: Optional[str] = None
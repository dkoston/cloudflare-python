# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .shared import UnnamedSchemaRef70f2c6ccd8a405358ac7ef8fc3d6751c
from .._models import BaseModel

__all__ = ["BlockRule", "ActionParameters", "ActionParametersResponse"]


class ActionParametersResponse(BaseModel):
    content: str
    """The content to return."""

    content_type: str
    """The type of the content to return."""

    status_code: int
    """The status code to return."""


class ActionParameters(BaseModel):
    response: Optional[ActionParametersResponse] = None
    """The response to show when the block is applied."""


class BlockRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["block"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[ActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[UnnamedSchemaRef70f2c6ccd8a405358ac7ef8fc3d6751c] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""
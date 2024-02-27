# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.tunnels import ManagementCreateResponse, management_create_params

__all__ = ["Management", "AsyncManagement"]


class Management(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManagementWithRawResponse:
        return ManagementWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManagementWithStreamingResponse:
        return ManagementWithStreamingResponse(self)

    def create(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        resources: List[Literal["logs"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagementCreateResponse:
        """Gets a management token used to access the management resources (i.e.

        Streaming
        Logs) of a tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ManagementCreateResponse,
            self._post(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/management",
                body=maybe_transform({"resources": resources}, management_create_params.ManagementCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ManagementCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncManagement(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManagementWithRawResponse:
        return AsyncManagementWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManagementWithStreamingResponse:
        return AsyncManagementWithStreamingResponse(self)

    async def create(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        resources: List[Literal["logs"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagementCreateResponse:
        """Gets a management token used to access the management resources (i.e.

        Streaming
        Logs) of a tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ManagementCreateResponse,
            await self._post(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/management",
                body=maybe_transform({"resources": resources}, management_create_params.ManagementCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ManagementCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ManagementWithRawResponse:
    def __init__(self, management: Management) -> None:
        self._management = management

        self.create = to_raw_response_wrapper(
            management.create,
        )


class AsyncManagementWithRawResponse:
    def __init__(self, management: AsyncManagement) -> None:
        self._management = management

        self.create = async_to_raw_response_wrapper(
            management.create,
        )


class ManagementWithStreamingResponse:
    def __init__(self, management: Management) -> None:
        self._management = management

        self.create = to_streamed_response_wrapper(
            management.create,
        )


class AsyncManagementWithStreamingResponse:
    def __init__(self, management: AsyncManagement) -> None:
        self._management = management

        self.create = async_to_streamed_response_wrapper(
            management.create,
        )
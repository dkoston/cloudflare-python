# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...types.access import (
    ServiceTokenListResponse,
    ServiceTokenCreateResponse,
    ServiceTokenDeleteResponse,
    ServiceTokenRotateResponse,
    ServiceTokenUpdateResponse,
    ServiceTokenRefreshResponse,
    service_token_create_params,
    service_token_update_params,
)

__all__ = ["ServiceTokens", "AsyncServiceTokens"]


class ServiceTokens(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceTokensWithRawResponse:
        return ServiceTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceTokensWithStreamingResponse:
        return ServiceTokensWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        zone_id: str,
        name: str,
        duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenCreateResponse:
        """Generates a new service token.

        **Note:** This is the only time you can get the
        Client Secret. If you lose the Client Secret, you will have to rotate the Client
        Secret or create a new service token.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          name: The name of the service token.

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/{account_id}/{zone_id}/access/service_tokens",
            body=maybe_transform(
                {
                    "name": name,
                    "duration": duration,
                },
                service_token_create_params.ServiceTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenCreateResponse], ResultWrapper[ServiceTokenCreateResponse]),
        )

    def update(
        self,
        uuid: str,
        *,
        account_id: str,
        zone_id: str,
        duration: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenUpdateResponse:
        """
        Updates a configured service token.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          uuid: UUID

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          name: The name of the service token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/{account_id}/{zone_id}/access/service_tokens/{uuid}",
            body=maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                },
                service_token_update_params.ServiceTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenUpdateResponse], ResultWrapper[ServiceTokenUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceTokenListResponse]:
        """
        Lists all service tokens.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/{account_id}/{zone_id}/access/service_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceTokenListResponse]], ResultWrapper[ServiceTokenListResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        account_id: str,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenDeleteResponse:
        """
        Deletes a service token.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/{account_id}/{zone_id}/access/service_tokens/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenDeleteResponse], ResultWrapper[ServiceTokenDeleteResponse]),
        )

    def refresh(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenRefreshResponse:
        """
        Refreshes the expiration of a service token.

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._post(
            f"/accounts/{identifier}/access/service_tokens/{uuid}/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenRefreshResponse], ResultWrapper[ServiceTokenRefreshResponse]),
        )

    def rotate(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenRotateResponse:
        """
        Generates a new Client Secret for a service token and revokes the old one.

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._post(
            f"/accounts/{identifier}/access/service_tokens/{uuid}/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenRotateResponse], ResultWrapper[ServiceTokenRotateResponse]),
        )


class AsyncServiceTokens(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceTokensWithRawResponse:
        return AsyncServiceTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceTokensWithStreamingResponse:
        return AsyncServiceTokensWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        zone_id: str,
        name: str,
        duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenCreateResponse:
        """Generates a new service token.

        **Note:** This is the only time you can get the
        Client Secret. If you lose the Client Secret, you will have to rotate the Client
        Secret or create a new service token.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          name: The name of the service token.

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/{account_id}/{zone_id}/access/service_tokens",
            body=maybe_transform(
                {
                    "name": name,
                    "duration": duration,
                },
                service_token_create_params.ServiceTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenCreateResponse], ResultWrapper[ServiceTokenCreateResponse]),
        )

    async def update(
        self,
        uuid: str,
        *,
        account_id: str,
        zone_id: str,
        duration: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenUpdateResponse:
        """
        Updates a configured service token.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          uuid: UUID

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          name: The name of the service token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/{account_id}/{zone_id}/access/service_tokens/{uuid}",
            body=maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                },
                service_token_update_params.ServiceTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenUpdateResponse], ResultWrapper[ServiceTokenUpdateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceTokenListResponse]:
        """
        Lists all service tokens.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/{account_id}/{zone_id}/access/service_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceTokenListResponse]], ResultWrapper[ServiceTokenListResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        account_id: str,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenDeleteResponse:
        """
        Deletes a service token.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/{account_id}/{zone_id}/access/service_tokens/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenDeleteResponse], ResultWrapper[ServiceTokenDeleteResponse]),
        )

    async def refresh(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenRefreshResponse:
        """
        Refreshes the expiration of a service token.

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._post(
            f"/accounts/{identifier}/access/service_tokens/{uuid}/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenRefreshResponse], ResultWrapper[ServiceTokenRefreshResponse]),
        )

    async def rotate(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenRotateResponse:
        """
        Generates a new Client Secret for a service token and revokes the old one.

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._post(
            f"/accounts/{identifier}/access/service_tokens/{uuid}/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenRotateResponse], ResultWrapper[ServiceTokenRotateResponse]),
        )


class ServiceTokensWithRawResponse:
    def __init__(self, service_tokens: ServiceTokens) -> None:
        self._service_tokens = service_tokens

        self.create = to_raw_response_wrapper(
            service_tokens.create,
        )
        self.update = to_raw_response_wrapper(
            service_tokens.update,
        )
        self.list = to_raw_response_wrapper(
            service_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            service_tokens.delete,
        )
        self.refresh = to_raw_response_wrapper(
            service_tokens.refresh,
        )
        self.rotate = to_raw_response_wrapper(
            service_tokens.rotate,
        )


class AsyncServiceTokensWithRawResponse:
    def __init__(self, service_tokens: AsyncServiceTokens) -> None:
        self._service_tokens = service_tokens

        self.create = async_to_raw_response_wrapper(
            service_tokens.create,
        )
        self.update = async_to_raw_response_wrapper(
            service_tokens.update,
        )
        self.list = async_to_raw_response_wrapper(
            service_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            service_tokens.delete,
        )
        self.refresh = async_to_raw_response_wrapper(
            service_tokens.refresh,
        )
        self.rotate = async_to_raw_response_wrapper(
            service_tokens.rotate,
        )


class ServiceTokensWithStreamingResponse:
    def __init__(self, service_tokens: ServiceTokens) -> None:
        self._service_tokens = service_tokens

        self.create = to_streamed_response_wrapper(
            service_tokens.create,
        )
        self.update = to_streamed_response_wrapper(
            service_tokens.update,
        )
        self.list = to_streamed_response_wrapper(
            service_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            service_tokens.delete,
        )
        self.refresh = to_streamed_response_wrapper(
            service_tokens.refresh,
        )
        self.rotate = to_streamed_response_wrapper(
            service_tokens.rotate,
        )


class AsyncServiceTokensWithStreamingResponse:
    def __init__(self, service_tokens: AsyncServiceTokens) -> None:
        self._service_tokens = service_tokens

        self.create = async_to_streamed_response_wrapper(
            service_tokens.create,
        )
        self.update = async_to_streamed_response_wrapper(
            service_tokens.update,
        )
        self.list = async_to_streamed_response_wrapper(
            service_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            service_tokens.delete,
        )
        self.refresh = async_to_streamed_response_wrapper(
            service_tokens.refresh,
        )
        self.rotate = async_to_streamed_response_wrapper(
            service_tokens.rotate,
        )
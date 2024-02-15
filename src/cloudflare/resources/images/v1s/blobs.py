# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    async_to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    StreamedBinaryAPIResponse,
    async_to_custom_streamed_response_wrapper,
    AsyncStreamedBinaryAPIResponse,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper

__all__ = ["Blobs", "AsyncBlobs"]


class Blobs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlobsWithRawResponse:
        return BlobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlobsWithStreamingResponse:
        return BlobsWithStreamingResponse(self)

    def cloudflare_images_base_image(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Fetch base image.

        For most images this will be the originally uploaded file. For
        larger images it can be a near-lossless version of the original.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._get(
            f"/accounts/{account_id}/images/v1/{image_id}/blob",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncBlobs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlobsWithRawResponse:
        return AsyncBlobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlobsWithStreamingResponse:
        return AsyncBlobsWithStreamingResponse(self)

    async def cloudflare_images_base_image(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Fetch base image.

        For most images this will be the originally uploaded file. For
        larger images it can be a near-lossless version of the original.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._get(
            f"/accounts/{account_id}/images/v1/{image_id}/blob",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class BlobsWithRawResponse:
    def __init__(self, blobs: Blobs) -> None:
        self._blobs = blobs

        self.cloudflare_images_base_image = to_custom_raw_response_wrapper(
            blobs.cloudflare_images_base_image,
            BinaryAPIResponse,
        )


class AsyncBlobsWithRawResponse:
    def __init__(self, blobs: AsyncBlobs) -> None:
        self._blobs = blobs

        self.cloudflare_images_base_image = async_to_custom_raw_response_wrapper(
            blobs.cloudflare_images_base_image,
            AsyncBinaryAPIResponse,
        )


class BlobsWithStreamingResponse:
    def __init__(self, blobs: Blobs) -> None:
        self._blobs = blobs

        self.cloudflare_images_base_image = to_custom_streamed_response_wrapper(
            blobs.cloudflare_images_base_image,
            StreamedBinaryAPIResponse,
        )


class AsyncBlobsWithStreamingResponse:
    def __init__(self, blobs: AsyncBlobs) -> None:
        self._blobs = blobs

        self.cloudflare_images_base_image = async_to_custom_streamed_response_wrapper(
            blobs.cloudflare_images_base_image,
            AsyncStreamedBinaryAPIResponse,
        )

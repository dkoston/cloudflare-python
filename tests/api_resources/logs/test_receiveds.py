# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.logs import ReceivedReceivedGetLogsReceivedResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logs import received_received_get_logs_received_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReceiveds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_received_get_logs_received(self, client: Cloudflare) -> None:
        received = client.logs.receiveds.received_get_logs_received(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        )
        assert_matches_type(ReceivedReceivedGetLogsReceivedResponse, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_received_get_logs_received_with_all_params(self, client: Cloudflare) -> None:
        received = client.logs.receiveds.received_get_logs_received(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
            count=1,
            fields="ClientIP,RayID,EdgeStartTimestamp",
            sample=0.1,
            start="2018-05-20T10:00:00Z",
            timestamps="unixnano",
        )
        assert_matches_type(ReceivedReceivedGetLogsReceivedResponse, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_received_get_logs_received(self, client: Cloudflare) -> None:
        response = client.logs.receiveds.with_raw_response.received_get_logs_received(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        received = response.parse()
        assert_matches_type(ReceivedReceivedGetLogsReceivedResponse, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_received_get_logs_received(self, client: Cloudflare) -> None:
        with client.logs.receiveds.with_streaming_response.received_get_logs_received(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            received = response.parse()
            assert_matches_type(ReceivedReceivedGetLogsReceivedResponse, received, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_received_get_logs_received(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.logs.receiveds.with_raw_response.received_get_logs_received(
                "",
                end="2018-05-20T10:01:00Z",
            )


class TestAsyncReceiveds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_received_get_logs_received(self, async_client: AsyncCloudflare) -> None:
        received = await async_client.logs.receiveds.received_get_logs_received(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        )
        assert_matches_type(ReceivedReceivedGetLogsReceivedResponse, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_received_get_logs_received_with_all_params(self, async_client: AsyncCloudflare) -> None:
        received = await async_client.logs.receiveds.received_get_logs_received(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
            count=1,
            fields="ClientIP,RayID,EdgeStartTimestamp",
            sample=0.1,
            start="2018-05-20T10:00:00Z",
            timestamps="unixnano",
        )
        assert_matches_type(ReceivedReceivedGetLogsReceivedResponse, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_received_get_logs_received(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logs.receiveds.with_raw_response.received_get_logs_received(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        received = await response.parse()
        assert_matches_type(ReceivedReceivedGetLogsReceivedResponse, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_received_get_logs_received(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.receiveds.with_streaming_response.received_get_logs_received(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            received = await response.parse()
            assert_matches_type(ReceivedReceivedGetLogsReceivedResponse, received, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_received_get_logs_received(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.logs.receiveds.with_raw_response.received_get_logs_received(
                "",
                end="2018-05-20T10:01:00Z",
            )

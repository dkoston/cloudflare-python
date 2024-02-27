# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import BotManagementGetResponse, BotManagementUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBotManagement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        bot_management = client.bot_management.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BotManagementUpdateResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        bot_management = client.bot_management.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auto_update_model=True,
            enable_js=True,
            fight_mode=True,
            optimize_wordpress=True,
            sbfm_definitely_automated="allow",
            sbfm_likely_automated="allow",
            sbfm_static_resource_protection=True,
            sbfm_verified_bots="allow",
            suppress_session_score=False,
        )
        assert_matches_type(BotManagementUpdateResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.bot_management.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_management = response.parse()
        assert_matches_type(BotManagementUpdateResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.bot_management.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_management = response.parse()
            assert_matches_type(BotManagementUpdateResponse, bot_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.bot_management.with_raw_response.update(
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bot_management = client.bot_management.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BotManagementGetResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.bot_management.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_management = response.parse()
        assert_matches_type(BotManagementGetResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.bot_management.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_management = response.parse()
            assert_matches_type(BotManagementGetResponse, bot_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.bot_management.with_raw_response.get(
                zone_id="",
            )


class TestAsyncBotManagement:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        bot_management = await async_client.bot_management.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BotManagementUpdateResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bot_management = await async_client.bot_management.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auto_update_model=True,
            enable_js=True,
            fight_mode=True,
            optimize_wordpress=True,
            sbfm_definitely_automated="allow",
            sbfm_likely_automated="allow",
            sbfm_static_resource_protection=True,
            sbfm_verified_bots="allow",
            suppress_session_score=False,
        )
        assert_matches_type(BotManagementUpdateResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.bot_management.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_management = await response.parse()
        assert_matches_type(BotManagementUpdateResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.bot_management.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_management = await response.parse()
            assert_matches_type(BotManagementUpdateResponse, bot_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.bot_management.with_raw_response.update(
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bot_management = await async_client.bot_management.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BotManagementGetResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.bot_management.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_management = await response.parse()
        assert_matches_type(BotManagementGetResponse, bot_management, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.bot_management.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_management = await response.parse()
            assert_matches_type(BotManagementGetResponse, bot_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.bot_management.with_raw_response.get(
                zone_id="",
            )
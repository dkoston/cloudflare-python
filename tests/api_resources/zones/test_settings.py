# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zones import SettingEditResponse, SettingListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        setting = client.zones.settings.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="oneOf doesnt match")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            items=[
                {
                    "id": "always_online",
                    "value": "on",
                },
                {
                    "id": "browser_cache_ttl",
                    "value": 18000,
                },
                {
                    "id": "ip_geolocation",
                    "value": "off",
                },
            ],
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="oneOf doesnt match")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            items=[
                {
                    "id": "always_online",
                    "value": "on",
                },
                {
                    "id": "browser_cache_ttl",
                    "value": 18000,
                },
                {
                    "id": "ip_geolocation",
                    "value": "off",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="oneOf doesnt match")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            items=[
                {
                    "id": "always_online",
                    "value": "on",
                },
                {
                    "id": "browser_cache_ttl",
                    "value": 18000,
                },
                {
                    "id": "ip_geolocation",
                    "value": "off",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="oneOf doesnt match")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                zone_id="",
                items=[
                    {
                        "id": "always_online",
                        "value": "on",
                    },
                    {
                        "id": "browser_cache_ttl",
                        "value": 18000,
                    },
                    {
                        "id": "ip_geolocation",
                        "value": "off",
                    },
                ],
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="oneOf doesnt match")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            items=[
                {
                    "id": "always_online",
                    "value": "on",
                },
                {
                    "id": "browser_cache_ttl",
                    "value": 18000,
                },
                {
                    "id": "ip_geolocation",
                    "value": "off",
                },
            ],
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="oneOf doesnt match")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            items=[
                {
                    "id": "always_online",
                    "value": "on",
                },
                {
                    "id": "browser_cache_ttl",
                    "value": 18000,
                },
                {
                    "id": "ip_geolocation",
                    "value": "off",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="oneOf doesnt match")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            items=[
                {
                    "id": "always_online",
                    "value": "on",
                },
                {
                    "id": "browser_cache_ttl",
                    "value": 18000,
                },
                {
                    "id": "ip_geolocation",
                    "value": "off",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="oneOf doesnt match")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                zone_id="",
                items=[
                    {
                        "id": "always_online",
                        "value": "on",
                    },
                    {
                        "id": "browser_cache_ttl",
                        "value": 18000,
                    },
                    {
                        "id": "ip_geolocation",
                        "value": "off",
                    },
                ],
            )
# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.devices import (
    NetworkUpdateResponse,
    NetworkDeleteResponse,
    NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse,
    NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse,
    NetworkGetResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.devices import network_update_params
from cloudflare.types.devices import network_device_managed_networks_create_device_managed_network_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNetworks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        network = client.devices.networks.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[NetworkUpdateResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        network = client.devices.networks.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            config={
                "sha256": "b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c",
                "tls_sockaddr": "foo.bar:1234",
            },
            name="managed-network-1",
            type="tls",
        )
        assert_matches_type(Optional[NetworkUpdateResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.devices.networks.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(Optional[NetworkUpdateResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.devices.networks.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(Optional[NetworkUpdateResponse], network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.networks.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        network = client.devices.networks.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[NetworkDeleteResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.devices.networks.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(Optional[NetworkDeleteResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.devices.networks.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(Optional[NetworkDeleteResponse], network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.networks.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_device_managed_networks_create_device_managed_network(self, client: Cloudflare) -> None:
        network = client.devices.networks.device_managed_networks_create_device_managed_network(
            "699d98642c564d2e855e9661899b7252",
            config={"tls_sockaddr": "foo.bar:1234"},
            name="managed-network-1",
            type="tls",
        )
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_device_managed_networks_create_device_managed_network_with_all_params(
        self, client: Cloudflare
    ) -> None:
        network = client.devices.networks.device_managed_networks_create_device_managed_network(
            "699d98642c564d2e855e9661899b7252",
            config={
                "sha256": "b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c",
                "tls_sockaddr": "foo.bar:1234",
            },
            name="managed-network-1",
            type="tls",
        )
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_device_managed_networks_create_device_managed_network(self, client: Cloudflare) -> None:
        response = client.devices.networks.with_raw_response.device_managed_networks_create_device_managed_network(
            "699d98642c564d2e855e9661899b7252",
            config={"tls_sockaddr": "foo.bar:1234"},
            name="managed-network-1",
            type="tls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_device_managed_networks_create_device_managed_network(self, client: Cloudflare) -> None:
        with client.devices.networks.with_streaming_response.device_managed_networks_create_device_managed_network(
            "699d98642c564d2e855e9661899b7252",
            config={"tls_sockaddr": "foo.bar:1234"},
            name="managed-network-1",
            type="tls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(
                Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse], network, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_device_managed_networks_list_device_managed_networks(self, client: Cloudflare) -> None:
        network = client.devices.networks.device_managed_networks_list_device_managed_networks(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_device_managed_networks_list_device_managed_networks(self, client: Cloudflare) -> None:
        response = client.devices.networks.with_raw_response.device_managed_networks_list_device_managed_networks(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_device_managed_networks_list_device_managed_networks(self, client: Cloudflare) -> None:
        with client.devices.networks.with_streaming_response.device_managed_networks_list_device_managed_networks(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(
                Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse], network, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        network = client.devices.networks.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[NetworkGetResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.devices.networks.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(Optional[NetworkGetResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.devices.networks.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(Optional[NetworkGetResponse], network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.networks.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncNetworks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        network = await async_client.devices.networks.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[NetworkUpdateResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        network = await async_client.devices.networks.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            config={
                "sha256": "b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c",
                "tls_sockaddr": "foo.bar:1234",
            },
            name="managed-network-1",
            type="tls",
        )
        assert_matches_type(Optional[NetworkUpdateResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.networks.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(Optional[NetworkUpdateResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.networks.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(Optional[NetworkUpdateResponse], network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.networks.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        network = await async_client.devices.networks.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[NetworkDeleteResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.networks.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(Optional[NetworkDeleteResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.networks.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(Optional[NetworkDeleteResponse], network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.networks.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_managed_networks_create_device_managed_network(
        self, async_client: AsyncCloudflare
    ) -> None:
        network = await async_client.devices.networks.device_managed_networks_create_device_managed_network(
            "699d98642c564d2e855e9661899b7252",
            config={"tls_sockaddr": "foo.bar:1234"},
            name="managed-network-1",
            type="tls",
        )
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_managed_networks_create_device_managed_network_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        network = await async_client.devices.networks.device_managed_networks_create_device_managed_network(
            "699d98642c564d2e855e9661899b7252",
            config={
                "sha256": "b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c",
                "tls_sockaddr": "foo.bar:1234",
            },
            name="managed-network-1",
            type="tls",
        )
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_device_managed_networks_create_device_managed_network(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.devices.networks.with_raw_response.device_managed_networks_create_device_managed_network(
                "699d98642c564d2e855e9661899b7252",
                config={"tls_sockaddr": "foo.bar:1234"},
                name="managed-network-1",
                type="tls",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_device_managed_networks_create_device_managed_network(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.networks.with_streaming_response.device_managed_networks_create_device_managed_network(
            "699d98642c564d2e855e9661899b7252",
            config={"tls_sockaddr": "foo.bar:1234"},
            name="managed-network-1",
            type="tls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(
                Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse], network, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_managed_networks_list_device_managed_networks(
        self, async_client: AsyncCloudflare
    ) -> None:
        network = await async_client.devices.networks.device_managed_networks_list_device_managed_networks(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_device_managed_networks_list_device_managed_networks(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.devices.networks.with_raw_response.device_managed_networks_list_device_managed_networks(
                "699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(
            Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse], network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_device_managed_networks_list_device_managed_networks(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.networks.with_streaming_response.device_managed_networks_list_device_managed_networks(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(
                Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse], network, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        network = await async_client.devices.networks.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[NetworkGetResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.networks.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(Optional[NetworkGetResponse], network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.networks.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(Optional[NetworkGetResponse], network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.networks.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

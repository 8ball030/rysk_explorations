# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 eightballer
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the scaffold contract definition."""

from typing import Any

from aea.common import JSONLike
from aea.contracts.base import Contract
from aea.crypto.base import Address, LedgerApi

from rysk_client.packages.eightballer.contracts.opyn_option_registry import \
    PUBLIC_ID


class OpynOptionRegistry(Contract):  # pylint: disable=too-many-public-methods
    """The scaffold contract class for a smart contract."""

    contract_id = PUBLIC_ID

    @classmethod
    def get_raw_transaction(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> JSONLike:
        """
        Handler method for the 'GET_RAW_TRANSACTION' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        del ledger_api, contract_address, kwargs
        raise NotImplementedError

    @classmethod
    def get_raw_message(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> bytes:
        """
        Handler method for the 'GET_RAW_MESSAGE' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        del ledger_api, contract_address, kwargs
        raise NotImplementedError

    @classmethod
    def get_state(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> JSONLike:
        """
        Handler method for the 'GET_STATE' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        del ledger_api, contract_address, kwargs
        raise NotImplementedError

    @classmethod
    def address_book(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'address_book' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.addressBook().call()
        return {"address": result}

    @classmethod
    def authority(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'authority' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.authority().call()
        return {"address": result}

    @classmethod
    def call_lower_health_factor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'call_lower_health_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.callLowerHealthFactor().call()
        return {"int": result}

    @classmethod
    def call_upper_health_factor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'call_upper_health_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.callUpperHealthFactor().call()
        return {"int": result}

    @classmethod
    def check_vault_health(
        cls, ledger_api: LedgerApi, contract_address: str, vault_id: int
    ) -> JSONLike:
        """Handler method for the 'check_vault_health' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.checkVaultHealth(vault_id=vault_id).call()
        return {
            "isBelowMin": result,
            "isAboveMax": result,
            "healthFactor": result,
            "upperHealthFactor": result,
            "collatRequired": result,
            "collatAsset": result,
        }

    @classmethod
    def collateral_asset(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'collateral_asset' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.collateralAsset().call()
        return {"address": result}

    @classmethod
    def get_collateral(
        cls, ledger_api: LedgerApi, contract_address: str, series: tuple, amount: int
    ) -> JSONLike:
        """Handler method for the 'get_collateral' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getCollateral(series=series, amount=amount).call()
        return {"int": result}

    @classmethod
    def get_issuance_hash(
        cls, ledger_api: LedgerApi, contract_address: str, _series: tuple
    ) -> JSONLike:
        """Handler method for the 'get_issuance_hash' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getIssuanceHash(_series=_series).call()
        return {"str": result}

    @classmethod
    def get_otoken(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        underlying: Address,
        strike_asset: Address,
        expiration: int,
        is_put: bool,
        strike: int,
        collateral: Address,
    ) -> JSONLike:
        """Handler method for the 'get_otoken' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getOtoken(
            underlying=underlying,
            strike_asset=strike_asset,
            expiration=expiration,
            is_put=is_put,
            strike=strike,
            collateral=collateral,
        ).call()
        return {"address": result}

    @classmethod
    def get_series(
        cls, ledger_api: LedgerApi, contract_address: str, _series: tuple
    ) -> JSONLike:
        """Handler method for the 'get_series' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getSeries(_series=_series).call()
        return {"address": result}

    @classmethod
    def get_series_address(
        cls, ledger_api: LedgerApi, contract_address: str, issuance_hash: str
    ) -> JSONLike:
        """Handler method for the 'get_series_address' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getSeriesAddress(issuance_hash=issuance_hash).call()
        return {"address": result}

    @classmethod
    def get_series_info(
        cls, ledger_api: LedgerApi, contract_address: str, series: Address
    ) -> JSONLike:
        """Handler method for the 'get_series_info' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getSeriesInfo(series=series).call()
        return {"tuple": result}

    @classmethod
    def keeper(
        cls, ledger_api: LedgerApi, contract_address: str, var_0: Address
    ) -> JSONLike:
        """Handler method for the 'keeper' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.keeper(var_0).call()
        return {"bool": result}

    @classmethod
    def liquidity_pool(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'liquidity_pool' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.liquidityPool().call()
        return {"address": result}

    @classmethod
    def put_lower_health_factor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'put_lower_health_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.putLowerHealthFactor().call()
        return {"int": result}

    @classmethod
    def put_upper_health_factor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'put_upper_health_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.putUpperHealthFactor().call()
        return {"int": result}

    @classmethod
    def series_info(
        cls, ledger_api: LedgerApi, contract_address: str, var_0: Address
    ) -> JSONLike:
        """Handler method for the 'series_info' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.seriesInfo(var_0).call()
        return {
            "expiration": result,
            "strike": result,
            "is_put": result,
            "underlying": result,
            "strike_asset": result,
            "collateral": result,
        }

    @classmethod
    def vault_count(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'vault_count' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.vaultCount().call()
        return {"int": result}

    @classmethod
    def vault_ids(
        cls, ledger_api: LedgerApi, contract_address: str, var_0: Address
    ) -> JSONLike:
        """Handler method for the 'vault_ids' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.vault_ids(var_0).call()
        return {"int": result}

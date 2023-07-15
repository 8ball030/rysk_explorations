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

from rysk_client.packages.eightballer.contracts.option_exchange import \
    PUBLIC_ID


class OptionExchange(Contract):  # pylint: disable=too-many-public-methods
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
    def addressbook(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'addressbook' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.addressbook().call()
        return {"address": result}

    @classmethod
    def approved_collateral(
        cls, ledger_api: LedgerApi, contract_address: str, var_0: Address, var_1: bool
    ) -> JSONLike:
        """Handler method for the 'approved_collateral' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.approvedCollateral(var_0, var_1).call()
        return {"bool": result}

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
    def catalogue(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'catalogue' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.catalogue().call()
        return {"address": result}

    @classmethod
    def check_hash(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        option_series: tuple,
        strike_decimal_converted: int,
        is_sell: bool,
    ) -> JSONLike:
        """Handler method for the 'check_hash' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.checkHash(
            optionSeries=option_series,
            strikeDecimalConverted=strike_decimal_converted,
            isSell=is_sell,
        ).call()
        return {"oHash": result}

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
    def fee_recipient(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'fee_recipient' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.feeRecipient().call()
        return {"address": result}

    @classmethod
    def get_delta(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_delta' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getDelta().call()
        return {"delta": result}

    @classmethod
    def get_option_details(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        series_address: Address,
        option_series: tuple,
    ) -> JSONLike:
        """Handler method for the 'get_option_details' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getOptionDetails(
            seriesAddress=series_address, optionSeries=option_series
        ).call()
        return {"address": result, "tuple": result, "int": result}

    @classmethod
    def get_pool_denominated_value(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_pool_denominated_value' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getPoolDenominatedValue().call()
        return {"int": result}

    @classmethod
    def held_tokens(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        var_0: Address,
        var_1: Address,
    ) -> JSONLike:
        """Handler method for the 'held_tokens' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.heldTokens(var_0, var_1).call()
        return {"int": result}

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
    def max_trade_size(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'max_trade_size' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.maxTradeSize().call()
        return {"int": result}

    @classmethod
    def min_trade_size(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'min_trade_size' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.minTradeSize().call()
        return {"int": result}

    @classmethod
    def paused(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'paused' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.paused().call()
        return {"bool": result}

    @classmethod
    def pool_fees(
        cls, ledger_api: LedgerApi, contract_address: str, var_0: Address
    ) -> JSONLike:
        """Handler method for the 'pool_fees' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.poolFees(var_0).call()
        return {"int": result}

    @classmethod
    def pricer(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'pricer' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.pricer().call()
        return {"address": result}

    @classmethod
    def protocol(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'protocol' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.protocol().call()
        return {"address": result}

    @classmethod
    def strike_asset(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'strike_asset' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.strikeAsset().call()
        return {"address": result}

    @classmethod
    def swap_router(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'swap_router' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.swapRouter().call()
        return {"address": result}

    @classmethod
    def underlying_asset(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'underlying_asset' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.underlyingAsset().call()
        return {"address": result}

    @classmethod
    def update(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'update' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.update().call()
        return {"int": result}

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

from rysk_client.packages.eightballer.contracts.o_token import PUBLIC_ID


class OToken(Contract):
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
    def domain_separator(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'domain_separator' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.DOMAIN_SEPARATOR().call()
        return {"str": result}

    @classmethod
    def allowance(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        owner: Address,
        spender: Address,
    ) -> JSONLike:
        """Handler method for the 'allowance' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.allowance(owner=owner, spender=spender).call()
        return {"int": result}

    @classmethod
    def balance_of(
        cls, ledger_api: LedgerApi, contract_address: str, account: Address
    ) -> JSONLike:
        """Handler method for the 'balance_of' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.balanceOf(account=account).call()
        return {"int": result}

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
    def controller(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'controller' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.controller().call()
        return {"address": result}

    @classmethod
    def decimals(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'decimals' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.decimals().call()
        return {"int": result}

    @classmethod
    def expiry_timestamp(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'expiry_timestamp' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.expiryTimestamp().call()
        return {"int": result}

    @classmethod
    def get_otoken_details(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_otoken_details' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getOtokenDetails().call()
        return {
            "address_0": result[0],
            "address_1": result[1],
            "address_2": result[2],
            "int_0": result[3],
            "int_1": result[4],
            "bool": result[5],
        }

    @classmethod
    def is_put(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'is_put' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.isPut().call()
        return {"bool": result}

    @classmethod
    def name(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'name' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.name().call()
        return {"str": result}

    @classmethod
    def nonces(
        cls, ledger_api: LedgerApi, contract_address: str, owner: Address
    ) -> JSONLike:
        """Handler method for the 'nonces' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.nonces(owner=owner).call()
        return {"int": result}

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
    def strike_price(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'strike_price' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.strikePrice().call()
        return {"int": result}

    @classmethod
    def symbol(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'symbol' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.symbol().call()
        return {"str": result}

    @classmethod
    def total_supply(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'total_supply' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.totalSupply().call()
        return {"int": result}

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

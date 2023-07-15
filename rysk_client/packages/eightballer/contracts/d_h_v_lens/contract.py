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
from aea.crypto.base import LedgerApi

from rysk_client.packages.eightballer.contracts.d_h_v_lens import PUBLIC_ID


class DHVLens(Contract):
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
    def exchange(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'exchange' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.exchange().call()
        return {"address": result}

    @classmethod
    def get_expirations(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_expirations' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getExpirations().call()
        return {"list[int]": result}

    @classmethod
    def get_option_chain(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_option_chain' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getOptionChain().call()
        return {"tuple": result}

    @classmethod
    def get_option_expiration_drill(
        cls, ledger_api: LedgerApi, contract_address: str, expiration: int
    ) -> JSONLike:
        """Handler method for the 'get_option_expiration_drill' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getOptionExpirationDrill(
            expiration=expiration
        ).call()
        return {"tuple": result}

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
    def underlying_asset(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'underlying_asset' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.underlyingAsset().call()
        return {"address": result}

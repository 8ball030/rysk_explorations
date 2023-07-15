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

from rysk_client.packages.eightballer.contracts.opyn_controller import \
    PUBLIC_ID


class OpynController(Contract):  # pylint: disable=too-many-public-methods
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
    def calculator(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'calculator' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.calculator().call()
        return {"address": result}

    @classmethod
    def call_restricted(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'call_restricted' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.callRestricted().call()
        return {"bool": result}

    @classmethod
    def can_settle_assets(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _expiry: int,
    ) -> JSONLike:
        """Handler method for the 'can_settle_assets' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.canSettleAssets(
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _expiry=_expiry,
        ).call()
        return {"bool": result}

    @classmethod
    def full_pauser(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'full_pauser' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.fullPauser().call()
        return {"address": result}

    @classmethod
    def get_account_vault_counter(
        cls, ledger_api: LedgerApi, contract_address: str, _account_owner: Address
    ) -> JSONLike:
        """Handler method for the 'get_account_vault_counter' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getAccountVaultCounter(
            _accountOwner=_account_owner
        ).call()
        return {"int": result}

    @classmethod
    def get_configuration(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_configuration' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getConfiguration().call()
        return {
            "address_0": result[0],
            "address_1": result[1],
            "address_2": result[2],
            "address_3": result[3],
        }

    @classmethod
    def get_naked_cap(
        cls, ledger_api: LedgerApi, contract_address: str, _asset: Address
    ) -> JSONLike:
        """Handler method for the 'get_naked_cap' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getNakedCap(_asset=_asset).call()
        return {"int": result}

    @classmethod
    def get_naked_pool_balance(
        cls, ledger_api: LedgerApi, contract_address: str, _asset: Address
    ) -> JSONLike:
        """Handler method for the 'get_naked_pool_balance' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getNakedPoolBalance(_asset=_asset).call()
        return {"int": result}

    @classmethod
    def get_payout(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        _otoken: Address,
        _amount: int,
    ) -> JSONLike:
        """Handler method for the 'get_payout' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getPayout(_otoken=_otoken, _amount=_amount).call()
        return {"int": result}

    @classmethod
    def get_proceed(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        _owner: Address,
        _vault_id: int,
    ) -> JSONLike:
        """Handler method for the 'get_proceed' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getProceed(
            _owner=_owner, _vault_id=_vault_id
        ).call()
        return {"int": result}

    @classmethod
    def get_vault(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        _owner: Address,
        _vault_id: int,
    ) -> JSONLike:
        """Handler method for the 'get_vault' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getVault(_owner=_owner, _vault_id=_vault_id).call()
        return {"tuple": result}

    @classmethod
    def get_vault_liquidation_details(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        _owner: Address,
        _vault_id: int,
    ) -> JSONLike:
        """Handler method for the 'get_vault_liquidation_details' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getVaultLiquidationDetails(
            _owner=_owner, _vault_id=_vault_id
        ).call()
        return {"address": result, "int_0": result, "int_1": result}

    @classmethod
    def get_vault_with_details(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        _owner: Address,
        _vault_id: int,
    ) -> JSONLike:
        """Handler method for the 'get_vault_with_details' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getVaultWithDetails(
            _owner=_owner, _vault_id=_vault_id
        ).call()
        return {"tuple": result[0], "int_0": result[1], "int_1": result[2]}

    @classmethod
    def has_expired(
        cls, ledger_api: LedgerApi, contract_address: str, _otoken: Address
    ) -> JSONLike:
        """Handler method for the 'has_expired' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.hasExpired(_otoken=_otoken).call()
        return {"bool": result}

    @classmethod
    def is_liquidatable(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        _owner: Address,
        _vault_id: int,
    ) -> JSONLike:
        """Handler method for the 'is_liquidatable' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.isLiquidatable(
            _owner=_owner, _vault_id=_vault_id
        ).call()
        return {"bool": result, "int_1": result, "int_2": result}

    @classmethod
    def is_operator(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        _owner: Address,
        _operator: Address,
    ) -> JSONLike:
        """Handler method for the 'is_operator' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.isOperator(
            _owner=_owner, _operator=_operator
        ).call()
        return {"bool": result}

    @classmethod
    def is_settlement_allowed(
        cls, ledger_api: LedgerApi, contract_address: str, _otoken: Address
    ) -> JSONLike:
        """Handler method for the 'is_settlement_allowed' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.isSettlementAllowed(_otoken=_otoken).call()
        return {"bool": result}

    @classmethod
    def oracle(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'oracle' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.oracle().call()
        return {"address": result}

    @classmethod
    def owner(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'owner' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.owner().call()
        return {"address": result}

    @classmethod
    def partial_pauser(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'partial_pauser' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.partialPauser().call()
        return {"address": result}

    @classmethod
    def pool(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'pool' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.pool().call()
        return {"address": result}

    @classmethod
    def system_fully_paused(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'system_fully_paused' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.systemFullyPaused().call()
        return {"bool": result}

    @classmethod
    def system_partially_paused(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'system_partially_paused' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.systemPartiallyPaused().call()
        return {"bool": result}

    @classmethod
    def whitelist(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'whitelist' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.whitelist().call()
        return {"address": result}

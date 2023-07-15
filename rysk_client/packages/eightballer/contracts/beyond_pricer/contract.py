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

from rysk_client.packages.eightballer.contracts.beyond_pricer import PUBLIC_ID


class BeyondPricer(Contract):  # pylint: disable=too-many-public-methods
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
    def bid_ask_i_v_spread(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'bid_ask_i_v_spread' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.bidAskIVSpread().call()
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
    def collateral_lending_rate(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'collateral_lending_rate' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.collateralLendingRate().call()
        return {"int": result}

    @classmethod
    def delta_band_width(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'delta_band_width' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.deltaBandWidth().call()
        return {"int": result}

    @classmethod
    def delta_borrow_rates(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'delta_borrow_rates' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.deltaBorrowRates().call()
        return {
            "sellLong": result,
            "sellShort": result,
            "buyLong": result,
            "buyShort": result,
        }

    @classmethod
    def fee_per_contract(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'fee_per_contract' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.feePerContract().call()
        return {"int": result}

    @classmethod
    def get_call_slippage_gradient_multipliers(
        cls, ledger_api: LedgerApi, contract_address: str, _tenor_index: int
    ) -> JSONLike:
        """Handler method for the 'get_call_slippage_gradient_multipliers' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getCallSlippageGradientMultipliers(
            _tenor_index=_tenor_index
        ).call()
        return {"list[int]": result}

    @classmethod
    def get_call_spread_collateral_multipliers(
        cls, ledger_api: LedgerApi, contract_address: str, _tenor_index: int
    ) -> JSONLike:
        """Handler method for the 'get_call_spread_collateral_multipliers' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getCallSpreadCollateralMultipliers(
            _tenor_index=_tenor_index
        ).call()
        return {"list[int]": result}

    @classmethod
    def get_call_spread_delta_multipliers(
        cls, ledger_api: LedgerApi, contract_address: str, _tenor_index: int
    ) -> JSONLike:
        """Handler method for the 'get_call_spread_delta_multipliers' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getCallSpreadDeltaMultipliers(
            _tenor_index=_tenor_index
        ).call()
        return {"list[int]": result}

    @classmethod
    def get_put_slippage_gradient_multipliers(
        cls, ledger_api: LedgerApi, contract_address: str, _tenor_index: int
    ) -> JSONLike:
        """Handler method for the 'get_put_slippage_gradient_multipliers' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getPutSlippageGradientMultipliers(
            _tenor_index=_tenor_index
        ).call()
        return {"list[int]": result}

    @classmethod
    def get_put_spread_collateral_multipliers(
        cls, ledger_api: LedgerApi, contract_address: str, _tenor_index: int
    ) -> JSONLike:
        """Handler method for the 'get_put_spread_collateral_multipliers' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getPutSpreadCollateralMultipliers(
            _tenor_index=_tenor_index
        ).call()
        return {"list[int]": result}

    @classmethod
    def get_put_spread_delta_multipliers(
        cls, ledger_api: LedgerApi, contract_address: str, _tenor_index: int
    ) -> JSONLike:
        """Handler method for the 'get_put_spread_delta_multipliers' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getPutSpreadDeltaMultipliers(
            _tenor_index=_tenor_index
        ).call()
        return {"list[int]": result}

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
    def low_delta_sell_option_flat_i_v(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'low_delta_sell_option_flat_i_v' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.lowDeltaSellOptionFlatIV().call()
        return {"int": result}

    @classmethod
    def low_delta_threshold(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'low_delta_threshold' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.lowDeltaThreshold().call()
        return {"int": result}

    @classmethod
    def max_tenor_value(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'max_tenor_value' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.maxTenorValue().call()
        return {"int": result}

    @classmethod
    def number_of_tenors(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'number_of_tenors' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.numberOfTenors().call()
        return {"int": result}

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
    def quote_option_price(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        _option_series: tuple,
        _amount: int,
        is_sell: bool,
        net_dhv_exposure: int,
    ) -> JSONLike:
        """Handler method for the 'quote_option_price' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.quoteOptionPrice(
            _optionSeries=_option_series,
            _amount=_amount,
            isSell=is_sell,
            netDhvExposure=net_dhv_exposure,
        ).call()
        return {"totalPremium": result, "totalDelta": result, "totalFees": result}

    @classmethod
    def risk_free_rate(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'risk_free_rate' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.riskFreeRate().call()
        return {"int": result}

    @classmethod
    def slippage_gradient(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'slippage_gradient' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.slippageGradient().call()
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
    def underlying_asset(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'underlying_asset' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.underlyingAsset().call()
        return {"address": result}

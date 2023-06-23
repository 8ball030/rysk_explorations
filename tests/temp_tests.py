"""
Tests for potential improvements and knows txs. 

currently unused..
"""
import logging
from typing import Any, Optional, Tuple

import pytest
from web3 import Web3

from rysk_client.src.action_type import ActionType
from rysk_client.src.utils import get_contract, get_logger

logger = get_logger()


@pytest.fixture
def web3():
    """
    Create a web3 instance.
    """
    return Web3(Web3.HTTPProvider("http://localhost:8545"))


@pytest.fixture
def options_exchange(web3):
    """
    Deploy the options exchange contract.
    """
    return get_contract("option_exchange", web3)


class TxTestCase:
    """TxTestCase."""

    tx_hash: str
    operate_tuple: Optional[Tuple[Any]]


def test_can_get_args_from_tx(options_exchange, web3):
    """
    Test that we can get the arguments from a transaction.
    We need to use a transaction that has already been mined.
    we will use 0x0f88769d7e8454192bb384bb1daf65638844311f0de2bad76178edc53e2df2a5
    """
    unknown_txs = [
        "0xca1f858547219d23bd68984b31f867d56684bb2028070e12c5a2da2e9082b096",
        "0xa729c880593c849360f0cd7ae494695a434e34ca68b113c0bb272f131e5a7aca",
        "0x3722bda7696d17fd06d85614a3c8e644488e6150aac0d5be6ebcab3d7543fdb7",
        "0x9aa51262bcc7aa75a5b1f5555a1968ca22cac5a88f7df714fccd6115866fa0fd",
        "0x089d6c9467d827ca3e25cc875f3fcd34d6ce05e41b36a4907ca4fecc6f7467fb",
        "0xc250aa456c0382ae91e53aa9dd709d9639150c9b68ee12bc1d64f9ae1cdb21b2",
        "0x0625d64c6fbccda6a84cb9a079b78b6116c98af5fe67122c4e4dd55f7ac87920",
        "0x0342da2465bf44c599cf862755eee5c3a0420ebab79c9db9b1258b08d0ef17cb",
        "0x43f9b918e7b6fbcf42b1bb6241862f2afe12699cf95ed2e4a5223be0572b2e0e",
        "0x853d0892a04f5445e70b29e65526c4d7a247321989cd1fb189cdd06acc75f742",
        "0x1f888ac09081f6533b419a2c5250cd0b6b66c3b1bdecaca06dd8763735c50f7c",
        "0x1c4c201d9b98612b39735b86781f9280c42e502815f2a3388a98051eb5214a7e",
        "0xffe868deade96157b4710d53b7b41f50fa405aded007abdbf2f18b9d978b423c",
        "0x9c4037d58e6d0a2a73000b8aebdbcdd9ab4e6610aefe0990e3a3cb19429f33e7",
        "0xbdcd1732076c7e8bb3250d4cb27d6969f90a4381419941530d6994c03e644185",
        "0x278eb27b5c72051362f969924a8be3a586bce405ec6c262e482a9cfb9affbeff",
        "0xb52e95816ad73199ad95ee22b8af73d7690bdc3e74e1e414e0fd6843831632cc",
        "0x03ce359df25bf3806b5a5ed763e41285878ff0b1dab9defd21d4fe7c741b1f5c",
        "0x25e01b88e8bfac9755f83a094050365fe78f567562f0cca4077b9d69b3abf535",
        "0x02d4c86b2d711674f90988042f187456a916733b8111de2936f5f94965acb61f",
        "0xf21705b0393f9568690d2312cdb68a60272f9f8038e385d0036a0555ea87270b",
        "0x076910bc9f977b85fef07fc67cbe49f4653cf0a79dfc36c28796c70817976b17",
        "0x980348f7c49e77ff3bfbaf03d04e75ea0e203cf417a1a2c59a6e3aeab3ac525a",
        "0x66fe1c6787343d0b7530969520d30ae0f42252e032a8cff6ee8bcc431d004e92",
        "0x85cc53f17cfa52d9b45e01c16365e92cfc79e2eb25e8a63770442343cfc1512b",
        "0x79721404bd7ee626bb13e5bba9f967dd2ae00a69f7e221eeb5472c1c0c652181",
        "0x6c257037b3919747d51628f918535342e4828de33fd7cfb45250f4ff5c6a4b73",
        "0x3e2fdb1243be3509550679d4ae4aa763416fb900f52357ef86bc53c3f596aeda",
        "0x20c58dc0d84f0b16dfb7dad9afb48d2b62bcde917576c28abbeca806a0609f89",
        "0x85effe30baaa0497f72fff5ab11d93eab17c0baef2a19657e573aa762f33e350",
        "0xb532891b463b10ec42b0c25635fb7381846d546622ddd65358c24600ed1387d6",
        "0xf1bd34d1d0e814e3a1c5c3ae979da68e8e64cb3335eff7e86736bb8a38cfd842",
        "0x2c3a2723b05e29dd9baa8025f7ad93451086b58784eccfa2e98a2202fa92f3fa",
        "0xa1bbaaf37269789bb97ad98f8a2aad439dddd94ee7a28a5d462b0f0de06e6a30",
        "0xff5ccc8a2fa8259f36b89bcfaf6fbd68ae7ab48d42d855570fa8d4ed70ac9ec4",
        "0x55c59afadb0eca5a7f691287108bffbc74329ac1d75d0bd5e3156592eb0005f8",
        "0x1c7318f088b687cc6b68e76c9a5725cc2009e9410b9e04030cd154feee9c9342",
        "0x69a06fc211c08bc5c47a49b40cb8c198b3a360468d4eb27930638c57d8d41f2c",
        "0xb09955f1c5f05a2fe2eaf7079ac2081b1f52222f547ff2a06ac71b598a2ad479",
        "0xd47088731edf40867f783ef7f82f6e49978d97bef3e324fc7752de5fb3a278bd",
        "0x99e618a097107eaa20a1573ba3d189edf88c8d214ed45da04cd6d851085e41bb",
        "0xb25270b0f40d713875534db10629e36178f7c3a6fc589c7601d6798109702adf",
        "0xdc3c9f547851d656b8aa930a43edf51ea3a4de1a26a3fef1c6cca065819cd6f7",
        "0x6cc852918a2c05acfb79e15c8c4d016ef5f3401d7ba2449c0b5750b68a2e0e4f",
        "0x52d0b69492c129039795071528d08e3c5e59484dea963a423558d933753121c9",
        "0xa7c90c9d5111f3e80b64b716c3aad37938c194976f13ce4a8b4d37d69490ea78",
        "0x38481d0f00cb868afebb7d762a3837ed29c568532f1621266d28daad7b3fee83",
        "0x6aa314281a1ec10b5277c847ead21542ca1507886f8a9579b783c590243f0bd9",
        "0x769262408962d253f0d4959a0b9267b9f98d701e6d117e8025a7359fd14ccd75",
        "0x3849c0d6a3de2f66ed033cc6e926c4cfcee9014b8f1f5554cce56c675048cca5",
        "0x5b6ebfe77b8b3b8681ff4d838cc7e9af478b54f81ab1d9f3281d00926e509e01",
        "0x7186fbf23110b19c407b98b2e1478e57835248a7aa6b1e4306279e1f40d1edc0",
        "0x340b7b4e2f87e91accb7df3a392ac776e8f5903fcfcb5162a649eba0594e4b29",
        "0x19b11ca6d77080cefb358a712cf0435762e78becb243ea0f75da847c4a938f87",
        "0xe2889c9b7e142aec05e3fa3107a231dfc086cddc9cd92b1a7c78328e616a40f3",
        "0x97c70e3ccea8f606043a6666425d558f17b7cbab9dc4c3a463bca46e389bd75f",
        "0xb9d637a018031e861f2c4b42c272b2f791b90cc718091550e87f054368bbac55",
        "0x3909e9a1ff8691bf9de7cb8fd810383fd6332e3d7cec62bbd078b125adacb248",
        "0x57abdfb52358b8213084db0047c4742d85117762acbadbbf390db1a25b028d3f",
        "0x3acbc2c7fd2086de579596878aa1f71c8c55ba37c81d8f0ecc567a9a13ef03e9",
        "0x87a111774eac1ff25b87d2d0aefeda78e6e78a7f199ff303316d97963e39584b",
        "0x50dae2eb3514133e8d8196ea1d0aaf8f4e7215dbffd59ad88ba7724d81b3cd18",
        "0xe8f7cf2be63468c470f52a513403eefedaf71643d553a0c48c1a4e63a2f91010",
        "0xae7a6bf6822df134ee1ee2ee19aee307051c9c9a6fa869ff73cef1221a198015",
        "0x580d9da3ef110dc4ef2e9f0444c43e317282a20bb54893a6ae434ea973e159b6",
        "0xeb76234037bd579806c87fd307ed396fdf8ee14947260ff1cfcee2630e2ba799",
        "0x1fdfaa497d7114eb42ff04ec03e2d4b5af04dcd442be195bec3e0894cfa3f6dd",
        "0xa2298b41e66bce7466f61905aa58ad8e0c7efa8e44ddfdbbdc63f8a8bc3263a9",
        "0x136ddfbb611a029fe950e4b3b91998fdc9bcb1c24018d9dc49f3c974e3603fd8",
        "0xf3802e195b15a3d3eace47dee445edbdcca11122d973b6284f60b8cf49dbe26d",
        "0x0e35a7e20599cd9f3f6565d2dc130d28b174cdf798a5ad9741c670c23dd4c128",
        "0x42c579f0173dac1377a560a12d2b384d8829d3c30f194df870f4c8de86f1206c",
        "0x259fec51eac65ee34bb510b5e0ea46e5eec92c359d86d3f2a1992a5de85db994",
        "0x73faeb5615c39dd2202b5ad27ef49570bdf0323a2ee17a72184b9d0e62253595",
        "0xce28f6408276a5272f73e4d9da39e41997d0494f8c933a14f35ede36004a48fb",
        "0x55d060fe2c7bec966ac579e702a2ba9b6885d80eb527b8367d2cf98306c26a9f",
        "0xd1d13ccfa0c05580085ab1f32666bd7ed26c30597d752a9adeb9b7f1e5dbaf7f",
        "0xbeef7ede035acf513292663ae9fd59a5aee7f326400b1841d674d2fddf9b7484",
        "0x4b7a41c1a3afe33dcaab804435b46b8a5e49e715fe9376bf162a29a2dfc32797",
        "0xb6f42f45ff121ae0397fa0bee13da6933fd3e2d55fc5b461f7a8889ad0bed02d",
        "0x14538e46e9da4383ba55c9acdd4b7c7a802d36f5af6d495d51262187521dd7be",
        "0xfe768a05b51ab42cba2752ada7b6e64fcd5875d0f6a81b546ec6b99b1a9dd1c1",
        "0xdf56bb61ac664d7393440124121f44148175962aca4ad5b3d78026ba7b9793be",
        "0xca309df1523847e45eced59721fddb65aeb9b3fe4ec1304df4204adc16eedffd",
        "0x6574674953dcd3d88e87ab8323d74d373d6972059e1c8c913ad282402efa523b",
        "0x9045f2c1f7b416507b2e91384137038b6d4d2775b0d70bbe81e496cf2b629b81",
        "0xabc38756f969434d1b0ded9cebc1a0f5654059207084f655c890e98c288b09a6",
        "0x87738b675800a56d22e88bb6d360bd81f25eb8ea544bf204d86dcb11cbfca32d",
        "0x6b8e217c1518a93b273d46b3f7a5a29cd7d43826ca297ff14fe82ac0cdeb6a94",
        "0x92a9f575a48fad75424672b26312272f30711ba251c55ea84cadd83aea791b48",
        "0x959c1976a24a050d6bd2f511e714ebec2b2d94af832b28f23bfd6261b87386f5",
        "0x9b1caa2c9a47dccb18cb7fdfb2f318470347b4e485027dc99098026502831908",
        "0xd584feb85532f7780e28228b2841f9df14228dc0f02b94f0b26e89d2091ac201",
        "0x35260877ff12b8ba8745a966596edebae6ee3176402e048d4358d5c219deb55f",
        "0x99558d904712a8052c6456b28e130a5106fd040b4d59ca50ae84e5d8f9a65719",
        "0xb19f0e8db6fac6690c085bc6a3fcba3cf273d06bba98b7abab5de39c0f808cb5",
    ]

    txs = []
    for tx_hash in unknown_txs:
        txn = TxTestCase()
        txn.tx_hash = tx_hash
        txn.operate_tuple = None
        txs.append(txn)

    tx_arguements = {}
    for txn in txs:
        tx_hash = txn.tx_hash
        arguments = get_tx_args(
            options_exchange,
            tx_hash,
            web3,
        )[1]
        tx_arguements[tx_hash] = arguments

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    buys = {}

    for txn, in_args in tx_arguements.items():
        logger.info(f"Transaction: {txn}")
        operate_procedures = in_args["_operationProcedures"]
        for operation in operate_procedures:
            for action in operation["operationQueue"]:
                _type = action["actionType"]

                logger.info(f"Operation: {ActionType(_type)}")

                if _type == ActionType.DEPOSIT_LONG_OPTION.value:
                    buys[txn] = in_args


def get_tx_args(
    contract,
    tx_hash,
    web3,
):
    """
    Get the arguments from a transaction.
    """
    transaction = web3.eth.get_transaction(tx_hash)
    contract_input = transaction["input"]
    return contract.decode_function_input(contract_input)

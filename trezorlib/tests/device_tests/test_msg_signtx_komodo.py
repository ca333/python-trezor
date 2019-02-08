# This file is part of the Trezor project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import pytest

from trezorlib import btc, messages as proto
from trezorlib.tools import parse_path

from ..support.tx_cache import tx_cache
from .common import TrezorTest

TX_API = tx_cache("Komodo Mainnet")

# TXHASH_fb2847 = bytes.fromhex(
#     "fb2847e4f3de789d4cfa0e0dcc96ad47f68c2ea2897013adbe40974c1e6dbe39"
# )
TXHASH_339c3e = bytes.fromhex(
    "339c3e78610e229f65ebc3fa722016fcb9fbde7bc196d2d876604f5257ada19c"
)


@pytest.mark.komodo
class TestMsgSigntxKomodo(TrezorTest):
    # ca333 - v1 Tests deactivated since v4 is mandatory
    # def test_one_one_fee_overwinter(self):
    #     self.setup_mnemonic_allallall()
    #
    #     # prevout: fb2847e4f3de789d4cfa0e0dcc96ad47f68c2ea2897013adbe40974c1e6dbe39:1
    #     # input 1: 16.82116 KMD
    #
    #     inp1 = proto.TxInputType(
    #         address_n=parse_path(
    #             "m/Komodo Mainnet/0h/0/0"
    #         ),  # RLCR1rMjGUV33ReXi4ptQq7JMhUpUai5tg
    #         amount=1682116000,
    #         prev_hash=TXHASH_fb2847,
    #         prev_index=1,
    #     )
    #
    #     out1 = proto.TxOutputType(
    #         address="RQC4SesZiZ7WiBnvpCTSLkikhfqLbpNT7Q",
    #         amount=1682116000 - 10000,
    #         script_type=proto.OutputScriptType.PAYTOADDRESS,
    #     )
    #
    #     with self.client:
    #         self.client.set_expected_responses(
    #             [
    #                 proto.TxRequest(
    #                     request_type=proto.RequestType.TXINPUT,
    #                     details=proto.TxRequestDetailsType(request_index=0),
    #                 ),
    #                 proto.TxRequest(
    #                     request_type=proto.RequestType.TXOUTPUT,
    #                     details=proto.TxRequestDetailsType(request_index=0),
    #                 ),
    #                 proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
    #                 proto.ButtonRequest(code=proto.ButtonRequestType.SignTx),
    #                 proto.TxRequest(
    #                     request_type=proto.RequestType.TXINPUT,
    #                     details=proto.TxRequestDetailsType(request_index=0),
    #                 ),
    #                 proto.TxRequest(
    #                     request_type=proto.RequestType.TXOUTPUT,
    #                     details=proto.TxRequestDetailsType(request_index=0),
    #                 ),
    #                 proto.TxRequest(request_type=proto.RequestType.TXFINISHED),
    #             ]
    #         )
    #
    #         details = proto.SignTx(
    #             version=1,
    #             overwintered=False,
    #             #version_group_id=0x3C48270,
    #             branch_id=0x5BA81B19,
    #         )
    #         _, serialized_tx = btc.sign_tx(
    #             self.client,
    #             "Komodo Mainnet",
    #             [inp1],
    #             [out1],
    #             details=details,
    #             prev_txes=TX_API,
    #         )
    #
    #     # Accepted by network: tx 66160449b3bdc499d2a7e711139febbb4f8a25f195c846f5d42db86db77e73ff
    #     assert (
    #         serialized_tx.hex()
    #         == "010000000139be6d1e4c9740bead137089a22e8cf647ad96cc0d0efa4c9d78def3e44728fb010000006b483045022100de573ae38d31c67560410774f9ec065ef2cf4222d4ce7667745e895d2f4f9cfe0220333bd1d480770e06cc75bca990d4e811f5ffa5b0e69063f7ebc62bbaa618a5dd012102f1bca007fabf60ff62145fa63835dac81dfaf6c5d390d9a7a2d1bf4360fc410fffffffff0190e64264000000001976a914a3916ee0099881a0e7da8ab5eb9395a9039bf4c388ac00000000"
    #     )

    def test_one_one_fee_sapling(self):
        self.setup_mnemonic_allallall()

        # prevout:  339c3e78610e229f65ebc3fa722016fcb9fbde7bc196d2d876604f5257ada19c:0
        # input 1: 2.9999 KMD

        inp1 = proto.TxInputType(
            address_n=parse_path(
                "m/Komodo Mainnet/0h/0/0"
            ),  # RDvyC66RQf7HKkUB5zyLKJhitV4ibzkKF5
            amount=299990000,
            prev_hash=TXHASH_339c3e,
            prev_index=0,
        )

        out1 = proto.TxOutputType(
            address="RDvyC66RQf7HKkUB5zyLKJhitV4ibzkKF5",
            amount=299990000 - 10000,
            script_type=proto.OutputScriptType.PAYTOADDRESS,
        )

        with self.client:
            self.client.set_expected_responses(
                [
                    proto.TxRequest(
                        request_type=proto.RequestType.TXINPUT,
                        details=proto.TxRequestDetailsType(request_index=0),
                    ),
                    proto.TxRequest(
                        request_type=proto.RequestType.TXOUTPUT,
                        details=proto.TxRequestDetailsType(request_index=0),
                    ),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.SignTx),
                    proto.TxRequest(
                        request_type=proto.RequestType.TXINPUT,
                        details=proto.TxRequestDetailsType(request_index=0),
                    ),
                    proto.TxRequest(
                        request_type=proto.RequestType.TXOUTPUT,
                        details=proto.TxRequestDetailsType(request_index=0),
                    ),
                    proto.TxRequest(request_type=proto.RequestType.TXFINISHED),
                ]
            )

            details = proto.SignTx(
                version=4,
                overwintered=True,
                version_group_id=0x892F2085,
                branch_id=0x76B809BB,
            )
            _, serialized_tx = btc.sign_tx(
                self.client,
                "Komodo Mainnet",
                [inp1],
                [out1],
                details=details,
                prev_txes=TX_API,
            )

        # Accepted by network: tx 92b45f54cb7c3cdfc4a88dbf088dfcc7c1417ad0955f02712e136da7fd5343d6
        assert (
            serialized_tx.hex()
            == "0400008085202f89019ca1ad57524f6076d8d296c17bdefbb9fc162072fac3eb659f220e61783e9c33000000006a47304402206972af8ff4dec4074da9edb1a741114bebda9e686bb411dd6f388aafd81f0af2022060a05d0ea66d5b8632868b6a6d377ad1a8941385d628be4631b31cc246014b8501210235ad92bb4efda1e6794890f248fa26aab75906bd496c07a6a8532b62a5bd80f7ffffffff01e054e111000000001976a91433058d6bb20e9297fc0a518e2e0262e854496a6c88ac6be15c5c000000000000000000000000000000"
        )

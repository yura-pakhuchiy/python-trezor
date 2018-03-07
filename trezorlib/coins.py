from .tx_api import TxApiBitcoin, TxApiTestnet, TxApiLitecoin, TxApiZcash, TxApiDash, TxApiBcash, TxApiDecredTestnet, TxApiDogecoin, TxApiMonacoin, TxApiBitcoinGold, TxApiZcoin

coins_slip44 = {
    'Bitcoin': 0,
    'Testnet': 1,
    'Decred Testnet': 1,
    'Litecoin': 2,
    'Dogecoin': 3,
    'Dash': 5,
    'Namecoin': 7,
    'Monacoin': 22,
    'Decred': 42,
    'Ether': 60,
    'EtherClassic': 61,
    'Zcash': 133,
    'Zcoin': 136,
    'Bcash': 145,
    'Bitcoin Gold': 156,
}

coins_txapi = {
    'Bitcoin': TxApiBitcoin,
    'Testnet': TxApiTestnet,
    'Litecoin': TxApiLitecoin,
    'Dash': TxApiDash,
    'Zcash': TxApiZcash,
    'Zcoin': TxApiZcoin,
    'Bcash': TxApiBcash,
    'Decred Testnet': TxApiDecredTestnet,
    'Dogecoin': TxApiDogecoin,
    'Monacoin': TxApiMonacoin,
    'Bitcoin Gold': TxApiBitcoinGold,
}

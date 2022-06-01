import secrets

from eth_account import Account


def generate_blockchain_address():
    """Generate a blockchain address for the user.

    Returns:
        str: A blockchain address.

    """
    priv: str = secrets.token_hex(32)
    private_key: str = Account.create(priv).privateKey
    acct: Account = Account.privateKeyToAccount(private_key)

    return acct.address, acct.privateKey

from solders.pubkey import Pubkey as PublicKey
from solders.keypair import Keypair
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import transfer, TransferParams

# Constants
PRIVATE_KEY = [157, 000, 132]
RECIPIENT_ADDRESS = "BdYDib4UApEXDFkdurWfSC7vWUa8HEpdqdMHsRG1bDss"
AMOUNT_SOL = 0.0001
SOLANA_CLUSTER = "https://api.mainnet-beta.solana.com"

# Convert private key to Keypair object
private_key_bytes = bytes(PRIVATE_KEY)
account = Keypair.from_secret_key(private_key_bytes)

# Initialize Solana client
client = Client(SOLANA_CLUSTER)

# Get recent blockhash
response = client.get_recent_blockhash()
recent_blockhash = response['result']['value']['blockhash']

# Create transfer transaction
transaction = Transaction()
transaction.recent_blockhash = recent_blockhash
transaction.add(
    transfer(
        TransferParams(
            from_pubkey=account.public_key(),
            to_pubkey=PublicKey.from_string(RECIPIENT_ADDRESS),
            lamports=int(AMOUNT_SOL * 10**9)
        )
    )
)

# Sign the transaction
transaction.sign(account)

# Send the transaction
response = client.send_transaction(transaction, account)
print("Transaction response:", response)

import time
import requests

# Solana JSON-RPC API endpoint
SOLANA_API_ENDPOINT = "https://api.mainnet-beta.solana.com"

# Wallet address to check
WALLET_ADDRESS = "HuxrKsehay3gPppSVxrQs6nrvRtPNMF4uFFJdCGKgL3D"

# Function to get the balance of a Solana wallet
def get_solana_balance(wallet_address):
    headers = {
        "Content-Type": "application/json",
    }
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [wallet_address]
    }
    
    response = requests.post(SOLANA_API_ENDPOINT, json=payload, headers=headers)
    response_data = response.json()
    
    if 'result' in response_data:
        lamports = response_data['result']['value']
        sol = lamports / 10**9
        return sol
    else:
        print("Error fetching balance:", response_data)
        return None

# Main loop to check balance every 10 seconds
def main():
    while True:
        balance = get_solana_balance(WALLET_ADDRESS)
        if balance is not None:
            print(f"Solana balance for wallet {WALLET_ADDRESS}: {balance} SOL")
        time.sleep(10)

if __name__ == "__main__":
    main()

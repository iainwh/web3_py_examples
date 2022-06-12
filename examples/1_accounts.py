from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/a724432af2964ead8717807bbc3a5656"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

# Fill in your account here
balance = web3.eth.getBalance("0x433393ee17085A1c4a03Cb23fB8559Ce227954F9")
print(web3.fromWei(balance, "ether"))

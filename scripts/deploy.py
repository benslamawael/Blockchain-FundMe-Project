from brownie import FundMe, accounts, network, MockV3Aggregator, config
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-alchemy"]

def deploy_fund_me():
    account = accounts[0]
    if network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        print(price_feed_address)
    else: 
        print("deploying Mocks")
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from" : account})
        print("Mocks Deployed")
        price_feed_address = MockV3Aggregator[-1].address
        print("deploying to ganache")
        
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from" : account}
        )
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()
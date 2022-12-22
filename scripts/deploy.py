from brownie import FundMe, accounts, network, MockV3Aggregator
from web3 import Web3

def deploy_fund_me():
    account = accounts[0]
    print("deploying Mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from" : account})
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
from brownie import FundMe, accounts, network, MockV3Aggregator
from web3 import Web3

def deploy_fund_me():
    account = accounts[0]
    print("deploying Mocks")
    mock_aggregator = MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from" : account})
    price_feed_address = mock_aggregator.address
    print("Mocks Deployed")
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from" : account}
        )
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()
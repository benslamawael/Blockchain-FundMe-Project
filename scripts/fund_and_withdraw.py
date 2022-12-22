from brownie import FundMe, accounts

def fund():
    fund_me = FundMe[-1]
    account = accounts[0]
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = accounts[0]
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()
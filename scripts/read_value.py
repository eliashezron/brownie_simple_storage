from brownie import SimpleStorage, accounts, config


def readContracts():
    simple_storage = SimpleStorage[-1]

    print("saved value:", simple_storage.retrieve())


def main():
    readContracts()

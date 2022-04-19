from brownie import SimpleStorage, accounts, config, network


def deploy_Scripts():
    # account = accounts.add(config.add(['wallets']['from_key']))
    # account = accounts[0]
    account = get_account()
    print(account)
    simple_Storage = SimpleStorage.deploy({"from": account})

    print("initial value:", simple_Storage.retrieve())
    print("updating value...")
    simple_Storage.store(5, {"from": account}).wait(1)
    print("updateValue:", simple_Storage.retrieve())
    print(simple_Storage)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_Scripts()

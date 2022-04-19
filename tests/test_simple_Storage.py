from brownie import SimpleStorage, accounts

# Arrange
def test_deploy():
    # Act
    account = accounts[0]
    # Act
    simple_Storage = SimpleStorage.deploy({"from": account})

    starting_value = simple_Storage.retrieve()

    expected = 0
    # Assert

    assert expected == starting_value


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    txn = simple_storage.store(expected, {"from": account})
    txn.wait(1)
    # Assert
    assert expected == simple_storage.retrieve()

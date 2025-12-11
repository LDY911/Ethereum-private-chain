from web3 import Web3

# 1. 连接到 Ganache 本地链
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
print("链是否连上：", w3.is_connected())


# 2. 查看账户列表
accounts = w3.eth.accounts
print("账户列表：", accounts)


# 3. 选第一个账户当默认发送者
w3.eth.default_account = accounts[0]


# 4. 看看前两个账户余额（单位：ETH）
def show_balance(i):
    balance_wei = w3.eth.get_balance(accounts[i])
    balance_eth = w3.from_wei(balance_wei, "ether")
    print(f"账户{i} ({accounts[i]}) 余额：{balance_eth} ETH")

show_balance(0)
show_balance(1)


# 5. 从账户0给账户1转 1 ETH
tx_hash = w3.eth.send_transaction({
    "from": accounts[0],
    "to": accounts[1],
    "value": w3.to_wei(1, "ether")
})
print("交易已发送，tx_hash：", tx_hash.hex())


# 6. 等交易打包（在本地链很快）
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("交易已上链，区块号：", receipt.blockNumber)


# 7. 再看余额
show_balance(0)
show_balance(1)



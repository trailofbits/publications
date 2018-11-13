from manticore.ethereum import ManticoreEVM

m = ManticoreEVM() # initiate the blockchain
with open('unprotected.sol') as f:
    source_code = f.read()

# Generate the accounts. Creator has 10 ethers; attacker 0 
creator_account = m.create_account(balance=10*10**18)
attacker_account = m.create_account(balance=0)
contract_account = m.solidity_create_contract(source_code, owner=creator_account)


# Deposit 1 ether, from the creator
contract_account.deposit(caller=creator_account, value=10**18)

# Two raw transactions from the attacker
symbolic_data = m.make_symbolic_buffer(320)
m.transaction(caller=attacker_account,
              address=contract_account,
              data=symbolic_data,
              value=0)

symbolic_data = m.make_symbolic_buffer(320)
m.transaction(caller=attacker_account,
              address=contract_account,
              data=symbolic_data,
              value=0)


for state in m.running_states:
    # Check if the attacker can ends with some ether

    balance = state.platform.get_balance(attacker_account.address)
    state.constrain(balance > 1)

    if state.is_feasible():
        print("Attacker can steal the ether! see {}".format(m.workspace))
        m.generate_testcase(state, 'WalletHack')

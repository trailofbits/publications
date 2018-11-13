from manticore.ethereum import ManticoreEVM, ABI
from manticore.core.smtlib import Operators, solver

m = ManticoreEVM() # initiate the blockchain
with open('overflow.sol') as f:
   source_code = f.read()

# Generate the accounts
user_account = m.create_account(balance=1000)
contract_account = m.solidity_create_contract(source_code, owner=user_account, balance=0)

# First add won't overflow uint256 representation
value_0 = m.make_symbolic_value()
contract_account.add(value_0)
# Potential overflow
value_1 = m.make_symbolic_value()
contract_account.add(value_1)
contract_account.sellerBalance()

for state in m.running_states:
    # Check if input0 > sellerBalance

    # last_return is the data returned
    last_return = state.platform.transactions[-1].return_data
    last_return = ABI.deserialize("uint", last_return)

    state.constrain(Operators.UGT(value_0, last_return))

    if state.is_feasible():
        print("Overflow found! see {}".format(m.workspace))
        m.generate_testcase(state, 'OverflowFound')


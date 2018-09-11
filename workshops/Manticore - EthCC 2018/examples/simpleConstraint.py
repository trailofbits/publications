from manticore.ethereum import ManticoreEVM
from manticore.core.smtlib import Operators
from manticore.core.smtlib import solver

m = ManticoreEVM() # initiate the blockchain
source_code = '''
pragma solidity^0.4.20;
contract Simple {
    function f(uint a) payable {
        if (a == 65) {
            throw;
        }
    }
}
'''

# Initiate the accounts
user_account = m.create_account(balance=1000)
contract_account = m.solidity_create_contract(source_code, owner=user_account, balance=0)

# Call f(a), with a symbolic value
contract_account.f(m.SValue, caller=user_account)

## Check if an execution ends with a REVERT or INVALID
for state in m.terminated_states:

    last_tx = state.platform.transactions[-1]
    if last_tx.result in ['REVERT', 'INVALID']:

        # return the first symbolic input
        input0 = state.input_symbols[0]
        # skip the function id, and extract the 32 bytes corresponding to the first parameter
        input0 = Operators.CONCAT(256, *input0[4:36])


    # we do not consider the path were a == 65
    state.constrain(input0 != 65)
    if not solver.check(state.constraints):
         print "Error found in infeasible path"
         continue

    print "Error found in f() execution (see %s)"%m.workspace
    m.generate_testcase(state, 'BugFound')

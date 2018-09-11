from manticore.ethereum import ManticoreEVM

# initiate the blockchain
m = ManticoreEVM()
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

# Check if an execution ends with a REVERT or INVALID
for state in m.terminated_states:
    last_tx = state.platform.transactions[-1]
    if last_tx.result in ['REVERT', 'INVALID']:
        print "Error found in f() execution (see %s)"%m.workspace
        m.generate_testcase(state, 'BugFound')

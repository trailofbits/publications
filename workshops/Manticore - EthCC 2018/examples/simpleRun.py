from manticore.ethereum import ManticoreEVM

# initiate the blockchain
m = ManticoreEVM()
source_code = '''
pragma solidity^0.4.20;
contract Simple {
    function f(uint a) payable public {
        if (a == 65) {
            revert();
        }
    }
}
'''

# Initiate the accounts
user_account = m.create_account(balance=1000)
contract_account = m.solidity_create_contract(source_code, owner=user_account, balance=0)

# Call f(a), with a symbolic value
contract_account.f(m.SValue, user_account)

print "Results are in %s" % m.workspace
m.finalize() # stop the exploration

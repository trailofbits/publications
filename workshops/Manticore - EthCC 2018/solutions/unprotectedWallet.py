from manticore.ethereum import ManticoreEVM
from manticore.core.smtlib import solver

m = ManticoreEVM() # initiate the blockchain
source_code = '''
pragma solidity ^0.4.20;
contract UnprotectedWallet{
    address public owner;

    modifier onlyowner {
        require(msg.sender==owner);
        _;
    }

    function UnprotectedWallet() public {
        owner = msg.sender;
    }
    function changeOwner(address _newOwner) public {
       owner = _newOwner;
    }

    function deposit() payable public { }

    function withdraw() onlyowner public {
        msg.sender.transfer(this.balance);
    }
}
'''


# Generate the accounts. Creator has 10 ethers; attacker 0 
creator_account = m.create_account(balance=10*10**18)
attacker_account = m.create_account(balance=0)
contract_account = m.solidity_create_contract(source_code, owner=creator_account)

print "Creator account: 0x%x (%d)"%(creator_account, creator_account)
print "Attacker account: 0x%x (%d)"%(attacker_account, attacker_account)

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

    balance = state.platform.get_balance(attacker_account)
    state.constrain(balance > 1)

    if solver.check(state.constraints):
        print "Attacker can steal the ether! see %s"%m.workspace
        m.generate_testcase(state, 'WalletHack')


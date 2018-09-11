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

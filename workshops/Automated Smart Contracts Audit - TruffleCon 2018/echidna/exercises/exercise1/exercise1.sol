pragma solidity 0.4.25;
import "token.sol";

contract TestToken is Token {

    address echidna_caller = 0x00a329c0648769a73afac7f9381e08fb43dbea70;

    constructor() public{
        balances[echidna_caller] = 10000;
    }

    // add the property

}

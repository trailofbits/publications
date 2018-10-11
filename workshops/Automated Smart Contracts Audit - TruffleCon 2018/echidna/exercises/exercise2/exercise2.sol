pragma solidity 0.4.25;
import "token.sol";

contract TestToken is Token {

    address echidna_caller = 0x00a329c0648769a73afac7f9381e08fb43dbea70;

    constructor(){
        paused();
        owner = 0x0; // lose ownership
    }

    // add the property

}

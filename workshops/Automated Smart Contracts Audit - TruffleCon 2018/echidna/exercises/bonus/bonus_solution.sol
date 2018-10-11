import "bonus.sol";


contract TestToken is MintableToken{

    address echidna_caller = 0x00a329c0648769a73afac7f9381e08fb43dbea70;
    function TestToken() MintableToken(10000){
        owner = echidna_caller;
    }

    // add the property
    function echidna_test_balance() view public returns(bool){
        return balances[msg.sender] <= 10000;
    }   



}


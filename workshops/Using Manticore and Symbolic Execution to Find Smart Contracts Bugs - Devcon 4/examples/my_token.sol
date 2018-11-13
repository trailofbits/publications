contract Token{
    mapping(address => uint) public balances;
    
    constructor(){
        balances[msg.sender] = 100;
    }
    
    function transfer(address to, uint val){
        // check for overflow
        if(balances[msg.sender] >= balances[to]){
            balances[msg.sender] -= val;
            balances[to] += val;
        }
    }
}


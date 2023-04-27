contract AlarmClock {

    address owner;
    uint gasBonus = 5000;


    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    constructor () {
        owner = msg.sender;
    }    

    function updateGasBonus(uint newGasBonus) external onlyOwner {
        gasBonus = newGasBonus;
    }

    function cancelAndRefund(address who) external {
        uint startGas = gasleft();
        // SOME EXPENSIVE CALL 
        who.call(msg.data);

        uint gasUsed = startGas - gasleft() + gasBonus;

        uint rewardOwed = gasUsed * tx.gasprice;

        payable(msg.sender).transfer(rewardOwed);
    }

}
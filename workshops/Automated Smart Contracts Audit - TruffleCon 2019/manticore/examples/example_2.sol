contract Simple {
    function f(uint a) payable public{
        if (a == 65) {
            revert();
        }
        if (a == 64){
            revert();
        }
    }
}

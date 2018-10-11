contract Suicidal {

  function backdoor() {
    selfdestruct(msg.sender);
  }

}

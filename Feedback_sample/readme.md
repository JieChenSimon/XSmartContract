### test01: Integer Overflow and Reentrancy
```python
pragma solidity ^0.4.15;

contract Reentrance {
    mapping (address => uint) userBalance;
   
    function getBalance(address u) constant returns(uint){
        return userBalance[u];
    }

    function addToBalance() payable{
        userBalance[msg.sender] += msg.value;
    }   

    function withdrawBalance(){
         
         
        if(!(msg.sender.call.value(userBalance[msg.sender])())){
            throw;
        }
        userBalance[msg.sender] = 0;
    }
   
}

// INFO:root:contract /home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test.sol:Reentrance:
// INFO:symExec:   ============ Results ===========
// INFO:symExec:     EVM Code Coverage:                     98.4%
// INFO:symExec:     Integer Underflow:                     False
// INFO:symExec:     Integer Overflow:                      True
// INFO:symExec:     Parity Multisig Bug 2:                 False
// INFO:symExec:     Callstack Depth Attack Vulnerability:  False
// INFO:symExec:     Transaction-Ordering Dependence (TOD): False
// INFO:symExec:     Timestamp Dependency:                  False
// INFO:symExec:     Re-Entrancy Vulnerability:             True
// INFO:symExec:/home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test.sol:11:9: Warning: Integer Overflow.
//         userBalance[msg.sender] += msg.value
// Integer Overflow occurs if:
//     userBalance[msg.sender] = 1
// INFO:symExec:/home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test.sol:17:14: Warning: Re-Entrancy Vulnerability.
//         if(!(msg.sender.call.value(userBalance[msg.sender])()
// INFO:symExec:   ====== Analysis Completed ======
 ```
 
 
### test02: Callstack
 ```python
 pragma solidity ^0.4.18;

contract Reentrance {

  mapping(address => uint) public balances;

  function donate(address _to) public payable {
    balances[_to] += msg.value;
  }

  function balanceOf(address _who) public view returns (uint balance) {
    return balances[_who];
  }

  function withdraw(uint _amount) public {
    if(balances[msg.sender] >= _amount) {
      if(msg.sender.call.value(_amount)()) {
        _amount;
      }
      balances[msg.sender] -= _amount;
    }
  }

  function() public payable {}
}

// INFO:root:contract /home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test2.sol:Reentrance:
// INFO:symExec:   ============ Results ===========
// INFO:symExec:     EVM Code Coverage:                     99.7%
// INFO:symExec:     Integer Underflow:                     False
// INFO:symExec:     Integer Overflow:                      True
// INFO:symExec:     Parity Multisig Bug 2:                 False
// INFO:symExec:     Callstack Depth Attack Vulnerability:  True
// INFO:symExec:     Transaction-Ordering Dependence (TOD): False
// INFO:symExec:     Timestamp Dependency:                  False
// INFO:symExec:     Re-Entrancy Vulnerability:             True
// INFO:symExec:/home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test2.sol:8:5: Warning: Integer Overflow.
//     balances[_to] += msg.value
// Integer Overflow occurs if:
//     balances[_to] = 1
// INFO:symExec:/home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test2.sol:17:10: Warning: Callstack Depth Attack Vulnerability.
//       if(msg.sender.call.value(_amount)()
// INFO:symExec:/home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test2.sol:17:10: Warning: Re-Entrancy Vulnerability.
//       if(msg.sender.call.value(_amount)()
// INFO:symExec:   ====== Analysis Completed ======
  ```
 ### test03：Timestamp 
```python
pragma solidity ^0.4.11;
contract hodlEthereum {
    event Hodl(address indexed hodler, uint indexed amount);
    event Party(address indexed hodler, uint indexed amount);
    mapping (address => uint) hodlers;
    uint constant partyTime = 1596067200;  
    function() payable {
        hodlers[msg.sender] += msg.value;
        Hodl(msg.sender, msg.value);
    }
    function party() {
        require (block.timestamp > partyTime && hodlers[msg.sender] > 0);
        uint value = hodlers[msg.sender];
        hodlers[msg.sender] = 0;
        msg.sender.transfer(value);
        Party(msg.sender, value);
    }
}
// INFO:root:contract /home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test3.sol:hodlEthereum:
// INFO:symExec:   ============ Results ===========
// INFO:symExec:     EVM Code Coverage:                     96.5%
// INFO:symExec:     Integer Underflow:                     False
// INFO:symExec:     Integer Overflow:                      True
// INFO:symExec:     Parity Multisig Bug 2:                 False
// INFO:symExec:     Callstack Depth Attack Vulnerability:  False
// INFO:symExec:     Transaction-Ordering Dependence (TOD): False
// INFO:symExec:     Timestamp Dependency:                  True
// INFO:symExec:     Re-Entrancy Vulnerability:             False
// INFO:symExec:/home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test3.sol:8:9: Warning: Integer Overflow.
//         hodlers[msg.sender] += msg.value
// Integer Overflow occurs if:
//     hodlers[msg.sender] = 1
// INFO:symExec:/home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test3.sol:12:18: Warning: Timestamp Dependency.
//         require (block.timestamp > partyTime && hodlers[msg.sender] > 0
// INFO:symExec:   ====== Analysis Completed ======
 ```
 
 ### test04: Timestamp
```python
pragma solidity ^0.4.11;
contract hodlEthereum {
    event Hodl(address indexed hodler, uint indexed amount);
    event Party(address indexed hodler, uint indexed amount);
    mapping (address => uint) hodlers;
    uint constant partyTime = 1596067200;  
    function() payable {
        hodlers[msg.sender] += msg.value;
        Hodl(msg.sender, msg.value);
    }
    function party() {
        require (block.timestamp > partyTime && hodlers[msg.sender] > 0);
        uint value = hodlers[msg.sender];
        hodlers[msg.sender] = 0;
        msg.sender.transfer(value);
        Party(msg.sender, value);
    }
}

// INFO:root:contract /home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test4.sol:hodlEthereum:
// INFO:symExec:   ============ Results ===========
// INFO:symExec:     EVM Code Coverage:                     98.2%
// INFO:symExec:     Integer Underflow:                     False
// INFO:symExec:     Integer Overflow:                      True
// INFO:symExec:     Parity Multisig Bug 2:                 False
// INFO:symExec:     Callstack Depth Attack Vulnerability:  False
// INFO:symExec:     Transaction-Ordering Dependence (TOD): False
// INFO:symExec:     Timestamp Dependency:                  True
// INFO:symExec:     Re-Entrancy Vulnerability:             False
// INFO:symExec:/home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test4.sol:8:9: Warning: Integer Overflow.
//         hodlers[msg.sender] += msg.value
// Integer Overflow occurs if:
//     hodlers[msg.sender] = 1
// INFO:symExec:/home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test4.sol:12:18: Warning: Timestamp Dependency.
//         require (block.timestamp > partyTime && hodlers[msg.sender] > 0
// INFO:symExec:   ====== Analysis Completed ======
 ```
 
 ### test5: TOD
```python
pragma solidity ^0.4.16;

contract EthTxOrderDependenceMinimal {
    address public owner;
    bool public claimed;
    uint public reward;

    function EthTxOrderDependenceMinimal() public {
        owner = msg.sender;
    }

    function setReward() public payable {
        require (!claimed);

        require(msg.sender == owner);
        owner.transfer(reward);
        reward = msg.value;
    }

    function claimReward(uint256 submission) {
        require (!claimed);
        require(submission < 10);

        msg.sender.transfer(reward);
        claimed = true;
    }
}

// INFO:root:contract /home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test5.sol:EthTxOrderDependenceMinimal:
// INFO:symExec:   ============ Results ===========
// INFO:symExec:     EVM Code Coverage:                     98.3%
// INFO:symExec:     Integer Underflow:                     False
// INFO:symExec:     Integer Overflow:                      False
// INFO:symExec:     Parity Multisig Bug 2:                 False
// INFO:symExec:     Callstack Depth Attack Vulnerability:  False
// INFO:symExec:     Transaction-Ordering Dependence (TOD): True
// INFO:symExec:     Timestamp Dependency:                  False
// INFO:symExec:     Re-Entrancy Vulnerability:             False
// INFO:symExec:Flow1
// /home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test5.sol:16:9: Warning: Transaction-Ordering Dependency.
//         owner.transfer(reward)
// Flow2
// /home/chen/workspace/codeproject/paperProject/exp_sc/data/data_sample/test5.sol:24:9: Warning: Transaction-Ordering Dependency.
//         msg.sender.transfer(reward)
// INFO:symExec:   ====== Analysis Completed ======
 ```

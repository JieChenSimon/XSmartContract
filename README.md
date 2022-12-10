

# XSmartContract
- Two Expert-based pricinples
  - Code localization
    - Line-level Methods
    - Char-level Methods
  - Expert-Rules Casting 

<!-- ![XSmartContract's GitHub stats](https://github-readme-stats.vercel.app/api?username=JiechenJohn&show_icons=true) -->


### Framework Feature

### Vulnerability Sample And its Result, Feedback.
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

### Install Expert vulnerability Detection System: Oyente: 
The instuction of Oyente is aviailable at https://github.com/enzymefinance/oyente.

<div align="center">
    <img width="40%"  src="readme/img/catcoding.gif" alt="catcoding" />

</div>

from slither import Slither
from slither.slithir.operations import Transfer
from slither.analyses.data_dependency.data_dependency import is_dependent
from slither.core.declarations.solidity_variables import SolidityVariableComposed

slither = Slither("0x4e201a5a5534bb334a3d7df4c82cd5db3bd82f29")
for contract in slither.contracts:
    for func in contract.functions:
        for node in func.nodes:
            for operation in node.irs:
                if isinstance(operation, Transfer) and is_dependent(
                    operation.call_value, SolidityVariableComposed("tx.gasprice"), func
                ):
                    print(f"{node.expression} uses tainted input, tx.gasprice, in {func}")
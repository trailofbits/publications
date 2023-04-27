from slither import Slither
slither = Slither("AlarmClock.sol")
from slither.slithir.operations import Transfer
from slither.analyses.data_dependency.data_dependency import is_dependent
from slither.core.declarations.solidity_variables import SolidityVariableComposed
alarm = slither.get_contract_from_name("AlarmClock")[0]
for func in alarm.functions:
    for node in func.nodes:
        for operation in node.irs:
            if isinstance(operation, Transfer) and is_dependent(
                operation.call_value, SolidityVariableComposed("tx.gasprice"), func
            ):
                print(f"{node.expression} uses tainted input, tx.gasprice, in {func}")

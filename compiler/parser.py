from ply import yacc

from compiler.lexer import Lexer
from compiler.functions import Function
from compiler.functions import FunctionBuilder
from compiler.functions import FunctionDirectory
from compiler.functions import IncorrectFunctionParameterAmountException
from compiler.functions import IncorrectFunctionParameterTypeException
from compiler.functions import IncorrectFunctionReturnTypeException
from compiler.functions import FunctionUndefinedException
from compiler.functions import ScopeNames
from compiler.functions import Scope
from compiler.intermediate_code import IntermediateCodeContainer
from compiler.memory import BaseVirtualMemoryAddress
from compiler.quadruples import ActivationRecordExpansionQuadruple
from compiler.quadruples import ArithmeticQuadruple
from compiler.quadruples import AssignmentQuadruple
from compiler.quadruples import ConstantStorageQuadruple
from compiler.quadruples import ConditionalControlTransferQuadruple
from compiler.quadruples import EndFunctionQuadruple
from compiler.quadruples import EndProgramQuadruple
from compiler.quadruples import LimitsVerificationQuadruple
from compiler.quadruples import ParameterPassingQuadruple
from compiler.quadruples import PrintQuadruple
from compiler.quadruples import ReadQuadruple
from compiler.quadruples import RelationalQuadruple
from compiler.quadruples import ReturnValueQuadruple
from compiler.quadruples import ReturnVoidQuadruple
from compiler.quadruples import StartSubroutineQuadruple
from compiler.quadruples import Quadruple
from compiler.quadruples import QuadrupleList
from compiler.quadruples import UnaryArithmeticQuadruple
from compiler.quadruples import UnconditionalControlTransferQuadruple
from compiler.stacks import DimensionedVariableAccessStack
from compiler.stacks import FunctionParameterCountStack
from compiler.stacks import JumpStack
from compiler.stacks import OperandStack
from compiler.stacks import OperatorStack
from compiler.variables import Boolean
from compiler.variables import DimensionNode
from compiler.variables import SemanticTable
from compiler.variables import Type
from compiler.variables import Variable
from compiler.variables import VariableBuilder
from compiler.variables import Operator


class Parser(object):
    tokens = Lexer.tokens

    def __init__(self) -> None:
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)

        self.function_builder = FunctionBuilder()
        self.variable_builder = VariableBuilder()
        self.semantic_table = SemanticTable()

        self.program_counter = None
        self.array_size = None
        self.global_scope = None
        self.function_directory = None
        self.jump_stack = None
        self.operator_stack = None
        self.operand_stack = None
        self.function_parameter_count_stack = None
        self.quadruple_list = None

    
    def reset(self):
        self.program_counter = 0
        self.array_size = 1
        self.global_scope = Scope()
        self.function_directory = FunctionDirectory()
        self.dimensioned_variable_access_stack = DimensionedVariableAccessStack()
        self.function_parameter_count_stack = FunctionParameterCountStack()
        self.jump_stack = JumpStack()
        self.operator_stack = OperatorStack()
        self.operand_stack = OperandStack()
        self.quadruple_list = QuadrupleList()

        self.function_builder.reset()
        self.variable_builder.reset()

        self.function_scope = None
        self.shared_variable_declaration_type = None


    def parse(self, file_data: str) -> IntermediateCodeContainer:
        self.reset()
        self.parser.parse(file_data)

        intermediate_code_container = self.generate_intermediate_code_container(
            self.global_scope,
            self.function_directory,
            self.quadruple_list,
        )
        return intermediate_code_container
        # return self.quadruple_list

    
    def generate_intermediate_code_container(
        self,
        global_scope: Scope,
        function_directory: FunctionDirectory,
        quadruple_list: QuadrupleList
    ) -> IntermediateCodeContainer:
        return IntermediateCodeContainer(global_scope, function_directory, quadruple_list)

    
    def generate_assignment_quadruple(
        self,
        value_variable: Variable,
        storage_variable: Variable
    ) -> AssignmentQuadruple:
        operator = Operator.ASGMT
        return AssignmentQuadruple(operator, value_variable, storage_variable)

    
    def generate_arithmetic_quadruple(
        self,
        operator: Operator,
        left_operand: Variable,
        right_operand: Variable,
        temporal_storage_variable: Variable
    ) -> ArithmeticQuadruple:
        return ArithmeticQuadruple(operator, left_operand, right_operand, temporal_storage_variable)
    

    def generate_addition_quadruple(
        self,
        left_operand: Variable,
        right_operand: Variable,
        temporal_storage_variable: Variable
    ) -> ArithmeticQuadruple:
        operator = Operator.PLUS
        return self.generate_arithmetic_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
    

    def generate_product_quadruple(
        self,
        left_operand: Variable,
        right_operand: Variable,
        temporal_storage_variable: Variable
    ) -> ArithmeticQuadruple:
        operator = Operator.TIMES
        return self.generate_arithmetic_quadruple(operator, left_operand, right_operand, temporal_storage_variable)

    
    def generate_unary_arithmetic_quadruple(
        self,
        operator: Operator,
        value_variable: Variable,
        temporal_storage_variable: Variable
    ) -> UnaryArithmeticQuadruple:
        return UnaryArithmeticQuadruple(operator, value_variable, temporal_storage_variable)


    def generate_relational_quadruple(
        self,
        operator: Operator,
        left_operand: Variable,
        right_operand: Variable,
        temporal_storage_variable: Variable
    ) -> RelationalQuadruple:
        return RelationalQuadruple(operator, left_operand, right_operand, temporal_storage_variable)


    def generate_empty_conditional_control_transfer_quadruple(
        self,
        operator: Operator,
        boolean_variable: Variable
    ) -> ConditionalControlTransferQuadruple:
        program_count = None

        return ConditionalControlTransferQuadruple(operator, boolean_variable, program_count)


    def generate_empty_unconditional_control_transfer_quadruple(
        self
    ) -> UnconditionalControlTransferQuadruple:
        operator = Operator.GOTO
        program_count = None

        return UnconditionalControlTransferQuadruple(operator, program_count)


    def generate_filled_unconditional_control_transfer_quadruple(
        self,
        program_count: int
    ) -> UnconditionalControlTransferQuadruple:
        operator = Operator.GOTO

        return UnconditionalControlTransferQuadruple(operator, program_count)


    def generate_constant_storage_quadruple(
        self,
        constant_value: str,
        storage_variable: Variable
    ) -> ConstantStorageQuadruple:
        operator = Operator.STORE_CONSTANT
        return ConstantStorageQuadruple(operator, constant_value, storage_variable)

    
    def generate_read_quadruple(self, storage_variable: Variable) -> ReadQuadruple:
        return ReadQuadruple(storage_variable)

    
    def generate_limits_verification_quadruple(self, index_variable: Variable, upper_bound: int) -> LimitsVerificationQuadruple:
        return LimitsVerificationQuadruple(index_variable, upper_bound)

    
    def generate_parameter_passing_quadruple(self, variable: Variable, parameter_number: int) -> ParameterPassingQuadruple:
        return ParameterPassingQuadruple(variable, parameter_number)

    
    def generate_print_quadruple(self, print_param: Variable) -> PrintQuadruple:
        return PrintQuadruple(print_param)

    
    def generate_return_value_quadruple(self, return_variable: Variable, function_global_variable: Variable) -> ReturnValueQuadruple:
        return ReturnValueQuadruple(return_variable, function_global_variable)

    
    def generate_return_void_quadruple(self) -> ReturnVoidQuadruple:
        return ReturnVoidQuadruple()

    
    def generate_start_subroutine_quadruple(self, function_id: str) -> StartSubroutineQuadruple:
        return StartSubroutineQuadruple(function_id)

    
    def generate_activation_record_expansion_quadruple(self, function_id: str):
        if not self.function_directory.function_exists(function_id):
            raise FunctionUndefinedException()

        return ActivationRecordExpansionQuadruple(function_id)

    
    def generate_end_function_quadruple(self) -> EndFunctionQuadruple:
        return EndFunctionQuadruple()

    
    def generate_end_program_quadruple(self) -> EndProgramQuadruple:
        return EndProgramQuadruple()


    def generate_dimension_node(self, upper_bound: int, m: int) -> DimensionNode:
        return DimensionNode(upper_bound, m)

    
    def insert_quadruple(self, quadruple: Quadruple) -> None:
        self.quadruple_list.insert_quadruple(quadruple)

    
    def insert_function_to_directory(self, function_id: str, function: Function) -> None:
        self.function_directory.insert_function(function_id, function)

    
    def get_global_variable(self, variable_id: str) -> Variable:
        return self.function_directory.get_global_variable(variable_id)


    def insert_global_variable(self, variable_id: str, variable: Variable) -> None:
        self.global_scope.insert_variable(variable_id, variable)

    
    def get_function_variable(self, function_id: str, variable_id: str) -> Variable:
        return self.function_directory.get_function_local_variable(function_id, variable_id)


    def insert_function_variable(self, function_id: str, variable_id: str, variable: Variable) -> None:
        self.function_directory.insert_function_local_variable(function_id, variable_id, variable)

    
    def function_variable_exists(self, function_id: str, variable_id: str) -> bool:
        return self.function_directory.variable_exists(function_id, variable_id)

    
    def insert_function_parameter(self, function_id: str, parameter: Variable) -> None:
        self.function_directory.insert_function_parameter(function_id, parameter)

    
    def get_function_return_type(self, function_id: str) -> Type:
        return self.function_directory.get_function_return_type(function_id)

    
    def create_global_function_return_variable(self, function_id: str, function_return_type: Type) -> Variable:
        base_virtual_memory_address = self.get_global_base_virtual_memory_address(function_return_type)
        local_variable_counter = self.get_global_variable_counter(function_return_type)

        variable_virtual_memory_address = base_virtual_memory_address + local_variable_counter
        variable = self.build_variable(function_id, function_return_type, variable_virtual_memory_address)
        
        return variable
    

    def get_global_variable_counter(self, variable_type: Type) -> int:
        return self.global_scope.get_variable_counter(variable_type)
    

    def increment_global_variable_counter(self, variable_type: Type) -> None:
        self.global_scope.increment_variable_counter(variable_type)

    
    def increment_global_variable_counter_array(self, variable_type: Type, array_size: int) -> None:
        self.global_scope.increment_variable_counter_array(variable_type, array_size)

    
    def push_current_count_jump_stack(self) -> None:
        self.jump_stack.push(self.program_counter)


    def push_previous_count_jump_stack(self) -> None:
        self.jump_stack.push(self.program_counter - 1)


    def fill_control_transfer_quadruple(self, quadruple_number: int, program_count: int) -> None:
        self.quadruple_list.fill_control_transfer_quadruple(quadruple_number, program_count)


    def create_function_temporal_variable(self, function_id: str, variable_type: Type) -> Variable:
        temporal_counter = self.get_function_temporal_counter(function_id, variable_type)
        base_virtual_address = self.get_temporal_base_virtual_memory_address(variable_type)
        
        variable_id = self.get_temporal_variable_name(variable_type, temporal_counter)
        variable_virtual_memory_address = base_virtual_address + temporal_counter
        variable = self.build_variable(variable_id, variable_type, variable_virtual_memory_address)

        return variable

    
    def create_function_constant_variable(self, function_id: str, variable_type: Type) -> Variable:
        constant_counter = self.get_function_constant_counter(function_id, variable_type)
        base_virtual_address = self.get_constant_base_virtual_memory_address(variable_type)

        variable_id = self.get_constant_variable_name(variable_type, constant_counter)
        variable_virtual_memory_address = base_virtual_address + constant_counter
        variable = self.build_variable(variable_id, variable_type, variable_virtual_memory_address)

        return variable

    
    def create_function_pointer_variable(self, function_id: str) -> Variable:
        pointer_counter = self.get_function_pointer_counter(function_id)
        base_virtual_address = self.get_pointer_base_virtual_memory_address()

        variable_id = self.get_pointer_variable_name(pointer_counter)
        variable_type = Type.POINTER
        variable_virtual_memory_address = base_virtual_address + pointer_counter
        variable = self.build_variable(variable_id, variable_type, variable_virtual_memory_address)

        return variable


    def build_variable(self, variable_id: str, variable_type: Type, variable_virtual_memory_address: int) -> Variable:
        self.variable_builder.set_id(variable_id)
        self.variable_builder.set_type(variable_type)
        self.variable_builder.set_virtual_memory_address(variable_virtual_memory_address)
        
        variable = self.variable_builder.build()
        return variable

    
    def get_global_module_id(self) -> str:
        return ScopeNames.GLOBAL.value

    
    def get_main_function_id(self) -> str:
        return ScopeNames.MAIN.value

    
    def get_temporal_variable_name(self, variable_type: Type, count: int) -> str:
        return f't_{variable_type.name}_{count}'

    
    def get_constant_variable_name(self, variable_type: Type, count: int) -> str:
        return f'c_{variable_type.name}_{count}'

    
    def get_pointer_variable_name(self, count: int) -> str:
        return f'p_{count}'

    
    def get_global_base_virtual_memory_address(self, variable_type: Type) -> int:
        return BaseVirtualMemoryAddress.get_global_base_virtual_memory_address(variable_type)
    

    def get_local_base_virtual_memory_address(self, variable_type: Type) -> int:
        return BaseVirtualMemoryAddress.get_local_base_virtual_memory_address(variable_type)

    
    def get_constant_base_virtual_memory_address(self, variable_type: Type) -> int:
        return BaseVirtualMemoryAddress.get_constant_base_virtual_memory_address(variable_type)

    
    def get_temporal_base_virtual_memory_address(self, variable_type: Type) -> int:
        return BaseVirtualMemoryAddress.get_temporal_base_virtual_memory_address(variable_type)

    
    def get_pointer_base_virtual_memory_address(self) -> int:
        return BaseVirtualMemoryAddress.get_pointer_base_virtual_memory_address()


    def push_operand_stack(self, operand: Variable) -> None:
        self.operand_stack.push(operand)

    
    def pop_operand_stack(self) -> Variable:
        return self.operand_stack.pop()

    
    def push_operator_stack(self, operator: Operator) -> None:
        self.operator_stack.push(operator)

    
    def pop_operator_stack(self) -> Operator:
        return self.operator_stack.pop()

    
    def push_jump_stack(self, quadruple_number: int) -> None:
        self.jump_stack.push(quadruple_number)

    
    def pop_jump_stack(self) -> int:
        return self.jump_stack.pop()
    

    def push_dimensioned_variable_access_stack(self, variable_id: str) -> None:
        self.dimensioned_variable_access_stack.push_id_dim(variable_id)

    
    def pop_dimensioned_variable_access_stack(self) -> tuple[str, int]:
        return self.dimensioned_variable_access_stack.pop_id_dim()
    

    def top_dimensioned_variable_access_stack(self) -> tuple[str, int]:
        return self.dimensioned_variable_access_stack.get_top_id()
    

    def increment_top_dimensioned_variable_access_stack(self) -> None:
        self.dimensioned_variable_access_stack.increment_top_id_dim()


    def get_operation_result_type(
        self,
        left_operand: Variable,
        right_operand: Variable,
        operator: Operator
    ) -> Type:

        return self.semantic_table.search_operation_result_type(
            left_operand.get_type(),
            right_operand.get_type(),
            operator
        )


    def get_program_counter(self) -> int:
        return self.program_counter


    def increment_program_counter(self) -> None:
        self.program_counter += 1

    
    def get_function_number_parameters(self, function_id: str) -> int:
        return self.function_directory.get_function_number_parameters(function_id)

    
    def get_function_parameter(self, function_id: str, number: int) -> Variable:
        return self.function_directory.get_function_parameter(function_id, number)


    def set_function_scope(self, function_id: str) -> None:
        self.function_scope = function_id


    def get_function_scope(self) -> str:
        return self.function_scope

    
    def set_shared_variable_type(self, variable_type: Type) -> None:
        self.shared_variable_declaration_type = variable_type

    
    def get_shared_variable_type(self) -> Type:
        return self.shared_variable_declaration_type


    def get_function_variable_counter(self, function_id: str, variable_type: Type) -> int:
        return self.function_directory.get_function_variable_counter(function_id, variable_type)


    def increment_function_variable_counter(self, function_id: str, variable_type: Type) -> None:
        self.function_directory.increment_function_variable_counter(function_id, variable_type)

    
    def increment_function_variable_counter_array(self, function_id: str, variable_type: Type, array_size: int) -> None:
        self.function_directory.increment_function_variable_counter_array(function_id, variable_type, array_size)


    def get_function_constant_counter(self, function_id: str, variable_type: Type) -> int:
        return self.function_directory.get_function_constant_counter(function_id, variable_type)


    def increment_function_constant_counter(self, function_id: str, variable_type: Type) -> None:
        self.function_directory.increment_function_constant_counter(function_id, variable_type)


    def get_function_temporal_counter(self, function_id: str, variable_type: Type) -> int:
        return self.function_directory.get_function_temporal_counter(function_id, variable_type)

    
    def increment_function_temporal_counter(self, function_id: str, variable_type: Type) -> None:
        self.function_directory.increment_function_temporal_counter(function_id, variable_type)

    
    def get_function_pointer_counter(self, function_id: str) -> int:
        return self.function_directory.get_function_pointer_counter(function_id)

    
    def increment_function_pointer_counter(self, function_id: str) -> None:
        self.function_directory.increment_function_pointer_counter(function_id)


    def push_count_function_parameter_count_stack(self, function_id: str) -> None:
        return self.function_parameter_count_stack.push_count(function_id)


    def pop_count_function_parameter_count_stack(self) -> tuple[str, int]:
        return self.function_parameter_count_stack.pop_count()


    def get_top_count_function_parameter_count_stack(self) -> tuple[str, int]:
        return self.function_parameter_count_stack.get_top_count()

    
    def increment_top_count_function_parameter_count_stack(self) -> None:
        self.function_parameter_count_stack.increment_top_count()


    def create_dimension_node(self, dimension_size: int) -> DimensionNode:
        return DimensionNode(dimension_size)


    def get_array_size(self) -> int:
        return self.array_size


    def set_array_size(self, array_size: int) -> None:
        self.array_size = array_size


    def reset_array_size(self) -> None:
        self.array_size = 1

    
    def p_program(self, p):
        '''program : init start'''
        main_function_id = ScopeNames.MAIN.value
        quadruple_number = self.pop_jump_stack()
        program_counter = self.get_program_counter()

        self.fill_control_transfer_quadruple(quadruple_number, program_counter)
        
        main_activation_record_expansion_quadruple = self.generate_activation_record_expansion_quadruple(main_function_id)
        self.insert_quadruple(main_activation_record_expansion_quadruple)
        self.increment_program_counter()

        start_main_subroutine_quadruple = self.generate_start_subroutine_quadruple(main_function_id)
        self.insert_quadruple(start_main_subroutine_quadruple)
        self.increment_program_counter()
        
        end_program_quadruple = self.generate_end_program_quadruple()
        self.insert_quadruple(end_program_quadruple)
        self.increment_program_counter()


    def p_init(self, p):
        '''init :'''
        self.push_current_count_jump_stack()

        main_control_transfer_quadruple = self.generate_empty_unconditional_control_transfer_quadruple()
        self.insert_quadruple(main_control_transfer_quadruple)
        self.increment_program_counter()


    def p_start(self, p):
        '''start : global_variables_declaration functions_definition entry_point_definition'''


    def p_global_variables_declaration(self, p):
        '''global_variables_declaration : GLOBAL parsed_global_scope variables_declaration
                                        | empty'''


    def p_parsed_global_scope(self, p):
        '''parsed_global_scope :'''
        global_scope_id = self.get_global_module_id()
        self.set_function_scope(global_scope_id)


    def p_functions_definition(self, p):
        '''functions_definition : functions_definition function_definition
                                | function_definition'''
        end_function_quadruple = self.generate_end_function_quadruple()
        self.insert_quadruple(end_function_quadruple)
        self.increment_program_counter()


    def p_function_definition(self, p):
        '''function_definition : FUNCTION type parsed_function_return_type ID parsed_type_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_block
                               | FUNCTION type parsed_function_return_type ID parsed_type_function_id LPAREN RPAREN local_variables_declaration instruction_block
                               | FUNCTION VOID parsed_function_void_return_type ID parsed_void_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_block
                               | FUNCTION VOID parsed_function_void_return_type ID parsed_void_function_id LPAREN RPAREN local_variables_declaration instruction_block
                               | empty'''


    def p_parsed_type_function_id(self, p):
        '''parsed_type_function_id :'''
        function_id = p[-1]
        function_start_quadruple_number = self.get_program_counter()
        
        self.function_builder.set_id(function_id)
        self.function_builder.set_start_quadruple_number(function_start_quadruple_number)
        function = self.function_builder.build()

        self.insert_function_to_directory(function_id, function)
        self.set_function_scope(function_id)

        function_return_type = function.get_return_type()
        global_function_variable = self.create_global_function_return_variable(function_id, function_return_type)
        self.insert_global_variable(function_id, global_function_variable)
        self.increment_global_variable_counter(function_return_type)


    def p_parsed_void_function_id(self, p):
        '''parsed_void_function_id :'''
        function_id = p[-1]
        function_start_quadruple_number = self.get_program_counter()
        
        self.function_builder.set_id(function_id)
        self.function_builder.set_start_quadruple_number(function_start_quadruple_number)
        function = self.function_builder.build()

        self.insert_function_to_directory(function_id, function)
        self.set_function_scope(function_id)


    def p_parsed_function_return_type(self, p):
        '''parsed_function_return_type :'''
        function_return_type = p[-1]
        self.function_builder.set_return_type(function_return_type)

    
    def p_parsed_function_void_return_type(self, p):
        '''parsed_function_void_return_type  :'''
        function_return_type = Type.VOID
        self.function_builder.set_return_type(function_return_type)


    def p_function_definition_params(self, p):
        '''function_definition_params : function_definition_params COMMA function_definition_param
                                      | function_definition_param'''


    def p_function_definition_param(self, p):
        '''function_definition_param : type ID'''
        variable_id = p[2]
        variable_type = p[1]

        function_id = self.get_function_scope()
        local_variable_counter = self.get_function_variable_counter(function_id, variable_type)
        local_base_virtual_memory_address = self.get_local_base_virtual_memory_address(variable_type)

        variable_virtual_memory_address = local_base_virtual_memory_address + local_variable_counter
        self.increment_function_variable_counter(function_id, variable_type)

        variable = self.build_variable(variable_id, variable_type, variable_virtual_memory_address)
        self.function_directory.insert_function_local_variable(function_id, variable_id, variable)
        self.function_directory.insert_function_parameter(function_id, variable)

    
    def p_entry_point_definition(self, p):
        '''entry_point_definition : START parsed_main_id LPAREN RPAREN local_variables_declaration instruction_block'''
        end_function_quadruple = self.generate_end_function_quadruple()
        self.insert_quadruple(end_function_quadruple)
        self.increment_program_counter()

 
    def p_parsed_main_id(self, p):
        '''parsed_main_id :'''
        main_function_id = ScopeNames.MAIN.value
        program_counter = self.get_program_counter()

        self.function_builder.set_id(main_function_id)
        self.function_builder.set_start_quadruple_number(program_counter)
        self.function_builder.set_return_type(Type.VOID)

        main_function = self.function_builder.build()
        self.insert_function_to_directory(main_function_id, main_function)

        self.set_function_scope(main_function_id)


    def p_local_variables_declaration(self, p):
        '''local_variables_declaration : LOCAL variables_declaration
                                       | empty'''

    
    def p_variables_declaration(self, p):
        '''variables_declaration : VARIABLES COLON distinct_type_variables_declaration'''


    def p_distinct_type_variables_declaration(self, p):
        '''distinct_type_variables_declaration : distinct_type_variables_declaration shared_type_variables_declaration
                                               | shared_type_variables_declaration'''


    def p_shared_type_variables_declaration(self, p):
        '''shared_type_variables_declaration : type parsed_type shared_type_variables_declaration_list SEMI'''

    
    def p_parsed_type(self, p):
        '''parsed_type :'''
        variable_type = p[-1]
        self.set_shared_variable_type(variable_type)

    
    def p_shared_type_variables_declaration_list(self, p):
        '''shared_type_variables_declaration_list : shared_type_variables_declaration_list COMMA variable_declaration
                                                  | variable_declaration'''


    def p_variable_declaration_1(self, p):
        '''variable_declaration : variable_id_declaration variable_dim_definition variable_dim_definition'''
        number_dimensions = self.variable_builder.get_number_dimensions()
        array_size = self.get_array_size()

        for dimension in range(number_dimensions):
            r = self.get_array_size()

            dimension_size = self.variable_builder.get_dimension_size(dimension)
            m = int(r / dimension_size)

            self.variable_builder.set_dimension_node_m(dimension, m)
            self.set_array_size(m)

        variable = self.variable_builder.build()
        variable_id = variable.get_id()
        variable_type = variable.get_type()

        function_id = self.get_function_scope()
        global_scope_id = self.get_global_module_id()

        if function_id == global_scope_id:
            self.insert_global_variable(variable_id, variable)
            self.increment_global_variable_counter_array(variable_type, array_size)
        else:
            self.insert_function_variable(function_id, variable_id, variable)
            self.increment_function_variable_counter_array(function_id, variable_type, array_size)


    def p_variable_declaration_2(self, p):
        '''variable_declaration : variable_id_declaration variable_dim_definition'''
        array_size = self.get_array_size()
        
        dimension = 0
        dimension_size = self.variable_builder.get_dimension_size(dimension)

        r = self.get_array_size()
        m = int(r / dimension_size)

        self.variable_builder.set_dimension_node_m(dimension, m)
        self.set_array_size(m)

        variable = self.variable_builder.build()
        variable_id = variable.get_id()
        variable_type = variable.get_type()

        function_id = self.get_function_scope()
        global_scope_id = self.get_global_module_id()


        if function_id == global_scope_id:
            self.insert_global_variable(variable_id, variable)
            self.increment_global_variable_counter_array(variable_type, array_size)
        else:
            self.insert_function_variable(function_id, variable_id, variable)
            self.increment_function_variable_counter_array(function_id, variable_type, array_size)

        self.reset_array_size()

    
    def p_variable_declaration_3(self, p):
        '''variable_declaration : variable_id_declaration'''
        function_id = self.get_function_scope()
        global_scope_id = self.get_global_module_id()

        variable = self.variable_builder.build()
        variable_id = variable.get_id()
        variable_type = variable.get_type()

        if function_id == global_scope_id:
            self.insert_global_variable(variable_id, variable)
            self.increment_global_variable_counter(variable_type)
        else:
            self.insert_function_variable(function_id, variable_id, variable)
            self.increment_function_variable_counter(function_id, variable_type)


    def p_variable_id_declaration(self, p):
        '''variable_id_declaration : ID'''
        variable_id = p[1]
        variable_type = self.get_shared_variable_type()

        function_id = self.get_function_scope()
        global_scope_id = self.get_global_module_id()

        if function_id == global_scope_id:    
            base_virtual_memory_address = self.get_global_base_virtual_memory_address(variable_type)
            variable_counter = self.get_global_variable_counter(variable_type)
        else:
            base_virtual_memory_address = self.get_local_base_virtual_memory_address(variable_type)
            variable_counter = self.get_function_variable_counter(function_id, variable_type)
        
        variable_virtual_memory_address = base_virtual_memory_address + variable_counter

        self.variable_builder.set_id(variable_id)
        self.variable_builder.set_type(variable_type)
        self.variable_builder.set_virtual_memory_address(variable_virtual_memory_address)


    def p_variable_dim_definition(self, p):
        '''variable_dim_definition : LBRACKET CONST_INT RBRACKET'''
        dimension_size = int(p[2])
        
        dimension_node = self.create_dimension_node(dimension_size)
        self.variable_builder.append_dimension_node(dimension_node)

        array_size = self.get_array_size() * dimension_size
        self.set_array_size(array_size)


    def p_instruction_block_1(self, p):
        '''instruction_block : LBRACE statements RBRACE'''

    
    def p_instruction_block_2(self, p):
        '''instruction_block : LBRACE RBRACE'''

    
    def p_statements_1(self, p):
        '''statements : statements single_statement'''

    
    def p_statements_2(self, p):
        '''statements : single_statement'''


    def p_single_statement_1(self, p):
        '''single_statement : assignment'''


    def p_single_statement_2(self, p):
        '''single_statement : function_call_stmt'''


    def p_single_statement_3(self, p):
        '''single_statement : print'''


    def p_single_statement_4(self, p):
        '''single_statement : conditional'''


    def p_single_statement_5(self, p):
        '''single_statement : loop'''


    def p_single_statement_6(self, p):
        '''single_statement : return'''

    
    def p_assignment_1(self, p):
        '''assignment : variable_access ASGMT expr SEMI'''
        operator = Operator.ASGMT
        value_variable = self.pop_operand_stack()
        storage_variable = self.pop_operand_stack()

        
        result_type = self.get_operation_result_type(storage_variable, value_variable, operator)

        if result_type == Type.ERROR:
            print(storage_variable.get_type(), value_variable.get_type(), result_type)
            raise TypeMismatchError()

        quadruple = self.generate_assignment_quadruple(value_variable, storage_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()


    def p_assignment_2(self, p):
        '''assignment : variable_access ASGMT READ LPAREN RPAREN SEMI'''
        storage_variable = self.pop_operand_stack()

        quadruple = self.generate_read_quadruple(storage_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()


    def p_variable_access(self, p):
        '''variable_access : ID parsed_id_variable_access dims_access'''
        function_id = self.get_function_scope()
        variable_id = p[1]

        # Get global/local variable reference
        if self.function_variable_exists(function_id, variable_id):
            variable = self.get_function_variable(function_id, variable_id)
        else:
            variable = self.get_global_variable(variable_id)
        
        if variable.has_dims():
            # Get summation variable
            summation_variable = self.pop_operand_stack()

            # Create pointer variable
            pointer_variable = self.create_function_pointer_variable(function_id)
            self.increment_function_pointer_counter(function_id)

            # Get pointer base virtual memory address
            base_virtual_memory_address = self.get_pointer_base_virtual_memory_address()

            # Store memory address in temporal variable
            memory_address_constant_storage_variable = self.create_function_constant_variable(function_id, Type.INT)
            self.increment_function_constant_counter(function_id, Type.INT)
            memory_address_constant_storage_quadruple = self.generate_constant_storage_quadruple(
                base_virtual_memory_address,
                memory_address_constant_storage_variable,
            )
            self.insert_quadruple(memory_address_constant_storage_quadruple)
            self.increment_program_counter()

            # Add 
            addition_quadruple = self.generate_addition_quadruple(
                    summation_variable,
                    memory_address_constant_storage_variable,
                    pointer_variable
            )
            self.insert_quadruple(addition_quadruple)
            self.increment_program_counter()

            self.push_operand_stack(pointer_variable)
        else:
            self.push_operand_stack(variable)

    
    def p_parsed_id_variable_access(self, p):
        '''parsed_id_variable_access :'''
        variable_id = p[-1]
        function_id = self.get_function_scope()

        if self.function_variable_exists(function_id, variable_id):
            variable = self.get_function_variable(function_id, variable_id)
        else:
            variable = self.get_global_variable(variable_id)

        if variable.has_dims():
            self.push_dimensioned_variable_access_stack(variable_id)


    def p_dims_access(self, p):
        '''dims_access : dims_access dim_access
                       | dim_access
                       | empty'''

        
    def p_dim_access(self, p):
        '''dim_access : LBRACKET expr RBRACKET'''
        function_id = self.get_function_scope()
        
        # Get index variable
        index_variable = self.pop_operand_stack()
        
        # Get dimensioned variable ID and current dimension number
        variable_id, dimension_number = self.top_dimensioned_variable_access_stack()
        
        # Get dimensioned variable reference
        dimensioned_variable = self.get_function_variable(function_id, variable_id)
        # Get dimension size
        dimension_size = dimensioned_variable.get_dimension_size(dimension_number)
        # Get dimension m
        dimension_m  = dimensioned_variable.get_dimension_m(dimension_number)

        # Store dimension m in a constant variable
        dimension_m_constant_variable = self.create_function_constant_variable(function_id, Type.INT)
        self.increment_function_constant_counter(function_id, Type.INT)
        dimension_m_constant_storage_quadruple = self.generate_constant_storage_quadruple(dimension_m, dimension_m_constant_variable)
        self.insert_quadruple(dimension_m_constant_storage_quadruple)
        self.increment_program_counter()
        
        # Generate limits verification quadruple
        limits_verification_quadruple = self.generate_limits_verification_quadruple(index_variable, dimension_size)
        self.insert_quadruple(limits_verification_quadruple)
        self.increment_program_counter()

        # Multiply index variable and dimension size to get step
        product_variable = self.create_function_temporal_variable(function_id, Type.INT)
        self.increment_function_temporal_counter(function_id, Type.INT)
        product_quadruple = self.generate_product_quadruple(index_variable, dimension_m_constant_variable, product_variable)
        self.insert_quadruple(product_quadruple)
        self.increment_program_counter()

        if dimension_number == 0:
            self.push_operand_stack(product_variable)
        
        # If dimension number is 2nd or greater
        if dimension_number > 0:
            print('Summation')
            # Get summation variable
            summation_variable = self.pop_operand_stack()

            addition_variable = self.create_function_temporal_variable(function_id, Type.INT)
            self.increment_function_temporal_counter(function_id, Type.INT)

            addition_quadruple = self.generate_addition_quadruple(summation_variable, product_variable, addition_variable)
            self.insert_quadruple(addition_quadruple)
            self.increment_program_counter()

            self.push_operand_stack(addition_variable)

        self.increment_top_dimensioned_variable_access_stack()

    
    def p_function_call_stmt(self, p):
        '''function_call_stmt : function_call SEMI'''

    
    def p_function_call_1(self, p):
        '''function_call : ID parsed_function_call_id LPAREN function_call_params RPAREN'''
        function_call_id, function_call_parameter_count = self.pop_count_function_parameter_count_stack()
        function_call_number_params = self.get_function_number_parameters(function_call_id)
        function_call_return_type = self.get_function_return_type(function_call_id)

        if function_call_parameter_count != function_call_number_params:
            raise IncorrectFunctionParameterAmountException()

        start_subroutine_quadruple = self.generate_start_subroutine_quadruple(function_call_id)
        self.insert_quadruple(start_subroutine_quadruple)
        self.increment_program_counter()

        if function_call_return_type != Type.VOID:
            function_scope = self.get_function_scope()

            global_function_variable = self.get_global_variable(function_call_id)
            temporal_function_return_variable = self.create_function_temporal_variable(function_scope, function_call_return_type)
            self.increment_function_temporal_counter(function_scope, function_call_return_type)
            
            assignment_quadruple = self.generate_assignment_quadruple(global_function_variable, temporal_function_return_variable)
            self.insert_quadruple(assignment_quadruple)
            self.increment_program_counter()

            self.push_operand_stack(temporal_function_return_variable)

    
    def p_function_call_2(self, p):
        '''function_call : ID parsed_function_call_id LPAREN RPAREN'''
        function_call_id, function_call_parameter_count = self.pop_count_function_parameter_count_stack()
        function_call_number_params = self.get_function_number_parameters(function_call_id)
        function_call_return_type = self.get_function_return_type(function_call_id)

        if function_call_parameter_count != function_call_number_params:
            raise IncorrectFunctionParameterAmountException()

        start_subroutine_quadruple = self.generate_start_subroutine_quadruple(function_call_id)
        self.insert_quadruple(start_subroutine_quadruple)
        self.increment_program_counter()

        if function_call_return_type != Type.VOID:
            function_scope = self.get_function_scope()

            global_function_variable = self.get_global_variable(function_call_id)
            temporal_function_return_variable = self.create_function_temporal_variable(function_scope, function_call_return_type)
            self.increment_function_temporal_counter(function_scope, function_call_return_type)
            
            assignment_quadruple = self.generate_assignment_quadruple(global_function_variable, temporal_function_return_variable)
            self.insert_quadruple(assignment_quadruple)
            self.increment_program_counter()

            self.push_operand_stack(temporal_function_return_variable)

    
    def p_parsed_function_call_id(self, p):
        '''parsed_function_call_id :'''
        function_id = p[-1]

        activation_record_expansion_quadruple = self.generate_activation_record_expansion_quadruple(function_id)
        self.insert_quadruple(activation_record_expansion_quadruple)
        self.increment_program_counter()

        self.push_count_function_parameter_count_stack(function_id)

    
    def p_function_call_params_1(self, p):
        '''function_call_params : function_call_params COMMA single_function_call_param'''


    def p_function_call_params_2(self, p):
        '''function_call_params : single_function_call_param'''


    def p_single_function_call_param(self, p):
        '''single_function_call_param : expr'''
        self.increment_top_count_function_parameter_count_stack()

        function_id, function_parameter_count = self.get_top_count_function_parameter_count_stack()
        function_number_params = self.get_function_number_parameters(function_id)

        if function_parameter_count > function_number_params:
            raise IncorrectFunctionParameterAmountException()

        signature_function_parameter = self.get_function_parameter(function_id, function_parameter_count)
        signature_function_parameter_type = signature_function_parameter.get_type()
        function_call_parameter = self.pop_operand_stack()
        function_call_parameter_type = function_call_parameter.get_type()

        if signature_function_parameter_type != function_call_parameter_type:
            raise IncorrectFunctionParameterTypeException()

        parameter_passing_quadruple = self.generate_parameter_passing_quadruple(function_call_parameter, function_parameter_count)
        self.insert_quadruple(parameter_passing_quadruple)
        self.increment_program_counter()


    
    def p_print_1(self, p):
        '''print : PRINT LPAREN print_params RPAREN SEMI'''

    
    def p_print_2(self, p):
        '''print : PRINT LPAREN RPAREN SEMI'''


    def p_print_params_1(self, p):
        '''print_params : print_params COMMA single_print_param'''

    
    def p_print_params_2(self, p):
        '''print_params : single_print_param'''

    
    def p_single_print_param_1(self, p):
        '''single_print_param : expr'''
        print_param = self.pop_operand_stack()
        quadruple = self.generate_print_quadruple(print_param)

        self.insert_quadruple(quadruple)
        self.increment_program_counter()

    
    def p_conditional_1(self, p):
        '''conditional : IF LPAREN expr RPAREN parsed_if_expr instruction_block ELSE parsed_else instruction_block'''
        quadruple_number = self.pop_jump_stack()
        program_count = self.program_counter

        self.fill_control_transfer_quadruple(quadruple_number, program_count)

    
    def p_conditional_2(self, p):
        '''conditional : IF LPAREN expr RPAREN parsed_if_expr instruction_block'''
        quadruple_number = self.pop_jump_stack()
        program_count = self.program_counter

        self.fill_control_transfer_quadruple(quadruple_number, program_count)

    
    def p_parsed_if_expr(self, p):
        '''parsed_if_expr :'''
        operator = Operator.GOTOF
        boolean_variable = self.pop_operand_stack()

        quadruple = self.generate_empty_conditional_control_transfer_quadruple(operator, boolean_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()
        
        self.push_previous_count_jump_stack()


    def p_parsed_else(self, p):
        '''parsed_else :'''
        quadruple = self.generate_empty_unconditional_control_transfer_quadruple()
        self.insert_quadruple(quadruple)
        self.increment_program_counter()

        quadruple_number = self.pop_jump_stack()
        program_count = self.program_counter
        self.push_previous_count_jump_stack()
        self.fill_control_transfer_quadruple(quadruple_number, program_count)


    def p_loop_1(self, p):
        '''loop : while'''

    
    def p_loop_2(self, p):
        '''loop : for'''


    def p_while(self, p):
        '''while : WHILE parsed_while LPAREN expr parsed_while_expr RPAREN instruction_block'''
        fill_quadruple_number = self.pop_jump_stack()
        unconditional_transfer_quadruple_number = self.pop_jump_stack()

        quadruple = self.generate_filled_unconditional_control_transfer_quadruple(unconditional_transfer_quadruple_number)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()

        program_counter = self.get_program_counter()
        self.fill_control_transfer_quadruple(fill_quadruple_number, program_counter)

    
    def p_parsed_while(self, p):
        '''parsed_while :'''
        self.push_current_count_jump_stack()

    
    def p_parsed_while_expr(self, p):
        '''parsed_while_expr :'''
        operator = Operator.GOTOF
        boolean_variable = self.pop_operand_stack()

        quadruple = self.generate_empty_conditional_control_transfer_quadruple(operator, boolean_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()
        self.push_previous_count_jump_stack()

    
    def p_for_1(self, p):
        '''for : FROM LPAREN for_index COLON for_limit COLON for_step RPAREN instruction_block'''
        function_id = self.get_function_scope()

        step_variable = self.pop_operand_stack()
        index_variable = self.pop_operand_stack()
        result_type = Type.INT
        operator = Operator.PLUS

        updated_index_variable = self.create_function_temporal_variable(function_id, result_type)
        self.increment_function_temporal_counter(function_id, result_type)

        addition_quadruple = self.generate_arithmetic_quadruple(operator, index_variable, step_variable, updated_index_variable)
        self.insert_quadruple(addition_quadruple)
        self.increment_program_counter()

        assignment_quadruple = self.generate_assignment_quadruple(updated_index_variable, index_variable)
        self.insert_quadruple(assignment_quadruple)
        self.increment_program_counter()

        fill_quadruple_number = self.pop_jump_stack()
        unconditional_transfer_quadruple_number = self.pop_jump_stack()

        quadruple = self.generate_filled_unconditional_control_transfer_quadruple(unconditional_transfer_quadruple_number)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()

        program_counter = self.get_program_counter()
        self.fill_control_transfer_quadruple(fill_quadruple_number, program_counter)

    
    def p_for_2(self, p):
        '''for : FROM LPAREN for_index COLON for_limit for_no_step RPAREN instruction_block'''
        function_id = self.get_function_scope()

        step_variable = self.pop_operand_stack()
        index_variable = self.pop_operand_stack()
        result_type = Type.INT
        operator = Operator.PLUS

        updated_index_variable = self.create_function_temporal_variable(function_id, result_type)
        self.increment_function_temporal_counter(function_id, result_type)

        addition_quadruple = self.generate_arithmetic_quadruple(operator, index_variable, step_variable, updated_index_variable)
        self.insert_quadruple(addition_quadruple)
        self.increment_program_counter()

        assignment_quadruple = self.generate_assignment_quadruple(updated_index_variable, index_variable)
        self.insert_quadruple(assignment_quadruple)
        self.increment_program_counter()

        fill_quadruple_number = self.pop_jump_stack()
        unconditional_transfer_quadruple_number = self.pop_jump_stack()

        quadruple = self.generate_filled_unconditional_control_transfer_quadruple(unconditional_transfer_quadruple_number)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()

        program_counter = self.get_program_counter()
        self.fill_control_transfer_quadruple(fill_quadruple_number, program_counter)
        

    def p_for_index_1(self, p):
        '''for_index : ID ASGMT CONST_INT'''
        index_variable_id = p[1]
        function_id = self.get_function_scope()
        index_variable = self.get_function_variable(function_id, index_variable_id)

        initial_value = p[3]
        initial_value_type = Type.INT
        initial_value_variable = self.create_function_constant_variable(function_id, initial_value_type)
        self.increment_function_constant_counter(function_id, initial_value_type)

        initial_value_storage_quadruple = self.generate_constant_storage_quadruple(initial_value, initial_value_variable)
        self.insert_quadruple(initial_value_storage_quadruple)
        self.increment_program_counter()

        operator = Operator.ASGMT
        result_type = self.get_operation_result_type(index_variable, initial_value_variable, operator)

        if result_type == Type.ERROR:
            raise TypeMismatchError()

        assignment_quadruple = self.generate_assignment_quadruple(initial_value_variable, index_variable)
        self.insert_quadruple(assignment_quadruple)
        self.increment_program_counter()

        self.push_operand_stack(index_variable)

    
    def p_for_index_2(self, p):
        '''for_index : ID ASGMT MINUS CONST_INT'''
        index_variable_id = p[1]
        function_id = self.get_function_scope()
        index_variable = self.get_function_variable(function_id, index_variable_id)

        absolute_initial_value = p[4]
        initial_value_type = Type.INT
        absolute_initial_value_variable = self.create_function_temporal_variable(function_id, initial_value_type)
        self.increment_function_temporal_counter(function_id, initial_value_type)

        absolute_initial_value_storage_quadruple = self.generate_constant_storage_quadruple(absolute_initial_value, absolute_initial_value_variable)
        self.insert_quadruple(absolute_initial_value_storage_quadruple)
        self.increment_program_counter()

        initial_value_variable = self.create_function_constant_variable(function_id, initial_value_type)
        self.increment_function_constant_counter(function_id, initial_value_type)

        unary_minus_operator = Operator.UNARY_MINUS
        unary_minus_quadruple = self.generate_unary_arithmetic_quadruple(unary_minus_operator, absolute_initial_value_variable, initial_value_variable)
        self.insert_quadruple(unary_minus_quadruple)
        self.increment_program_counter()

        operator = Operator.ASGMT
        result_type = self.get_operation_result_type(index_variable, initial_value_variable, operator)

        if result_type == Type.ERROR:
            raise TypeMismatchError()

        assignment_quadruple = self.generate_assignment_quadruple(initial_value_variable, index_variable)
        self.insert_quadruple(assignment_quadruple)
        self.increment_program_counter()

        self.push_operand_stack(index_variable)

    
    def p_for_limit_1(self, p):
        '''for_limit : CONST_INT'''
        function_id = self.get_function_scope()

        limit_type = Type.INT
        limit_value = p[1]
        limit_variable = self.create_function_constant_variable(function_id, limit_type)
        self.increment_function_constant_counter(function_id, limit_type)

        limit_storage_quadruple = self.generate_constant_storage_quadruple(limit_value, limit_variable)
        self.insert_quadruple(limit_storage_quadruple)
        self.increment_program_counter()

        self.push_operand_stack(limit_variable)

    
    def p_for_limit_2(self, p):
        '''for_limit : MINUS CONST_INT'''
        function_id = self.get_function_scope()

        limit_type = Type.INT
        absolute_limit_value = p[2]
        absolute_limit_variable = self.create_function_temporal_variable(function_id, limit_type)
        self.increment_function_temporal_counter(function_id, limit_type)

        absolute_limit_storage_quadruple = self.generate_constant_storage_quadruple(absolute_limit_value, absolute_limit_variable)
        self.insert_quadruple(absolute_limit_storage_quadruple)
        self.increment_program_counter()

        limit_variable = self.create_function_constant_variable(function_id, limit_type)
        self.increment_function_constant_counter(function_id, limit_type)

        unary_minus_operator = Operator.UNARY_MINUS
        quadruple = self.generate_unary_arithmetic_quadruple(unary_minus_operator, absolute_limit_variable, limit_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()

        self.push_operand_stack(limit_variable)


    def p_for_no_step(self, p):
        '''for_no_step :'''
        function_id = self.get_function_scope()

        step_type = Type.INT
        step_value = '1'
        step_variable = self.create_function_constant_variable(function_id, step_type)
        self.increment_function_constant_counter(function_id, step_type)

        step_storage_quadruple = self.generate_constant_storage_quadruple(step_value, step_variable)
        self.insert_quadruple(step_storage_quadruple)
        self.increment_program_counter()

        limit_variable = self.pop_operand_stack()
        index_variable = self.pop_operand_stack()
        
        boolean_type = Type.BOOL
        boolean_variable = self.create_function_temporal_variable(function_id, boolean_type)
        self.increment_function_temporal_counter(function_id, boolean_type)

        self.push_current_count_jump_stack()
        relational_operator = Operator.LTHAN_EQUAL
        relational_quadruple = self.generate_relational_quadruple(relational_operator, index_variable, limit_variable, boolean_variable)
        self.insert_quadruple(relational_quadruple)
        self.increment_program_counter()

        control_transfer_operator = Operator.GOTOF
        control_transfer_quadruple = self.generate_empty_conditional_control_transfer_quadruple(control_transfer_operator, boolean_variable)
        self.insert_quadruple(control_transfer_quadruple)
        self.increment_program_counter()

        self.push_previous_count_jump_stack()

        self.push_operand_stack(index_variable)
        self.push_operand_stack(step_variable)

    
    def p_for_step_1(self, p):
        '''for_step : CONST_INT'''
        function_id = self.get_function_scope()

        step_type = Type.INT
        step_value = p[1]
        step_variable = self.create_function_constant_variable(function_id, step_type)
        self.increment_function_constant_counter(function_id, step_type)

        step_storage_quadruple = self.generate_constant_storage_quadruple(step_value, step_variable)
        self.insert_quadruple(step_storage_quadruple)
        self.increment_program_counter()

        limit_variable = self.pop_operand_stack()
        index_variable = self.pop_operand_stack()
        
        boolean_type = Type.BOOL
        boolean_variable = self.create_function_temporal_variable(function_id, boolean_type)
        self.increment_function_temporal_counter(function_id, boolean_type)

        self.push_current_count_jump_stack()
        relational_operator = Operator.LTHAN_EQUAL
        relational_quadruple = self.generate_relational_quadruple(relational_operator, index_variable, limit_variable, boolean_variable)
        self.insert_quadruple(relational_quadruple)
        self.increment_program_counter()

        control_transfer_operator = Operator.GOTOF
        control_transfer_quadruple = self.generate_empty_conditional_control_transfer_quadruple(control_transfer_operator, boolean_variable)
        self.insert_quadruple(control_transfer_quadruple)
        self.increment_program_counter()

        self.push_previous_count_jump_stack()

        self.push_operand_stack(index_variable)
        self.push_operand_stack(step_variable)

    
    def p_for_step_2(self, p):
        '''for_step : MINUS CONST_INT'''
        function_id = self.get_function_scope()

        step_type = Type.INT
        absolute_step_value = p[2]
        absolute_step_variable = self.create_function_temporal_variable(function_id, step_type)
        self.increment_function_temporal_counter(function_id, step_type)
        
        absolute_step_storage_quadruple = self.generate_constant_storage_quadruple(absolute_step_value, absolute_step_variable)
        self.insert_quadruple(absolute_step_storage_quadruple)
        self.increment_program_counter()

        step_variable = self.create_function_constant_variable(function_id, step_type)
        self.increment_function_constant_counter(function_id, step_type)

        unary_minus_operator = Operator.UNARY_MINUS
        unary_minus_quadruple = self.generate_unary_arithmetic_quadruple(unary_minus_operator, absolute_step_variable, step_variable)
        self.insert_quadruple(unary_minus_quadruple)
        self.increment_program_counter()

        limit_variable = self.pop_operand_stack()
        index_variable = self.pop_operand_stack()
        
        boolean_type = Type.BOOL
        boolean_variable = self.create_function_temporal_variable(function_id, boolean_type)
        self.increment_function_temporal_counter(function_id, boolean_type)

        self.push_current_count_jump_stack()
        relational_operator = Operator.GTHAN_EQUAL
        relational_quadruple = self.generate_relational_quadruple(relational_operator, index_variable, limit_variable, boolean_variable)
        self.insert_quadruple(relational_quadruple)
        self.increment_program_counter()

        control_transfer_operator = Operator.GOTOF
        control_transfer_quadruple = self.generate_empty_conditional_control_transfer_quadruple(control_transfer_operator, boolean_variable)
        self.insert_quadruple(control_transfer_quadruple)
        self.increment_program_counter()

        self.push_previous_count_jump_stack()

        self.push_operand_stack(index_variable)
        self.push_operand_stack(step_variable)

    
    def p_return_1(self, p):
        '''return : RETURN expr SEMI'''
        function_id = self.get_function_scope()
        function_return_type = self.get_function_return_type(function_id)

        return_variable = self.pop_operand_stack()
        return_variable_type = return_variable.get_type()

        if return_variable_type != function_return_type:
            raise IncorrectFunctionReturnTypeException()

        function_global_variable = self.get_global_variable(function_id)

        return_value_quadruple = self.generate_return_value_quadruple(return_variable, function_global_variable)
        self.insert_quadruple(return_value_quadruple)
        self.increment_program_counter()


    def p_return_2(self, p):
        '''return : RETURN SEMI'''
        function_id = self.get_function_scope()
        function_return_type = self.get_function_return_type(function_id)

        return_variable_type = Type.VOID

        if return_variable_type != function_return_type:
            raise IncorrectFunctionReturnTypeException()

        return_void_quadruple = self.generate_return_void_quadruple()
        self.insert_quadruple(return_void_quadruple)
        self.increment_program_counter()


    def p_expr_1(self, p):
        '''expr : expr OR and_expr'''


    def p_expr_2(self, p):
        '''expr : and_expr'''


    def p_and_expr_1(self, p):
        '''and_expr : equality_expr AND equality_expr'''


    def p_and_expr_2(self, p):
        '''and_expr : equality_expr'''


    def p_equality_expr_1(self, p):
        '''equality_expr : relational_expr EQUAL parsed_equal relational_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.EQUAL:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_relational_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_equal(self, p):
        '''parsed_equal :'''
        self.operator_stack.push(Operator.EQUAL)


    def p_equality_expr_2(self, p):
        '''equality_expr : relational_expr NEQUAL parsed_nequal relational_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.NEQUAL:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_relational_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_nequal(self, p):
        '''parsed_nequal :'''
        self.operator_stack.push(Operator.NEQUAL)


    def p_equality_expr_3(self, p):
        '''equality_expr : relational_expr'''


    def p_relational_expr_1(self, p):
        '''relational_expr : additive_expr LTHAN_EQUAL parsed_lthan_equal additive_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.LTHAN_EQUAL:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_relational_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_lthan_equal(self, p):
        '''parsed_lthan_equal :'''
        self.operator_stack.push(Operator.LTHAN_EQUAL)

    
    def p_relational_expr_2(self, p):
        '''relational_expr : additive_expr LTHAN parsed_lthan additive_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.LTHAN:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_relational_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_lthan(self, p):
        '''parsed_lthan :'''
        self.operator_stack.push(Operator.LTHAN)

    
    def p_relational_expr_3(self, p):
        '''relational_expr : additive_expr GTHAN_EQUAL parsed_gthan_equal additive_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.GTHAN_EQUAL:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_relational_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_gthan_equal(self, p):
        '''parsed_gthan_equal :'''
        self.operator_stack.push(Operator.GTHAN_EQUAL)

    
    def p_relational_expr_4(self, p):
        '''relational_expr : additive_expr GTHAN parsed_gthan additive_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.GTHAN:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_relational_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_gthan(self, p):
        '''parsed_gthan :'''
        self.operator_stack.push(Operator.GTHAN)

    
    def p_relational_expr_5(self, p):
        '''relational_expr : additive_expr'''


    def p_additive_expr_1(self, p):
        '''additive_expr : additive_expr PLUS parsed_plus multiplicative_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.PLUS:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_arithmetic_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)
    

    def p_parsed_plus(self, p):
        '''parsed_plus :'''
        self.operator_stack.push(Operator.PLUS)

    
    def p_additive_expr_2(self, p):
        '''additive_expr : additive_expr MINUS parsed_minus multiplicative_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.MINUS:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_arithmetic_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_minus(self, p):
        '''parsed_minus :'''
        self.operator_stack.push(Operator.MINUS)

    
    def p_additive_expr_3(self, p):
        '''additive_expr : multiplicative_expr'''


    def p_multiplicative_expr_1(self, p):
        '''multiplicative_expr : multiplicative_expr TIMES parsed_times unary_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.TIMES:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_arithmetic_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_times(self, p):
        '''parsed_times :'''
        self.operator_stack.push(Operator.TIMES)

    
    def p_multiplicative_expr_2(self, p):
        '''multiplicative_expr : multiplicative_expr DIVIDE parsed_divide unary_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.DIVIDE:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_arithmetic_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_divide(self, p):
        '''parsed_divide :'''
        self.operator_stack.push(Operator.DIVIDE)


    def p_multiplicative_expr_3(self, p):
        '''multiplicative_expr : multiplicative_expr MODULO parsed_modulo unary_expr'''
        function_id = self.get_function_scope()
        operator = self.operator_stack.top()
        if operator == Operator.MODULO:
            right_operand = self.pop_operand_stack()
            left_operand = self.pop_operand_stack()
            self.pop_operator_stack()

            result_type = self.get_operation_result_type(left_operand, right_operand, operator)
            if (result_type == Type.ERROR):
                raise TypeMismatchError()

            temporal_storage_variable = self.create_function_temporal_variable(function_id, result_type)
            self.increment_function_temporal_counter(function_id, result_type)

            quadruple = self.generate_arithmetic_quadruple(operator, left_operand, right_operand, temporal_storage_variable)
            self.insert_quadruple(quadruple)
            self.increment_program_counter()
            self.push_operand_stack(temporal_storage_variable)

    
    def p_parsed_modulo(self, p):
        '''parsed_modulo :'''
        self.operator_stack.push(Operator.MODULO)


    def p_multiplicative_expr_4(self, p):
        '''multiplicative_expr : unary_expr'''

    
    def p_unary_expr_1(self, p):
        '''unary_expr : MINUS postfix_expr'''
        operator = Operator.UNARY_MINUS
        value_variable = self.pop_operand_stack()

        quadruple = self.generate_unary_arithmetic_quadruple(operator, value_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()

    
    def p_unary_expr_2(self, p):
        '''unary_expr : PLUS postfix_expr'''
        operator = Operator.PLUS
        value_variable = self.pop_operand_stack()

        quadruple = self.generate_unary_arithmetic_quadruple(operator, value_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()

    
    def p_unary_expr_3(self, p):
        '''unary_expr : NOT postfix_expr'''

    
    def p_unary_expr_4(self, p):
        '''unary_expr : postfix_expr'''

    
    def p_postfix_expr_1(self, p):
        '''postfix_expr : LPAREN expr RPAREN'''

    
    def p_postfix_expr_2(self, p):
        '''postfix_expr : variable_access'''

    
    def p_postfix_expr_3(self, p):
        '''postfix_expr : function_call'''

    
    def p_postfix_expr_4(self, p):
        '''postfix_expr : constant'''


    def p_constant_1(self, p):
        '''constant : CONST_INT'''
        function_id = self.get_function_scope()
        constant_value = p[1]
        constant_type = Type.INT

        constant_storage_variable = self.create_function_constant_variable(function_id, constant_type)
        self.increment_function_constant_counter(function_id, constant_type)

        quadruple = self.generate_constant_storage_quadruple(constant_value, constant_storage_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()
        self.push_operand_stack(constant_storage_variable)

                
    def p_constant_2(self, p):
        '''constant : CONST_REAL'''
        function_id = self.get_function_scope()
        constant_value = p[1]
        constant_type = Type.REAL

        constant_storage_variable = self.create_function_constant_variable(function_id, constant_type)
        self.increment_function_constant_counter(function_id, constant_type)

        quadruple = self.generate_constant_storage_quadruple(constant_value, constant_storage_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()
        self.push_operand_stack(constant_storage_variable)


    def p_constant_3(self, p):
        '''constant : CONST_CHAR'''
        function_id = self.get_function_scope()
        constant_value = p[1]
        constant_type = Type.CHAR

        constant_storage_variable = self.create_function_constant_variable(function_id, constant_type)
        self.increment_function_constant_counter(function_id, constant_type)

        quadruple = self.generate_constant_storage_quadruple(constant_value, constant_storage_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()
        self.push_operand_stack(constant_storage_variable)


    def p_constant_4(self, p):
        '''constant : CONST_STRING'''
        function_id = self.get_function_scope()
        constant_value = p[1]
        constant_type = Type.STRING

        constant_storage_variable = self.create_function_constant_variable(function_id, constant_type)
        self.increment_function_constant_counter(function_id, constant_type)

        quadruple = self.generate_constant_storage_quadruple(constant_value, constant_storage_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()
        self.push_operand_stack(constant_storage_variable)

    
    def p_constant_5(self, p):
        '''constant : constant_bool'''
        function_id = self.get_function_scope()
        constant_value = p[1]
        constant_type = Type.BOOL

        constant_storage_variable = self.create_function_constant_variable(function_id, constant_type)
        self.increment_function_constant_counter(function_id, constant_type)

        quadruple = self.generate_constant_storage_quadruple(constant_value, constant_storage_variable)
        self.insert_quadruple(quadruple)
        self.increment_program_counter()
        self.push_operand_stack(constant_storage_variable)

    
    def p_constant_bool_1(self, p):
        '''constant_bool : TRUE'''
        p[0] = Boolean.TRUE

    
    def p_constant_bool_2(self, p):
        '''constant_bool : FALSE'''
        p[0] = Boolean.FALSE

    
    def p_type_1(self, p):
        '''type : INT'''
        p[0] = Type.INT


    def p_type_2(self, p):
        '''type : REAL'''
        p[0] = Type.REAL


    def p_type_3(self, p):
        '''type : CHAR'''
        p[0] = Type.CHAR


    def p_type_4(self, p):
        '''type : BOOL'''
        p[0] = Type.BOOL

    
    def p_empty(self, p):
        'empty :'
        pass


    def p_error(self, p):
        if p:
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
            raise SyntaxError('Syntax error at token', p)
        else:
          raise SyntaxError('Error at EOF')


class TypeMismatchError(RuntimeError):
    pass


class SyntaxError(RuntimeError):
    pass
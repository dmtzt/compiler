
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASGMT BOOL CHAR COLON COMMA CONST_CHAR CONST_INT CONST_REAL CONST_STRING DIVIDE ELSE EQUAL FALSE FROM FUNCTION GLOBAL GTHAN GTHAN_EQUAL ID IF INT LBRACE LBRACKET LOCAL LPAREN LTHAN LTHAN_EQUAL MINUS MODULO NEQUAL NOT OR PLUS PRINT RBRACE RBRACKET READ REAL RETURN RPAREN SEMI START TIMES TRUE VARIABLES VOID WHILEprogram : init startinit :start : global_variables_declaration functions_definition entry_point_definitionstart : global_variables_declaration entry_point_definitionstart : functions_definition entry_point_definitionstart : entry_point_definitionglobal_variables_declaration : GLOBAL parsed_global_scope variables_declarationparsed_global_scope :functions_definition : functions_definition single_function_definitionfunctions_definition : single_function_definitionsingle_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_blocksingle_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN function_definition_params RPAREN instruction_blocksingle_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN RPAREN local_variables_declaration instruction_blocksingle_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN RPAREN instruction_blocksingle_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_blocksingle_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN function_definition_params RPAREN instruction_blocksingle_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN RPAREN local_variables_declaration instruction_blocksingle_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN RPAREN instruction_blockparsed_function_id :parsed_function_return_type :parsed_function_void_return_type  :function_definition_params : function_definition_params COMMA single_function_definition_paramfunction_definition_params : single_function_definition_paramsingle_function_definition_param : type IDentry_point_definition : START parsed_main_id LPAREN RPAREN local_variables_declaration instruction_blockentry_point_definition : START parsed_main_id LPAREN RPAREN instruction_blockparsed_main_id :local_variables_declaration : LOCAL variables_declarationvariables_declaration : VARIABLES COLON distinct_type_variables_declarationdistinct_type_variables_declaration : distinct_type_variables_declaration shared_type_variables_declarationdistinct_type_variables_declaration : shared_type_variables_declarationshared_type_variables_declaration : type parsed_type shared_type_variables_declaration_list SEMIparsed_type :shared_type_variables_declaration_list : shared_type_variables_declaration_list COMMA single_variable_declarationshared_type_variables_declaration_list : single_variable_declarationsingle_variable_declaration : ID dim_definition dim_definitionsingle_variable_declaration : ID dim_definitionsingle_variable_declaration : IDdim_definition : LBRACKET CONST_INT RBRACKETinstruction_block : LBRACE statements RBRACEinstruction_block : LBRACE RBRACEstatements : statements single_statementstatements : single_statementsingle_statement : assignmentsingle_statement : function_call_stmtsingle_statement : printsingle_statement : conditionalsingle_statement : loopsingle_statement : returnassignment : variable_access ASGMT expr SEMIassignment : variable_access ASGMT READ LPAREN RPAREN SEMIvariable_access : ID parsed_id_variable_access dims_accessparsed_id_variable_access :dims_access : single_dim_access single_dim_accessdims_access : single_dim_accessdims_access : emptysingle_dim_access : LBRACKET expr RBRACKETfunction_call_stmt : function_call SEMIfunction_call : ID parsed_function_call_id LPAREN function_call_params RPARENfunction_call : ID parsed_function_call_id LPAREN RPARENparsed_function_call_id :function_call_params : function_call_params COMMA single_function_call_paramfunction_call_params : single_function_call_paramsingle_function_call_param : exprprint : PRINT LPAREN print_params RPAREN SEMIprint : PRINT LPAREN RPAREN SEMIprint_params : print_params COMMA single_print_paramprint_params : single_print_paramsingle_print_param : exprconditional : IF LPAREN expr RPAREN parsed_if_expr instruction_block ELSE parsed_else instruction_blockconditional : IF LPAREN expr RPAREN parsed_if_expr instruction_blockparsed_if_expr :parsed_else :loop : whileloop : forwhile : WHILE parsed_while LPAREN expr parsed_while_expr RPAREN instruction_blockparsed_while :parsed_while_expr :for : FROM LPAREN for_index COLON for_limit COLON for_step RPAREN instruction_blockfor : FROM LPAREN for_index COLON for_limit for_no_step RPAREN instruction_blockfor_index : ID ASGMT CONST_INTfor_index : ID ASGMT MINUS CONST_INTfor_limit : CONST_INTfor_limit : MINUS CONST_INTfor_no_step :for_step : CONST_INTfor_step : MINUS CONST_INTreturn : RETURN expr SEMIreturn : RETURN SEMIexpr : expr OR and_exprexpr : and_exprand_expr : equality_expr AND equality_exprand_expr : equality_exprequality_expr : relational_expr EQUAL parsed_equal relational_exprparsed_equal :equality_expr : relational_expr NEQUAL parsed_nequal relational_exprparsed_nequal :equality_expr : relational_exprrelational_expr : additive_expr LTHAN_EQUAL parsed_lthan_equal additive_exprparsed_lthan_equal :relational_expr : additive_expr LTHAN parsed_lthan additive_exprparsed_lthan :relational_expr : additive_expr GTHAN_EQUAL parsed_gthan_equal additive_exprparsed_gthan_equal :relational_expr : additive_expr GTHAN parsed_gthan additive_exprparsed_gthan :relational_expr : additive_expradditive_expr : additive_expr PLUS parsed_plus multiplicative_exprparsed_plus :additive_expr : additive_expr MINUS parsed_minus multiplicative_exprparsed_minus :additive_expr : multiplicative_exprmultiplicative_expr : multiplicative_expr TIMES parsed_times unary_exprparsed_times :multiplicative_expr : multiplicative_expr DIVIDE parsed_divide unary_exprparsed_divide :multiplicative_expr : multiplicative_expr MODULO parsed_modulo unary_exprparsed_modulo :multiplicative_expr : unary_exprunary_expr : MINUS postfix_exprunary_expr : PLUS postfix_exprunary_expr : NOT postfix_exprunary_expr : postfix_exprpostfix_expr : LPAREN expr RPARENpostfix_expr : variable_accesspostfix_expr : function_callpostfix_expr : constantconstant : CONST_INTconstant : CONST_REALconstant : CONST_CHARconstant : CONST_STRINGconstant : constant_boolconstant_bool : TRUEconstant_bool : FALSEtype : INTtype : REALtype : CHARtype : BOOLempty :'
    
_lr_action_items = {'GLOBAL':([0,2,],[-2,7,]),'START':([0,2,4,5,8,11,14,24,33,34,42,47,70,109,150,153,187,189,191,192,218,219,],[-2,9,9,9,-10,9,-9,-7,-29,-31,-30,-41,-40,-32,-14,-18,-12,-13,-16,-17,-11,-15,]),'FUNCTION':([0,2,4,5,8,11,14,24,33,34,42,47,70,109,150,153,187,189,191,192,218,219,],[-2,10,10,10,-10,10,-9,-7,-29,-31,-30,-41,-40,-32,-14,-18,-12,-13,-16,-17,-11,-15,]),'$end':([1,3,6,12,13,23,37,44,47,70,],[0,-1,-6,-4,-5,-3,-26,-25,-41,-40,]),'VARIABLES':([7,15,38,],[-8,25,25,]),'LPAREN':([9,16,31,32,40,41,57,58,61,62,63,64,72,74,75,82,84,87,88,100,101,114,121,122,123,124,125,126,127,128,129,130,132,133,134,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[-27,26,-19,-19,65,66,74,75,88,-61,-77,102,88,88,88,88,88,88,88,142,143,158,88,88,-95,-97,-100,-102,-104,-106,-109,-111,-114,-116,-118,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'VOID':([10,],[18,]),'INT':([10,29,33,34,42,65,66,109,148,],[19,19,19,-31,-30,19,19,-32,19,]),'REAL':([10,29,33,34,42,65,66,109,148,],[20,20,20,-31,-30,20,20,-32,20,]),'CHAR':([10,29,33,34,42,65,66,109,148,],[21,21,21,-31,-30,21,21,-32,21,]),'BOOL':([10,29,33,34,42,65,66,109,148,],[22,22,22,-31,-30,22,22,-32,22,]),'ID':([17,18,19,20,21,22,27,28,35,39,43,46,47,48,49,50,51,52,53,54,59,60,61,70,71,72,73,74,75,77,82,84,87,88,102,103,110,120,121,122,123,124,125,126,127,128,129,130,132,133,134,141,142,143,157,160,161,165,166,167,168,169,170,171,172,173,174,175,195,211,220,221,229,237,238,239,],[-20,-21,-135,-136,-137,-138,31,32,-33,62,69,62,-41,-43,-44,-45,-46,-47,-48,-49,-74,-75,62,-40,-42,62,-58,62,62,-89,62,62,62,62,145,146,69,-88,62,62,-95,-97,-100,-102,-104,-106,-109,-111,-114,-116,-118,62,62,62,-50,62,-66,62,62,62,62,62,62,62,62,62,62,62,-65,62,-51,-71,-76,-80,-70,-79,]),'COLON':([25,144,213,214,216,226,227,],[29,184,224,-83,-81,-84,-82,]),'RPAREN':([26,62,65,66,74,78,79,80,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,104,106,107,115,117,118,119,131,135,136,137,138,139,140,142,146,158,163,164,176,177,179,180,181,182,183,188,196,198,199,200,201,202,203,204,205,206,207,208,209,210,212,213,214,222,225,226,230,231,236,],[30,-53,105,108,116,-91,-93,-98,-107,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,147,-23,151,159,-68,-69,162,-121,-120,-122,176,-52,-55,-56,180,-24,194,-90,-92,-124,-54,210,-60,-63,-64,-78,-22,-67,-94,-96,-99,-101,-103,-105,-108,-110,-113,-115,-117,-57,-59,223,-85,-83,-62,233,-84,235,-86,-87,]),'LOCAL':([30,105,108,147,151,],[38,38,38,38,38,]),'LBRACE':([30,33,34,36,42,45,105,108,109,147,149,151,152,162,186,190,197,223,228,233,234,235,],[39,-29,-31,39,-30,-28,39,39,-32,39,39,39,39,-72,39,39,39,39,-73,39,39,39,]),'RBRACE':([39,46,47,48,49,50,51,52,53,54,59,60,70,71,73,77,120,157,161,195,220,221,229,237,238,239,],[47,70,-41,-43,-44,-45,-46,-47,-48,-49,-74,-75,-40,-42,-58,-89,-88,-50,-66,-65,-51,-71,-76,-80,-70,-79,]),'PRINT':([39,46,47,48,49,50,51,52,53,54,59,60,70,71,73,77,120,157,161,195,220,221,229,237,238,239,],[57,57,-41,-43,-44,-45,-46,-47,-48,-49,-74,-75,-40,-42,-58,-89,-88,-50,-66,-65,-51,-71,-76,-80,-70,-79,]),'IF':([39,46,47,48,49,50,51,52,53,54,59,60,70,71,73,77,120,157,161,195,220,221,229,237,238,239,],[58,58,-41,-43,-44,-45,-46,-47,-48,-49,-74,-75,-40,-42,-58,-89,-88,-50,-66,-65,-51,-71,-76,-80,-70,-79,]),'RETURN':([39,46,47,48,49,50,51,52,53,54,59,60,70,71,73,77,120,157,161,195,220,221,229,237,238,239,],[61,61,-41,-43,-44,-45,-46,-47,-48,-49,-74,-75,-40,-42,-58,-89,-88,-50,-66,-65,-51,-71,-76,-80,-70,-79,]),'WHILE':([39,46,47,48,49,50,51,52,53,54,59,60,70,71,73,77,120,157,161,195,220,221,229,237,238,239,],[63,63,-41,-43,-44,-45,-46,-47,-48,-49,-74,-75,-40,-42,-58,-89,-88,-50,-66,-65,-51,-71,-76,-80,-70,-79,]),'FROM':([39,46,47,48,49,50,51,52,53,54,59,60,70,71,73,77,120,157,161,195,220,221,229,237,238,239,],[64,64,-41,-43,-44,-45,-46,-47,-48,-49,-74,-75,-40,-42,-58,-89,-88,-50,-66,-65,-51,-71,-76,-80,-70,-79,]),'ELSE':([47,70,221,],[-41,-40,228,]),'ASGMT':([55,62,99,138,139,140,145,177,209,],[72,-53,-139,-52,-55,-56,185,-54,-57,]),'SEMI':([56,61,62,67,68,69,76,78,79,80,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,111,113,116,131,135,136,138,139,140,154,155,159,163,164,176,177,180,193,194,198,199,200,201,202,203,204,205,206,207,208,209,210,],[73,77,-53,109,-35,-38,120,-91,-93,-98,-107,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-37,157,161,-121,-120,-122,-52,-55,-56,-34,-36,195,-90,-92,-124,-54,-60,-39,220,-94,-96,-99,-101,-103,-105,-108,-110,-113,-115,-117,-57,-59,]),'MINUS':([61,62,72,74,75,81,83,85,86,88,89,90,91,92,93,94,95,96,97,98,99,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,176,177,180,184,185,200,201,202,203,204,205,206,207,208,209,210,211,224,],[84,-53,84,84,84,130,-112,-119,-123,84,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,84,84,-95,-97,-100,-102,-104,-106,-109,-111,-121,-114,-116,-118,-120,-122,-52,-55,-56,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,-124,-54,-60,215,217,130,130,130,130,-108,-110,-113,-115,-117,-57,-59,84,232,]),'PLUS':([61,62,72,74,75,81,83,85,86,88,89,90,91,92,93,94,95,96,97,98,99,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,176,177,180,200,201,202,203,204,205,206,207,208,209,210,211,],[82,-53,82,82,82,129,-112,-119,-123,82,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,82,82,-95,-97,-100,-102,-104,-106,-109,-111,-121,-114,-116,-118,-120,-122,-52,-55,-56,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,-124,-54,-60,129,129,129,129,-108,-110,-113,-115,-117,-57,-59,82,]),'NOT':([61,72,74,75,88,121,122,123,124,125,126,127,128,129,130,132,133,134,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[87,87,87,87,87,87,87,-95,-97,-100,-102,-104,-106,-109,-111,-114,-116,-118,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,]),'CONST_INT':([61,72,74,75,82,84,87,88,112,121,122,123,124,125,126,127,128,129,130,132,133,134,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,184,185,211,215,217,224,232,],[92,92,92,92,92,92,92,92,156,92,92,-95,-97,-100,-102,-104,-106,-109,-111,-114,-116,-118,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,214,216,92,226,227,231,236,]),'CONST_REAL':([61,72,74,75,82,84,87,88,121,122,123,124,125,126,127,128,129,130,132,133,134,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[93,93,93,93,93,93,93,93,93,93,-95,-97,-100,-102,-104,-106,-109,-111,-114,-116,-118,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'CONST_CHAR':([61,72,74,75,82,84,87,88,121,122,123,124,125,126,127,128,129,130,132,133,134,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[94,94,94,94,94,94,94,94,94,94,-95,-97,-100,-102,-104,-106,-109,-111,-114,-116,-118,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'CONST_STRING':([61,72,74,75,82,84,87,88,121,122,123,124,125,126,127,128,129,130,132,133,134,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[95,95,95,95,95,95,95,95,95,95,-95,-97,-100,-102,-104,-106,-109,-111,-114,-116,-118,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'TRUE':([61,72,74,75,82,84,87,88,121,122,123,124,125,126,127,128,129,130,132,133,134,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[97,97,97,97,97,97,97,97,97,97,-95,-97,-100,-102,-104,-106,-109,-111,-114,-116,-118,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,]),'FALSE':([61,72,74,75,82,84,87,88,121,122,123,124,125,126,127,128,129,130,132,133,134,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[98,98,98,98,98,98,98,98,98,98,-95,-97,-100,-102,-104,-106,-109,-111,-114,-116,-118,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'LBRACKET':([62,69,99,111,139,193,209,],[-53,112,141,112,141,-39,-57,]),'TIMES':([62,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,204,205,206,207,208,209,210,],[-53,132,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,132,132,-113,-115,-117,-57,-59,]),'DIVIDE':([62,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,204,205,206,207,208,209,210,],[-53,133,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,133,133,-113,-115,-117,-57,-59,]),'MODULO':([62,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,204,205,206,207,208,209,210,],[-53,134,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,134,134,-113,-115,-117,-57,-59,]),'LTHAN_EQUAL':([62,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,204,205,206,207,208,209,210,],[-53,125,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,-108,-110,-113,-115,-117,-57,-59,]),'LTHAN':([62,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,204,205,206,207,208,209,210,],[-53,126,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,-108,-110,-113,-115,-117,-57,-59,]),'GTHAN_EQUAL':([62,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,204,205,206,207,208,209,210,],[-53,127,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,-108,-110,-113,-115,-117,-57,-59,]),'GTHAN':([62,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,204,205,206,207,208,209,210,],[-53,128,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,-108,-110,-113,-115,-117,-57,-59,]),'EQUAL':([62,80,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,200,201,202,203,204,205,206,207,208,209,210,],[-53,123,-107,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,-99,-101,-103,-105,-108,-110,-113,-115,-117,-57,-59,]),'NEQUAL':([62,80,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,200,201,202,203,204,205,206,207,208,209,210,],[-53,124,-107,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,-99,-101,-103,-105,-108,-110,-113,-115,-117,-57,-59,]),'AND':([62,79,80,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,176,177,180,198,199,200,201,202,203,204,205,206,207,208,209,210,],[-53,122,-98,-107,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,-124,-54,-60,-94,-96,-99,-101,-103,-105,-108,-110,-113,-115,-117,-57,-59,]),'OR':([62,76,78,79,80,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,113,118,119,131,135,136,137,138,139,140,163,164,176,177,178,180,182,183,198,199,200,201,202,203,204,205,206,207,208,209,210,],[-53,121,-91,-93,-98,-107,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,121,121,121,-121,-120,-122,121,-52,-55,-56,-90,-92,-124,-54,121,-60,121,121,-94,-96,-99,-101,-103,-105,-108,-110,-113,-115,-117,-57,-59,]),'COMMA':([62,67,68,69,78,79,80,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,104,106,107,111,115,117,118,131,135,136,138,139,140,146,154,155,163,164,176,177,179,180,181,182,188,193,196,198,199,200,201,202,203,204,205,206,207,208,209,210,222,],[-53,110,-35,-38,-91,-93,-98,-107,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,148,-23,148,-37,160,-68,-69,-121,-120,-122,-52,-55,-56,-24,-34,-36,-90,-92,-124,-54,211,-60,-63,-64,-22,-39,-67,-94,-96,-99,-101,-103,-105,-108,-110,-113,-115,-117,-57,-59,-62,]),'RBRACKET':([62,78,79,80,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,131,135,136,138,139,140,156,163,164,176,177,178,180,198,199,200,201,202,203,204,205,206,207,208,209,210,],[-53,-91,-93,-98,-107,-112,-119,-123,-125,-126,-127,-128,-129,-130,-131,-132,-133,-134,-139,-121,-120,-122,-52,-55,-56,193,-90,-92,-124,-54,209,-60,-94,-96,-99,-101,-103,-105,-108,-110,-113,-115,-117,-57,-59,]),'READ':([72,],[114,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'init':([0,],[2,]),'start':([2,],[3,]),'global_variables_declaration':([2,],[4,]),'functions_definition':([2,4,],[5,11,]),'entry_point_definition':([2,4,5,11,],[6,12,13,23,]),'single_function_definition':([2,4,5,11,],[8,8,14,14,]),'parsed_global_scope':([7,],[15,]),'parsed_main_id':([9,],[16,]),'type':([10,29,33,65,66,148,],[17,35,35,103,103,103,]),'variables_declaration':([15,38,],[24,45,]),'parsed_function_return_type':([17,],[27,]),'parsed_function_void_return_type':([18,],[28,]),'distinct_type_variables_declaration':([29,],[33,]),'shared_type_variables_declaration':([29,33,],[34,42,]),'local_variables_declaration':([30,105,108,147,151,],[36,149,152,186,190,]),'instruction_block':([30,36,105,108,147,149,151,152,186,190,197,223,233,234,235,],[37,44,150,153,187,189,191,192,218,219,221,229,237,238,239,]),'parsed_function_id':([31,32,],[40,41,]),'parsed_type':([35,],[43,]),'statements':([39,],[46,]),'single_statement':([39,46,],[48,71,]),'assignment':([39,46,],[49,49,]),'function_call_stmt':([39,46,],[50,50,]),'print':([39,46,],[51,51,]),'conditional':([39,46,],[52,52,]),'loop':([39,46,],[53,53,]),'return':([39,46,],[54,54,]),'variable_access':([39,46,61,72,74,75,82,84,87,88,121,122,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[55,55,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'function_call':([39,46,61,72,74,75,82,84,87,88,121,122,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[56,56,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'while':([39,46,],[59,59,]),'for':([39,46,],[60,60,]),'shared_type_variables_declaration_list':([43,],[67,]),'single_variable_declaration':([43,110,],[68,154,]),'expr':([61,72,74,75,88,141,142,143,160,211,],[76,113,118,119,137,178,182,183,118,182,]),'and_expr':([61,72,74,75,88,121,141,142,143,160,211,],[78,78,78,78,78,163,78,78,78,78,78,]),'equality_expr':([61,72,74,75,88,121,122,141,142,143,160,211,],[79,79,79,79,79,79,164,79,79,79,79,79,]),'relational_expr':([61,72,74,75,88,121,122,141,142,143,160,165,166,211,],[80,80,80,80,80,80,80,80,80,80,80,198,199,80,]),'additive_expr':([61,72,74,75,88,121,122,141,142,143,160,165,166,167,168,169,170,211,],[81,81,81,81,81,81,81,81,81,81,81,81,81,200,201,202,203,81,]),'multiplicative_expr':([61,72,74,75,88,121,122,141,142,143,160,165,166,167,168,169,170,171,172,211,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,204,205,83,]),'unary_expr':([61,72,74,75,88,121,122,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,206,207,208,85,]),'postfix_expr':([61,72,74,75,82,84,87,88,121,122,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[86,86,86,86,131,135,136,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'constant':([61,72,74,75,82,84,87,88,121,122,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'constant_bool':([61,72,74,75,82,84,87,88,121,122,141,142,143,160,165,166,167,168,169,170,171,172,173,174,175,211,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'parsed_id_variable_access':([62,],[99,]),'parsed_function_call_id':([62,],[100,]),'parsed_while':([63,],[101,]),'function_definition_params':([65,66,],[104,107,]),'single_function_definition_param':([65,66,148,],[106,106,188,]),'dim_definition':([69,111,],[111,155,]),'print_params':([74,],[115,]),'single_print_param':([74,160,],[117,196,]),'dims_access':([99,],[138,]),'single_dim_access':([99,139,],[139,177,]),'empty':([99,],[140,]),'for_index':([102,],[144,]),'parsed_equal':([123,],[165,]),'parsed_nequal':([124,],[166,]),'parsed_lthan_equal':([125,],[167,]),'parsed_lthan':([126,],[168,]),'parsed_gthan_equal':([127,],[169,]),'parsed_gthan':([128,],[170,]),'parsed_plus':([129,],[171,]),'parsed_minus':([130,],[172,]),'parsed_times':([132,],[173,]),'parsed_divide':([133,],[174,]),'parsed_modulo':([134,],[175,]),'function_call_params':([142,],[179,]),'single_function_call_param':([142,211,],[181,222,]),'parsed_if_expr':([162,],[197,]),'parsed_while_expr':([183,],[212,]),'for_limit':([184,],[213,]),'for_no_step':([213,],[225,]),'for_step':([224,],[230,]),'parsed_else':([228,],[234,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> init start','program',2,'p_program','parser.py',445),
  ('init -> <empty>','init',0,'p_init','parser.py',455),
  ('start -> global_variables_declaration functions_definition entry_point_definition','start',3,'p_start_1','parser.py',466),
  ('start -> global_variables_declaration entry_point_definition','start',2,'p_start_2','parser.py',470),
  ('start -> functions_definition entry_point_definition','start',2,'p_start_3','parser.py',474),
  ('start -> entry_point_definition','start',1,'p_start_4','parser.py',478),
  ('global_variables_declaration -> GLOBAL parsed_global_scope variables_declaration','global_variables_declaration',3,'p_global_variables_declaration','parser.py',482),
  ('parsed_global_scope -> <empty>','parsed_global_scope',0,'p_parsed_global_scope','parser.py',486),
  ('functions_definition -> functions_definition single_function_definition','functions_definition',2,'p_functions_definition_1','parser.py',491),
  ('functions_definition -> single_function_definition','functions_definition',1,'p_functions_definition_2','parser.py',495),
  ('single_function_definition -> FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_block','single_function_definition',10,'p_single_function_definition_primitive_type_1','parser.py',502),
  ('single_function_definition -> FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN function_definition_params RPAREN instruction_block','single_function_definition',9,'p_single_function_definition_primitive_type_2','parser.py',506),
  ('single_function_definition -> FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN RPAREN local_variables_declaration instruction_block','single_function_definition',9,'p_single_function_definition_primitive_type_3','parser.py',510),
  ('single_function_definition -> FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN RPAREN instruction_block','single_function_definition',8,'p_single_function_definition_primitive_type_4','parser.py',514),
  ('single_function_definition -> FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_block','single_function_definition',10,'p_single_function_definition_void_type_1','parser.py',518),
  ('single_function_definition -> FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN function_definition_params RPAREN instruction_block','single_function_definition',9,'p_single_function_definition_void_type_2','parser.py',522),
  ('single_function_definition -> FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN RPAREN local_variables_declaration instruction_block','single_function_definition',9,'p_single_function_definition_void_type_3','parser.py',526),
  ('single_function_definition -> FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN RPAREN instruction_block','single_function_definition',8,'p_single_function_definition_void_type_4','parser.py',530),
  ('parsed_function_id -> <empty>','parsed_function_id',0,'p_parsed_function_id','parser.py',534),
  ('parsed_function_return_type -> <empty>','parsed_function_return_type',0,'p_parsed_function_return_type','parser.py',547),
  ('parsed_function_void_return_type -> <empty>','parsed_function_void_return_type',0,'p_parsed_function_void_return_type','parser.py',553),
  ('function_definition_params -> function_definition_params COMMA single_function_definition_param','function_definition_params',3,'p_function_definition_params_1','parser.py',559),
  ('function_definition_params -> single_function_definition_param','function_definition_params',1,'p_function_definition_params_2','parser.py',563),
  ('single_function_definition_param -> type ID','single_function_definition_param',2,'p_single_function_definition_param','parser.py',567),
  ('entry_point_definition -> START parsed_main_id LPAREN RPAREN local_variables_declaration instruction_block','entry_point_definition',6,'p_entry_point_definition_1','parser.py',583),
  ('entry_point_definition -> START parsed_main_id LPAREN RPAREN instruction_block','entry_point_definition',5,'p_entry_point_definition_2','parser.py',587),
  ('parsed_main_id -> <empty>','parsed_main_id',0,'p_parsed_main_id','parser.py',591),
  ('local_variables_declaration -> LOCAL variables_declaration','local_variables_declaration',2,'p_local_variables_declaration','parser.py',601),
  ('variables_declaration -> VARIABLES COLON distinct_type_variables_declaration','variables_declaration',3,'p_variables_declaration','parser.py',605),
  ('distinct_type_variables_declaration -> distinct_type_variables_declaration shared_type_variables_declaration','distinct_type_variables_declaration',2,'p_distinct_type_variables_declaration_1','parser.py',609),
  ('distinct_type_variables_declaration -> shared_type_variables_declaration','distinct_type_variables_declaration',1,'p_distinct_type_variables_declaration_2','parser.py',613),
  ('shared_type_variables_declaration -> type parsed_type shared_type_variables_declaration_list SEMI','shared_type_variables_declaration',4,'p_shared_type_variables_declaration','parser.py',617),
  ('parsed_type -> <empty>','parsed_type',0,'p_parsed_type','parser.py',621),
  ('shared_type_variables_declaration_list -> shared_type_variables_declaration_list COMMA single_variable_declaration','shared_type_variables_declaration_list',3,'p_shared_type_variables_declaration_list_1','parser.py',627),
  ('shared_type_variables_declaration_list -> single_variable_declaration','shared_type_variables_declaration_list',1,'p_shared_type_variables_declaration_list_2','parser.py',631),
  ('single_variable_declaration -> ID dim_definition dim_definition','single_variable_declaration',3,'p_single_variable_declaration_1','parser.py',635),
  ('single_variable_declaration -> ID dim_definition','single_variable_declaration',2,'p_single_variable_declaration_2','parser.py',639),
  ('single_variable_declaration -> ID','single_variable_declaration',1,'p_single_variable_declaration_3','parser.py',643),
  ('dim_definition -> LBRACKET CONST_INT RBRACKET','dim_definition',3,'p_dim_definition','parser.py',658),
  ('instruction_block -> LBRACE statements RBRACE','instruction_block',3,'p_instruction_block_1','parser.py',662),
  ('instruction_block -> LBRACE RBRACE','instruction_block',2,'p_instruction_block_2','parser.py',666),
  ('statements -> statements single_statement','statements',2,'p_statements_1','parser.py',670),
  ('statements -> single_statement','statements',1,'p_statements_2','parser.py',674),
  ('single_statement -> assignment','single_statement',1,'p_single_statement_1','parser.py',678),
  ('single_statement -> function_call_stmt','single_statement',1,'p_single_statement_2','parser.py',682),
  ('single_statement -> print','single_statement',1,'p_single_statement_3','parser.py',686),
  ('single_statement -> conditional','single_statement',1,'p_single_statement_4','parser.py',690),
  ('single_statement -> loop','single_statement',1,'p_single_statement_5','parser.py',694),
  ('single_statement -> return','single_statement',1,'p_single_statement_6','parser.py',698),
  ('assignment -> variable_access ASGMT expr SEMI','assignment',4,'p_assignment_1','parser.py',702),
  ('assignment -> variable_access ASGMT READ LPAREN RPAREN SEMI','assignment',6,'p_assignment_2','parser.py',718),
  ('variable_access -> ID parsed_id_variable_access dims_access','variable_access',3,'p_variable_access','parser.py',727),
  ('parsed_id_variable_access -> <empty>','parsed_id_variable_access',0,'p_parsed_id_variable_access','parser.py',731),
  ('dims_access -> single_dim_access single_dim_access','dims_access',2,'p_dims_access_1','parser.py',741),
  ('dims_access -> single_dim_access','dims_access',1,'p_dims_access_2','parser.py',745),
  ('dims_access -> empty','dims_access',1,'p_dims_access_3','parser.py',749),
  ('single_dim_access -> LBRACKET expr RBRACKET','single_dim_access',3,'p_single_dim_access','parser.py',753),
  ('function_call_stmt -> function_call SEMI','function_call_stmt',2,'p_function_call_stmt','parser.py',757),
  ('function_call -> ID parsed_function_call_id LPAREN function_call_params RPAREN','function_call',5,'p_function_call_1','parser.py',761),
  ('function_call -> ID parsed_function_call_id LPAREN RPAREN','function_call',4,'p_function_call_2','parser.py',770),
  ('parsed_function_call_id -> <empty>','parsed_function_call_id',0,'p_parsed_function_call_id','parser.py',774),
  ('function_call_params -> function_call_params COMMA single_function_call_param','function_call_params',3,'p_function_call_params_1','parser.py',785),
  ('function_call_params -> single_function_call_param','function_call_params',1,'p_function_call_params_2','parser.py',789),
  ('single_function_call_param -> expr','single_function_call_param',1,'p_single_function_call_param','parser.py',793),
  ('print -> PRINT LPAREN print_params RPAREN SEMI','print',5,'p_print_1','parser.py',804),
  ('print -> PRINT LPAREN RPAREN SEMI','print',4,'p_print_2','parser.py',808),
  ('print_params -> print_params COMMA single_print_param','print_params',3,'p_print_params_1','parser.py',812),
  ('print_params -> single_print_param','print_params',1,'p_print_params_2','parser.py',816),
  ('single_print_param -> expr','single_print_param',1,'p_single_print_param_1','parser.py',820),
  ('conditional -> IF LPAREN expr RPAREN parsed_if_expr instruction_block ELSE parsed_else instruction_block','conditional',9,'p_conditional_1','parser.py',829),
  ('conditional -> IF LPAREN expr RPAREN parsed_if_expr instruction_block','conditional',6,'p_conditional_2','parser.py',837),
  ('parsed_if_expr -> <empty>','parsed_if_expr',0,'p_parsed_if_expr','parser.py',845),
  ('parsed_else -> <empty>','parsed_else',0,'p_parsed_else','parser.py',857),
  ('loop -> while','loop',1,'p_loop_1','parser.py',870),
  ('loop -> for','loop',1,'p_loop_2','parser.py',874),
  ('while -> WHILE parsed_while LPAREN expr parsed_while_expr RPAREN instruction_block','while',7,'p_while','parser.py',878),
  ('parsed_while -> <empty>','parsed_while',0,'p_parsed_while','parser.py',891),
  ('parsed_while_expr -> <empty>','parsed_while_expr',0,'p_parsed_while_expr','parser.py',896),
  ('for -> FROM LPAREN for_index COLON for_limit COLON for_step RPAREN instruction_block','for',9,'p_for_1','parser.py',907),
  ('for -> FROM LPAREN for_index COLON for_limit for_no_step RPAREN instruction_block','for',8,'p_for_2','parser.py',938),
  ('for_index -> ID ASGMT CONST_INT','for_index',3,'p_for_index_1','parser.py',969),
  ('for_index -> ID ASGMT MINUS CONST_INT','for_index',4,'p_for_index_2','parser.py',997),
  ('for_limit -> CONST_INT','for_limit',1,'p_for_limit_1','parser.py',1033),
  ('for_limit -> MINUS CONST_INT','for_limit',2,'p_for_limit_2','parser.py',1049),
  ('for_no_step -> <empty>','for_no_step',0,'p_for_no_step','parser.py',1073),
  ('for_step -> CONST_INT','for_step',1,'p_for_step_1','parser.py',1110),
  ('for_step -> MINUS CONST_INT','for_step',2,'p_for_step_2','parser.py',1147),
  ('return -> RETURN expr SEMI','return',3,'p_return_1','parser.py',1192),
  ('return -> RETURN SEMI','return',2,'p_return_2','parser.py',1196),
  ('expr -> expr OR and_expr','expr',3,'p_expr_1','parser.py',1200),
  ('expr -> and_expr','expr',1,'p_expr_2','parser.py',1204),
  ('and_expr -> equality_expr AND equality_expr','and_expr',3,'p_and_expr_1','parser.py',1208),
  ('and_expr -> equality_expr','and_expr',1,'p_and_expr_2','parser.py',1212),
  ('equality_expr -> relational_expr EQUAL parsed_equal relational_expr','equality_expr',4,'p_equality_expr_1','parser.py',1216),
  ('parsed_equal -> <empty>','parsed_equal',0,'p_parsed_equal','parser.py',1238),
  ('equality_expr -> relational_expr NEQUAL parsed_nequal relational_expr','equality_expr',4,'p_equality_expr_2','parser.py',1243),
  ('parsed_nequal -> <empty>','parsed_nequal',0,'p_parsed_nequal','parser.py',1265),
  ('equality_expr -> relational_expr','equality_expr',1,'p_equality_expr_3','parser.py',1270),
  ('relational_expr -> additive_expr LTHAN_EQUAL parsed_lthan_equal additive_expr','relational_expr',4,'p_relational_expr_1','parser.py',1274),
  ('parsed_lthan_equal -> <empty>','parsed_lthan_equal',0,'p_parsed_lthan_equal','parser.py',1296),
  ('relational_expr -> additive_expr LTHAN parsed_lthan additive_expr','relational_expr',4,'p_relational_expr_2','parser.py',1301),
  ('parsed_lthan -> <empty>','parsed_lthan',0,'p_parsed_lthan','parser.py',1323),
  ('relational_expr -> additive_expr GTHAN_EQUAL parsed_gthan_equal additive_expr','relational_expr',4,'p_relational_expr_3','parser.py',1328),
  ('parsed_gthan_equal -> <empty>','parsed_gthan_equal',0,'p_parsed_gthan_equal','parser.py',1350),
  ('relational_expr -> additive_expr GTHAN parsed_gthan additive_expr','relational_expr',4,'p_relational_expr_4','parser.py',1355),
  ('parsed_gthan -> <empty>','parsed_gthan',0,'p_parsed_gthan','parser.py',1377),
  ('relational_expr -> additive_expr','relational_expr',1,'p_relational_expr_5','parser.py',1382),
  ('additive_expr -> additive_expr PLUS parsed_plus multiplicative_expr','additive_expr',4,'p_additive_expr_1','parser.py',1386),
  ('parsed_plus -> <empty>','parsed_plus',0,'p_parsed_plus','parser.py',1408),
  ('additive_expr -> additive_expr MINUS parsed_minus multiplicative_expr','additive_expr',4,'p_additive_expr_2','parser.py',1413),
  ('parsed_minus -> <empty>','parsed_minus',0,'p_parsed_minus','parser.py',1435),
  ('additive_expr -> multiplicative_expr','additive_expr',1,'p_additive_expr_3','parser.py',1440),
  ('multiplicative_expr -> multiplicative_expr TIMES parsed_times unary_expr','multiplicative_expr',4,'p_multiplicative_expr_1','parser.py',1444),
  ('parsed_times -> <empty>','parsed_times',0,'p_parsed_times','parser.py',1466),
  ('multiplicative_expr -> multiplicative_expr DIVIDE parsed_divide unary_expr','multiplicative_expr',4,'p_multiplicative_expr_2','parser.py',1471),
  ('parsed_divide -> <empty>','parsed_divide',0,'p_parsed_divide','parser.py',1493),
  ('multiplicative_expr -> multiplicative_expr MODULO parsed_modulo unary_expr','multiplicative_expr',4,'p_multiplicative_expr_3','parser.py',1498),
  ('parsed_modulo -> <empty>','parsed_modulo',0,'p_parsed_modulo','parser.py',1520),
  ('multiplicative_expr -> unary_expr','multiplicative_expr',1,'p_multiplicative_expr_4','parser.py',1525),
  ('unary_expr -> MINUS postfix_expr','unary_expr',2,'p_unary_expr_1','parser.py',1529),
  ('unary_expr -> PLUS postfix_expr','unary_expr',2,'p_unary_expr_2','parser.py',1539),
  ('unary_expr -> NOT postfix_expr','unary_expr',2,'p_unary_expr_3','parser.py',1549),
  ('unary_expr -> postfix_expr','unary_expr',1,'p_unary_expr_4','parser.py',1553),
  ('postfix_expr -> LPAREN expr RPAREN','postfix_expr',3,'p_postfix_expr_1','parser.py',1557),
  ('postfix_expr -> variable_access','postfix_expr',1,'p_postfix_expr_2','parser.py',1561),
  ('postfix_expr -> function_call','postfix_expr',1,'p_postfix_expr_3','parser.py',1565),
  ('postfix_expr -> constant','postfix_expr',1,'p_postfix_expr_4','parser.py',1569),
  ('constant -> CONST_INT','constant',1,'p_constant_1','parser.py',1573),
  ('constant -> CONST_REAL','constant',1,'p_constant_2','parser.py',1588),
  ('constant -> CONST_CHAR','constant',1,'p_constant_3','parser.py',1603),
  ('constant -> CONST_STRING','constant',1,'p_constant_4','parser.py',1618),
  ('constant -> constant_bool','constant',1,'p_constant_5','parser.py',1633),
  ('constant_bool -> TRUE','constant_bool',1,'p_constant_bool_1','parser.py',1648),
  ('constant_bool -> FALSE','constant_bool',1,'p_constant_bool_2','parser.py',1653),
  ('type -> INT','type',1,'p_type_1','parser.py',1658),
  ('type -> REAL','type',1,'p_type_2','parser.py',1663),
  ('type -> CHAR','type',1,'p_type_3','parser.py',1668),
  ('type -> BOOL','type',1,'p_type_4','parser.py',1673),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',1678),
]

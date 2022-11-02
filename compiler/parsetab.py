
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASGMT BOOL BOOL_FALSE BOOL_TRUE CHAR COLON COMMA CONST_CHAR CONST_FLOAT CONST_INT CONST_STRING DIVIDE ELSE EQUAL FROM FUNCTION GLOBAL GTHAN GTHAN_EQUAL ID IF INT LBRACE LBRACKET LOCAL LPAREN LTHAN LTHAN_EQUAL MINUS MODULO NEQUAL NOT OR PLUS PRINT RBRACE RBRACKET READ REAL RPAREN SEMI START TIMES VARIABLES VOID WHILEstart : global_variables_declaration function_definition entry_point_definitionglobal_variables_declaration : GLOBAL variables_declaration\n                                        | emptyfunction_definition : function_definition function_definition\n                               | FUNCTION type ID LPAREN RPAREN local_variables_declaration instruction_block\n                               | FUNCTION VOID ID LPAREN RPAREN local_variables_declaration instruction_block\n                               | FUNCTION type ID LPAREN function_definition_param RPAREN local_variables_declaration instruction_block\n                               | FUNCTION VOID ID LPAREN function_definition_param RPAREN local_variables_declaration instruction_block\n                               | emptyfunction_definition_param : function_definition_param COMMA function_definition_param\n                                     | type ID dims_definitiondims_definition : dims_definition dims_definition\n                           | LBRACKET CONST_INT RBRACKET\n                           | emptyentry_point_definition : START LPAREN RPAREN local_variables_declaration instruction_blocklocal_variables_declaration : LOCAL variables_declaration\n                                       | emptyinstruction_block : LBRACE statement RBRACEvariables_declaration : VARIABLES COLON variable_declarationvariable_declaration : variable_declaration variable_declaration\n                                | type ID SEMItype : INT\n                | REAL\n                | CHAR\n                | BOOLstatement : emptyempty :'
    
_lr_action_items = {'GLOBAL':([0,],[3,]),'FUNCTION':([0,2,4,5,7,8,10,23,28,38,53,56,58,61,62,],[-27,6,-3,6,-9,-2,6,-19,-20,-21,-5,-6,-18,-7,-8,]),'START':([0,2,4,5,7,8,10,23,28,38,53,56,58,61,62,],[-27,-27,-3,12,-9,-2,-4,-19,-20,-21,-5,-6,-18,-7,-8,]),'$end':([1,11,39,58,],[0,-1,-15,-18,]),'VARIABLES':([3,31,],[9,9,]),'VOID':([6,],[14,]),'INT':([6,19,23,26,27,28,38,45,],[15,15,15,15,15,15,-21,15,]),'REAL':([6,19,23,26,27,28,38,45,],[16,16,16,16,16,16,-21,16,]),'CHAR':([6,19,23,26,27,28,38,45,],[17,17,17,17,17,17,-21,17,]),'BOOL':([6,19,23,26,27,28,38,45,],[18,18,18,18,18,18,-21,18,]),'COLON':([9,],[19,]),'LPAREN':([12,21,22,],[20,26,27,]),'ID':([13,14,15,16,17,18,24,33,],[21,22,-22,-23,-24,-25,29,42,]),'RPAREN':([20,26,27,35,37,42,50,52,55,59,63,],[25,34,36,44,47,-27,-11,-14,-10,-12,-13,]),'LBRACE':([23,25,28,30,32,34,36,38,41,43,44,46,47,54,57,],[-19,-27,-20,40,-17,-27,-27,-21,-16,40,-27,40,-27,40,40,]),'LOCAL':([25,34,36,44,47,],[31,31,31,31,31,]),'SEMI':([29,],[38,]),'COMMA':([35,37,42,50,52,55,59,63,],[45,45,-27,-11,-14,45,-12,-13,]),'RBRACE':([40,48,49,],[-27,58,-26,]),'LBRACKET':([42,50,52,59,63,],[51,51,-14,51,-13,]),'CONST_INT':([51,],[60,]),'RBRACKET':([60,],[63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'global_variables_declaration':([0,],[2,]),'empty':([0,2,5,10,25,34,36,40,42,44,47,50,59,],[4,7,7,7,32,32,32,49,52,32,32,52,52,]),'function_definition':([2,5,10,],[5,10,10,]),'variables_declaration':([3,31,],[8,41,]),'entry_point_definition':([5,],[11,]),'type':([6,19,23,26,27,28,45,],[13,24,24,33,33,24,33,]),'variable_declaration':([19,23,28,],[23,28,28,]),'local_variables_declaration':([25,34,36,44,47,],[30,43,46,54,57,]),'function_definition_param':([26,27,45,],[35,37,55,]),'instruction_block':([30,43,46,54,57,],[39,53,56,61,62,]),'statement':([40,],[48,]),'dims_definition':([42,50,59,],[50,59,59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> global_variables_declaration function_definition entry_point_definition','start',3,'p_start','parser.py',17),
  ('global_variables_declaration -> GLOBAL variables_declaration','global_variables_declaration',2,'p_global_variables_declaration','parser.py',21),
  ('global_variables_declaration -> empty','global_variables_declaration',1,'p_global_variables_declaration','parser.py',22),
  ('function_definition -> function_definition function_definition','function_definition',2,'p_function_definition','parser.py',26),
  ('function_definition -> FUNCTION type ID LPAREN RPAREN local_variables_declaration instruction_block','function_definition',7,'p_function_definition','parser.py',27),
  ('function_definition -> FUNCTION VOID ID LPAREN RPAREN local_variables_declaration instruction_block','function_definition',7,'p_function_definition','parser.py',28),
  ('function_definition -> FUNCTION type ID LPAREN function_definition_param RPAREN local_variables_declaration instruction_block','function_definition',8,'p_function_definition','parser.py',29),
  ('function_definition -> FUNCTION VOID ID LPAREN function_definition_param RPAREN local_variables_declaration instruction_block','function_definition',8,'p_function_definition','parser.py',30),
  ('function_definition -> empty','function_definition',1,'p_function_definition','parser.py',31),
  ('function_definition_param -> function_definition_param COMMA function_definition_param','function_definition_param',3,'p_function_definition_param','parser.py',35),
  ('function_definition_param -> type ID dims_definition','function_definition_param',3,'p_function_definition_param','parser.py',36),
  ('dims_definition -> dims_definition dims_definition','dims_definition',2,'p_dims_definition','parser.py',40),
  ('dims_definition -> LBRACKET CONST_INT RBRACKET','dims_definition',3,'p_dims_definition','parser.py',41),
  ('dims_definition -> empty','dims_definition',1,'p_dims_definition','parser.py',42),
  ('entry_point_definition -> START LPAREN RPAREN local_variables_declaration instruction_block','entry_point_definition',5,'p_entry_point_definition','parser.py',46),
  ('local_variables_declaration -> LOCAL variables_declaration','local_variables_declaration',2,'p_local_variables_declaration','parser.py',50),
  ('local_variables_declaration -> empty','local_variables_declaration',1,'p_local_variables_declaration','parser.py',51),
  ('instruction_block -> LBRACE statement RBRACE','instruction_block',3,'p_instruction_block','parser.py',55),
  ('variables_declaration -> VARIABLES COLON variable_declaration','variables_declaration',3,'p_variables_declaration','parser.py',59),
  ('variable_declaration -> variable_declaration variable_declaration','variable_declaration',2,'p_variables_declaration_list','parser.py',63),
  ('variable_declaration -> type ID SEMI','variable_declaration',3,'p_variables_declaration_list','parser.py',64),
  ('type -> INT','type',1,'p_type','parser.py',67),
  ('type -> REAL','type',1,'p_type','parser.py',68),
  ('type -> CHAR','type',1,'p_type','parser.py',69),
  ('type -> BOOL','type',1,'p_type','parser.py',70),
  ('statement -> empty','statement',1,'p_statement','parser.py',74),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',78),
]
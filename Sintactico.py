import sys
import ply.yacc as yacc
from lexico import tokens

VERBOSE = 1

precedence = (
	('left', 'EQUAL'),
	('nonassoc', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
)

#APERTURA Y CIERRE DEL PROGRAMA
def p_program(p):
    '''program : PUBLIC CLASS VARIABLE declaration_list END CLASS
    '''
    pass

#DECLARACIONES DENTRO DEL PROGRAMA
def p_declaration_list(p):
   '''declaration_list : declaration_list  declaration
   					   | declaration
   '''

def p_declaration(p):
	'''declaration : var_declaration
                   | selection_stmt
	'''
	pass

#DECLARACIÓN DE UNA VARIABLE
def p_var_declaration(p):
	'''var_declaration : DIM VARIABLE AS tipo_dato 
                        | DIM VARIABLE
	'''
	pass

#El tipo de dato de una variable
def p_tipo_dato(p):
	'''tipo_dato : STRING 
                | DOUBLE
	'''
	pass

#DECLARACIÓN DE LA SENTENCIA IF
def p_selection_stmt(p):
	'''selection_stmt : IF expression THEN statement_list END IF
					  | IF expression THEN statement_list selection END IF
	'''
	pass

def p_selection(p):
	'''selection : ELSEIF expression THEN statement_list
                 |  ELSEIF expression THEN statement_list selection
	 '''
	pass

#DECLARACIÓN DE STATEMENT
def p_statement_list(p):
	'''statement_list : statement_list statement
					  | empty
	'''
	pass

def p_statement(p):
	'''statement : expression
	'''
	pass

#DECLARACIÓN DE UNA EXPRESIÓN
def p_expression(p):
	'''expression : var EQUAL expression
				  | simple_expression
			      | expression AND expression
	'''
	pass

#EXPRESIONES SIMPLES
def p_simple_expression(p):
	'''simple_expression : additive_expression relop additive_expression
						 | additive_expression
	'''
	pass

#SIMBOLOS DE IGUALDAD Y DESIGUALDAD
def p_relop(p):
	'''relop : LESS
			 | LESSEQUAL
			 | GREATER
			 | GREATEREQUAL
	'''
	pass

#EXPRESION DE SUMA O RESTA
def p_additive_expression(p):
	'''additive_expression : additive_expression addop term
    					   | term
	'''
	pass

def p_var(p):
	'''var : VARIABLE
	'''
	pass

#SIMBOLOS + -
def p_addop(p):
	'''addop : PLUS
			 | MINUS
	'''
	pass

#TERMINO SUMA Y RESTA
def p_term(p):
	'''term : term mulop factor
			| factor
	'''
	pass

#SIMBILOS * /
def p_mulop(p):
	'''mulop : TIMES
			 | DIVIDE
	'''
	pass

#FACTOR
def p_factor(p):
	'''factor : var
			  | NUMERO
              | TEXTO
	'''
	pass

#VACIO
def p_empty(p):
	'empty :'
	pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print(chr(27)+"[1;31m"+"\t ERROR: Syntax error - Unexpected token" + chr(27)+"[0m")
            print ("\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
        else:
            print (chr(27)+"[1;31m"+"\t ERROR: Syntax error"+chr(27)+"[0m")
            print ("\t\tLine:  "+str(lexico.lexer.lineno))

    else:
        raise Exception('syntax', 'error')
        
parser = yacc.yacc()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)

        print (chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
        parser.parse(scriptdata, tracking=False)
        print (chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")

    else:
        print (chr(27)+"[0;31m"+"Pase el archivo de script PHP como parametro:")
        print (chr(27)+"[0;36m"+"\t$ python php_parser.py"+chr(27)+"[1;31m"+" <filename>.php"+chr(27)+"[0m")
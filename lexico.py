import sys
from tabulate import tabulate
import ply.lex as lex

tokens = (
    #PALABRAS RESERVADAS
    #https://docs.microsoft.com/en-us/dotnet/visual-basic/language-reference/keywords/
    'DIM','AS','IF','THEN','ELSEIF','ENDIF','DOUBLE','STRING','END','PUBLIC','CLASS','SUB','AND',

    # SYMBOLS
    #https://docs.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/
    'PLUS','MINUS','TIMES','DIVIDE','LESS','LESSEQUAL','GREATER','GREATEREQUAL','EQUAL',

    #OTHERS
    'VARIABLE','NUMERO','TEXTO'
)

# IGNORED CHARACTERS
t_ignore = " \t" #Ignora espaio

def t_newline(t): #Ignora si hay una linea vacia
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print (chr(27)+"[1;31m"+"\t ERROR: Illegal character"+chr(27)+"[0m")
    print ("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)

#PALABRAS RESERVADAS
def t_DIM(t):
    r'[dD]im'
    return t

def t_AS(t):
    r'[aA]s'
    return t

def t_AND(t):
    r'[aA]nd'
    return t

def t_DOUBLE(t):
    r'[dD]ouble'
    return t

def t_STRING(t):
    r'[sS]tring'
    return t

def t_IF(t):
    r'[iI]f'
    return t

def t_THEN(t):
    r'[tT]hen'
    return t

def t_ELSEIF(t):
    r'[eE]lse[iI]f'
    return t

def t_END(t):
    r'[eE]nd'
    return t

def t_PUBLIC(t):
    r'[pP]ublic'
    return t

def t_CLASS(t):
    r'[cC]lass'
    return t

def t_SUB(t):
    r'[sS]ub'
    return t

# RE SYMBOLS
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'\/'
t_EQUAL     = r'='
t_LESS      = r'<'
t_GREATER   = r'>'

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

# RE OTHERS
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'\w+(\w\d)*'
    return t

def t_TEXTO(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

lexer = lex.lex()

#PIDE EL ARCHIVO A LEER, COMANDO: python Lexico.py <filename.vb>
if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        lexer.input(scriptdata)

        print (chr(27)+"[0;36m"+"INICIA ANALISIS LEXICO"+chr(27)+"[0m")
        i = 1
        resultado=[]
        while True:
            tok = lexer.token()
            if not tok:
                break
            #SE GUARDA EN UN LISTA DE ARREGLO
            resultado.append([str(i),'Line: '+str(tok.lineno),str(tok.type),str(tok.value)])
            i += 1
        #IMPRIME EL RESULTADO USANDO TABULATE
        print(tabulate(resultado, headers=["ID","LINEA DE CODIGO", "TOKEN", "VALOR"], tablefmt="pretty",numalign="right"))
        print (chr(27)+"[0;36m"+"TERMINA ANALISIS LEXICO"+chr(27)+"[0m")
    else:
        print (chr(27)+"[0;31m"+"Pase el archivo de script PHP como parametro:")
        print (chr(27)+"[0;36m"+"\t$ python php_lexer.py"+chr(27)+"[1;31m"+" <filename>.php"+chr(27)+"[0m")
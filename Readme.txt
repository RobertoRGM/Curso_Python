##AUla 5##
Manipula��o cadeia de textos

Fatiamento: 
Nome da vari�el[].Numero da vari�vel que ser� retornada dentro dos colchetes.
Em caso de range exemplo [x:y] ser� iniciado em "x" mas "y" ser� Y-1 pegando at� a variavel que precede Y como final.
Em cado de [x:y:Z] segue o mesmo exemplo a cima por�m o Z indica o numero de variaveis que ir� pular.
Se eu omito o primeiro indice antes dos : ex [:Y] o python entende que inicia no indice zero.
Em caso de se omitir o segundo indice ex [x:] o python entender� e ir� retornar at� o ultimo caracter.
Para [X::Z] seguindo a mesma regra de omiss�o de um dos indices o python entender� que ir� iniciar em "x" at� o final pois n�o tem o segundo argumento e pulando de acordo com o informado em "Z"

An�lise de String:

m�todo len(frase) = mostra o comprimento da variavel frase ou seja quantidade de caracteres.
       frase.count("x") = retorna quantas vezes o caracter x pararece na variavel denominada frase.
       frase.count("x",N,N) = Faz a contagem j� com fatiamento onde N mostra o inicio e o final.
       frase.find("abc") = localiza e informa a posi��o onde iniciou os caracteres informados, quando se busca um conjunto de caracteres que n�o faz parte da string ele retorna o valor -1.
       operador in = informa se o valor procurado existe dentro da string
   
Transforma��o:

       replace = substitui "palavra" pela informada - frase.replace('xxxx','yyyyy')
       upper = transforma todas os caracteres que estiverem e letra minuscula em maiscula - frase.upper()
       lower = func��o contr�ria ao upper
       capitalize = toda a string � colocada em letra minuscula e apenas a primeira letra fica maiuscula.
       title = todas as primeiras letras de cada palavra se tornam maiusculas.
       strip = remove os espa�os inuteis no incio e final da string
       rstrip = remove os espa�os a direita
       lstrip = remove os espa�oes da esquerda

Divis�o:

       split = divide a string eliminando os espa�os em uma lista
       join = separa a string = '-'.join(frase)    
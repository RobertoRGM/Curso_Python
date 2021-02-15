##AUla 5##
Manipulação cadeia de textos

Fatiamento: 
Nome da variáel[].Numero da variável que será retornada dentro dos colchetes.
Em caso de range exemplo [x:y] será iniciado em "x" mas "y" será Y-1 pegando até a variavel que precede Y como final.
Em cado de [x:y:Z] segue o mesmo exemplo a cima porém o Z indica o numero de variaveis que irá pular.
Se eu omito o primeiro indice antes dos : ex [:Y] o python entende que inicia no indice zero.
Em caso de se omitir o segundo indice ex [x:] o python entenderá e irá retornar até o ultimo caracter.
Para [X::Z] seguindo a mesma regra de omissão de um dos indices o python entenderá que irá iniciar em "x" até o final pois não tem o segundo argumento e pulando de acordo com o informado em "Z"

Análise de String:

método len(frase) = mostra o comprimento da variavel frase ou seja quantidade de caracteres.
       frase.count("x") = retorna quantas vezes o caracter x pararece na variavel denominada frase.
       frase.count("x",N,N) = Faz a contagem já com fatiamento onde N mostra o inicio e o final.
       frase.find("abc") = localiza e informa a posição onde iniciou os caracteres informados, quando se busca um conjunto de caracteres que não faz parte da string ele retorna o valor -1.
       operador in = informa se o valor procurado existe dentro da string
   
Transformação:

       replace = substitui "palavra" pela informada - frase.replace('xxxx','yyyyy')
       upper = transforma todas os caracteres que estiverem e letra minuscula em maiscula - frase.upper()
       lower = funcção contrária ao upper
       capitalize = toda a string é colocada em letra minuscula e apenas a primeira letra fica maiuscula.
       title = todas as primeiras letras de cada palavra se tornam maiusculas.
       strip = remove os espaços inuteis no incio e final da string
       rstrip = remove os espaços a direita
       lstrip = remove os espaçoes da esquerda

Divisão:

       split = divide a string eliminando os espaços em uma lista
       join = separa a string = '-'.join(frase)    
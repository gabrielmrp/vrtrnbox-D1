Classificador de ondas

Neste exercício, é apresentada uma tabela em csv, dessa forma as colunas 22 são separadas pelo caractere de vírgula e as 5000 linhas por quebras-de-linha. Tal tabela corresponde à um conjunto de formas de ondas, nos quais as 21 primeiras colunas são os atributos das ondas e a última coluna há indicação de qual das três classes de onda existentes ela pertence.

Para carregar a tabela em python utilizou-se de um leitor de csv, repassando seu conteúdo a uma matriz. Após isso são separados os dados de que servirão para nutrir a árvore binária de classificação a ser montada. Como entradas são utilizados os atributos das formas de onda e, como saída o array de classes.

Os dados de entrada e de saída correspondentes foram divididos em duas classes, de treinamento (70%) e de teste (30%). Tal divisão é importante para a avaliação da qualidade da classificação, uma vez que um modelo só pode ser considerado válido se for testado com um conjunto de dados que não foi utilizado para constituição do modelo de classificação. Métodos de validação mais confiáveis não foram utilizados nesse projeto, uma vez que não foi enunciado um critério de rigor quanto à qualidade da classificação, este só se serviu para verificar que a mesma estava no caminho correto.

Criou-se uma árvore binária de classificação com os dados de treinamento, a fim de facilitar a elucidação das regras que compõem a classificação, a mesma foi podada de modo a limitar ao no máximo dez folhas. Dessa forma são mantidas apenas as regras que geram estas as ______

A árvore binária construída, passa a ser representada no formato de um grafo orientado em arquivo ".dot" e, posteriormente, é desenhado como uma imagem no formato png (veja o arquivo tree.png no diretório raiz). Por fim, as regras obtidas pela árvore que definem a classificação estão dispostas no arquivo rules.txt no diretório raiz.








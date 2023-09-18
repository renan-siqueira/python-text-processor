# Processador de Texto com Python

## Visão Geral

O `python-text-processor` é um projeto Python desenvolvido para processar, analisar e manipular textos. 
Ele oferece uma variedade de funcionalidades, desde análises estatísticas básicas até recursos mais avançados, como tradução de texto.

--- 

## Funcionalidades:

*1. Leitura e Escrita de Arquivos*
- `read_from_file(filename)`: Lê o conteúdo de um arquivo e retorna o texto.
- `write_to_file(filename, content)`: Escreve ou sobrescreve o conteúdo em um arquivo.

*2. Análise Estatística*
- `count_words(text)`: Conta o número de palavras no texto.
- `count_characters(text, spaces=True)`: Conta o número de caracteres no texto. O parâmetro spaces determina se os espaços serão contados ou não.

*3. Manipulação de Texto*
- `remove_text(text, substring)`: Remove todas as ocorrências da substring do texto.
- `replace_text(text, old, new)`: Substitui todas as ocorrências de uma substring por outra.

*4. Tradução de Texto*
- `translate_text(text, to_language="en", from_language="auto")`: Traduz um texto para um idioma especificado. A detecção de idioma de origem é automática por padrão, mas pode ser especificada.

---

## Exemplos de Uso

Aqui estão exemplos de como usar cada funcionalidade através da linha de comando:

---

### Contagem de Palavras:

Para obter a contagem total de palavras no arquivo:
```
python main.py seu_arquivo.txt --count
```

Output:
```
Total de palavras: [número de palavras]
```

---

### Frequência de Palavras:

Para obter a frequência de cada palavra no arquivo:
```
python main.py seu_arquivo.txt --freq
```

Output:
```
palavra1: [contagem]
palavra2: [contagem]
...
```

---

### Encontrar Padrões (Regex):

Para encontrar todas as correspondências de um padrão específico no texto:
```
python main.py seu_arquivo.txt --pattern "seu_regex_aqui"
```

Output:
```
Correspondência encontrada: [match1]
Correspondência encontrada: [match2]
...
```

---

### Tradução de Texto:

Se você deseja traduzir o texto de um idioma específico para outro:
```
python main.py seu_arquivo.txt --translate en:pt
```

Isso traduzirá o texto do inglês para o português. 
Se desejar que o programa detecte automaticamente o idioma de origem:
```
python main.py seu_arquivo.txt --translate :pt
```

Output:
```
Texto Traduzido: [texto traduzido aqui]
```

---

## Para obter ajuda sobre os argumentos disponíveis e como usá-los:
```
python main.py --help
```

Estes exemplos de uso fornecem uma visão clara sobre como interagir com as funcionalidades do sistema através da linha de comando. 
Ao seguir estas instruções, você pode aproveitar ao máximo todas as ferramentas disponíveis no sistema `python-text-processor`.

---

## Testes Unitários

O projeto `python-text-processor` valoriza a qualidade do código e, por esse motivo, conta com testes unitários para garantir o correto funcionamento das suas funcionalidades. Estes testes ajudam a identificar bugs ou comportamentos inesperados, facilitando a manutenção e a expansão do projeto.

### Executando os Testes

Para executar os testes unitários, navegue até a raiz do projeto e execute o seguinte comando:
```
python tests.py
```

Este comando irá rodar todos os testes disponíveis nas classes `TestReader`, `TestAnalyzer` e `TestTranslation`.

---

## Adicionando Mais Testes

Caso deseje expandir o projeto ou contribuir com ele, é altamente recomendável que novos testes unitários sejam adicionados para cobrir as novas funcionalidades. 
Isso garante que o projeto continue estável e confiável à medida que cresce.

Ao adicionar uma nova funcionalidade ou módulo, considere criar uma nova classe de testes no diretório `tests/` e, em seguida, atualize o arquivo `tests.py` para incluir essa nova classe na execução.

---

## Contribuindo

Sinta-se à vontade para contribuir com o projeto, seja adicionando novas funcionalidades, corrigindo bugs ou melhorando a documentação. 
Todas as contribuições são bem-vindas!

---
# CEP Enricher

Script que enriquece uma base de endereços incompleta consultando 
a API ViaCEP — recebe um CSV com CEPs e retorna um novo arquivo 
com logradouro, bairro, cidade e estado preenchidos automaticamente.

## Como executar

1. git clone https://github.com/edu76666/cep-enricher
2. cd cep-enricher
3. pip install -r requirements.txt
4. python main.py

## Como usar

1. Adicione os CEPs no arquivo `enderecos.csv`, um por linha
2. Execute o script:
   python main.py
3. O arquivo `resultado.csv` será gerado com os dados completos

## Tecnologias

- Python 3.14
- Requests
- Pandas

## Autor

Eduardo Cruz Junior — LinkedIn · GitHub

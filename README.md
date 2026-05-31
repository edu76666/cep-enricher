# CEP Enricher

Script que enriquece uma base de endereços incompleta consultando 
a API ViaCEP — recebe um CSV com CEPs e retorna um novo arquivo 
com logradouro, bairro, cidade e estado preenchidos automaticamente.

## Como executar

git clone https://github.com/edu76666/cep-enricher
cd cep-enricher
pip install -r requirements.txt
python main.py --input enderecos.csv --output resultado.csv

## Tecnologias

- Python 3.14
- Requests
- Pandas

## Autor

Eduardo Cruz Junior — LinkedIn · GitHub

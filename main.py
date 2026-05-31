import requests
import pandas as pd

def buscar_cep(cep):
    cep = cep.replace("-", "").strip()
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    return response.json()

def main():
    df = pd.read_csv("enderecos.csv", dtype={"cep": str})

    resultados = []
    for cep in df["cep"]:
        dados = buscar_cep(cep)
        if "erro" in dados:
            resultados.append({"cep": cep, "logradouro": None, "bairro": None, "cidade": None, "estado": None})
        else:
            resultados.append({
                "cep": cep,
                "logradouro": dados.get("logradouro"),
                "bairro": dados.get("bairro"),
                "cidade": dados.get("localidade"),
                "estado": dados.get("uf"),
            })
    
    df_resultado = pd.DataFrame(resultados)
    df_resultado.to_csv("resultado.csv", index=False)
    print("Arquivo resultado.csv gerado com sucesso.")

if __name__=="__main__":
    main()
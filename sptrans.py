import requests
from datetime import datetime

# TOKEN DA SUA CONTA
TOKEN = "b2ef23d8961253e24ff6ffd4e6beb4cc75c79a7323f6a3ab1cfa45e42d8d681b"
API_BASE = "http://api.olhovivo.sptrans.com.br/v2.1"

# Linha 2013-10 (código base sem hífen)
CODIGO_LINHA = 2013

# Programado por sentido
programado = {
    "TPTS": 149,
    "TSTP": 149
}

# Autenticar e manter sessão ativa
def autenticar():
    s = requests.Session()
    r = s.post(f"{API_BASE}/Login/Autenticar?token={TOKEN}")
    if r.ok and r.text.lower() == "true":
        return s
    else:
        raise Exception("Erro na autenticação SPTrans")

# Buscar dados reais da linha
def get_monitoramento():
    try:
        sessao = autenticar()
        resposta = sessao.get(f"{API_BASE}/Posicao/Linha?codigoLinha={CODIGO_LINHA}")
        dados = resposta.json()

        # Separar veículos por sentido
        veiculos = dados.get("vs", [])
        tpts = [v for v in veiculos if v["p"] == 1]  # Sentido 1
        tstp = [v for v in veiculos if v["p"] == 2]  # Sentido 2

        resultados = []

        for sentido, lista, nome in [("TPTS", tpts, "1"), ("TSTP", tstp, "2")]:
            prog = programado[sentido]
            moni = len(lista)
            percentual = round((moni / prog) * 100, 2)
            perdas = prog - moni

            resultados.append({
                "sentido": sentido,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "programado": prog,
                "monitorado": moni,
                "percentual": percentual,
                "perdas": perdas,
                "perdas_real": perdas
            })

        return resultados

    except Exception as e:
        return {"erro": str(e)}

from datetime import datetime
import random

# Programado fixo para ambos os sentidos
programado = {
    "TPTS": 149,
    "TSTP": 149
}

# Simulação de monitorado (exemplo)
def get_monitoramento():
    # Aqui você pode substituir pela consulta real à API quando funcionar
    monitorado = {
        "TPTS": random.randint(120, 149),
        "TSTP": random.randint(100, 149)
    }

    resultado = []
    for sentido in ["TPTS", "TSTP"]:
        prog = programado[sentido]
        moni = monitorado[sentido]
        percentual = round((moni / prog) * 100, 2)
        perdas = prog - moni

        resultado.append({
            "sentido": sentido,
            "data": datetime.now().strftime("%Y-%m-%d"),
            "programado": prog,
            "monitorado": moni,
            "percentual": percentual,
            "perdas": perdas,
            "perdas_real": perdas  # Pode aplicar fator se quiser ajustar
        })

    return resultado

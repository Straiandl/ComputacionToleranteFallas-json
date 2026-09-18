import json
import os
import time
import sentry_sdk

sentry_sdk.init(
    dsn="https://tu_clave_de_ejemplo@o0.ingest.sentry.io/0",
    traces_sample_rate=1.0
)

ARCHIVO_CHECKPOINT = "estado_sistema.json"

def cargar_estado():
    if os.path.exists(ARCHIVO_CHECKPOINT):
        with open(ARCHIVO_CHECKPOINT, "r") as f:
            print("⚠️ Checkpoint detectado. Restaurando progreso previo...")
            return json.load(f)
    return {"ultimo_id_procesado": 0, "ventas_totales": 0}

def guardar_checkpoint(estado):
    with open(ARCHIVO_CHECKPOINT, "w") as f:
        json.dump(estado, f, indent=4)
    print(f" Checkpoint guardado tras procesar la transacción {estado['ultimo_id_procesado']}")

transacciones = [
    {"id": 1, "monto": 1000, "clientes": 5},
    {"id": 2, "monto": 2000, "clientes": 0},
    {"id": 3, "monto": 1500, "clientes": 3}
]

# --- FLUJO PRINCIPAL ---
estado = cargar_estado()
print(f"Iniciando procesamiento desde la transacción #{estado['ultimo_id_procesado'] + 1}...\n")

for tx in transacciones:
    if tx["id"] <= estado["ultimo_id_procesado"]:
        print(f"Omitiendo transacción {tx['id']} (Ya procesada exitosamente).")
        continue

    try:
        print(f"Procesando transacción {tx['id']}...")
        time.sleep(1)
        
        promedio = tx["monto"] / tx["clientes"]
        
        estado["ultimo_id_procesado"] = tx["id"]
        estado["ventas_totales"] += tx["monto"]
        
        guardar_checkpoint(estado)

    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f" ERROR detectado en la transacción {tx['id']}. Notificado a Sentry.")
        print(" El sistema continúa con la siguiente tarea sin perder el estado guardado.\n")

print(f"\n Proceso finalizado. Total acumulado en estado: ${estado['ventas_totales']}")
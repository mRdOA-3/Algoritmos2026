from app import crear_sistema_simulado, crear_base_firmas
from estrategias import EscaneoRapido, EscaneoProfundo
from motor import MotorEscaneo


def ejecutar_demo(nombre_estrategia, estrategia):
    print("\n" + "=" * 10, nombre_estrategia, "=" * 10)

    sistema = crear_sistema_simulado()
    firmas = crear_base_firmas()

    motor = MotorEscaneo(firmas, estrategia)
    resultados = motor.escanear(sistema)

    for r in resultados:
        texto = (
            f"[{r.estado.upper()}] "
            f"{r.ruta} | "
            f"Riesgo: {r.riesgo} | "
            f"{r.detalle}"
        )
        print(texto)

    resumen = motor.generar_resumen()

    print("\nResumen final")
    print(resumen)


if __name__ == "__main__":
    ejecutar_demo("Escaneo rápido", EscaneoRapido())
    ejecutar_demo("Escaneo profundo", EscaneoProfundo())

from __future__ import annotations
from typing import List
from modelo import Archivo, Carpeta, NodoSistema, ResultadoEscaneo
from firmas import BaseFirmas
from estrategias import EstrategiaEscaneo


class MotorEscaneo:

    def __init__(self, base_firmas: BaseFirmas, estrategia: EstrategiaEscaneo) -> None:
        self.base_firmas = base_firmas
        self.estrategia = estrategia
        self.resultados: List[ResultadoEscaneo] = []

    def escanear(self, raiz: Carpeta) -> List[ResultadoEscaneo]:
        self.resultados = []
        self._escanear_nodo(raiz, "")
        return self.resultados

    def _escanear_nodo(self, nodo: NodoSistema, ruta_padre: str) -> None:
        ruta_actual = nodo.obtener_ruta(ruta_padre)

        if isinstance(nodo, Archivo):
            res = self.estrategia.escanear_archivo(nodo, ruta_actual, self.base_firmas)
            self.resultados.append(res)

        elif isinstance(nodo, Carpeta):
            for hijo in nodo.hijos:
                self._escanear_nodo(hijo, ruta_actual)

    def generar_resumen(self) -> dict:
        total = len(self.resultados)
        limpios = sum(1 for r in self.resultados if r.estado == "limpio")
        sospechosos = sum(1 for r in self.resultados if r.estado == "sospechoso")
        maliciosos = sum(1 for r in self.resultados if r.estado == "malicioso")

        return {
            "total_archivos": total,
            "limpios": limpios,
            "sospechosos": sospechosos,
            "maliciosos": maliciosos,
        }

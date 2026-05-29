from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
import hashlib


@dataclass
class NodoSistema:
    nombre: str

    def obtener_ruta(self, ruta_padre: str = "") -> str:
        if ruta_padre == "":
            return self.nombre
        
        return f"{ruta_padre}/{self.nombre}"
        



@dataclass
class Archivo(NodoSistema):
    contenido: str
    extension: str = ".txt"

    def calcular_hash(self) -> str:
        contenido_bytes = self.contenido.encode("utf-8")
        return hashlib.sha256(contenido_bytes).hexdigest()

    def tamano(self) -> int:
        return len(self.contenido)


@dataclass
class Carpeta(NodoSistema):
    hijos: List[NodoSistema] = field(default_factory=list)

    def agregar_hijo(self, nodo: NodoSistema) -> None:
        self.hijos.append(nodo)


@dataclass
class FirmaMalware:
    identificador: str
    patron: str
    tipo: str
    severidad: int
    descripcion: str


@dataclass
class ResultadoEscaneo:
    ruta: str
    estado: str
    riesgo: int
    firma_detectada: str | None
    detalle: str
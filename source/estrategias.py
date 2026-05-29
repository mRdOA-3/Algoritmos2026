from abc import ABC, abstractmethod
from modelo import Archivo, ResultadoEscaneo
from firmas import BaseFirmas


class EstrategiaEscaneo(ABC):
    @abstractmethod # Una solución dada por ia ya que daba error
    def escanear_archivo(self, archivo, ruta, base_firmas):
        pass


class EscaneoRapido(EstrategiaEscaneo):
    def escanear_archivo(self, archivo, ruta, base_firmas):
        hash_archivo = archivo.calcular_hash()
        firma = base_firmas.buscar_por_hash(hash_archivo)

        if firma:
            if firma.severidad >= 7:
                estado = "malicioso"
            else:
                estado = "sospechoso"
            return ResultadoEscaneo(
                ruta=ruta,
                estado=estado,
                riesgo=firma.severidad,
                firma_detectada=firma.identificador,
                detalle=f"Coincidencia exacta por hash: {firma.tipo}"
            )

        return ResultadoEscaneo(
            ruta=ruta,
            estado="limpio",
            riesgo=0,
            firma_detectada=None,
            detalle="Sin coincidencias por hash"
        )


class EscaneoProfundo(EstrategiaEscaneo):
    def escanear_archivo(self, archivo, ruta, base_firmas):
        hash_archivo = archivo.calcular_hash()
        firma_hash = base_firmas.buscar_por_hash(hash_archivo)

        if firma_hash:
            if firma_hash.severidad >= 7:
                estado = "malicioso"
            else:
                estado = "sospechoso"
            return ResultadoEscaneo(
                ruta=ruta,
                estado=estado,
                riesgo=firma_hash.severidad,
                firma_detectada=firma_hash.identificador,
                detalle=f"Coincidencia exacta por hash: {firma_hash.tipo}"
            )

        firma_patron = base_firmas.buscar_patron_en_contenido(archivo.contenido)

        if firma_patron:
            if firma_patron.severidad >= 7:
                estado = "malicioso"
            else:
                estado = "sospechoso"
            return ResultadoEscaneo(
                ruta=ruta,
                estado=estado,
                riesgo=firma_patron.severidad,
                firma_detectada=firma_patron.identificador,
                detalle=f"Patrón detectado: {firma_patron.tipo}"
            )

        return ResultadoEscaneo(
            ruta=ruta,
            estado="limpio",
            riesgo=0,
            firma_detectada=None,
            detalle="Sin coincidencias por hash ni patrones"
        )

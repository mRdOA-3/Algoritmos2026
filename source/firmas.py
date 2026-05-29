from typing import Dict
from modelo import FirmaMalware


class BaseFirmas:
    def __init__(self):
        self.firmas_por_hash = {}
        self.firmas_por_patron = {}

    def agregar_firma_hash(self, hash_archivo, firma):
        self.firmas_por_hash[hash_archivo] = firma

    def agregar_firma_patron(self, patron, firma):
        self.firmas_por_patron[patron] = firma

    def buscar_por_hash(self, hash_archivo):
        return self.firmas_por_hash.get(hash_archivo)

    def buscar_patron_en_contenido(self, contenido):
        firma_mas_grave = None

        for patron, firma in self.firmas_por_patron.items():
            if patron in contenido:
                if firma_mas_grave is None or firma.severidad > firma_mas_grave.severidad:
                    firma_mas_grave = firma

        return firma_mas_grave

    def cantidad_firmas(self):
        return len(self.firmas_por_hash) + len(self.firmas_por_patron)

    def obtener_hashes_registrados(self):
        return self.firmas_por_hash

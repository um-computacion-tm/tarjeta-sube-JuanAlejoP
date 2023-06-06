class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass


PRECIO_TICKET = 70
ACTIVADO = 'activado'
DESACTIVADO = 'desactivado'
PRIMARIO = 'primario'
SECUNDARIO = 'secundario'
UNIVERSITARIO = 'universitario'
JUBILADO = 'jubilado'
DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}


class Sube:
    def __init__(self):
        self.estado = ACTIVADO
        self.saldo = 0
        self.grupo_beneficiario = None

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario != None:
            DESCUENTOS[self.grupo_beneficiario]
            descuento = (PRECIO_TICKET*(DESCUENTOS[self.grupo_beneficiario]/100))
            precio = PRECIO_TICKET - descuento
        else:
            precio = PRECIO_TICKET
        return precio

    def pagar_pasaje(self):
        if self.saldo < self.obtener_precio_ticket():
            raise NoHaySaldoException('Saldo insuficiente.')
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException('Usuario desactivado.')
        self.saldo -= self.obtener_precio_ticket()

    def cambiar_estado(self, estado):
        if not (estado == ACTIVADO or estado == DESACTIVADO):
            raise EstadoNoExistenteException('Estado inexistente.')
        self.estado = estado
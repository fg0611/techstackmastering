# NO
class Usuario:
    def guardar_usuario(self):  # Responsabilidad: Persistencia
        pass
    def enviar_email(self):     # Responsabilidad: Notificación
        pass

# SI
class Usuario:
    def guardar_usuario(self):
        pass

class EmailService:
    def enviar_email(self):
        pass
from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    avaible_permissions = {
        'cadastrar_cliente': True,
        'cadastrar_vendedor': True,
        'visualizar_dashboard': True,

    }


class Vendedor(AbstractUserRole):
    avaible_permissions = {
        'realizar_venda': True
    }
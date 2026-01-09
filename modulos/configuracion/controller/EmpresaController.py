from helpers.componentes import AlertaPersonalizada
class EmpresaController:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

        # Inyectar el controlador en la vista (estilo práctico)
        self.vista.controller = self

        # Cargar datos iniciales
        self.cargar_datos_empresa()

    def cargar_datos_empresa(self):
        id_emp = self.vista.session.get('id_empresa')
        datos = self.modelo.obtener_empresa(id_emp)

        if datos:
            # Llamamos a un método en la vista que rellene los Entry
            self.vista.rellenar_campos(datos)

    def handle_guardar(self):
        # 1. Recolectar datos de todas las pestañas (la vista los empaqueta)
        datos = self.vista.get_datos_formulario()

        # 2. Validaciones rápidas
        if not datos['nombre_fiscal']:
            AlertaPersonalizada("Faltan datos", "El nombre fiscal es obligatorio.")
            return

        # 3. Guardar vía Modelo
        if self.modelo.guardar_empresa(datos):
            AlertaPersonalizada("Éxito", "Configuración guardada correctamente.")
        else:
            AlertaPersonalizada("Error", "No se pudo guardar la configuración.")

    def inicializar_db_emergencia(self):
        """Lógica para el botón de la pestaña 'Base de Datos'."""
        # Aquí llamarías a la lógica de lectura del .sql que vimos antes
        pass
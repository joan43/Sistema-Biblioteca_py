
import logging
import os
import traceback


class Logger:
    def __init__(self):
    #   inicializa el Logger al crear la instancia    
        self.logger = self.__set_logger()

    def __set_logger(self):
        # Obtener la carpeta del archivo actual (app_logger.py)
        project_dir = os.path.dirname(os.path.abspath(__file__))

        # Crear la carpeta Logs dentro del proyecto
        log_directory = os.path.join(project_dir, 'Logs') #donde se guardaran los logs

        # Crear la carpeta si no existe
        os.makedirs(log_directory, exist_ok=True)

        # Definir nombre y ruta completa del archivo de Logs 
        log_filename = 'logs.log'
        log_path = os.path.join(log_directory, log_filename)

        # Configurar logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        
        # Handler para escribir logs en el archivo de Logs
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        
        # Formato del log:
        # Ej: 2026-03-29 14:30:00 | INFO | Mensaje
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter) # <-- asignar el formato al handler

        # Limpiar handlers previos
        if logger.hasHandlers():
            logger.handlers.clear()
        
        # asociar el Handler al Logger
        logger.addHandler(file_handler)

        return logger

    def add_to_log(self, level, message):
        try:  # Diccionario que mapea strings a funciones del logger
            log_levels = {
                "critical": self.logger.critical,
                "debug": self.logger.debug,
                "error": self.logger.error,
                "info": self.logger.info,
                "warning": self.logger.warning
            }
             # Obtener la función correspondiente al nivel (case-insensitive)
            log_function = log_levels.get(level.lower())
            if log_function:
                log_function(message)  # Ejecutar la funcion de Log correspondiente al nivel
            else:
                self.logger.warning(f"Nivel de log no reconocido: {level}. Mensaje: %{message}")

        except Exception as ex:
            self.logger.error("Error al registrar el log: %s", traceback.format_exc())
            self.logger.error(str(ex))


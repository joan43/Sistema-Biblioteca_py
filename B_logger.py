
import logging
import os
import traceback


class Logger:
    def __init__(self):
        self.logger = self.__set_logger()

    def __set_logger(self):
        # Obtener la carpeta del archivo actual (app_logger.py)
        project_dir = os.path.dirname(os.path.abspath(__file__))
        log_directory = os.path.join(project_dir, 'Logs')  # carpeta Logs dentro del proyecto

        # Crear la carpeta si no existe
        os.makedirs(log_directory, exist_ok=True)

        log_filename = 'logs.log'
        log_path = os.path.join(log_directory, log_filename)

        # Configurar logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        # Limpiar handlers previos
        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(file_handler)

        return logger

    def add_to_log(self, level, message):
        try:
            log_levels = {
                "critical": self.logger.critical,
                "debug": self.logger.debug,
                "error": self.logger.error,
                "info": self.logger.info,
                "warning": self.logger.warning
            }

            log_function = log_levels.get(level.lower())
            if log_function:
                log_function(message)
            else:
                self.logger.warning(f"Nivel de log no reconocido: {level}. Mensaje: %{message}")

        except Exception as ex:
            self.logger.error("Error al registrar el log: %s", traceback.format_exc())
            self.logger.error(str(ex))


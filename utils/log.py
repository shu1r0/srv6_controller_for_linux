from logging import getLogger, Formatter, handlers, StreamHandler


formatter = Formatter("%(asctime)s | %(process)d | %(name)s, %(lineno)d | %(levelname)s | %(message)s")

def get_file_handler(filename, log_level):
    file_handler = handlers.RotatingFileHandler(filename=filename,
                                                maxBytes=16777216,
                                                backupCount=0)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    return file_handler

def get_stream_handler(log_level):
    stream_handler = StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)
    return stream_handler

import logging
import logging.handlers
import os

# 创建日志目录
LOG_DIR = "api_logs"
os.makedirs(LOG_DIR, exist_ok=True)

# 创建日志格式器
formatter = logging.Formatter(
    fmt='[%(asctime)s] %(name)s %(levelname)s %(funcName)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def setup_logger(
    name: str,
    log_file: str,
    level: int = logging.INFO
):
    """创建一个可复用的日志器"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False  # 防止日志向上传递

    # 避免重复添加 handler
    if logger.handlers:
        return logger

    # 文件处理器（按天滚动）
    file_handler = logging.handlers.TimedRotatingFileHandler(
        os.path.join(LOG_DIR, log_file),
        when="midnight",
        interval=1,
        backupCount=7,  # 保留7天
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger("fastapi_app", "app.log")

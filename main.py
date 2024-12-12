import platform
import logging
from typing import Dict
from datetime import datetime
import os

# Ensure logs directory exists
os.makedirs("./logs", exist_ok=True)

# Configure logging
handlers = [
    logging.FileHandler("./logs/log.log"),
    logging.StreamHandler()
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=handlers,
)

logger = logging.getLogger(__name__)

# Define functions


def get_system_info() -> Dict[str, str]:
    try:
        return {
            "system": platform.system(),
            "platform": platform.platform(),
            "processor": platform.processor(),
            "architecture": str(platform.architecture()[0]),
            "python_version": platform.python_version(),
            "node": platform.node(),
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Error gathering system information: {e}")
        return {}


def display_system_info(info: Dict[str, str]) -> None:
    if not info:
        logger.error("No system information available")
        return

    logger.info("System Information:")
    for key, value in info.items():
        logger.info(f"{key.replace('_', ' ').title()}: {value}")


def main():
    logger.info("Starting system information gathering...")

    system_info = get_system_info()
    display_system_info(system_info)

    logger.info("System information gathering completed")


if __name__ == "__main__":
    main()

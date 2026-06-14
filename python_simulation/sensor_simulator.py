import random
from datetime import datetime

from config.settings import (
    VOLTAGE_MIN,
    VOLTAGE_MAX,
    CURRENT_MIN,
    CURRENT_MAX
)

class SensorSimulator:

    def __init__(self):
        pass

    def generate_voltage(self):
        return round(
            random.uniform(
                VOLTAGE_MIN,
                VOLTAGE_MAX
            ),
            2
        )

    def generate_current(self):
        return round(
            random.uniform(
                CURRENT_MIN,
                CURRENT_MAX
            ),
            2
        )

    def generate_reading(self):
        return {
            "timestamp": datetime.now(),
            "voltage": self.generate_voltage(),
            "current": self.generate_current()
        }
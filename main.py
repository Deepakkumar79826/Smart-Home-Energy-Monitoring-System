import time

from python_simulation.sensor_simulator import SensorSimulator
from python_simulation.appliance_manager import ApplianceManager
from python_simulation.energy_calculator import EnergyCalculator
from python_simulation.cost_estimator import CostEstimator
from python_simulation.alert_engine import AlertEngine
from python_simulation.csv_logger import CSVLogger
# from python_simulation.mqtt_client import MQTTManager

print("=" * 60)
print("SMART HOME ENERGY MONITORING SYSTEM")
print("=" * 60)

sensor = SensorSimulator()

appliances = ApplianceManager()

calculator = EnergyCalculator()

cost_estimator = CostEstimator()

alert_engine = AlertEngine()

logger = CSVLogger()

mqtt = None

energy_total = 0.0

try:

    while True:

        sensor_data = sensor.generate_reading()

        appliance_load = appliances.get_total_load()

        power = calculator.calculate_power(
            sensor_data["voltage"],
            sensor_data["current"]
        )

        energy_total = calculator.calculate_energy(
            power,
            energy_total
        )

        cost = cost_estimator.calculate_cost(
            energy_total
        )

        alert = alert_engine.check_alert(
            power
        )

        row = {
            "timestamp": sensor_data["timestamp"],
            "voltage": sensor_data["voltage"],
            "current": sensor_data["current"],
            "power": round(power, 2),
            "energy": round(energy_total, 5),
            "cost": round(cost, 2),
            "load": appliance_load,
            "alert": alert
        }

        logger.log(row)

        pass

        print(row)

        time.sleep(1)

except KeyboardInterrupt:

    print("\nSystem Stopped.")
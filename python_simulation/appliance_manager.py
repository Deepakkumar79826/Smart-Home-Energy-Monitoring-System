import json
import os


class ApplianceManager:

    def __init__(self):

        self.appliances = self.load_appliances()

        self.active_appliances = [
            "Fan",
            "Laptop"
        ]

    def load_appliances(self):

        path = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "data",
            "appliances.json"
        )

        with open(
            path,
            "r"
        ) as file:

            return json.load(file)

    def get_total_load(self):

        total = 0

        for appliance in self.active_appliances:

            total += self.appliances.get(
                appliance,
                0
            )

        return total
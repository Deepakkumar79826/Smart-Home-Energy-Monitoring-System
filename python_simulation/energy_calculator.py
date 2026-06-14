class EnergyCalculator:

    def __init__(self):
        pass

    def calculate_power(
        self,
        voltage,
        current
    ):

        return voltage * current

    def calculate_energy(
        self,
        power,
        previous_energy
    ):
        """
        Energy in kWh

        Loop interval = 1 second
        """

        energy_increment = (
            power / 1000
        ) / 3600

        return (
            previous_energy +
            energy_increment
        )

    def daily_projection(
        self,
        current_power
    ):

        return (
            current_power * 24
        ) / 1000

    def monthly_projection(
        self,
        current_power
    ):

        return (
            current_power * 24 * 30
        ) / 1000
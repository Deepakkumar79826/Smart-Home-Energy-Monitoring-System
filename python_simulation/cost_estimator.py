from config.settings import TARIFF_RATE


class CostEstimator:

    def __init__(self):

        self.tariff = TARIFF_RATE

    def calculate_cost(
        self,
        energy_kwh
    ):

        return (
            energy_kwh *
            self.tariff
        )

    def estimate_daily_cost(
        self,
        daily_energy
    ):

        return (
            daily_energy *
            self.tariff
        )

    def estimate_monthly_cost(
        self,
        monthly_energy
    ):

        return (
            monthly_energy *
            self.tariff
        )
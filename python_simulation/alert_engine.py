from config.settings import POWER_THRESHOLD


class AlertEngine:

    def __init__(self):

        self.threshold = POWER_THRESHOLD

    def check_alert(
        self,
        power
    ):

        if power >= self.threshold:

            return (
                "HIGH CONSUMPTION"
            )

        return "NORMAL"

    def get_alert_color(
        self,
        alert
    ):

        if alert == "HIGH CONSUMPTION":

            return "red"

        return "green"
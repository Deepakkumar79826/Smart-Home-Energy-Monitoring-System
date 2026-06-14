import json

try:
    import paho.mqtt.client as mqtt
except ImportError:
    mqtt = None


class MQTTManager:

    def __init__(self):

        self.client = None

        if mqtt is not None:

            try:

                self.client = mqtt.Client()

                self.client.connect(
                    "broker.hivemq.com",
                    1883,
                    60
                )

            except Exception:

                self.client = None

    def publish(
        self,
        payload
    ):

        if self.client is None:
            return

        try:

            self.client.publish(
                "smart_home_energy_monitor",
                json.dumps(
                    payload,
                    default=str
                )
            )

        except Exception:
            pass
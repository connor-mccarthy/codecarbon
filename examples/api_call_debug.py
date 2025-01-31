import logging
import time

from codecarbon import track_emissions
from codecarbon.external.logger import logger


@track_emissions(
    project_name="just_sleep",
    api_endpoint="http://app-d6bc59c3-0f69-4d8b-a6a3-bc39a9ceb0c2.cleverapps.io",
    experiment_id="82ba0923-0713-4da1-9e57-cea70b460ee9",
    measure_power_secs=10,
    api_call_interval=2,
    api_key="12aaaaaa-0b23-1234-1234-abcdef123456",
    save_to_api=True,
)
def train_model():
    """
    This function will do nothing during (occurence * delay) seconds.
    The Code Carbon API will be called every (measure_power_secs * api_call_interval) seconds.
    """
    occurence = 60 * 24
    delay = 60  # Seconds
    for i in range(occurence):
        print(f"{occurence * delay - i * delay} seconds before ending script...")
        time.sleep(delay)


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler("codecarbon.log")
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)-12s: %(levelname)-8s %(message)s"
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.debug("GO!")
    model = train_model()
    logger.debug("THE END!")

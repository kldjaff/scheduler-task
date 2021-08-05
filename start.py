# coding=utf-8
import schedule
import os
import logging

import local_settings
from jobs import GenApi


logging.basicConfig(format='%(levelname)5s %(asctime)-15s #%(filename)-20s@%(funcName)-20s: %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":

    interval = int(os.getenv("SCHEDULE_INTERVAL"))
    interval_unit = os.getenv("INTERVAL_UNIT")
    logging.info(f"Scheduled Job will be running every {interval} {interval_unit}s")
    gen_api = GenApi(
        method=local_settings.METHOD,
        endpoint=local_settings.ENDPOINT,
        header=local_settings.HEADER
    )

    if interval_unit == "second":
        schedule.every(interval).seconds.do(gen_api.run)
    elif interval_unit == "hour":
        schedule.every(interval).hours.do(gen_api.run)
    elif interval_unit == "day":
        schedule.every(interval).days.do(gen_api.run)
    else:
        schedule.every(1).seconds.do(gen_api.run)

    while True:
        schedule.run_pending()

# coding=utf-8
import time

import os
import sys

import logging
logging.basicConfig(format='%(levelname)5s %(asctime)-15s #%(filename)-20s@%(funcName)-20s: %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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
    """ manage multiple tasks 
    https://schedule.readthedocs.io/en/stable/multiple-schedulers.html    
    
    Limitations:
    (1) all schedulers will run in serial, a later scheduler will NOT be activated until the former scheduler has finished its job. 
        For example,
            If the 1st scheduler runs every 10 seconds and the 2nd one runs every 5 seconds, 
            it will be impossible to activate the 2nd scheduler on time. 
        
        For now, API response time ie not expected to exceed several minutes.                  
        As long as local_settings.py is carefully prepared, this solution is acceptable.
        
    (2) 'secondly' tasks are left only for debugging, not for release        
    """

    # logging.info(local_settings.TASKS)

    scheduler_ = []
    for task in local_settings.TASKS:
        interval = int(task.get('SCHEDULE_INTERVAL'))
        interval_unit = task.get('INTERVAL_UNIT')
        gen_api = GenApi(
            method=task.get('METHOD'),
            endpoint=task.get('ENDPOINT'),
            headers=task.get('HEADER'),
            payload=task.get('PAYLOAD'),
            params=task.get('PARAMS')
        )
        sc = schedule.Scheduler()
        if interval_unit == 'second':
            sc.every(interval).seconds.do(gen_api.run)
        elif interval_unit == 'hour':
            sc.every(interval).hours.do(gen_api.run)
        elif interval_unit == 'day':
            sc.every(interval).days.do(gen_api.run)
        else:
            logging.error(f"unrecognized interval_unit -- {interval_unit}")
            exit(1)

        logging.info(f"Scheduled Job will be running every {interval} {interval_unit}s")
        scheduler_.append(sc)

    while True:
        for sc in scheduler_:
            try:
                sc.run_pending()
                logging.info(sc.get_jobs())
            except Exception as ex:
                logging.error(ex)

        time.sleep(60 * 60)
        # None 'secondly' task is serious, let the outer loop take a nap every 60 * 60 seconds.

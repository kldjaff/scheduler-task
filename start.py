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
            Assume that the 1st scheduler runs every 10 seconds (and it lasts 20 seconds) 
                        the 2nd scheduler runs every 5 seconds, 
            Then the 2nd scheduler will always be activated on the 31th second.
        
        For now, API response time ie not expected to exceed several minutes.                  
        As long as local_settings.py is carefully prepared, this solution is acceptable.
        
    (2) 'secondly' tasks are left only for debugging, not for release        
    """

    scheduler_ = []
    job_title_ = []
    for task in local_settings.TASKS:
        interval = int(task.get('SCHEDULE_INTERVAL'))
        interval_unit = task.get('INTERVAL_UNIT')
        gen_api = GenApi(
            method=task.get('METHOD'),
            endpoint=task.get('ENDPOINT'),
            headers=task.get('HEADER'),
            payload=task.get('PAYLOAD'),
            payload_json=task.get('PAYLOAD_JSON'),
            params=task.get('PARAMS')
        )

        sc = schedule.Scheduler()
        if interval_unit == 'second':
            sc.every(interval).seconds.do(gen_api.run)
        elif interval_unit == 'minute':
            sc.every(interval).minutes.do(gen_api.run)
        elif interval_unit == 'hour':
            sc.every(interval).hours.do(gen_api.run)
        elif interval_unit == 'day':
            sc.every(interval).days.do(gen_api.run)
        else:
            logging.error(f"unrecognized interval_unit -- {interval_unit}")
            exit(1)

        job_title = task.get('title', '')
        job_title_.append(job_title)
        logging.info(f"Scheduled Job {job_title} will be running every {interval} {interval_unit}s")
        scheduler_.append(sc)

    n_jobs = len(scheduler_)
    while True:
        for i in range(n_jobs):
            try:
                sc = scheduler_[i]
                logging.info(f"{job_title_[i]}  - {sc.get_jobs()}")
                sc.run_pending()
            except Exception as ex:
                logging.error(ex)

        logging.info('snoring...')
        time.sleep(60 * 60)
        # On production, let the outer loop take a nap every 60 * 60 seconds. (1 hour)
        # For debugging, take a nap every 60 * 10 seconds. (10 minutes)

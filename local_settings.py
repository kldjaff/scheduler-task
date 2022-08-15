# coding=utf-8
TASKS = [
    {
        'INTERVAL_UNIT': 'day',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT' : "http://192.168.100.5/xxx/push",
        'METHOD' : "GET",
        'HEADER' : {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD' : {},
        'PARAMS' : {}
    },
    {
        'INTERVAL_UNIT': 'day',
        'SCHEDULE_INTERVAL': 3,
        'ENDPOINT' : "http://192.168.100.5/xxx/pull",
        'METHOD' : "GET",
        'HEADER' : {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD' : {},
        'PARAMS' : {}
    },
    {
        'INTERVAL_UNIT': 'day',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT': "http://192.168.100.5/xxx/import/format",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD': {},
        'PARAMS': {}
    },
    {
        'INTERVAL_UNIT': 'day',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT': "http://192.168.100.5/xxx/import/data",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD': {},
        'PARAMS': {}
    },
    {
        'INTERVAL_UNIT': 'day',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT': "http://192.168.100.5/xxx/cleanup",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD': {},
        'PARAMS': {}
    },
]
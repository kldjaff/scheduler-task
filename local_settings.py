# coding=utf-8
TASKS = [
    {
        'INTERVAL_UNIT': 'second',
        'SCHEDULE_INTERVAL': 10,
        'ENDPOINT' : "http://localhost:5000/hello",
        'METHOD' : "GET",
        'HEADER' : {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD' : {},
        'PARAMS' : {}
    },
    {
        'INTERVAL_UNIT': 'second',
        'SCHEDULE_INTERVAL': 5,
        'ENDPOINT' : "http://localhost:5001/hello2",
        'METHOD' : "GET",
        'HEADER' : {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD' : {},
        'PARAMS' : {}
    },
    {
        'INTERVAL_UNIT': 'second',
        'SCHEDULE_INTERVAL': 5,
        'ENDPOINT': "http://localhost:5001/hello3",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD': {},
        'PARAMS': {}
    }
]
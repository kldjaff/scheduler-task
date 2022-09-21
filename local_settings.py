# coding=utf-8
TASKS = [
    {
        'INTERVAL_UNIT': 'minute',
        'SCHEDULE_INTERVAL': 2,
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
        'title': '导入format文件',
        'INTERVAL_UNIT': 'hour',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT' : "http://localhost:5001/tds/api/v1.0/import/format",
        'METHOD' : "GET",
        'HEADER' : {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD' : {},
        'PARAMS' : {}
    },
    {
        'title': '导入zip文件',
        'INTERVAL_UNIT': 'hour',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT': "http://localhost:5001/tds/api/v1.0/import/zip",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD': {},
        'PARAMS': {}
    },
    {
        'title': '向五室推送数据',
        'INTERVAL_UNIT': 'hour',
        'SCHEDULE_INTERVAL': 12,
        'ENDPOINT': "http://localhost:5000/cts/api/v1.0/mdm/push",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD': {},
        'PARAMS': {}
    },
    {
        'title': '下载五室的文件',
        'INTERVAL_UNIT': 'hour',
        'SCHEDULE_INTERVAL': 6,
        'ENDPOINT': "http://localhost:5000/cts/api/v1.0/mdm/push/ex1/download",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD': {},
        'PARAMS': {}
    },
    {
        'title': '下载八室的数据',
        'INTERVAL_UNIT': 'hour',
        'SCHEDULE_INTERVAL': 6,
        'ENDPOINT': "http://localhost:5000/cts/api/v1.0/r8mro/sync",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD': {'steps': ['product', 'sample', 'postsale']},
        'PARAMS': {}
    }
]
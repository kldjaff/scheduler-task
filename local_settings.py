# coding=utf-8
TASKS = [
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
        'PAYLOAD_JSON' : {}
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
        'PAYLOAD_JSON': {}
    },
    {
        'title': '导入dat文件',
        'INTERVAL_UNIT': 'hour',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT': "http://localhost:5001/tds/api/v1.0/import/dat",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD_JSON': {}
    },
    {
        'title': '向五室推送数据',
        'INTERVAL_UNIT': 'minute',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT': "http://localhost:5000/cts/api/v1.0/mdm/push",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        },
        'PARAMS': { 'limit': 5 }
    },
    {
        'title': '下载五室的文件',
        'INTERVAL_UNIT': 'day',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT': "http://localhost:5000/cts/api/v1.0/mdm/ex1/download",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        }
    },
    {
        'title': '八室数据同步 - 售后数据和成功子样',
        'INTERVAL_UNIT': 'minute',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT': "http://localhost:5000/cts/api/v1.0/r8mro/sync",
        'METHOD': "POST",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD_JSON': {"steps": ["sample", "postsale"]}
    },
    {
        'title': '八室数据同步 - 产品目录',
        'INTERVAL_UNIT': 'minute',
        'SCHEDULE_INTERVAL': 2,
        'ENDPOINT': "http://localhost:5000/cts/api/v1.0/r8mro/sync",
        'METHOD': "POST",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD_JSON': {'steps': ['product']}
    },
    {
        'title': 'cts空间清理',
        'INTERVAL_UNIT': 'hour',
        'SCHEDULE_INTERVAL': 12,
        'ENDPOINT': "http://localhost:5000/hello",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD_JSON': {},
        'PAYLOAD': {},
        'PARAMS': {}
    }
]
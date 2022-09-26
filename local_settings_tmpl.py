# coding=utf-8
TASKS = [
    {
        'title': '下载文件',
        'INTERVAL_UNIT': 'day',
        'SCHEDULE_INTERVAL': 1,
        'ENDPOINT': "http://localhost/download",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        },
        'PARAMS': {'limit':10}
    },
    {
        'title': '空间清理',
        'INTERVAL_UNIT': 'hour',
        'SCHEDULE_INTERVAL': 12,
        'ENDPOINT': "http://localhost/mopup",
        'METHOD': "GET",
        'HEADER': {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        },
        'PAYLOAD_JSON': {'steps': ['product']}
    }
]
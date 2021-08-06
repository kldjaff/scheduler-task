# scheduler-task
schedule-task to execute some web-api

## build the image
docker build -t cts-scheduler:0.0.1 .

## run the scheduled task
docker run --name daily-job -d -e INTERVAL_UNIT='day' -e SCHEDULE_INTERVAL=1 cts-scheduler:0.0.1

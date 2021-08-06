# scheduler-task
schedule-task to execute some web-api
This is a small project to host scheduling web api execution by using schedule


# How to use it

## build the image
git clone git@github.com:kldjaff/scheduler-task.git
docker build -t simple-scheduler:0.0.1 .

## run the scheduled task
docker run --name daily-job -d -e INTERVAL_UNIT='day' -e SCHEDULE_INTERVAL=1 simple-scheduler:0.0.1

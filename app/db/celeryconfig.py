from kombu import Queue, Exchange

BROKER_URL = "amqp://guest:guest@localhost:5672/"
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    "app.services.smtp"
)

CELERY_QUEUES = (
    Queue("Default", exchange=Exchange("default"), routing_key="default"),
    Queue("EmailTasks", exchange=Exchange("EmailTasks"), routing_key="EmailTasks")
)

CELERY_ROUTES = {
    "send_message_task": {"queue": "EmailTasks", "routing_key": "EmailTasks"}
}

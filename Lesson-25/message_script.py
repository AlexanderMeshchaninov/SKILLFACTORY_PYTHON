import schedule, time

def message_task():
    print('Hello! I am a task!')
    return

# Время выполнения
schedule.every(1).minute.do(message_task)

# Цикл выполнения
while True:
    schedule.run_pending()
    time.sleep(1)
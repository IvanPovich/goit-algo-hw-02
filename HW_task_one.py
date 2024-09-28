import queue
from const import message

queue_requests = queue.Queue()

def generate_request():
    request = input("\nВаша нова заявка: ")
    queue_requests.put(request)
    print("\nНова заявка створена")

def process_request():
    if not queue_requests.empty():
        queue_requests.get()
        print(f"\nЗaявка видалена. Кількість заявок: {queue_requests.qsize()}")

    else:
        print("\nНемає заявок для обробки")

def main():
    while True:
        action = input(f"{message}")

        if action == 'c':
            generate_request()
        elif action == 'p':
            process_request()
        elif action == 'exit':
            print("Віхід з програми")
            break
        else:
            print('\nНе вірна команда!!!!!')

if __name__ == "__main__":
    main()
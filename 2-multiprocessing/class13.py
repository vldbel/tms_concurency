# channels
import multiprocessing, time

def sender(conn):
    for i in range(5):
        time.sleep(1)
        message = f'Message {i}'
        conn.send(message)
        print(f'Сообщение {message} отпрвлено')
    conn.send(None)
    conn.close()
    
def receiver(conn):
    while True:
        message = conn.recv()
        if message is None:
            break
        print(f'Прочитано сообщение: {message}')
    time.sleep(2)
    

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    
    sender_process = multiprocessing.Process(target=sender, args=(child_conn,))
    receiver_process = multiprocessing.Process(target=receiver, args=(parent_conn,))
    
    sender_process.start()
    receiver_process.start()
    
    sender_process.join()
    receiver_process.join()

    print('Процессы заверщены')
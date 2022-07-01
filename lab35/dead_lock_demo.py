import threading
import time

resource1 = threading.Lock()
resource2 = threading.Lock()

def worker1(name):
  with resource1:
    print('thread',name,'has lock resource1')
    time.sleep(0.5)
    with resource2:
      print('thread',name,'has lock resource2')
      print('thread',name,'run into deadLock,\nthis line will never run')

def worker2(name):
  with resource2:
    print('thread',name,'has lock resource2')
    time.sleep(0.3)
    with resource1:
      print('thread',name,'has lock resource1')
      print('thread',name,'run into deadLock,\nthis line will never run')

if __name__ == '__main__':
  thread1=threading.Thread(target=worker1, args=['thread1',])
  thread2=threading.Thread(target=worker2, args=['thread2',])

  thread1.start()
  thread2.start()
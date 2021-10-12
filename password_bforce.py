from xeger import Xeger
import hashlib
import multiprocessing

password = hashlib.sha256()
password.update(b"112")
pass_hash = password.hexdigest()

def work(event):
    while not event.is_set():
        x = Xeger(limit = 5)
        t = hashlib.sha256()
        pass_try = x.xeger("([0-9a-z]+)")
        t.update(pass_try.encode())

        if(t.hexdigest() == pass_hash):
            print(pass_try)
            event.set()
            return pass_try
        
if __name__ == '__main__':
    m = multiprocessing.Manager()
    e = m.Event()
    
    with multiprocessing.Pool(processes = 3) as pool:
        results = pool.map(work, [e] * 3)
        
    print(results)
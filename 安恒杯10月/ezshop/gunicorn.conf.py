import multiprocessing

bind = 'unix:/var/run/gunicorn.sock'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'

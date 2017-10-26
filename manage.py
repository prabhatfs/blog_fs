
#!/usr/bin/env python
import os
import sys

# Using below code for tornado

import tornado.httpserver
import tornado.ioloop
import tornado.wsgi

import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
    #import pdb;pdb.set_trace()
    from django.core.management import execute_from_command_line

    if len(sys.argv) >2 and sys.argv[2] == "tornado":
        application = django.core.handlers.wsgi.WSGIHandler()
        application = get_wsgi_application()
        container = tornado.wsgi.WSGIContainer(application)
        http_server = tornado.httpserver.HTTPServer(container)
        http_server.listen(8001)
        http_server.listen(8002)
        http_server.listen(8003)
        http_server.listen(8000)
        tornado.ioloop.IOLoop.instance().start()
    else:
        execute_from_command_line(sys.argv)

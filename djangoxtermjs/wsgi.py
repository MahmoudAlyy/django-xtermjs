"""
WSGI config for djangoxtermjs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import socketio
import eventlet
import eventlet.wsgi
from xterm.views import sio

django_app = get_wsgi_application()
application = socketio.Middleware(sio, django_app)

eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), application)

import urllib2
import json

from irgsh_repo.conf import settings
from irgsh_repo.utils import send_message

FAILURE = -1
SUCCESS = 0
COMPLETE = 1

URL_UPDATE_STATUS = '%(host)s/build/%(spec_id)s/repo/status/'
URL_PING = '%(host)s/worker/+ping/'
URL_SPEC_INFO = '%(host)s/build/%(spec_id)s/info/'
URL_TASK_INFO = '%(host)s/task/%(task_id)s/info/'

def update_status(spec_id, status, arch=None):
    host = settings.SERVER.rstrip('/')
    url = URL_UPDATE_STATUS % {'host': host, 'spec_id': spec_id}

    param = {'status': status}
    if arch is not None:
        param['arch'] = arch
    send_message(url, param)

def ping():
    host = settings.SERVER.rstrip('/')
    url = URL_PING % {'host': host}

    param = {}
    send_message(url, param)

def get_spec_info(spec_id):
    host = settings.SERVER.rstrip('/')
    url = URL_SPEC_INFO % {'host': host, 'spec_id': spec_id}

    return json.loads(send_message(url))

def get_task_info(task_id):
    host = settings.SERVER.rstrip('/')
    url = URL_TASK_INFO % {'host': host, 'task_id': task_id}

    return json.loads(send_message(url))


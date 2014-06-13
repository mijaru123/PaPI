from multiprocessing import current_process, cpu_count
from multiprocessing import Manager, Process, Condition, Lock, Pool
from multiprocessing.managers import BaseManager
from datetime import datetime
import sys

class Thing(object):
    def __init__(self, initial_value=0):
        self.value = initial_value
        self.change_log = list()          # list of tuples

    def __repr__(self):
        if not self.modified:
            return "<Thing value=%s>" % self.value
        else:
            return "<Thing value=%s (%s, total changes=%s)>" % (self.value, self.last_modified, len(self.change_log))

    def modify(self, new_value=0, modifier_pid=0):
        self.value = new_value
        # tuple format (new_value, modifier_pid, datetime of modification)
        self.change_log.append((new_value, modifier_pid, datetime.now()))

    @property
    def modified(self):
        if len(self.change_log)>1:
            return True
        return False

    @property
    def last_modified(self):
        if self.modified:
            value, pid, timestamp = self.change_log[-1]
            return "Modified to %s by %s at %s" % (value, pid, timestamp)
        else:
            return ""

## Subclassing BaseManager permits registration of a shared object
class ScriptManager(BaseManager):
    pass
ScriptManager.register('Thing', Thing, exposed=['modify', 'modified',
    'last_modified'])

def process(lock, shared_object):
    try:
        with lock:
            shared_object.modify(new_value=1, modifier_pid=current_process().name)
        print "FOO %s: %s" % (current_process().name, shared_object)
    except:
        print "FATAL: %s running process(%s, %s) exited with %s" % (current_process().name, lock, shared_object, sys.exc_info())

if __name__=='__main__':
    manager = ScriptManager()
    manager.start()
    shared_thing = manager.Thing()   # Create an instance of Thing to share
    lock = Lock()
    ### Create two python processes, which run process()
    p1 = Process(target=process, name='process_1', args=(lock, shared_thing))
    p1.start()
    p2 = Process(target=process, name='process_2', args=(lock, shared_thing))
    p2.start()
    p3 = Process(target=process, name='process_3', args=(lock, shared_thing))
    p3.start()
    p4 = Process(target=process, name='process_4', args=(lock, shared_thing))
    p4.start()
    ## Wait for the processes to finish
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    


import unittest
import time
import threading

from rwlock import RWLock

class RWLockTest(unittest.TestCase):

    def test_integration(self):
        state = ThreadState()
        Reader('1', state).start()
        Reader('2', state).start()
        Writer('1', state).start()
        Writer('2', state).start()
        # ReaderWriter(state).start()
        # WriterReader(state).start()
        Reader('3', state).start()

        state.point('ready-reader-start-1')
        state.point('ready-reader-start-2')
        state.wait_for('test', 'reader-start-1')
        state.wait_for('test', 'reader-start-2')
        state.wait_for('test', 'reader-aquired-1')
        state.wait_for('test', 'reader-aquired-2')
        state.point('ready-writer-start-1')
        state.wait_for('test', 'writer-start-1')
        self.assertNotIn('writer-aquired-1', state.encounter_state)
        state.point('ready-reader-stop-1')
        state.wait_for('test', 'reader-release-1')
        self.assertNotIn('writer-aquired-1', state.encounter_state)
        state.point('ready-reader-stop-2')
        state.wait_for('test', 'reader-release-2')
        state.wait_for('test', 'writer-aquired-1')
        state.point('ready-writer-start-2')
        state.wait_for('test', 'writer-start-2')
        self.assertNotIn('writer-aquired-2', state.encounter_state)
        state.point('ready-writer-stop-1')
        state.wait_for('test', 'writer-release-1')
        state.wait_for('test', 'writer-aquired-2')
        state.point('ready-reader-start-3')
        state.wait_for('test', 'reader-start-3')
        self.assertNotIn('reader-aquired-3', state.encounter_state)
        state.point('ready-writer-stop-2')
        state.wait_for('test', 'writer-release-2')
        state.wait_for('test', 'reader-aquired-3')
        state.point('ready-reader-stop-3')
        state.wait_for('test', 'reader-release-3')


TIMEOUT = 5

class ThreadState(object):
    def __init__(self):
        self.rwl = RWLock()
        self.encounter_state = []
        self.current_state = 'init'
    
    def point(self, state):
        self.encounter_state.append(state)
    
    def wait_for(self, name, expected_state: str):
        timeout = time.perf_counter() + TIMEOUT
        while time.perf_counter() < timeout and expected_state not in self.encounter_state:
            time.sleep(0.001)
        if expected_state not in self.encounter_state:
            raise Exception('{0} did not reach {1}, currently at {2}'.format(name, expected_state, self.encounter_state))
    


class Reader(threading.Thread):
    def __init__(self, name, state: ThreadState):
        threading.Thread.__init__(self)
        self.state = state
        self.name = name

    def run(self):
        self.state.wait_for('Reader', 'ready-reader-start-' + self.name)
        self.state.point('reader-start-' + self.name)
        self.state.rwl.acquire_read()
        self.state.point('reader-aquired-' + self.name)
        self.state.wait_for('Reader', 'ready-reader-stop-' + self.name)
        self.state.point('reader-stop-' + self.name)
        self.state.rwl.release()
        self.state.point('reader-release-' + self.name)

class Writer(threading.Thread):
    def __init__(self, name, state: ThreadState):
        threading.Thread.__init__(self)
        self.state = state
        self.name = name

    def run(self):
        self.state.wait_for('Writer', 'ready-writer-start-' + self.name)
        self.state.point('writer-start-' + self.name)
        self.state.rwl.acquire_write()
        self.state.point('writer-aquired-' + self.name)
        self.state.wait_for('Writer', 'ready-writer-stop-' + self.name)
        self.state.point('writer-stop-' + self.name)
        self.state.rwl.release()
        self.state.point('writer-release-' + self.name)

class ReaderWriter(threading.Thread):
    def __init__(self, state: ThreadState):
        threading.Thread.__init__(self)
        self.state = state

    def run(self):
        self.state.wait_for('ready-rw-start')
        self.state.point('rw-start')
        self.state.rwl.acquire_read()
        self.state.point('rw-acquire-read')
        self.state.wait_for('ReaderWriter', 'ready-rw-promote')
        self.state.rwl.promote()
        self.state.point('rw-promoted')
        self.state.wait_for('ReaderWriter', 'ready-rw-stop')
        self.state.point('rw-stop')
        self.state.rwl.release()
        self.state.point('rw-release')

class WriterReader(threading.Thread):
    def __init__(self, state: ThreadState):
        threading.Thread.__init__(self)
        self.state = state

    def run(self):
        self.state.wait_for('WriterReader', 'ready-wr-start')
        self.state.point('wr-start')
        self.state.rwl.acquire_write()
        self.state.point('wr-aquire-write')
        self.state.wait_for('WriterReader', 'ready-wr-demote')
        self.state.point('wr-demoted')
        self.state.rwl.demote()
        self.state.wait_for('WriterReader', 'ready-wr-stop')
        self.state.point('wr-stop')
        self.state.rwl.release()
        self.state.point('wr-release')

if __name__ == '__main__':
    unittest.main()

import cv2
import numpy as np

from zuper_nodes_python2 import ComponentInterface


def go():
    AIDONODE_DATA_IN = '/fifos/agent-in'
    AIDONODE_DATA_OUT = '/fifos/agent-out'
    ci = ComponentInterface(AIDONODE_DATA_IN, AIDONODE_DATA_OUT, 'agent', timeout=5)
    ci.write_topic_and_expect_zero(u'seed', 32)

    ci.write_topic_and_expect_zero(u'episode_start', {u'episode_name': u'episode'})

    while True:
        bgr = np.zeros((640, 480, 3), 'uint8')
        retval, s = cv2.imencode('.jpg', bgr)
        data = s.tostring()

        obs = {u'camera': {u'jpg_data': data}}
        ci.write_topic_and_expect_zero(u'observations', obs)
        commands = ci.write_topic_and_expect(u'get_commands', expect=u'commands')
        commands = commands.data[u'wheels']
        print(commands)


if __name__ == '__main__':
    go()

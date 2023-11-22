# Choregraphe simplified export in Python.
from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.24, 0.4, 0.72, 0.88, 0.96])
    keys.append([-0.013848, 0.415673, -0.151908, 0.247837, 0.1733])

    names.append("HeadYaw")
    times.append([0.24, 0.4, 0.72, 0.88, 0.96])
    keys.append([-4.19617e-05, 0.010696, 0.0199001, 0.010696, -4.19617e-05])

    names.append("LElbowRoll")
    times.append([0.08, 0.4])
    keys.append([-0.843657, -1.10137])

    names.append("LElbowYaw")
    times.append([0.08, 0.4])
    keys.append([-1.3561, -1.10606])

    names.append("LHand")
    times.append([0.56])
    keys.append([0.161481])

    names.append("LShoulderPitch")
    times.append([0.08, 0.4])
    keys.append([1.66742, 1.41584])

    names.append("LShoulderRoll")
    times.append([0.08, 0.4])
    keys.append([0.214717, 0.15796])

    names.append("LWristYaw")
    times.append([0.56])
    keys.append([-0.48632])

    names.append("RElbowRoll")
    times.append([0.08, 0.4])
    keys.append([1.1981, 1.36837])

    names.append("RElbowYaw")
    times.append([0.08, 0.4])
    keys.append([0.816046, 0.704064])

    names.append("RHand")
    times.append([0.56])
    keys.append([0.280389])

    names.append("RShoulderPitch")
    times.append([0.08, 0.4])
    keys.append([1.37451, 1.07691])

    names.append("RShoulderRoll")
    times.append([0.08, 0.4])
    keys.append([-0.084412, -0.067538])

    names.append("RWristYaw")
    times.append([0.56])
    keys.append([0.722472])

    
    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        motion = ALProxy("ALMotion", robotIP, port)
        motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


if __name__ == "__main__":

    robotIP = "127.0.0.1" #"192.168.1.11"

    port = 9559 # Insert NAO port

    if len(sys.argv) == 2:
        robotIP = sys.argv[1]
    elif len(sys.argv) > 2:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)
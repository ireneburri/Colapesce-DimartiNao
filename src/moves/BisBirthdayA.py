# Choregraphe simplified export in Python.
from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-0.0414599, -0.154976, -0.162646, -0.154976, -0.154976, -0.1335])

    names.append("HeadYaw")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-0.00157596, -0.214801, -0.213269, -0.214801, -0.2102, -4.19617e-05])

    names.append("LAnklePitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-0.113689, -0.340721, -0.244079, -0.340721, -0.00170743, 0.00749657])

    names.append("LAnkleRoll")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.0168944, -0.0398637, -0.167186, -0.0398637, -0.265362, 0.0092244])

    names.append("LElbowRoll")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-0.340507, -1.54776, -1.54163, -1.54776, -1.54009, -0.558334])

    names.append("LElbowYaw")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-0.767043, -1.14441, -1.47882, -1.14441, -1.33155, -1.86232])

    names.append("LHand")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.916387, 0.41748, 0.417116, 0.41748, 0.41748, 1])

    names.append("LHipPitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.0749446, -0.242594, 0.438502, -0.242594, 0.271296, 0.378677])

    names.append("LHipRoll")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-0.0477461, 0.17315, 0.185422, 0.17315, 0.24218, -0.0324061])

    names.append("LHipYawPitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.0275685, -0.523138, -0.401951, -0.523138, -0.357466, -0.369738])

    names.append("LKneePitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.0886521, 0.775884, 0.133138, 0.775884, 0.00581614, 0.0119521])

    names.append("LShoulderPitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([1.58765, 1.45266, 1.98343, 1.45266, 2.0187, 0.708667])

    names.append("LShoulderRoll")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.303691, 0, 0.115008, 0, 0, 0])

    names.append("LWristYaw")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-1.00328, -0.694945, -0.65506, -0.694945, -0.688808, -0.690342])

    names.append("RAnklePitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-0.104339, 0.0398569, -0.270011, 0.0398569, -0.451023, -0.167233])

    names.append("RAnkleRoll")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-0.00456227, 0.108954, 0.0859437, 0.108954, 0.00464174, 0.147304])

    names.append("RElbowRoll")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.305309, 1.12907, 1.1214, 1.12907, 1.126, 0.553816])

    names.append("RElbowYaw")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.786901, 1.52475, 1.18574, 1.52475, 1.51555, 1.7886])

    names.append("RHand")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.917842, 0.411661, 0.411661, 0.411661, 0.411661, 1])

    names.append("RHipPitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.039827, 0.315946, 0.010681, 0.315946, 0.042895, 0.243849])

    names.append("RHipRoll")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.0153604, 0.0260984, -0.144176, 0.0260984, -0.0644075, -0.200933])

    names.append("RKneePitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.103898, 0, 0.570234, 0, 0.665342, 0.243493])

    names.append("RShoulderPitch")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([1.55859, 2.01572, 1.48035, 2.01572, 1.43893, 0.529271])

    names.append("RShoulderRoll")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([-0.296104, -0.082878, -0.01078, -0.082878, -0.081344, -0.00924597])

    names.append("RWristYaw")
    times.append([0.2, 0.466667, 0.733333, 1.06667, 1.33333, 1.6])
    keys.append([0.946436, 0.76389, 0.766959, 0.76389, 0.760822, 0.77923])


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
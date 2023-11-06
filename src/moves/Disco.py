# Choregraphe bezier export in Python.
from naoqi import ALProxy

def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.8])
    keys.append([[-0.476475, [3, -0.56, 0], [3, 0.266667, 0]], [0.338594, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.476475, [3, -0.306667, 0], [3, 0.266667, 0]], [0.338594, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.476475, [3, -0.293333, 0], [3, 0.266667, 0]], [0.338594, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.476475, [3, -0.306667, 0], [3, 0.266667, 0]], [0.338594, [3, -0.266667, 0], [3, 0.36, 0]], [-0.476475, [3, -0.36, 0], [3, 0.266667, 0]], [0.338594, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.476475, [3, -0.306667, 0], [3, 0.266667, 0]], [0.338594, [3, -0.266667, 0], [3, 0.28, 0]], [-0.476475, [3, -0.28, 0], [3, 0.266667, 0]], [0.338594, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.476475, [3, -0.293333, 0], [3, 0.266667, 0]], [0.338594, [3, -0.266667, 0], [3, 0.44, 0]], [-0.17185, [3, -0.44, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.8])
    keys.append([[-0.745256, [3, -0.56, 0], [3, 0.266667, 0]], [0.289725, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.745256, [3, -0.306667, 0], [3, 0.266667, 0]], [0.289725, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.745256, [3, -0.293333, 0], [3, 0.266667, 0]], [0.289725, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.745256, [3, -0.306667, 0], [3, 0.266667, 0]], [0.289725, [3, -0.266667, -0.21142], [3, 0.36, 0.285417]], [0.745256, [3, -0.36, 0], [3, 0.266667, 0]], [-0.289725, [3, -0.266667, 0], [3, 0.306667, 0]], [0.745256, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.289725, [3, -0.266667, 0], [3, 0.28, 0]], [0.745256, [3, -0.28, 0], [3, 0.266667, 0]], [-0.289725, [3, -0.266667, 0], [3, 0.293333, 0]], [0.745256, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.289725, [3, -0.266667, 0], [3, 0.44, 0]], [0.00916195, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[-0.046062, [3, -0.24, 0], [3, 0.293333, 0]], [0.0444441, [3, -0.293333, -0.0361586], [3, 0.266667, 0.0328714]], [0.161028, [3, -0.266667, 0], [3, 0.306667, 0]], [0.0444441, [3, -0.306667, 0], [3, 0.266667, 0]], [0.161028, [3, -0.266667, 0], [3, 0.293333, 0]], [0.0444441, [3, -0.293333, 0], [3, 0.266667, 0]], [0.161028, [3, -0.266667, 0], [3, 0.306667, 0]], [0.0444441, [3, -0.306667, 0], [3, 0.266667, 0]], [0.161028, [3, -0.266667, 0], [3, 0.36, 0]], [0.092082, [3, -0.36, 0.0124254], [3, 0.266667, -0.00920399]], [0.082878, [3, -0.266667, 0], [3, 0.306667, 0]], [0.092082, [3, -0.306667, 0], [3, 0.266667, 0]], [0.082878, [3, -0.266667, 0], [3, 0.28, 0]], [0.092082, [3, -0.28, 0], [3, 0.266667, 0]], [0.082878, [3, -0.266667, 0], [3, 0.293333, 0]], [0.092082, [3, -0.293333, 0], [3, 0.266667, 0]], [0.082878, [3, -0.266667, 0], [3, 0.44, 0]], [0.0873961, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[-0.0183661, [3, -0.24, 0], [3, 0.293333, 0]], [0.062936, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.248467, [3, -0.266667, 0], [3, 0.306667, 0]], [0.062936, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.248467, [3, -0.266667, 0], [3, 0.293333, 0]], [0.062936, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.248467, [3, -0.266667, 0], [3, 0.306667, 0]], [0.062936, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.248467, [3, -0.266667, 0.0114248], [3, 0.36, -0.0154235]], [-0.26389, [3, -0.36, 0], [3, 0.266667, 0]], [0.0904641, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.26389, [3, -0.306667, 0], [3, 0.266667, 0]], [0.0904641, [3, -0.266667, 0], [3, 0.28, 0]], [-0.26389, [3, -0.28, 0], [3, 0.266667, 0]], [0.0904641, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.26389, [3, -0.293333, 0], [3, 0.266667, 0]], [0.0904641, [3, -0.266667, 0], [3, 0.44, 0]], [-0.121144, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.8, 1.24, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12, 8.72, 9.12, 9.52, 10, 10.44, 10.84, 11.24, 11.72, 12.08, 12.48, 12.88, 13.36, 13.76, 14.16, 14.56, 15.04, 15.88])
    keys.append([[-1.37289, [3, -0.28, 0], [3, 0.146667, 0]], [-1.12923, [3, -0.146667, -0.175168], [3, 0.133333, 0.159244]], [-0.369652, [3, -0.133333, -0.083603], [3, 0.266667, 0.167206]], [-0.202446, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.369652, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.202446, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.369652, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.202446, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.369652, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.202446, [3, -0.266667, 0], [3, 0.186667, 0]], [-1.54462, [3, -0.186667, 0], [3, 0.2, 0]], [-0.138102, [3, -0.2, 0], [3, 0.133333, 0]], [-1.309, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.257754, [3, -0.133333, 0], [3, 0.16, 0]], [-1.4591, [3, -0.16, 0], [3, 0.146667, 0]], [-0.138102, [3, -0.146667, 0], [3, 0.133333, 0]], [-1.309, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.257754, [3, -0.133333, 0], [3, 0.16, 0]], [-1.4591, [3, -0.16, 0], [3, 0.12, 0]], [-0.138102, [3, -0.12, 0], [3, 0.133333, 0]], [-1.309, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.257754, [3, -0.133333, 0], [3, 0.16, 0]], [-1.4591, [3, -0.16, 0], [3, 0.133333, 0]], [-0.138102, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.309, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.257754, [3, -0.133333, 0], [3, 0.16, 0]], [-1.4591, [3, -0.16, 0], [3, 0.28, 0]], [-0.424876, [3, -0.28, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.8, 1.24, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12, 8.72, 9.12, 9.52, 10, 10.44, 10.84, 11.24, 11.72, 12.08, 12.48, 12.88, 13.36, 13.76, 14.16, 14.56, 15.04, 15.88])
    keys.append([[-0.65506, [3, -0.28, 0], [3, 0.146667, 0]], [-1.76453, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.380475, [3, -0.133333, 0], [3, 0.266667, 0]], [-0.618244, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.380475, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.618244, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.380475, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.618244, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.380475, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.618244, [3, -0.266667, 0.23777], [3, 0.186667, -0.166439]], [-1.65632, [3, -0.186667, 0], [3, 0.2, 0]], [0.851412, [3, -0.2, 0], [3, 0.133333, 0]], [0.0750492, [3, -0.133333, 0.0734732], [3, 0.133333, -0.0734732]], [0.00157596, [3, -0.133333, 0], [3, 0.16, 0]], [0.460767, [3, -0.16, -0.147798], [3, 0.146667, 0.135481]], [0.851412, [3, -0.146667, 0], [3, 0.133333, 0]], [0.0750492, [3, -0.133333, 0.0734732], [3, 0.133333, -0.0734732]], [0.00157596, [3, -0.133333, 0], [3, 0.16, 0]], [0.460767, [3, -0.16, -0.161873], [3, 0.12, 0.121405]], [0.851412, [3, -0.12, 0], [3, 0.133333, 0]], [0.0750492, [3, -0.133333, 0.0734732], [3, 0.133333, -0.0734732]], [0.00157596, [3, -0.133333, 0], [3, 0.16, 0]], [0.460767, [3, -0.16, -0.154516], [3, 0.133333, 0.128763]], [0.851412, [3, -0.133333, 0], [3, 0.133333, 0]], [0.0750492, [3, -0.133333, 0.0734732], [3, 0.133333, -0.0734732]], [0.00157596, [3, -0.133333, 0.0734732], [3, 0.16, -0.0881678]], [-0.682424, [3, -0.16, 0.146902], [3, 0.28, -0.257079]], [-1.21037, [3, -0.28, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.8, 1.24, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12, 8.72, 9.12, 9.52, 10, 10.44, 10.84, 11.24, 11.72, 12.08, 12.48, 12.88, 13.36, 13.76, 14.16, 14.56, 15.04, 15.88])
    keys.append([[0.2, [3, -0.28, 0], [3, 0.146667, 0]], [0.6, [3, -0.146667, 0], [3, 0.133333, 0]], [0.2648, [3, -0.133333, 0.000400007], [3, 0.266667, -0.000800014]], [0.264, [3, -0.266667, 0], [3, 0.306667, 0]], [0.2648, [3, -0.306667, 0], [3, 0.266667, 0]], [0.264, [3, -0.266667, 0], [3, 0.293333, 0]], [0.2648, [3, -0.293333, 0], [3, 0.266667, 0]], [0.264, [3, -0.266667, 0], [3, 0.306667, 0]], [0.2648, [3, -0.306667, 0], [3, 0.266667, 0]], [0.264, [3, -0.266667, 0.000800014], [3, 0.186667, -0.00056001]], [0.13, [3, -0.186667, 0], [3, 0.2, 0]], [0.678, [3, -0.2, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.133333, 0]], [0.6784, [3, -0.133333, 0], [3, 0.16, 0]], [0.3, [3, -0.16, 0], [3, 0.146667, 0]], [0.678, [3, -0.146667, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.133333, 0]], [0.6784, [3, -0.133333, 0], [3, 0.16, 0]], [0.3, [3, -0.16, 0], [3, 0.12, 0]], [0.678, [3, -0.12, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.133333, 0]], [0.6784, [3, -0.133333, 0], [3, 0.16, 0]], [0.3, [3, -0.16, 0], [3, 0.133333, 0]], [0.678, [3, -0.133333, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.133333, 0]], [0.6784, [3, -0.133333, 0], [3, 0.16, 0]], [0.3, [3, -0.16, 0.00182859], [3, 0.28, -0.00320002]], [0.2968, [3, -0.28, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[-0.153358, [3, -0.24, 0], [3, 0.293333, 0]], [0.185656, [3, -0.293333, 0], [3, 0.266667, 0]], [0.147306, [3, -0.266667, 0], [3, 0.306667, 0]], [0.185656, [3, -0.306667, 0], [3, 0.266667, 0]], [0.147306, [3, -0.266667, 0], [3, 0.293333, 0]], [0.185656, [3, -0.293333, 0], [3, 0.266667, 0]], [0.147306, [3, -0.266667, 0], [3, 0.306667, 0]], [0.185656, [3, -0.306667, 0], [3, 0.266667, 0]], [0.147306, [3, -0.266667, 0.0119793], [3, 0.36, -0.016172]], [0.101202, [3, -0.36, 0], [3, 0.266667, 0]], [0.259204, [3, -0.266667, 0], [3, 0.306667, 0]], [0.101202, [3, -0.306667, 0], [3, 0.266667, 0]], [0.259204, [3, -0.266667, 0], [3, 0.28, 0]], [0.101202, [3, -0.28, 0], [3, 0.266667, 0]], [0.259204, [3, -0.266667, 0], [3, 0.293333, 0]], [0.101202, [3, -0.293333, 0], [3, 0.266667, 0]], [0.259204, [3, -0.266667, 0], [3, 0.44, 0]], [0.139636, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[0.00464395, [3, -0.24, 0], [3, 0.293333, 0]], [-0.144154, [3, -0.293333, 0], [3, 0.266667, 0]], [0.329852, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.144154, [3, -0.306667, 0], [3, 0.266667, 0]], [0.329852, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.144154, [3, -0.293333, 0], [3, 0.266667, 0]], [0.329852, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.144154, [3, -0.306667, 0], [3, 0.266667, 0]], [0.329852, [3, -0.266667, 0], [3, 0.36, 0]], [0.297554, [3, -0.36, 0.0322973], [3, 0.266667, -0.0239239]], [-0.14117, [3, -0.266667, 0], [3, 0.306667, 0]], [0.297554, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.14117, [3, -0.266667, 0], [3, 0.28, 0]], [0.297554, [3, -0.28, 0], [3, 0.266667, 0]], [-0.14117, [3, -0.266667, 0], [3, 0.293333, 0]], [0.297554, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.14117, [3, -0.266667, 0], [3, 0.44, 0]], [0.10282, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[-0.443284, [3, -0.24, 0], [3, 0.293333, 0]], [-0.37272, [3, -0.293333, -0.014999], [3, 0.266667, 0.0136355]], [-0.357381, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.37272, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.357381, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.37272, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.357381, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.37272, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.357381, [3, -0.266667, 0], [3, 0.36, 0]], [-0.37272, [3, -0.36, 0], [3, 0.266667, 0]], [-0.357381, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.37272, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.357381, [3, -0.266667, 0], [3, 0.28, 0]], [-0.37272, [3, -0.28, 0], [3, 0.266667, 0]], [-0.357381, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.37272, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.357381, [3, -0.266667, -0.0153397], [3, 0.44, 0.0253105]], [-0.170232, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[0.404934, [3, -0.24, 0], [3, 0.293333, 0]], [-0.090548, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.0798099, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.090548, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.0798099, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.090548, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.0798099, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.090548, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.0798099, [3, -0.266667, 0], [3, 0.36, 0]], [-0.0904641, [3, -0.36, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.0904641, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.28, 0]], [-0.0904641, [3, -0.28, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.0904641, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.44, 0]], [-0.0782759, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.8, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12, 8.72, 9.52, 10.44, 11.24, 12.08, 12.88, 13.76, 14.56, 15.36, 15.88])
    keys.append([[0.639635, [3, -0.28, 0], [3, 0.28, 0]], [1.74718, [3, -0.28, -0.114372], [3, 0.266667, 0.108926]], [1.85611, [3, -0.266667, 0], [3, 0.306667, 0]], [1.74718, [3, -0.306667, 0], [3, 0.266667, 0]], [1.85611, [3, -0.266667, 0], [3, 0.293333, 0]], [1.74718, [3, -0.293333, 0], [3, 0.266667, 0]], [1.85611, [3, -0.266667, 0], [3, 0.306667, 0]], [1.74718, [3, -0.306667, 0], [3, 0.266667, 0]], [1.85611, [3, -0.266667, 0], [3, 0.186667, 0]], [1.21475, [3, -0.186667, 0.49048], [3, 0.2, -0.525514]], [-1.19188, [3, -0.2, 0], [3, 0.266667, 0]], [0.995607, [3, -0.266667, 0], [3, 0.306667, 0]], [-1.19188, [3, -0.306667, 0], [3, 0.266667, 0]], [0.995607, [3, -0.266667, 0], [3, 0.28, 0]], [-1.19188, [3, -0.28, 0], [3, 0.266667, 0]], [0.995607, [3, -0.266667, 0], [3, 0.293333, 0]], [-1.19188, [3, -0.293333, 0], [3, 0.266667, 0]], [0.995607, [3, -0.266667, -0.0690435], [3, 0.266667, 0.0690435]], [1.06465, [3, -0.266667, -0.0690434], [3, 0.173333, 0.0448782]], [1.47106, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.8, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12, 8.72, 9.12, 9.52, 10, 10.44, 10.84, 11.24, 11.72, 12.08, 12.48, 12.88, 13.36, 13.76, 14.16, 14.56, 15.04, 15.88])
    keys.append([[0.340507, [3, -0.28, 0], [3, 0.28, 0]], [0.24233, [3, -0.28, 0.0246191], [3, 0.266667, -0.0234467]], [0.196309, [3, -0.266667, 0], [3, 0.306667, 0]], [0.24233, [3, -0.306667, 0], [3, 0.266667, 0]], [0.196309, [3, -0.266667, 0], [3, 0.293333, 0]], [0.24233, [3, -0.293333, 0], [3, 0.266667, 0]], [0.196309, [3, -0.266667, 0], [3, 0.306667, 0]], [0.24233, [3, -0.306667, 0], [3, 0.266667, 0]], [0.196309, [3, -0.266667, 0.0150047], [3, 0.186667, -0.0105033]], [0.165806, [3, -0.186667, 0], [3, 0.2, 0]], [0.328317, [3, -0.2, -0.0858702], [3, 0.133333, 0.0572468]], [0.595157, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.314159, [3, -0.133333, 0], [3, 0.16, 0]], [0.595157, [3, -0.16, 0], [3, 0.146667, 0]], [0.328317, [3, -0.146667, 0], [3, 0.133333, 0]], [0.595157, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.314159, [3, -0.133333, 0], [3, 0.16, 0]], [0.595157, [3, -0.16, 0], [3, 0.12, 0]], [0.328317, [3, -0.12, 0], [3, 0.133333, 0]], [0.595157, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.314159, [3, -0.133333, 0], [3, 0.16, 0]], [0.595157, [3, -0.16, 0], [3, 0.133333, 0]], [0.328317, [3, -0.133333, 0], [3, 0.133333, 0]], [0.595157, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.314159, [3, -0.133333, 0], [3, 0.16, 0]], [0.595157, [3, -0.16, 0], [3, 0.28, 0]], [0.153358, [3, -0.28, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.8, 1.24, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.72, 9.52, 10.44, 11.24, 12.08, 12.88, 13.76, 14.56, 15.88])
    keys.append([[0.11961, [3, -0.28, 0], [3, 0.146667, 0]], [-1.45037, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.395814, [3, -0.133333, 0], [3, 0.266667, 0]], [-0.420357, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.395814, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.420357, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.395814, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.420357, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.395814, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.420357, [3, -0.266667, 0], [3, 0.386667, 0]], [-0.107338, [3, -0.386667, 0], [3, 0.266667, 0]], [-0.400331, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.107338, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.400331, [3, -0.266667, 0], [3, 0.28, 0]], [-0.107338, [3, -0.28, 0], [3, 0.266667, 0]], [-0.400331, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.107338, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.400331, [3, -0.266667, 0], [3, 0.44, 0]], [0.0827939, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[-0.052114, [3, -0.24, 0], [3, 0.293333, 0]], [0.092082, [3, -0.293333, 0], [3, 0.266667, 0]], [0.082878, [3, -0.266667, 0], [3, 0.306667, 0]], [0.092082, [3, -0.306667, 0], [3, 0.266667, 0]], [0.082878, [3, -0.266667, 0], [3, 0.293333, 0]], [0.092082, [3, -0.293333, 0], [3, 0.266667, 0]], [0.082878, [3, -0.266667, 0], [3, 0.306667, 0]], [0.092082, [3, -0.306667, 0], [3, 0.266667, 0]], [0.082878, [3, -0.266667, 0.00675715], [3, 0.36, -0.00912215]], [0.0444441, [3, -0.36, 0], [3, 0.266667, 0]], [0.161028, [3, -0.266667, 0], [3, 0.306667, 0]], [0.0444441, [3, -0.306667, 0], [3, 0.266667, 0]], [0.161028, [3, -0.266667, 0], [3, 0.28, 0]], [0.0444441, [3, -0.28, 0], [3, 0.266667, 0]], [0.161028, [3, -0.266667, 0], [3, 0.293333, 0]], [0.0444441, [3, -0.293333, 0], [3, 0.266667, 0]], [0.161028, [3, -0.266667, 0], [3, 0.44, 0]], [0.093616, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[0.0966839, [3, -0.24, 0], [3, 0.293333, 0]], [0.26389, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.306667, 0]], [0.26389, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.293333, 0]], [0.26389, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.306667, 0]], [0.26389, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.36, 0]], [-0.062936, [3, -0.36, -0.027528], [3, 0.266667, 0.0203911]], [0.248467, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.062936, [3, -0.306667, 0], [3, 0.266667, 0]], [0.248467, [3, -0.266667, 0], [3, 0.28, 0]], [-0.062936, [3, -0.28, 0], [3, 0.266667, 0]], [0.248467, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.062936, [3, -0.293333, 0], [3, 0.266667, 0]], [0.248467, [3, -0.266667, 0], [3, 0.44, 0]], [0.119694, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.88, 1.32, 1.72, 2.12, 2.52, 3, 3.44, 3.84, 4.24, 4.72, 5.12, 5.52, 5.92, 6.4, 6.84, 7.24, 7.64, 8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.08, 15.4, 15.8])
    keys.append([[1.34689, [3, -0.306667, 0], [3, 0.146667, 0]], [1.1205, [3, -0.146667, 0.211059], [3, 0.133333, -0.191872]], [0.138102, [3, -0.133333, 0], [3, 0.133333, 0]], [1.309, [3, -0.133333, 0], [3, 0.133333, 0]], [0.257754, [3, -0.133333, 0], [3, 0.16, 0]], [1.4591, [3, -0.16, 0], [3, 0.146667, 0]], [0.138102, [3, -0.146667, 0], [3, 0.133333, 0]], [1.309, [3, -0.133333, 0], [3, 0.133333, 0]], [0.257754, [3, -0.133333, 0], [3, 0.16, 0]], [1.4591, [3, -0.16, 0], [3, 0.133333, 0]], [0.138102, [3, -0.133333, 0], [3, 0.133333, 0]], [1.309, [3, -0.133333, 0], [3, 0.133333, 0]], [0.257754, [3, -0.133333, 0], [3, 0.16, 0]], [1.4591, [3, -0.16, 0], [3, 0.146667, 0]], [0.138102, [3, -0.146667, 0], [3, 0.133333, 0]], [1.309, [3, -0.133333, 0], [3, 0.133333, 0]], [0.257754, [3, -0.133333, 0], [3, 0.16, 0]], [1.54462, [3, -0.16, 0], [3, 0.173333, 0]], [0.369652, [3, -0.173333, 0.108684], [3, 0.266667, -0.167206]], [0.202446, [3, -0.266667, 0], [3, 0.306667, 0]], [0.369652, [3, -0.306667, 0], [3, 0.266667, 0]], [0.202446, [3, -0.266667, 0], [3, 0.28, 0]], [0.369652, [3, -0.28, 0], [3, 0.266667, 0]], [0.202446, [3, -0.266667, 0], [3, 0.293333, 0]], [0.369652, [3, -0.293333, 0], [3, 0.266667, 0]], [0.202446, [3, -0.266667, 0], [3, 0.2, 0]], [0.82205, [3, -0.2, -0.121082], [3, 0.106667, 0.0645772]], [0.886627, [3, -0.106667, 0], [3, 0.133333, 0]], [0.429562, [3, -0.133333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.88, 1.32, 1.72, 2.12, 2.52, 3, 3.44, 3.84, 4.24, 4.72, 5.12, 5.52, 5.92, 6.4, 6.84, 7.24, 7.64, 8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.08, 15.4, 15.8])
    keys.append([[0.59515, [3, -0.306667, 0], [3, 0.146667, 0]], [0.567232, [3, -0.146667, 0.0279183], [3, 0.133333, -0.0253803]], [-0.851412, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.0750492, [3, -0.133333, -0.0734732], [3, 0.133333, 0.0734732]], [-0.00157596, [3, -0.133333, 0], [3, 0.16, 0]], [-0.460767, [3, -0.16, 0.147798], [3, 0.146667, -0.135481]], [-0.851412, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.0750492, [3, -0.133333, -0.0734732], [3, 0.133333, 0.0734732]], [-0.00157596, [3, -0.133333, 0], [3, 0.16, 0]], [-0.460767, [3, -0.16, 0.154516], [3, 0.133333, -0.128763]], [-0.851412, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.0750492, [3, -0.133333, -0.0734732], [3, 0.133333, 0.0734732]], [-0.00157596, [3, -0.133333, 0], [3, 0.16, 0]], [-0.460767, [3, -0.16, 0.147798], [3, 0.146667, -0.135481]], [-0.851412, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.0750492, [3, -0.133333, -0.0734732], [3, 0.133333, 0.0734732]], [-0.00157596, [3, -0.133333, -0.0734732], [3, 0.16, 0.0881678]], [1.65632, [3, -0.16, 0], [3, 0.173333, 0]], [0.380475, [3, -0.173333, 0], [3, 0.266667, 0]], [0.618244, [3, -0.266667, 0], [3, 0.306667, 0]], [0.380475, [3, -0.306667, 0], [3, 0.266667, 0]], [0.618244, [3, -0.266667, 0], [3, 0.28, 0]], [0.380475, [3, -0.28, 0], [3, 0.266667, 0]], [0.618244, [3, -0.266667, 0], [3, 0.293333, 0]], [0.380475, [3, -0.293333, 0], [3, 0.266667, 0]], [0.618244, [3, -0.266667, -0.22839], [3, 0.2, 0.171293]], [1.57952, [3, -0.2, 0], [3, 0.106667, 0]], [1.03323, [3, -0.106667, 0], [3, 0.133333, 0]], [1.21028, [3, -0.133333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.88, 1.32, 1.72, 2.12, 2.52, 3, 3.44, 3.84, 4.24, 4.72, 5.12, 5.52, 5.92, 6.4, 6.84, 7.24, 7.64, 8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.4, 15.8])
    keys.append([[0.2, [3, -0.306667, 0], [3, 0.146667, 0]], [0.5, [3, -0.146667, -0.0834603], [3, 0.133333, 0.075873]], [0.678, [3, -0.133333, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.133333, 0]], [0.6784, [3, -0.133333, 0], [3, 0.16, 0]], [0.3, [3, -0.16, 0], [3, 0.146667, 0]], [0.678, [3, -0.146667, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.133333, 0]], [0.6784, [3, -0.133333, 0], [3, 0.16, 0]], [0.3, [3, -0.16, 0], [3, 0.133333, 0]], [0.678, [3, -0.133333, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.133333, 0]], [0.6784, [3, -0.133333, 0], [3, 0.16, 0]], [0.3, [3, -0.16, 0], [3, 0.146667, 0]], [0.678, [3, -0.146667, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.133333, 0]], [0.6784, [3, -0.133333, 0], [3, 0.16, 0]], [0.13, [3, -0.16, 0], [3, 0.173333, 0]], [0.2648, [3, -0.173333, 0], [3, 0.266667, 0]], [0.264, [3, -0.266667, 0], [3, 0.306667, 0]], [0.2648, [3, -0.306667, 0], [3, 0.266667, 0]], [0.264, [3, -0.266667, 0], [3, 0.28, 0]], [0.2648, [3, -0.28, 0], [3, 0.266667, 0]], [0.264, [3, -0.266667, 0], [3, 0.293333, 0]], [0.2648, [3, -0.293333, 0], [3, 0.266667, 0]], [0.264, [3, -0.266667, 0.000800014], [3, 0.306667, -0.000920016]], [0.24, [3, -0.306667, 0], [3, 0.133333, 0]], [0.2976, [3, -0.133333, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[-0.177985, [3, -0.24, 0], [3, 0.293333, 0]], [0.101202, [3, -0.293333, -0.0763346], [3, 0.266667, 0.0693951]], [0.259204, [3, -0.266667, 0], [3, 0.306667, 0]], [0.101202, [3, -0.306667, 0], [3, 0.266667, 0]], [0.259204, [3, -0.266667, 0], [3, 0.293333, 0]], [0.101202, [3, -0.293333, 0], [3, 0.266667, 0]], [0.259204, [3, -0.266667, 0], [3, 0.306667, 0]], [0.101202, [3, -0.306667, 0], [3, 0.266667, 0]], [0.259204, [3, -0.266667, 0], [3, 0.36, 0]], [0.185656, [3, -0.36, 0.0214273], [3, 0.266667, -0.0158721]], [0.147306, [3, -0.266667, 0], [3, 0.306667, 0]], [0.185656, [3, -0.306667, 0], [3, 0.266667, 0]], [0.147306, [3, -0.266667, 0], [3, 0.28, 0]], [0.185656, [3, -0.28, 0], [3, 0.266667, 0]], [0.147306, [3, -0.266667, 0], [3, 0.293333, 0]], [0.185656, [3, -0.293333, 0], [3, 0.266667, 0]], [0.147306, [3, -0.266667, 0.00676402], [3, 0.44, -0.0111606]], [0.131882, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[-0.11961, [3, -0.24, 0], [3, 0.293333, 0]], [-0.297554, [3, -0.293333, 0], [3, 0.266667, 0]], [0.14117, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.297554, [3, -0.306667, 0], [3, 0.266667, 0]], [0.14117, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.297554, [3, -0.293333, 0], [3, 0.266667, 0]], [0.14117, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.297554, [3, -0.306667, 0], [3, 0.266667, 0]], [0.14117, [3, -0.266667, -0.0022105], [3, 0.36, 0.00298417]], [0.144154, [3, -0.36, 0], [3, 0.266667, 0]], [-0.329852, [3, -0.266667, 0], [3, 0.306667, 0]], [0.144154, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.329852, [3, -0.266667, 0], [3, 0.28, 0]], [0.144154, [3, -0.28, 0], [3, 0.266667, 0]], [-0.329852, [3, -0.266667, 0], [3, 0.293333, 0]], [0.144154, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.329852, [3, -0.266667, 0], [3, 0.44, 0]], [-0.0966001, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([1.56, 3.28, 4.96, 6.68, 8.56, 10.28, 11.92, 13.6, 15.72])
    keys.append([[-0.37272, [3, -0.533333, 0], [3, 0.573333, 0]], [-0.37272, [3, -0.573333, 0], [3, 0.56, 0]], [-0.37272, [3, -0.56, 0], [3, 0.573333, 0]], [-0.37272, [3, -0.573333, 0], [3, 0.626667, 0]], [-0.37272, [3, -0.626667, 0], [3, 0.573333, 0]], [-0.37272, [3, -0.573333, 0], [3, 0.546667, 0]], [-0.37272, [3, -0.546667, 0], [3, 0.56, 0]], [-0.37272, [3, -0.56, 0], [3, 0.706667, 0]], [-0.170232, [3, -0.706667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48, 8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])
    keys.append([[0.426494, [3, -0.24, 0], [3, 0.293333, 0]], [-0.0904641, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.0904641, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.0904641, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.0904641, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.0904641, [3, -0.266667, 0], [3, 0.36, 0]], [-0.090548, [3, -0.36, 0], [3, 0.266667, 0]], [-0.0798099, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.090548, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.0798099, [3, -0.266667, 0], [3, 0.28, 0]], [-0.090548, [3, -0.28, 0], [3, 0.266667, 0]], [-0.0798099, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.090548, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.0798099, [3, -0.266667, 0], [3, 0.44, 0]], [-0.091998, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.88, 1.72, 2.52, 3.44, 4.24, 5.12, 5.92, 6.84, 7.64, 8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.4, 15.8])
    keys.append([[0.915841, [3, -0.306667, 0], [3, 0.28, 0]], [-1.19188, [3, -0.28, 0], [3, 0.266667, 0]], [0.995607, [3, -0.266667, 0], [3, 0.306667, 0]], [-1.19188, [3, -0.306667, 0], [3, 0.266667, 0]], [0.995607, [3, -0.266667, 0], [3, 0.293333, 0]], [-1.19188, [3, -0.293333, 0], [3, 0.266667, 0]], [0.995607, [3, -0.266667, 0], [3, 0.306667, 0]], [-1.19188, [3, -0.306667, 0], [3, 0.266667, 0]], [0.995607, [3, -0.266667, -0.365236], [3, 0.16, 0.219142]], [1.21475, [3, -0.16, -0.120252], [3, 0.173333, 0.130272]], [1.74718, [3, -0.173333, -0.0708019], [3, 0.266667, 0.108926]], [1.85611, [3, -0.266667, 0], [3, 0.306667, 0]], [1.74718, [3, -0.306667, 0], [3, 0.266667, 0]], [1.85611, [3, -0.266667, 0], [3, 0.28, 0]], [1.74718, [3, -0.28, 0], [3, 0.266667, 0]], [1.85611, [3, -0.266667, 0], [3, 0.293333, 0]], [1.74718, [3, -0.293333, 0], [3, 0.266667, 0]], [1.85611, [3, -0.266667, 0], [3, 0.306667, 0]], [1.18508, [3, -0.306667, 0], [3, 0.133333, 0]], [1.47268, [3, -0.133333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.88, 1.32, 1.72, 2.12, 2.52, 3, 3.44, 3.84, 4.24, 4.72, 5.12, 5.52, 5.92, 6.4, 6.84, 7.24, 7.64, 8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.08, 15.8])
    keys.append([[-0.266959, [3, -0.306667, 0], [3, 0.146667, 0]], [-0.670206, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.328317, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.595157, [3, -0.133333, 0], [3, 0.133333, 0]], [0.314159, [3, -0.133333, 0], [3, 0.16, 0]], [-0.595157, [3, -0.16, 0], [3, 0.146667, 0]], [-0.328317, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.595157, [3, -0.133333, 0], [3, 0.133333, 0]], [0.314159, [3, -0.133333, 0], [3, 0.16, 0]], [-0.595157, [3, -0.16, 0], [3, 0.133333, 0]], [-0.328317, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.595157, [3, -0.133333, 0], [3, 0.133333, 0]], [0.314159, [3, -0.133333, 0], [3, 0.16, 0]], [-0.595157, [3, -0.16, 0], [3, 0.146667, 0]], [-0.328317, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.595157, [3, -0.133333, 0], [3, 0.133333, 0]], [0.314159, [3, -0.133333, 0], [3, 0.16, 0]], [-0.165806, [3, -0.16, 0.0706375], [3, 0.173333, -0.0765239]], [-0.24233, [3, -0.173333, 0], [3, 0.266667, 0]], [-0.196309, [3, -0.266667, 0], [3, 0.306667, 0]], [-0.24233, [3, -0.306667, 0], [3, 0.266667, 0]], [-0.196309, [3, -0.266667, 0], [3, 0.28, 0]], [-0.24233, [3, -0.28, 0], [3, 0.266667, 0]], [-0.196309, [3, -0.266667, 0], [3, 0.293333, 0]], [-0.24233, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.196309, [3, -0.266667, 0], [3, 0.2, 0]], [-0.455531, [3, -0.2, 0], [3, 0.24, 0]], [-0.16418, [3, -0.24, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.88, 1.32, 1.72, 2.52, 3.44, 4.24, 5.12, 5.92, 6.84, 7.64, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.8])
    keys.append([[-0.401949, [3, -0.306667, 0], [3, 0.146667, 0]], [1.39277, [3, -0.146667, 0], [3, 0.133333, 0]], [0.107338, [3, -0.133333, 0], [3, 0.266667, 0]], [0.400331, [3, -0.266667, 0], [3, 0.306667, 0]], [0.107338, [3, -0.306667, 0], [3, 0.266667, 0]], [0.400331, [3, -0.266667, 0], [3, 0.293333, 0]], [0.107338, [3, -0.293333, 0], [3, 0.266667, 0]], [0.400331, [3, -0.266667, 0], [3, 0.306667, 0]], [0.107338, [3, -0.306667, 0], [3, 0.266667, 0]], [0.400331, [3, -0.266667, 0], [3, 0.333333, 0]], [0.395814, [3, -0.333333, 0], [3, 0.266667, 0]], [0.420357, [3, -0.266667, 0], [3, 0.306667, 0]], [0.395814, [3, -0.306667, 0], [3, 0.266667, 0]], [0.420357, [3, -0.266667, 0], [3, 0.28, 0]], [0.395814, [3, -0.28, 0], [3, 0.266667, 0]], [0.420357, [3, -0.266667, 0], [3, 0.293333, 0]], [0.395814, [3, -0.293333, 0], [3, 0.266667, 0]], [0.420357, [3, -0.266667, 0], [3, 0.44, 0]], [0.108872, [3, -0.44, 0], [3, 0, 0]]])

    try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    # motion = ALProxy("ALMotion", IP, 9559)
    motion = ALProxy("ALMotion")
    motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
    print err


if __name__ == "__main__":

    robotIP = "127.0.0.1" 

    port = 9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)
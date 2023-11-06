# Choregraphe bezier export in Python.
from naoqi import ALProxy

def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-0.0414599, [3, -0.244444, 0], [3, 0.155556, 0]], [-0.154976, [3, -0.155556, 0.00767002], [3, 0.155556, -0.00767002]], [-0.162646, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.154976, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.154976, [3, -0.133333, 0], [3, 0.155556, 0]], [-0.154976, [3, -0.155556, 0], [3, 0.177778, 0]], [-0.154976, [3, -0.177778, 0], [3, 0.155556, 0]], [-0.154976, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.154976, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.1335, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.145772, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.1335, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.145772, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.1335, [3, -0.244444, 0], [3, 0.2, 0]], [-0.145772, [3, -0.2, 0], [3, 0.266667, 0]], [-0.1335, [3, -0.266667, 0], [3, 0.288889, 0]], [-0.1335, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-0.00157596, [3, -0.244444, 0], [3, 0.155556, 0]], [-0.214801, [3, -0.155556, 0], [3, 0.155556, 0]], [-0.213269, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.214801, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.2102, [3, -0.133333, 0], [3, 0.155556, 0]], [-0.214801, [3, -0.155556, 0], [3, 0.177778, 0]], [-0.2102, [3, -0.177778, 0], [3, 0.155556, 0]], [-0.214801, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.2102, [3, -0.133333, -0.00460069], [3, 0.222222, 0.00766782]], [-4.19617e-05, [3, -0.222222, 0], [3, 0.177778, 0]], [-4.19617e-05, [3, -0.177778, 0], [3, 0.222222, 0]], [-4.19617e-05, [3, -0.222222, 0], [3, 0.177778, 0]], [-4.19617e-05, [3, -0.177778, 0], [3, 0.244444, 0]], [-4.19617e-05, [3, -0.244444, 0], [3, 0.2, 0]], [-4.19617e-05, [3, -0.2, 0], [3, 0.266667, 0]], [-4.19617e-05, [3, -0.266667, 0], [3, 0.288889, 0]], [-4.19617e-05, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-0.113689, [3, -0.244444, 0], [3, 0.155556, 0]], [-0.340721, [3, -0.155556, 0], [3, 0.155556, 0]], [-0.244079, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.340721, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.00170743, [3, -0.133333, 0], [3, 0.155556, 0]], [-0.340721, [3, -0.155556, 0], [3, 0.177778, 0]], [-0.00170743, [3, -0.177778, 0], [3, 0.155556, 0]], [-0.340721, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.00170743, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.0139794, [3, -0.222222, 0.0045452], [3, 0.177778, -0.00363616]], [-0.0262515, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.0139794, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.0262515, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.0139794, [3, -0.244444, 0], [3, 0.2, 0]], [-0.0262515, [3, -0.2, 0], [3, 0.266667, 0]], [-0.0139794, [3, -0.266667, -0.00539969], [3, 0.288889, 0.00584967]], [0.00749657, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.0168944, [3, -0.244444, 0], [3, 0.155556, 0]], [-0.0398637, [3, -0.155556, 0.03068], [3, 0.155556, -0.03068]], [-0.167186, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.0398637, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.265362, [3, -0.133333, 0], [3, 0.155556, 0]], [-0.0398637, [3, -0.155556, 0], [3, 0.177778, 0]], [-0.265362, [3, -0.177778, 0], [3, 0.155556, 0]], [-0.0398637, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.265362, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.259225, [3, -0.222222, -0.00198838], [3, 0.177778, 0.00159071]], [-0.254624, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.259225, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.254624, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.259225, [3, -0.244444, 0], [3, 0.2, 0]], [-0.254624, [3, -0.2, 0], [3, 0.266667, 0]], [-0.259225, [3, -0.266667, 0], [3, 0.288889, 0]], [0.0092244, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-0.340507, [3, -0.244444, 0], [3, 0.155556, 0]], [-1.54776, [3, -0.155556, 0], [3, 0.155556, 0]], [-1.54163, [3, -0.155556, 0], [3, 0.133333, 0]], [-1.54776, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.54009, [3, -0.133333, 0], [3, 0.155556, 0]], [-1.54776, [3, -0.155556, 0], [3, 0.177778, 0]], [-1.54009, [3, -0.177778, 0], [3, 0.155556, 0]], [-1.54776, [3, -0.155556, 0], [3, 0.133333, 0]], [-1.54009, [3, -0.133333, -0.00766897], [3, 0.222222, 0.0127816]], [-0.814512, [3, -0.222222, -0.164195], [3, 0.177778, 0.131356]], [-0.653443, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.814512, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.653443, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.814512, [3, -0.244444, 0], [3, 0.2, 0]], [-0.653443, [3, -0.2, 0], [3, 0.266667, 0]], [-0.814512, [3, -0.266667, 0], [3, 0.288889, 0]], [-0.558334, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-0.767043, [3, -0.244444, 0], [3, 0.155556, 0]], [-1.14441, [3, -0.155556, 0.118629], [3, 0.155556, -0.118629]], [-1.47882, [3, -0.155556, 0], [3, 0.133333, 0]], [-1.14441, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.33155, [3, -0.133333, 0], [3, 0.155556, 0]], [-1.14441, [3, -0.155556, 0], [3, 0.177778, 0]], [-1.33155, [3, -0.177778, 0], [3, 0.155556, 0]], [-1.14441, [3, -0.155556, 0], [3, 0.133333, 0]], [-1.33155, [3, -0.133333, 0.0655786], [3, 0.222222, -0.109298]], [-1.66903, [3, -0.222222, 0], [3, 0.177778, 0]], [-1.42666, [3, -0.177778, 0], [3, 0.222222, 0]], [-1.66903, [3, -0.222222, 0], [3, 0.177778, 0]], [-1.42666, [3, -0.177778, 0], [3, 0.244444, 0]], [-1.66903, [3, -0.244444, 0], [3, 0.2, 0]], [-1.42666, [3, -0.2, 0], [3, 0.266667, 0]], [-1.66903, [3, -0.266667, 0.0697051], [3, 0.288889, -0.0755139]], [-1.86232, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.916387, [3, -0.244444, 0], [3, 0.155556, 0]], [0.41748, [3, -0.155556, 0.000364006], [3, 0.155556, -0.000364006]], [0.417116, [3, -0.155556, 0], [3, 0.133333, 0]], [0.41748, [3, -0.133333, 0], [3, 0.133333, 0]], [0.41748, [3, -0.133333, 0], [3, 0.155556, 0]], [0.41748, [3, -0.155556, 0], [3, 0.177778, 0]], [0.41748, [3, -0.177778, 0], [3, 0.155556, 0]], [0.41748, [3, -0.155556, 0], [3, 0.133333, 0]], [0.41748, [3, -0.133333, 0], [3, 0.222222, 0]], [0.421116, [3, -0.222222, 0], [3, 0.177778, 0]], [0.421116, [3, -0.177778, 0], [3, 0.222222, 0]], [0.421116, [3, -0.222222, 0], [3, 0.177778, 0]], [0.421116, [3, -0.177778, 0], [3, 0.244444, 0]], [0.421116, [3, -0.244444, 0], [3, 0.2, 0]], [0.421116, [3, -0.2, 0], [3, 0.266667, 0]], [0.421116, [3, -0.266667, 0], [3, 0.288889, 0]], [1, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.0749446, [3, -0.244444, 0], [3, 0.155556, 0]], [-0.242594, [3, -0.155556, 0], [3, 0.155556, 0]], [0.438502, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.242594, [3, -0.133333, 0], [3, 0.133333, 0]], [0.271296, [3, -0.133333, 0], [3, 0.155556, 0]], [-0.242594, [3, -0.155556, 0], [3, 0.177778, 0]], [0.271296, [3, -0.177778, 0], [3, 0.155556, 0]], [-0.242594, [3, -0.155556, 0], [3, 0.133333, 0]], [0.271296, [3, -0.133333, -0.00920486], [3, 0.222222, 0.0153414]], [0.286637, [3, -0.222222, -0.0059658], [3, 0.177778, 0.00477264]], [0.303511, [3, -0.177778, 0], [3, 0.222222, 0]], [0.286637, [3, -0.222222, 0], [3, 0.177778, 0]], [0.303511, [3, -0.177778, 0], [3, 0.244444, 0]], [0.286637, [3, -0.244444, 0], [3, 0.2, 0]], [0.303511, [3, -0.2, 0], [3, 0.266667, 0]], [0.286637, [3, -0.266667, 0], [3, 0.288889, 0]], [0.378677, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-0.0477461, [3, -0.244444, 0], [3, 0.155556, 0]], [0.17315, [3, -0.155556, -0.0122721], [3, 0.155556, 0.0122721]], [0.185422, [3, -0.155556, 0], [3, 0.133333, 0]], [0.17315, [3, -0.133333, 0], [3, 0.133333, 0]], [0.24218, [3, -0.133333, 0], [3, 0.155556, 0]], [0.17315, [3, -0.155556, 0], [3, 0.177778, 0]], [0.24218, [3, -0.177778, 0], [3, 0.155556, 0]], [0.17315, [3, -0.155556, 0], [3, 0.133333, 0]], [0.24218, [3, -0.133333, 0], [3, 0.222222, 0]], [0.22684, [3, -0.222222, 0.00568137], [3, 0.177778, -0.0045451]], [0.211501, [3, -0.177778, 0], [3, 0.222222, 0]], [0.22684, [3, -0.222222, 0], [3, 0.177778, 0]], [0.211501, [3, -0.177778, 0], [3, 0.244444, 0]], [0.22684, [3, -0.244444, 0], [3, 0.2, 0]], [0.211501, [3, -0.2, 0], [3, 0.266667, 0]], [0.22684, [3, -0.266667, 0], [3, 0.288889, 0]], [-0.0324061, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.0275685, [3, -0.244444, 0], [3, 0.155556, 0]], [-0.523138, [3, -0.155556, 0], [3, 0.155556, 0]], [-0.401951, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.523138, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.357466, [3, -0.133333, 0], [3, 0.155556, 0]], [-0.523138, [3, -0.155556, 0], [3, 0.177778, 0]], [-0.357466, [3, -0.177778, 0], [3, 0.155556, 0]], [-0.523138, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.357466, [3, -0.133333, -0.00644342], [3, 0.222222, 0.010739]], [-0.346727, [3, -0.222222, -0.00369299], [3, 0.177778, 0.00295439]], [-0.337524, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.346727, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.337524, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.346727, [3, -0.244444, 0], [3, 0.2, 0]], [-0.337524, [3, -0.2, 0], [3, 0.266667, 0]], [-0.346727, [3, -0.266667, 0.00515417], [3, 0.288889, -0.00558368]], [-0.369738, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.0886521, [3, -0.244444, 0], [3, 0.155556, 0]], [0.775884, [3, -0.155556, 0], [3, 0.155556, 0]], [0.133138, [3, -0.155556, 0], [3, 0.133333, 0]], [0.775884, [3, -0.133333, 0], [3, 0.133333, 0]], [0.00581614, [3, -0.133333, 0], [3, 0.155556, 0]], [0.775884, [3, -0.155556, 0], [3, 0.177778, 0]], [0.00581614, [3, -0.177778, 0], [3, 0.155556, 0]], [0.775884, [3, -0.155556, 0], [3, 0.133333, 0]], [0.00581614, [3, -0.133333, 0], [3, 0.222222, 0]], [0.0226902, [3, -0.222222, -0.00596557], [3, 0.177778, 0.00477245]], [0.0380302, [3, -0.177778, 0], [3, 0.222222, 0]], [0.0226902, [3, -0.222222, 0], [3, 0.177778, 0]], [0.0380302, [3, -0.177778, 0], [3, 0.244444, 0]], [0.0226902, [3, -0.244444, 0], [3, 0.2, 0]], [0.0380302, [3, -0.2, 0], [3, 0.266667, 0]], [0.0226902, [3, -0.266667, 0.00417249], [3, 0.288889, -0.0045202]], [0.0119521, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[1.58765, [3, -0.244444, 0], [3, 0.155556, 0]], [1.45266, [3, -0.155556, 0], [3, 0.155556, 0]], [1.98343, [3, -0.155556, 0], [3, 0.133333, 0]], [1.45266, [3, -0.133333, 0], [3, 0.133333, 0]], [2.0187, [3, -0.133333, 0], [3, 0.155556, 0]], [1.45266, [3, -0.155556, 0], [3, 0.177778, 0]], [2.0187, [3, -0.177778, 0], [3, 0.155556, 0]], [1.45266, [3, -0.155556, 0], [3, 0.133333, 0]], [2.0187, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.72409, [3, -0.222222, 0], [3, 0.177778, 0]], [1.62907, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.72409, [3, -0.222222, 0], [3, 0.177778, 0]], [1.62907, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.72409, [3, -0.244444, 0], [3, 0.2, 0]], [1.62907, [3, -0.2, 0], [3, 0.266667, 0]], [-0.72409, [3, -0.266667, 0], [3, 0.288889, 0]], [0.708667, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.303691, [3, -0.244444, 0], [3, 0.155556, 0]], [0, [3, -0.155556, 0], [3, 0.155556, 0]], [0.115008, [3, -0.155556, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.155556, 0]], [0, [3, -0.155556, 0], [3, 0.177778, 0]], [0, [3, -0.177778, 0], [3, 0.155556, 0]], [0, [3, -0.155556, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.222222, 0]], [0.314428, [3, -0.222222, 0], [3, 0.177778, 0]], [0.059784, [3, -0.177778, 0], [3, 0.222222, 0]], [0.314428, [3, -0.222222, 0], [3, 0.177778, 0]], [0.059784, [3, -0.177778, 0], [3, 0.244444, 0]], [0.314428, [3, -0.244444, 0], [3, 0.2, 0]], [0.059784, [3, -0.2, 0], [3, 0.266667, 0]], [0.314428, [3, -0.266667, 0], [3, 0.288889, 0]], [0, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-1.00328, [3, -0.244444, 0], [3, 0.155556, 0]], [-0.694945, [3, -0.155556, -0.0398843], [3, 0.155556, 0.0398843]], [-0.65506, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.694945, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.688808, [3, -0.133333, 0], [3, 0.155556, 0]], [-0.694945, [3, -0.155556, 0], [3, 0.177778, 0]], [-0.688808, [3, -0.177778, 0], [3, 0.155556, 0]], [-0.694945, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.688808, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.690342, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.681137, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.690342, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.681137, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.690342, [3, -0.244444, 0], [3, 0.2, 0]], [-0.681137, [3, -0.2, 0], [3, 0.266667, 0]], [-0.690342, [3, -0.266667, 0], [3, 0.288889, 0]], [-0.690342, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-0.104339, [3, -0.244444, 0], [3, 0.155556, 0]], [0.0398569, [3, -0.155556, 0], [3, 0.155556, 0]], [-0.270011, [3, -0.155556, 0], [3, 0.133333, 0]], [0.0398569, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.451023, [3, -0.133333, 0], [3, 0.155556, 0]], [0.0398569, [3, -0.155556, 0], [3, 0.177778, 0]], [-0.451023, [3, -0.177778, 0], [3, 0.155556, 0]], [0.0398569, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.451023, [3, -0.133333, 0.00460244], [3, 0.222222, -0.00767074]], [-0.458693, [3, -0.222222, 0.00284069], [3, 0.177778, -0.00227255]], [-0.466362, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.458693, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.466362, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.458693, [3, -0.244444, 0], [3, 0.2, 0]], [-0.466362, [3, -0.2, 0], [3, 0.266667, 0]], [-0.458693, [3, -0.266667, -0.00766897], [3, 0.288889, 0.00830805]], [-0.167233, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-0.00456227, [3, -0.244444, 0], [3, 0.155556, 0]], [0.108954, [3, -0.155556, 0], [3, 0.155556, 0]], [0.0859437, [3, -0.155556, 0], [3, 0.133333, 0]], [0.108954, [3, -0.133333, 0], [3, 0.133333, 0]], [0.00464174, [3, -0.133333, 0], [3, 0.155556, 0]], [0.108954, [3, -0.155556, 0], [3, 0.177778, 0]], [0.00464174, [3, -0.177778, 0], [3, 0.155556, 0]], [0.108954, [3, -0.155556, 0], [3, 0.133333, 0]], [0.00464174, [3, -0.133333, 0.000920403], [3, 0.222222, -0.001534]], [0.00310773, [3, -0.222222, 0.000568149], [3, 0.177778, -0.000454519]], [0.00157374, [3, -0.177778, 0], [3, 0.222222, 0]], [0.00310773, [3, -0.222222, 0], [3, 0.177778, 0]], [0.00157374, [3, -0.177778, 0], [3, 0.244444, 0]], [0.00310773, [3, -0.244444, 0], [3, 0.2, 0]], [0.00157374, [3, -0.2, 0], [3, 0.266667, 0]], [0.00310773, [3, -0.266667, -0.001534], [3, 0.288889, 0.00166183]], [0.147304, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.305309, [3, -0.244444, 0], [3, 0.155556, 0]], [1.12907, [3, -0.155556, 0], [3, 0.155556, 0]], [1.1214, [3, -0.155556, 0], [3, 0.133333, 0]], [1.12907, [3, -0.133333, 0], [3, 0.133333, 0]], [1.126, [3, -0.133333, 0], [3, 0.155556, 0]], [1.12907, [3, -0.155556, 0], [3, 0.177778, 0]], [1.126, [3, -0.177778, 0], [3, 0.155556, 0]], [1.12907, [3, -0.155556, 0], [3, 0.133333, 0]], [1.126, [3, -0.133333, 0], [3, 0.222222, 0]], [1.33616, [3, -0.222222, 0], [3, 0.177778, 0]], [1.25485, [3, -0.177778, 0], [3, 0.222222, 0]], [1.33616, [3, -0.222222, 0], [3, 0.177778, 0]], [1.25485, [3, -0.177778, 0], [3, 0.244444, 0]], [1.33616, [3, -0.244444, 0], [3, 0.2, 0]], [1.25485, [3, -0.2, 0], [3, 0.266667, 0]], [1.33616, [3, -0.266667, 0], [3, 0.288889, 0]], [0.553816, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.786901, [3, -0.244444, 0], [3, 0.155556, 0]], [1.52475, [3, -0.155556, 0], [3, 0.155556, 0]], [1.18574, [3, -0.155556, 0], [3, 0.133333, 0]], [1.52475, [3, -0.133333, 0], [3, 0.133333, 0]], [1.51555, [3, -0.133333, 0], [3, 0.155556, 0]], [1.52475, [3, -0.155556, 0], [3, 0.177778, 0]], [1.51555, [3, -0.177778, 0], [3, 0.155556, 0]], [1.52475, [3, -0.155556, 0], [3, 0.133333, 0]], [1.51555, [3, -0.133333, 0.00920482], [3, 0.222222, -0.0153414]], [1.26397, [3, -0.222222, 0], [3, 0.177778, 0]], [1.27931, [3, -0.177778, 0], [3, 0.222222, 0]], [1.26397, [3, -0.222222, 0], [3, 0.177778, 0]], [1.27931, [3, -0.177778, 0], [3, 0.244444, 0]], [1.26397, [3, -0.244444, 0], [3, 0.2, 0]], [1.27931, [3, -0.2, 0], [3, 0.266667, 0]], [1.26397, [3, -0.266667, 0], [3, 0.288889, 0]], [1.7886, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.917842, [3, -0.244444, 0], [3, 0.155556, 0]], [0.411661, [3, -0.155556, 0], [3, 0.155556, 0]], [0.411661, [3, -0.155556, 0], [3, 0.133333, 0]], [0.411661, [3, -0.133333, 0], [3, 0.133333, 0]], [0.411661, [3, -0.133333, 0], [3, 0.155556, 0]], [0.411661, [3, -0.155556, 0], [3, 0.177778, 0]], [0.411661, [3, -0.177778, 0], [3, 0.155556, 0]], [0.411661, [3, -0.155556, 0], [3, 0.133333, 0]], [0.411661, [3, -0.133333, 0], [3, 0.222222, 0]], [0.414571, [3, -0.222222, 0], [3, 0.177778, 0]], [0.414571, [3, -0.177778, 0], [3, 0.222222, 0]], [0.414571, [3, -0.222222, 0], [3, 0.177778, 0]], [0.414571, [3, -0.177778, 0], [3, 0.244444, 0]], [0.414571, [3, -0.244444, 0], [3, 0.2, 0]], [0.414571, [3, -0.2, 0], [3, 0.266667, 0]], [0.414571, [3, -0.266667, 0], [3, 0.288889, 0]], [1, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.039827, [3, -0.244444, 0], [3, 0.155556, 0]], [0.315946, [3, -0.155556, 0], [3, 0.155556, 0]], [0.010681, [3, -0.155556, 0], [3, 0.133333, 0]], [0.315946, [3, -0.133333, 0], [3, 0.133333, 0]], [0.042895, [3, -0.133333, 0], [3, 0.155556, 0]], [0.315946, [3, -0.155556, 0], [3, 0.177778, 0]], [0.042895, [3, -0.177778, 0], [3, 0.155556, 0]], [0.315946, [3, -0.155556, 0], [3, 0.133333, 0]], [0.042895, [3, -0.133333, 0], [3, 0.222222, 0]], [0.047497, [3, -0.222222, -0.00170444], [3, 0.177778, 0.00136355]], [0.0520989, [3, -0.177778, 0], [3, 0.222222, 0]], [0.047497, [3, -0.222222, 0], [3, 0.177778, 0]], [0.0520989, [3, -0.177778, 0], [3, 0.244444, 0]], [0.047497, [3, -0.244444, 0], [3, 0.2, 0]], [0.0520989, [3, -0.2, 0], [3, 0.266667, 0]], [0.047497, [3, -0.266667, 0], [3, 0.288889, 0]], [0.243849, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.0153604, [3, -0.244444, 0], [3, 0.155556, 0]], [0.0260984, [3, -0.155556, 0], [3, 0.155556, 0]], [-0.144176, [3, -0.155556, 0], [3, 0.133333, 0]], [0.0260984, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.0644075, [3, -0.133333, 0], [3, 0.155556, 0]], [0.0260984, [3, -0.155556, 0], [3, 0.177778, 0]], [-0.0644075, [3, -0.177778, 0], [3, 0.155556, 0]], [0.0260984, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.0644075, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.0598056, [3, -0.222222, -0.00170444], [3, 0.177778, 0.00136355]], [-0.0552035, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.0598056, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.0552035, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.0598056, [3, -0.244444, 0], [3, 0.2, 0]], [-0.0552035, [3, -0.2, 0], [3, 0.266667, 0]], [-0.0598056, [3, -0.266667, 0.00460208], [3, 0.288889, -0.00498559]], [-0.200933, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.103898, [3, -0.244444, 0], [3, 0.155556, 0]], [0, [3, -0.155556, 0], [3, 0.155556, 0]], [0.570234, [3, -0.155556, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.133333, 0]], [0.665342, [3, -0.133333, 0], [3, 0.155556, 0]], [0, [3, -0.155556, 0], [3, 0.177778, 0]], [0.665342, [3, -0.177778, 0], [3, 0.155556, 0]], [0, [3, -0.155556, 0], [3, 0.133333, 0]], [0.665342, [3, -0.133333, -0.0128858], [3, 0.222222, 0.0214763]], [0.686818, [3, -0.222222, -0.00795417], [3, 0.177778, 0.00636334]], [0.708295, [3, -0.177778, 0], [3, 0.222222, 0]], [0.686818, [3, -0.222222, 0], [3, 0.177778, 0]], [0.708295, [3, -0.177778, 0], [3, 0.244444, 0]], [0.686818, [3, -0.244444, 0], [3, 0.2, 0]], [0.708295, [3, -0.2, 0], [3, 0.266667, 0]], [0.686818, [3, -0.266667, 0.0214763], [3, 0.288889, -0.023266]], [0.243493, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[1.55859, [3, -0.244444, 0], [3, 0.155556, 0]], [2.01572, [3, -0.155556, 0], [3, 0.155556, 0]], [1.48035, [3, -0.155556, 0], [3, 0.133333, 0]], [2.01572, [3, -0.133333, 0], [3, 0.133333, 0]], [1.43893, [3, -0.133333, 0], [3, 0.155556, 0]], [2.01572, [3, -0.155556, 0], [3, 0.177778, 0]], [1.43893, [3, -0.177778, 0], [3, 0.155556, 0]], [2.01572, [3, -0.155556, 0], [3, 0.133333, 0]], [1.43893, [3, -0.133333, 0.175067], [3, 0.222222, -0.291779]], [0.615176, [3, -0.222222, 0.364751], [3, 0.177778, -0.291801]], [-0.530721, [3, -0.177778, 0], [3, 0.222222, 0]], [0.615176, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.530721, [3, -0.177778, 0], [3, 0.244444, 0]], [0.615176, [3, -0.244444, 0], [3, 0.2, 0]], [-0.530721, [3, -0.2, 0], [3, 0.266667, 0]], [0.615176, [3, -0.266667, 0], [3, 0.288889, 0]], [0.529271, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[-0.296104, [3, -0.244444, 0], [3, 0.155556, 0]], [-0.082878, [3, -0.155556, -0.047554], [3, 0.155556, 0.047554]], [-0.01078, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.082878, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.081344, [3, -0.133333, 0], [3, 0.155556, 0]], [-0.082878, [3, -0.155556, 0], [3, 0.177778, 0]], [-0.081344, [3, -0.177778, 0], [3, 0.155556, 0]], [-0.082878, [3, -0.155556, 0], [3, 0.133333, 0]], [-0.081344, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.460242, [3, -0.222222, 0.110789], [3, 0.177778, -0.088631]], [-0.679603, [3, -0.177778, 0], [3, 0.222222, 0]], [-0.460242, [3, -0.222222, 0], [3, 0.177778, 0]], [-0.679603, [3, -0.177778, 0], [3, 0.244444, 0]], [-0.460242, [3, -0.244444, 0], [3, 0.2, 0]], [-0.679603, [3, -0.2, 0], [3, 0.266667, 0]], [-0.460242, [3, -0.266667, -0.107257], [3, 0.288889, 0.116195]], [-0.00924597, [3, -0.288889, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.666667, 1.13333, 1.6, 2, 2.4, 2.86667, 3.4, 3.86667, 4.26667, 4.93333, 5.46667, 6.13333, 6.66667, 7.4, 8, 8.8, 9.66667])
    keys.append([[0.946436, [3, -0.244444, 0], [3, 0.155556, 0]], [0.76389, [3, -0.155556, 0], [3, 0.155556, 0]], [0.766959, [3, -0.155556, 0], [3, 0.133333, 0]], [0.76389, [3, -0.133333, 0.00102276], [3, 0.133333, -0.00102276]], [0.760822, [3, -0.133333, 0], [3, 0.155556, 0]], [0.76389, [3, -0.155556, 0], [3, 0.177778, 0]], [0.760822, [3, -0.177778, 0], [3, 0.155556, 0]], [0.76389, [3, -0.155556, 0], [3, 0.133333, 0]], [0.760822, [3, -0.133333, 0], [3, 0.222222, 0]], [0.77923, [3, -0.222222, 0], [3, 0.177778, 0]], [0.777696, [3, -0.177778, 0], [3, 0.222222, 0]], [0.77923, [3, -0.222222, 0], [3, 0.177778, 0]], [0.777696, [3, -0.177778, 0], [3, 0.244444, 0]], [0.77923, [3, -0.244444, 0], [3, 0.2, 0]], [0.777696, [3, -0.2, 0], [3, 0.266667, 0]], [0.77923, [3, -0.266667, 0], [3, 0.288889, 0]], [0.77923, [3, -0.288889, 0], [3, 0, 0]]])

    try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    # motion = ALProxy("ALMotion", IP, 9559)
    motion = ALProxy("ALMotion")
    motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
    print err


if __name__ == "__main__":

    robotIP = "127.0.0.1" #"192.168.1.11"

    port = 9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)
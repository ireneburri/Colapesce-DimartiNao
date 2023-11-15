from Nao import NaoProblem
from utils import *
from search import *

import vlc
import subprocess
import time
import math

def play_song(song_name):
    p = vlc.MediaPlayer(song_name)
    try:
        c = p.play()
        time.sleep(60)
    except Exception as e:
        print(e)

def do_moves(moves, ip, port):
    for move in moves:
        print(f"Move: {move}... ", end="", flush=True)
        # We create a command to execute each move one by one
        command = f"python2 ./Animations/{move}.py  {ip} {port}"
        start_move = time.time()
        process = subprocess.run(command.split(), stdout=subprocess.PIPE)
        end_move = time.time()
        # We used this print in testing to adjust the execution time of our moves set
        print("\nExecution time: %.2f seconds." % (end_move-start_move), flush=True)

def main(ip, port):
    
    ########## Definition of moves ########### (Ancora troppo lente)
    moves = {'StandUp': [2.6926817893981934, {'standing': False}, {'standing': True}], #AI
            #'DiagonalLeft': [6.5762670040130615, {}, {'standing': True}], #AI
            '9-Diagonal_left': [4.640681982040405, {}, {'standing': True}], #NOI
            'DoubleMovement': [8.062368392944336, {}, {}], #AI
            #'3-Double_movement': [8.972091674804688, {}, {}], #NOI
            #'MoveBackward': [6.146073579788208, {}, {'standing': True}], #AI
            '8-Move_backward': [5.696051359176636, {}, {'standing': True}], #NOI
            'MoveForward': [4.480520963668823, {}, {'standing': True}], #AI
            #'7-Move_forward': [7.902349233627319, {}, {'standing': True}], #NOI
            'RotationFootLLeg': [9.037095546722412, {'standing': True}, {'standing': True}], #AI
            #'RotationHandgun': [7.611491918563843, {}, {}], #AI
            '1-Rotation_handgun_object': [5.3489086627960205, {}, {}], #NOI
            #'Union_arms': [12.452294826507568, {}, {}], #AI
            '5-Union_arms': [12.324305057525635, {}, {}], #NOI
            'ArmsOpening': [7.709415674209595, {}, {}], #AI
            #'4-Arms_opening': [9.06206750869751, {}, {}], #NOI
            'BlowKisses': [6.305241823196411, {'standing': True}, {'standing': True}], #NO
            'Bow': [5.573694705963135, {'standing': True}, {'standing': True}], #NO
            #'DiagonalRight': [4.8617730140686035, {}, {'standing': True}], #AI
            '10-Diagonal_right': [4.309990406036377, {}, {'standing': True}], #NOI
            'DanceMove': [8.829241037368774, {'standing': True}, {'standing': True}], #NO
            'SprinklerL': [6.331864833831787, {'standing': True}, {'standing': True}], #AI
            #'sprinkler_left': [13.973316431045532, {'standing': True}, {'standing': True}], #NOI
            'SprinklerR': [6.37097430229187, {'standing': True}, {'standing': True}], #AI
            #'sprinkler_right': [12.346796035766602, {'standing': True}, {'standing': True}], #NOI
            #'TheRobot': [8.881108283996582, {'standing': True}, {'standing': True}], #AI
            'the_robot_2': [7.365086317062378, {'standing': True}, {'standing': True}], #NOI
            'ComeOn': [5.594178199768066, {'standing': True}, {'standing': True}], #NO
            'StayingAlive': [8.572153329849243, {'standing': True}, {'standing': True}], #NO
            'Rhythm': [4.64671516418457, {'standing': True}, {'standing': True}], #NO
            'PulpFiction': [8.020118713378906, {'standing': True}, {'standing': True}], #NO
            'RightArm': [13.841203689575195, {}, {}], #AI
            #'2-Right_arm': [15.06546950340271, {}, {}], #NOI 
            'Wave': [5.356391429901123, {}, {}], #NO
            'Glory': [4.884756326675415, {}, {}], #NO
            'Clap': [5.965200901031494, {}, {}], #AI
            #'do_clapping_nosound': [6.812563896179199, {}, {}], #NOI
            'Joy': [6.400599718093872, {}, {}], #NO
            'M_Hello': [6.406063079833984, {'standing': True}, {'standing': True}], #AI
            'birthday_dance_no_sound': [14.775976181030273, {}, {}], #NOI
            'Disco': [23.86342430114746, {}, {}], #NOI
            'hand_on_hip_with_point': [5.939987659454346, {}, {}], #NOI
            'hands_on_hips': [3.282095193862915, {}, {}], #NOI
            'head_nod': [4.943183660507202, {}, {}], #NOI
            #'Headbang': [19.383045434951782, {}, {}], #NOI
            'raise_the_roof': [5.969377756118774, {}, {}], #NOI
            'shake_head': [5.66715145111084, {}, {}], #NOI
            #'sing_with_me': [25.218955516815186, {}, {}], #NOI
            }
    
    """moves nostre= {
            'birthday_dance_no_sound': [14.775976181030273, {}, {}], 
            'Disco': [23.86342430114746, {}, {}], 
            'do_clapping_nosound': [6.812563896179199, {}, {}], 
            'hand_on_hip_with_point': [5.939987659454346, {}, {}], 
            'hands_on_hips': [3.282095193862915, {}, {}], 
            'head_nod': [4.943183660507202, {}, {}], 
            'Headbang': [19.383045434951782, {}, {}], 
            'raise_the_roof': [5.969377756118774, {}, {}], 
            'shake_head': [5.66715145111084, {}, {}], 
            'sing_with_me': [25.218955516815186, {}, {}], 
            'sprinkler_left': [13.973316431045532, {'standing': True}, {'standing': True}], 
            'sprinkler_right': [12.346796035766602, {'standing': True}, {'standing': True}], 
            'the_robot_2': [7.365086317062378, {'standing': True}, {'standing': True}], 
            '1-Rotation_handgun_object': [5.3489086627960205, {}, {}], 
            '2-Right_arm': [15.06546950340271, {}, {}], 
            '3-Double_movement': [8.972091674804688, {}, {}], 
            '4-Arms_opening': [9.06206750869751, {}, {}], 
            '5-Union_arms': [12.324305057525635, {}, {}], 
            '7-Move_forward': [7.902349233627319, {}, {'standing': True}], 
            '8-Move_backward': [5.696051359176636, {}, {'standing': True}], 
            '9-Diagonal_left': [4.640681982040405, {}, {'standing': True}], 
            '10-Diagonal_right': [4.309990406036377, {}, {'standing': True}]}
    """

    Mmoves = {'6-Crouch': [5.711416721343994, {'standing': True}, {'standing': True}], 
              'M_WipeForehead': [6.438775539398193, {'standing': True}, {'standing': True}], #AI 
              #'WipeForehead': [6.847378730773926, {'standing': True}, {'standing': True}], #NOI
              'Hello': [6.775498390197754, {'standing': True}, {'standing': True}], 
              #'M_Stand': [3.652195930480957, {'standing': True}, {'standing': True}], #AI
              '11-Stand': [1.9577922821044922, {'standing': True}, {'standing': True}], #NOI
              'M_StandInit': [2.5300939083099365, {'standing': True}, {'standing': True}], #AI
              #'14-StandInit': [2.794734477996826, {'standing': True}, {'standing': True}], #NOI
              '15-StandZero': [3.192218780517578, {'standing': True}, {'standing': True}], 
              '16-Sit': [6.1734857559204, {'standing': True}, {'standing': False}], 
              'M_SitRelax': [5.870312213897705, {'standing': False}, {'standing': False}] #AI
              #'17-SitRelax': [10.248263120651245, {'standing': False}, {'standing': False}], #NOI
            }
    
    start_pos = 'M_StandInit'
    mandatory_pos = ['11-Stand', '15-StandZero', 'Hello', 'M_WipeForehead', '16-Sit', 'M_SitRelax']
    end_pos = '6-Crouch'
    pos_list = [start_pos, *mandatory_pos, end_pos]
    time_used = 0.0
    for pos in pos_list:
        time_used += Mmoves[pos][0] #duration
        
    avg_time = 0.0
    for pos in moves.values():
        avg_time += pos[0]
    avg_time = avg_time/len(moves)
    print(f"avg time {avg_time}")
    
    solution = []
    print("SOLUTION:")
    starting_time = time.time()
    interval_time = (120 - time_used) / (len(pos_list) - 1)
    print(f"interv time: {interval_time} e time used {time_used}")
    waste = 0.0
    for i in range(1, len(pos_list)):
        initial_pos = pos_list[i - 1]
        final_pos = pos_list[i]
        
        choreography = (initial_pos, ) # Per ora è un singolo oggetto, poi da cambiare
        
        initial_standing = Mmoves[pos_list[i]][1]['standing']
        final_standing = Mmoves[pos_list[i]][2]['standing']
        print(initial_standing, final_standing)
        
        cur_state = (
            ('choreography', choreography),
            ('standing', initial_standing),
            ('remaining_time', interval_time + waste),
            ('moves_done', 0),
            ('entropy', 0.0))
        cur_goal_state = (
            ('standing', final_standing),
            ('remaining_time', 0),
            ('moves_done', 3), #dovrebbe essere 5!!!!
            ('entropy', 0.0)) # entropia da calcolare, deve essere variabile
        
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves, tuple(solution), avg_time)
        cur_solutionT = astar_search(cur_problem)
        
        print(cur_solutionT)
        if cur_solutionT is None:
            raise RuntimeError(f'In step {i} i could not find a solution!')
        cur_solution = dict((key, value) for key, value in cur_solutionT.state)

        print('Step ', i, ':')
        for j in cur_solution['choreography']:
            print(' ' + j)
        
        # save the remaining time
        waste = cur_solution['remaining_time']
        solution.append(cur_solution['choreography'])
        
    ending_time = time.time()
    solution.append(end_pos)
    
    # Execution of the dance
    print('\nExecuting dance:')
    
    # Soundtrack starting
    play_song("music.mp3")
    start_dance = time.time()
    do_moves(solution, ip, port)
    end_dance = time.time()
    
    print('\nRESULTS:')
    print('Planning time: %.2f s.' % (ending_time - starting_time))
    print('Estimated duration: %.2f s.' % (120 - waste))
    print('Real duration: %.2f s.' % (end_dance - start_dance))
    print('Entropy: ', cur_solution['entropy'])



if __name__ == "__main__":

    robot_ip = "127.0.0.1"
    port = 9559  # Standard NAO port
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]
    elif len(sys.argv) == 2:
        robot_ip = sys.argv[1]

    main(robot_ip, port)
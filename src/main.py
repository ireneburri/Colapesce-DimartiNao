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
    moves = {'birthday_dance_no_sound': [14.775976181030273, True, True], 'Disco': [23.86342430114746, True, True], 
     'do_clapping_nosound': [6.812563896179199, True, True], 'hand_on_hip_with_point': [5.939987659454346, True, True], 
     'hands_on_hips': [3.282095193862915, True, True], 'head_nod': [4.943183660507202, True, True], 
     'Headbang': [19.383045434951782, True, True], 'raise_the_roof': [5.969377756118774, True, True], 
     'shake_head': [5.66715145111084, True, True], 'sing_with_me': [25.218955516815186, True, True], 
     'sprinkler_left': [13.973316431045532, True, True], 'sprinkler_right': [12.346796035766602, True, True], 
     'the_robot_2': [7.365086317062378, True, True], '1-Rotation_handgun_object': [5.3489086627960205, True, True], 
     '2-Right_arm': [15.06546950340271, True, True], '3-Double_movement': [8.972091674804688, True, True], 
     '4-Arms_opening': [9.06206750869751, True, True], '5-Union_arms': [12.324305057525635, True, True], 
     '6-Crouch': [5.711416721343994, True, True], '7-Move_forward': [7.902349233627319, True, True], 
     '8-Move_backward': [5.696051359176636, True, True], '9-Diagonal_left': [4.640681982040405, True, True], 
     '10-Diagonal_right': [4.309990406036377, True, True], 'WipeForehead': [6.847378730773926, True, True], 
     'Hello': [6.775498390197754, True, True], '11-Stand': [1.9577922821044922, True, True], 
     '14-StandInit': [2.794734477996826, True, True], '15-StandZero': [3.192218780517578, True, True], 
     '16-Sit': [6.1734857559204, True, False], '17-SitRelax': [10.248263120651245, False, False]}
    
    start_pos = '14-StandInit'
    mandatory_pos = ['16-Sit', '17-SitRelax', '11-Stand', '15-StandZero', 'Hello', 'WipeForehead']
    end_pos = '6-Crouch'
    pos_list = [start_pos, *mandatory_pos, end_pos]
    print(pos_list)
    time_used = 0.0
    for pos in pos_list:
        time_used += moves[pos][0] #duration
        
    
    ######### Possible definition of average time #########
    
    
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
        if initial_pos == '17-SitRelax':
        # Is the only position that requires the sitting prerequisite
            initial_standing = False
        else:
            initial_standing = True
        
        if final_pos == '16-Sit' or final_pos == '17-SitRelax':
            final_standing = False
        else:
            final_standing = True
        
        cur_state = (
            ('choreography', choreography),
            ('standing', initial_standing),
            ('remaining_time', interval_time + waste),
            ('moves_done', 0),
            ('entropy', 0.0))
        cur_goal_state = (
            ('standing', final_standing),
            ('remaining_time', 0),
            ('moves_done', 1), #dovrebbe essere 5!!!!
            ('entropy', 2.0)) # entropia da calcolare, deve essere variabile
        
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves, tuple(solution))
        cur_solution = astar_search(cur_problem)
        if cur_solution is None:
            raise RuntimeError(f'In step {i} i could not find a solution!')
        
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
from Nao import NaoProblem
from utils import *
from search import *

def main(ip, port):
    
    ########## Definition of moves ###########
    moves = {[], []}
    
    start_pos = {'14-StandInit': [0.0, True, True]}
    mandatory_pos = ['16-Sit', '17-SitRelax', '11-Stand', '15-StandZero']#, #'Hello', 'WipeForehead']
    end_pos = {'6-Crouch': [0.0, True, True]}
    pos_list = [start_pos, *mandatory_pos, end_pos]
    
    time_used = 0.0
    for pos in pos_list:
        time_used += moves[pos][] # duration
        
    ######### Possible definition of average time #########
    
    
    solution = []
    print("SOLUTION:")
    startin_time = time.time()
    interval_time = (120 - time_used) / (len(pos_list) - 1)
    waste = 0.0
    for i in range(1, len(pos_list)):
        initial_pos = pos_list[i - 1]
        final_pos = pos_list[i]
        
        choreography = [initial_pos] # Per ora è un singolo oggetto, poi da cambiare
        if initial_pos == '17-SitRelax':
        # Is the only position that requires the sitting prerequisite
            initial_standing = False
        else:
            initial_standing = True
        
        if final_pos == '16-Sit' or final_pos == '17-SitRelax':
            final_standing = False
        else:
            final_standing = True
        
        cur_state = {
            'choreography': choreography,
            'standing': initial_standing,
            'remaining_time': interval_time + waste,
            'moves_done': 0,
            'entropy': 0.0}
        cur_goal_state = {
            'standing': final_standing,
            'remaining_time': 0,
            'moves_done': 5,
            'entropy': 2.0} # entropia da calcolare, deve essere variabile
        
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves)
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
    ##### play_song('song.mp3') #####
    start_dance = time.time()
    do_moves(solution, ip, port)
    end_dance = time.time()
    
    print('\nRESULTS:')
    print('Planning time: %.2f s.' % (ending_time - startin_time))
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
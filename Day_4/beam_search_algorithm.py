# def beam_search(start_state, beam_width, max_steps):
#     # Initialize the beam with the start state
#     beam = [(start_state, 0)]
    
#     for _ in range(max_steps):
#         # Generate all possible next states from the current beam
#         next_beam = []
#         for state, score in beam:
#             next_states = generate_next_states(state)
#             for next_state in next_states:
#                 next_beam.append((next_state, score + evaluate(next_state)))
        
#         # Sort the next beam based on the scores
#         next_beam.sort(key=lambda x: x[1], reverse=True)
        
#         # Keep only the top beam_width states
#         beam = next_beam[:beam_width]
    
#     # Return the best state from the final beam
#     best_state = beam[0][0]
#     return best_state



# def evaluate(state):
#     # Evaluate the state
#     return sum(state)


# def generate_next_states(state):
#     # Generate all possible next states from the current state
#     next_states = []
#     for i in range(len(state)):
#         for j in range(i+1, len(state)):
#             next_state = state.copy()
#             next_state[i], next_state[j] = next_state[j], next_state[i]
#             next_states.append(next_state)
#     return next_states

# def initialize_start_state():
#     # Initialize the start state
#     return [1,2,3,4,5,6,7,8]

# # Example usage
# start_state = initialize_start_state()
# beam_width = 3
# max_steps = 5
# best_state = beam_search(start_state, beam_width, max_steps)
# print("Best state:", best_state)




# beam search

from numpy import array

# main munction 
# beta here is width of beam and distances can be considered as weights
def beam_search(distances, beta):
    # initializing some sort of record for the same
    paths_so_far = [[list()]]

    # iterating over the distances
    for distance in distances:
        # initializing a new list
        new_paths = list()
        # iterating over the paths
        for path in paths_so_far:
            # iterating over the distance
            for i in range(len(distance)):
                # appending the path with the distance
                new_paths.append([*path, i])
        # sorting the new paths
        new_paths.sort(key=lambda path: sum(distance[i] for i in path))
        # updating the paths so far
        paths_so_far = new_paths[:beta]
    # returning the paths so far
    return paths_so_far


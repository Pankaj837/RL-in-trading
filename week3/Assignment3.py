# Environment 1 - Slippery Walk

swf_mdp = {

    0 : {
        "Right" : [(1, 0, 0, True)],
        "Left" : [(1, 0, 0, True)],
    },

    1 : {
        "Right" : [
            (1/2, 2, 0, False),
            (1/3, 1, 0, False),
            (1/6, 0, 0, True),
        ],
        "Left" : [
            (1/2, 0, 0, True),
            (1/3, 1, 0, False),
            (1/6, 2, 0, False),
        ]
    }, 

    2: {
    "Right": [(1/2, 3, 0, False), (1/3, 2, 0, False), (1/6, 1, 0, False)],
    "Left":  [(1/2, 1, 0, False), (1/3, 2, 0, False), (1/6, 3, 0, False)],
    },
  
    3: {
    "Right": [(1/2, 4, 0, False), (1/3, 3, 0, False), (1/6, 2, 0, False)],
    "Left":  [(1/2, 2, 0, False), (1/3, 3, 0, False), (1/6, 4, 0, False)],
    },
  
    4: {
    "Right": [(1/2, 5, 0, False), (1/3, 4, 0, False), (1/6, 3, 0, False)],
    "Left":  [(1/2, 3, 0, False), (1/3, 4, 0, False), (1/6, 5, 0, False)],
    },
  
    5: {
    "Right": [(1/2, 6, 1, True), (1/3, 5, 0, False), (1/6, 4, 0, False)],
    "Left":  [(1/2, 4, 0, False), (1/3, 5, 0, False), (1/6, 6, 1, True)],
    },
  
    6: {
    "Right": [(1, 6, 0, True)],
    "Left":  [(1, 6, 0, True)],
    }
   
}


# Environment 2 - Frozen Lake Environment

import gym

# create gym environment and extract MDP
env = gym.make("FrozenLake-v1")
P = env.env.P

# initialize MDP dictionary
fl_mdp = {}

actions = ["Left", "Down", "Right", "Up"]

for state in range(16):
    transitions = {}

    for a_idx, action in enumerate(actions):
        transitions[action] = []

        for prob, next_state, reward, done in P[state][a_idx]:
            transitions[action].append((prob, next_state, reward, done))

    fl_mdp[state] = transitions


from gym.envs.registration import register

register(
    id='arithmaticrobo-v0',
    entry_point='gym_arithmaticrobo.envs:ArithmaticRobo',
)
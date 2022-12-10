from isaacgym import gymapi  # We have to put this line here!
from policydissect.legged_gym.envs import *  # We have to put this line here!
from policydissect.legged_gym.utils import get_args
from policydissect.utils.isaacgym_utils import play_cassie

if __name__ == '__main__':
    # This is a policy with Elu which is not a symmetric activation function.
    # Use tanh will definitely improve the performance
    """
    Keymap:
    - KEY_W:Forward
    - KEY_A:Left
    - KEY_S:Stop
    - KEY_C:Crouch
    - KEY_X:Tiptoe
    - KEY_Q:Jump
    - KEY_D:Right
    - KEY_SPACE:Back Flip
    - KEY_R:Reset
    """
    forward_cassie = {
        # 0
        "Tiptoe": {
            0: [(261, 10), (212, 5), (395, 5), (260, 10), (30, -1)]
        },
        "Crouch": {
            0: [(261, -12), (260, 14)]
        },
        # 0,3
        "Back Flip": {
            0: [(47, 50), (479, 40), (261, 45)]
        },
        # 2
        "Left": {
            0: [(30, 7)]
        },
        "Right": {
            0: [(30, -7.5), (452, 10), (261, -4)]
        },
        # 1
        "Forward": {
            0: [(452, 25), (30, -4.1), (227, 8)]
        },
        # 21/15 hip flexion
        "Jump": {
            0: [(212, 25), (395, 25), (261, 10), (260, 5), (30, -15), (227, 12)]
        },
        "Stop": {}
    }
    args = get_args(
        [{
            "name": "--parkour",
            "action": "store_true",
            "default": False,
            "help": "Build a parkour environment"
        }]
    )
    args.num_envs = 1
    args.task = "cassie"
    activation = "elu"
    play_cassie(args, activation_func=activation, map=forward_cassie, model_name="forward_cassie", parkour=args.parkour)

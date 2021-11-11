import os
import numpy as np
import pybullet_multigoal_gym as pmg
import matplotlib.pyplot as plt

camera_setup = [
    {
        'cameraEyePosition': [-1.0, 0.25, 0.6],
        'cameraTargetPosition': [-0.6, 0.05, 0.2],
        'cameraUpVector': [0, 0, 1],
        'render_width': 128,
        'render_height': 128
    },
    {
        'cameraEyePosition': [-1.0, -0.25, 0.6],
        'cameraTargetPosition': [-0.6, -0.05, 0.2],
        'cameraUpVector': [0, 0, 1],
        'render_width': 128,
        'render_height': 128
    }
]

env = pmg.make_env(
    # task args
    task='block_rearrange',
    gripper='parallel_jaw',
    grip_informed_goal=False,
    num_block=4,  # only meaningful for multi-block tasks
    render=True,
    binary_reward=True,
    max_episode_steps=5,
    # image observation args
    image_observation=True,
    depth_image=False,
    goal_image=True,
    visualize_target=True,
    camera_setup=camera_setup,
    observation_cam_id=1,
    goal_cam_id=1,
    # curriculum args
    use_curriculum=True,
    num_goals_to_generate=20,
    task_decomposition=False)

obs = env.reset()
env.activate_curriculum_update()
time_done = False
f, axarr = plt.subplots(1, 2)
# env.set_sub_goal(0)
# print(env.desired_goal)
# t = 0
while True:
    # action = env.action_space.sample()
    # obs, reward, time_done, info = env.step(action)
    axarr[0].imshow(obs['desired_goal_img'])
    axarr[1].imshow(obs['achieved_goal_img'])
    plt.pause(0.00001)
    # t += 1
    # if t == 3:
    #     env.set_sub_goal(1)
    # if t == 6:
    #     env.set_sub_goal(2)
    # if t == 9:
    #     env.set_sub_goal(3)
    # if t == 12:
    #     env.set_sub_goal(4)
    obs = env.reset()

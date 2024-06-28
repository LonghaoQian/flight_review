import numpy as np
from scipy.spatial.transform import Rotation

def QuaT2EulerAngles(quat_w, quat_x, quat_y, quat_z):
    roll = list()
    pitch = list()
    yaw = list()

    for i in range(quat_w.size):
        r = Rotation.from_quat([quat_x[i], quat_y[i], quat_z[i], quat_w[i]])
        euler = r.as_euler('xyz', degrees=True)
        roll.append(euler[0])
        pitch.append(euler[1])
        yaw.append(euler[2])
    return roll, pitch, yaw

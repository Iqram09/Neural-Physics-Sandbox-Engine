"""
Scenario generator for MuJoCo-based data generation.
"""
import mujoco
import numpy as np
import h5py

def generate_scenario(model_path, hdf5_out, seed=42, steps=1000):
    np.random.seed(seed)
    # Load MuJoCo model
    m = mujoco.MjModel.from_xml_path(model_path)
    d = mujoco.MjData(m)

    positions = []
    for step in range(steps):
        mujoco.mj_step(m, d)
        positions.append(np.copy(d.qpos))

    positions = np.stack(positions)
    with h5py.File(hdf5_out, "w") as f:
        f.create_dataset("positions", data=positions)

    print(f"Saved {steps} steps to {hdf5_out}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python mujoco_gen.py <model.xml> <output.h5>")
        exit(1)
    model_path = sys.argv[1]
    hdf5_out = sys.argv[2]
    generate_scenario(model_path, hdf5_out)

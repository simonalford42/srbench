from pysr import PySRRegressor
# from multiprocessing import cpu_count
import os


def complexity(est):
    return est.get_best()["complexity"]


def model(est):
    return str(est.sympy())


try:
    num_cpus = int(os.environ.get('SLURM_CPUS_ON_NODE')) * int(os.environ.get('SLURM_JOB_NUM_NODES'))
except TypeError:
    num_cpus = 10

est = PySRRegressor(
    niterations=1_000_000_000,
    populations=3*num_cpus,
    timeout_in_seconds=10*60,
    maxsize=40,
    maxdepth=20,
    binary_operators=["+", "-", "*", "/"],
    unary_operators=["sin", "cos", "exp", "log", "sqrt"],
    # procs=num_cpus,
    # parallelism="multiprocessing",
    parallelism="serial",
    deterministic=True,
    procs=1,
    verbosity=5,
    batching=True,
    batch_size=50,
    # turbo=True,
    # constraints={
    #     **dict(
    #         sin=9,
    #         exp=9,
    #         log=9,
    #         sqrt=9,
    #     ),
    #     **{"/": (-1, 9)}
    # },
    # nested_constraints=dict(
    #     sin=dict(
    #         sin=0,
    #         exp=1,
    #         log=1,
    #         sqrt=1,
    #     ),
    #     exp=dict(
    #         exp=0,
    #         log=0,
    #     ),
    #     log=dict(
    #         exp=0,
    #         log=0,
    #     ),
    #     sqrt=dict(
    #         sqrt=0,
    #     )
    # ),
)

# See https://astroautomata.com/PySR/tuning/ for tuning advice
hyper_params = [{}]

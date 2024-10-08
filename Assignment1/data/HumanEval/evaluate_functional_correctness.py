import fire
import sys

import argparse
from baseline import HUMAN_EVAL
from evaluation import evaluate_functional_correctness


def entry_point(
    sample_file: str,
    k: str = "1,10,100",
    n_workers: int = 4,
    timeout: float = 3.0,
    problem_file: str = HUMAN_EVAL,
):
    """
    Evaluates the functional correctness of generated samples, and writes
    results to f"{sample_file}_results.jsonl.gz"
    """
    k = list(map(int, k.split(",")))
    results = evaluate_functional_correctness(sample_file, k, n_workers, timeout, problem_file)
    print(results)


# def main():
#     fire.Fire(entry_point)
#
#
# sys.exit(main())
if __name__ == '__main__':
    '''
    On Windows the subprocesses will import (i.e. execute) the main module at start. You need to insert an if __name__ == '__main__': guard in the main module to avoid creating subprocesses recursively.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem_file", type=str, required=True, help="problem prompt")
    parser.add_argument("--sample_file", type=str, required=True, help="prediction file saving task_id and completion")
    args = parser.parse_args()
    entry_point(sample_file=args.sample_file,
                problem_file=args.problem_file)


'''
python evaluate_functional_correctness.py --sample_file example_samples.jsonl --problem_file example_problem.jsonl
'''
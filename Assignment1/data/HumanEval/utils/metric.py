from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from execution import check_correctness
from baseline import read_problems


problems = read_problems()
prompts = []
for p in problems:
    prompt = problems[p]["prompt"]
    prompts.append(prompt)

problem = prompts[0]


results = []

codes = []
with ProcessPoolExecutor() as p:
    try:
        future_to_completion = {
            p.submit(check_correctness, problem, code, 3.): (code, completion)
            for code, completion in zip(codes, completions)
        }
        for future in as_completed(future_to_completion):
            result = future.result()
            code, completion = future_to_completion[future]
            results.append((result["passed"], result["result"], code, completion))
    except Exception as e:
        print("Error: ", e)
        raise e
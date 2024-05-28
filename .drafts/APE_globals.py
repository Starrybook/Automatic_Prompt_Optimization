""" APE_utils.py """
TARGET_MODEL = "gpt-3.5-turbo"
OPTIMIZER_MODEL = "gpt-3.5-turbo"
CURRENT_DATASET = "movie"
CURRENT_RESPONSES_FILE_PATH = ""    # update during the process

""" template.py """
FEEDBACK_REASONS_NUM = 3
FEEDBACK_IMPROVED_PROMPTS_NUM = 2
ANSWER_FORMAT_SPEC = "Your answer should contain both the final answer and an explanation.\nWrap your final answer with <A> and </A>.\nWrap your explanation with <E> and </E>.\nPlease be concise and to the point.\nYour answer:\n"
MOVIE_INIT_INST = "Given the user's preference and unpreference, identify whether the user will like the target movie by answering \"Yes.\" or \"No.\"."
GSM8K_INIT_INST = "Please solve the following mathematical problem and provide the final numerical answer."

""" data_process.py """

"""
Dataset 1: Movie
Stored in .json file, like this:
[
    {
        "instruction": "Given the user's preference and unpreference, ......",
        "input": "User Preference: \"Clockwork Orange, A (1971)\"\nUser Unpreference: ......",
        "output": "No."
    },
    ...... 
]
"""
MOVIE_100_SAMPLES_PATH = "./data/movie/eval.json"
MOVIE_1000_SAMPLES_PATH = "./data/movie/train.json"
MOVIE_RESPONSES_DIR = "./data/response/movie"


"""
Dataset 2: Gsm8k
Stored in .json file, like this:
[
    {
        "question": "A robe takes 2 bolts of blue fiber and half that much white fiber.  How many bolts in total does it take?", 
        "answer": "It takes 2/2=<<2/2=1>>1 bolt of white fiber\nSo the total amount of fabric is 2+1=<<2+1=3>>3 bolts of fabric\n#### 3"
    }, 
    ......
]

"""
GSM8K_100_SAMPLES_PATH = "./data/gsm8k/eval.json"
GSM8K_1374_SAMPLES_PATH = "./data/gsm8k/test.json"
GSM8K_RESPONSES_DIR = "./data/response/gsm8k"
import json
import math
import os.path
import random
from enum import Enum
from typing import Optional, List

from utils import load_module

TEMPLATE_FILE_PATH = 'task_template.py'
RESULTS = {"grade": None}

OUTPUT_TASK_FILE = "task.py"
INPUT_STORAGE = "in_storage"


class LevelEnum(str, Enum):
    JUNIOR = "junior"
    MIDDLE = "middle"
    SENIOR = "senior"


class LanguageEnum(str, Enum):
    PYTHON = "python"
    JAVA = "java"
    CPP = "cpp"
    R = "r"


class OSEnum(str, Enum):
    UNIX = "unix"
    WINDOWS = "windows"


class DegreeEnum(str, Enum):
    YES = "yes"
    NO = "no"


class QuestionEnum(str, Enum):
    ASK_LEVEL = "ask_level"
    ASK_LANGUAGE = "ask_language"
    ASK_OS = "ask_os"
    ASK_GRADE = "ask_grade"
    ASK_DEGREE = "ask_degree"
    HIRE = "hire"
    DECLINE = "decline"


class Candidate:
    def __init__(self,
                 level=None,
                 lang=None,
                 os=None,
                 degree=None):
        self.level: Optional[LevelEnum] = level
        self.lang: Optional[LanguageEnum] = lang
        self.degree: Optional[DegreeEnum] = degree
        self.os: Optional[OSEnum] = os


def get_text_task_1():
    return ("Необходимо реализовать функцию select по фотографии ниже.\n"
            "Часть кода уже написана, для большего понимания")


def get_photo_file_task_1() -> str:
    return f"{INPUT_STORAGE}/task_1.png"


def get_text_task_2():
    return "Необходимо реализовать функцию, которая будет вычислять энтропию Шеннона"


def get_photo_file_task_2() -> str:
    return f"{INPUT_STORAGE}/task_2.png"


def save_results():
    with open("grade.json", "w") as f:
        json.dump(RESULTS, f)


def test_task():
    grade = 5

    def valid_entropy(class_probabilities: List[float]) -> float:
        return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)

    try:
        user_file = os.path.join(OUTPUT_TASK_FILE)
        module = load_module(user_file)
        func_select = module.select
        candidate_no_attributes = Candidate()

        if func_select(candidate_no_attributes) != QuestionEnum.ASK_LEVEL:
            grade -= 1

        candidate_with_level = Candidate(level=LevelEnum.JUNIOR)
        if func_select(candidate_with_level) != QuestionEnum.ASK_LANGUAGE:
            grade -= 1

        candidate_with_level_and_lang = Candidate(level=LevelEnum.JUNIOR,
                                                  lang=LanguageEnum.PYTHON)
        if func_select(
                candidate_with_level_and_lang) != QuestionEnum.ASK_DEGREE:
            grade -= 1

        random_class_probabilities = [random.randint(0, 10) / 10 for i in
                                      range(10)]
        func_entropy = module.entropy

        if valid_entropy(random_class_probabilities) != func_entropy(
                random_class_probabilities):
            grade -= 2

    except Exception as e:
        grade = str(e)

    RESULTS["grade"] = grade

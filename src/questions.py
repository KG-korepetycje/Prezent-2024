from dataclasses import dataclass


@dataclass
class Question:
    question: str
    hashed_answer: str
    hints: dict[int, str] | None


questions = [
    Question(
        question="Jak się nazywał rejon we Włoszech, gdzie byliśmy na wakacjach w 2023 roku?",
        hashed_answer=""
    )
]

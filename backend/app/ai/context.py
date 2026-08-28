import json
from pathlib import Path
from app.models.candidate import Candidate


CANDIDATE_FILE = (
    Path(__file__).resolve().parents[1] / "data" / "candidate.json"
)


def load_candidate() -> Candidate:
    with open(CANDIDATE_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Candidate.model_validate(data)

def get_candidate_context() -> str:
    candidate = load_candidate()

    return candidate.model_dump_json(indent=2)
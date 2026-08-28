import json

from app.models.candidate import Candidate


with open(
    "app/data/candidate.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)


candidate = Candidate.model_validate(data)


print("Candidate JSON validation successful!")
print("-----------------------------------")

print(f"Name: {candidate.profile.name}")
print(f"Title: {candidate.profile.professional_title}")

print(
    f"College: "
    f"{candidate.education[0].institution}"
)

print(
    f"CGPA: "
    f"{candidate.education[0].cgpa}/"
    f"{candidate.education[0].scale}"
)

print(
    f"LeetCode Problems: "
    f"{candidate.data_structures_and_algorithms.leetcode_problems_solved}+"
)

print("\nSkills:")
for skill in candidate.skills.programming_languages:
    print(f"- {skill.name}")

print("\nProjects:")
for project in candidate.projects:
    print(f"- {project.name}")

print("\nValidation completed successfully!")
from app.ai.context import load_candidate, get_candidate_context


candidate = load_candidate()

print("Candidate validation successful!")
print(f"Name: {candidate.profile.name}")
print(f"Title: {candidate.profile.professional_title}")
print()


context = get_candidate_context()

print("Candidate context generated successfully!")
print(context[:1000])
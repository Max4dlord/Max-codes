#!/usr/bin/env python3
"""Assemble the EEE 202 bank (topics + questions A/B) and emit .eee202_out.json."""
import json
from eee_topics import TOPICS
from eee_questions_a import QUESTIONS_A
from eee_questions_b import QUESTIONS_B

QUESTIONS = QUESTIONS_A + QUESTIONS_B

# validate structure
errors = []
seen = set()
counters = {}
for q in QUESTIONS:
    if q["correct"] < 0 or q["correct"] >= len(q["options"]):
        errors.append(f"{q['topicId']}: bad correct index")
    if len(q["options"]) < 4:
        errors.append(f"{q['topicId']}: too few options")
    if q["kind"] not in ("calc", "theory"):
        errors.append(f"{q['topicId']}: bad kind")
    if q["kind"] == "calc" and "$" not in q["solution"]:
        errors.append(f"{q['topicId']}: calculation solution missing LaTeX math ($...$)")
    for banned in ["simplifying yields", "similarly", "by inspection", "it follows that"]:
        if banned in q["solution"]:
            errors.append(f"{q['topicId']}: banned phrase '{banned}'")
    counters[q["topicId"]] = counters.get(q["topicId"], 0) + 1
    q["id"] = f"eee_{q['topicId'].replace('eee-','')}_{counters[q['topicId']]:02d}"
    if q["id"] in seen:
        errors.append(f"duplicate id {q['id']}")
    seen.add(q["id"])

if errors:
    print("ERRORS:")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

calc_n = sum(1 for q in QUESTIONS if q["kind"] == "calc")
theory_n = sum(1 for q in QUESTIONS if q["kind"] == "theory")
print(f"TOTAL: {len(QUESTIONS)} | calc: {calc_n} | theory: {theory_n}")
for t in TOPICS:
    print(" ", t["id"], "->", counters.get(t["id"], 0))

json.dump({"topics": TOPICS, "questions": QUESTIONS},
          open(".eee202_out.json", "w"), ensure_ascii=False, indent=2)
print("emitted .eee202_out.json")

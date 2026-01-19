# from flask import Blueprint, request, jsonify

# from app.agents.resume_scoring_agent import score_resume
# from app.agents.skill_gap_agent import find_skill_gap
# from app.agents.interview_agent import generate_interview_questions

# resume_api = Blueprint("resume_api", __name__)


# @resume_api.route("/score", methods=["POST"])
# def resume_score():
#     data = request.json
#     resume_text = data.get("resume_text")
#     job_description = data.get("job_description")

#     result = score_resume(resume_text, job_description)
#     return jsonify(result)


# @resume_api.route("/skill-gap", methods=["POST"])
# def skill_gap():
#     data = request.json
#     resume_text = data.get("resume_text")
#     job_description = data.get("job_description")

#     result = find_skill_gap(resume_text, job_description)
#     return jsonify(result)


# @resume_api.route("/interview-questions", methods=["POST"])
# def interview_questions():
#     data = request.json
#     resume_text = data.get("resume_text")
#     job_description = data.get("job_description")

#     result = generate_interview_questions(resume_text, job_description)
#     return jsonify(result)


# from flask import Blueprint, request, jsonify

# from app.agents.resume_scoring_agent import score_resume
# from app.agents.skill_gap_agent import analyze_skill_gap   # <- updated
# from app.agents.interview_agent import generate_interview_questions

# resume_api = Blueprint("resume_api", __name__)


# @resume_api.route("/score", methods=["POST"])
# def resume_score():
#     data = request.json
#     resume_text = data.get("resume_text")
#     job_description = data.get("job_description")

#     result = score_resume(resume_text, job_description)
#     return jsonify(result)


# @resume_api.route("/skill-gap", methods=["POST"])
# def skill_gap():
#     data = request.json
#     resume_text = data.get("resume_text")
#     job_description = data.get("job_description")

#     result = analyze_skill_gap(resume_text, job_description)   # <- updated
#     return jsonify(result)


# @resume_api.route("/interview-questions", methods=["POST"])
# def interview_questions():
#     data = request.json
#     resume_text = data.get("resume_text")
#     job_description = data.get("job_description")

#     result = generate_interview_questions(resume_text, job_description)
#     return jsonify(result)

from flask import Blueprint, request, jsonify
from app.agents.resume_scoring_agent import score_resume
from app.agents.skill_gap_agent import analyze_skill_gap  # updated name
from app.agents.interview_agent import generate_interview_questions

resume_api = Blueprint("resume_api", __name__)

@resume_api.route("/")
def home():
    return "Resume API is running!"

@resume_api.route("/score", methods=["POST"])
def resume_score():
    data = request.json
    resume_text = data.get("resume_text")
    job_description = data.get("job_description")
    result = score_resume(resume_text, job_description)
    return jsonify(result)

@resume_api.route("/skill-gap", methods=["POST"])
def skill_gap():
    data = request.json
    resume_text = data.get("resume_text")
    job_description = data.get("job_description")
    result = analyze_skill_gap(resume_text, job_description)
    return jsonify(result)

@resume_api.route("/interview-questions", methods=["POST"])
def interview_questions():
    data = request.json
    resume_text = data.get("resume_text")
    job_description = data.get("job_description")
    result = generate_interview_questions(resume_text, job_description)
    return jsonify(result)

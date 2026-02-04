from openai import OpenAI

client = OpenAI()

def explain_plan(priorities, schedule):

    # Here I am preparing a summary of priorities and schedule to provide context to the LLM.
    priority_summary = []
    for item in priorities:
        c = item["course"]
        priority_summary.append({
            "course": c.name,
            "deadline_urgency": getattr(c, "deadline_urgency", "None"),
            "risk_score": c.risk_score,
            "priority_score": item["priority_score"],
        })

    schedule_summary = []
    for item in schedule:
        schedule_summary.append({
            "course": item["course"].name,
            "minutes": item["minutes"],
        })

# Writing a prompt for the LLM to explain how it should respond based on data and setting guard rails.
    prompt = f"""
You are an academic planning assistant. A student has multiple courses. The system computed priorities and a study schedule.

PRIORITIES (higher score = higher priority):
{priority_summary}

SCHEDULE (time allocated today):
{schedule_summary}

You should usually explain:
1. Why the top 1–2 courses were prioritized
2. How deadlines vs risk affected the plan
3. Whether the schedule is balanced or stressful

You may also converse with the student if they have any questions and provide further explanations.

Be concise, clear, and supportive. Only answer based on the data provided to you.
"""

# Here I am calling the OpenAI API to get the actual explanation from the LLM based on the prompt.
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You explain academic planning decisions clearly."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3, # A lower temperature value results in more focused and consistent responses.
    )

    return response.choices[0].message.content

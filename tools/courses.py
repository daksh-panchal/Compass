import os
from .notion_client_wrapper import notion
from datetime import datetime
from models.course_model import Course

COURSES_DB_ID = os.getenv("COURSES_DB_ID")
if not COURSES_DB_ID:
    raise RuntimeError("COURSES_DB_ID not found")

def get_courses():
    # Here I am retrieving courses from a database I made in Notion.
    db = notion.databases.retrieve(database_id=COURSES_DB_ID)

    data_sources = db.get("data_sources", [])
    if not data_sources:
        raise RuntimeError(
            "No data sources found for this database."
        )

    # Now, I am querying the data source to get the courses.
    data_source_id = data_sources[0]["id"]
    response = notion.data_sources.query(
        data_source_id=data_source_id,
        page_size=100,
    )

    # Here I am returning a list of course objects parsed from the response.
    return [_parse_course(row) for row in response.get("results", [])]


# This function will parse through a row from the "Courses" database in Notion and convert it into a course object.
def _parse_course(row) -> Course:
    properties = row["properties"] # Getting all the properties of the row.

    # Now, I will extract each individual property needed to create a Course object.
    title = properties["Course Name"]["title"] 
    name = title[0]["plain_text"] if title else "Untitled" 

    current_standing = properties["Current Standing"]["select"]["name"] 
    cognitive_load = properties["Cognitive Load"]["select"]["name"] 
    recovery_cost = properties["Recovery Cost"]["select"]["name"] 

    last_worked_raw = properties["Last Worked On"]["date"]
    last_worked_on = (
        datetime.fromisoformat(last_worked_raw["start"]).date()
        if last_worked_raw else None
    )

    grading_scheme = [
        item["name"]
        for item in properties["Grading Scheme"]["multi_select"]
    ]

    course_type = [
        item["name"]
        for item in properties["Course Type"]["multi_select"]
    ]

    deadline_raw = properties["Next Assignment/Lab Deadline"]["date"]
    next_deadline = (
    datetime.fromisoformat(deadline_raw["start"]).date()
    if deadline_raw else None
    )

    return Course(
        name=name,
        current_standing=current_standing,
        cognitive_load=cognitive_load,
        recovery_cost=recovery_cost,
        last_worked_on=last_worked_on,
        grading_scheme=grading_scheme,
        course_type=course_type,
        next_deadline=next_deadline,
    )



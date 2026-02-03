import os
from .notion_client_wrapper import notion

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

    # Here I will extract course names and return them as a list to verify functionality.
    courses = []
    for row in response.get("results", []):
        title = row["properties"]["Course Name"]["title"]
        if title:
            courses.append(title[0]["plain_text"])

    return courses




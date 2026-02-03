# I am choosing the standard time block duration to be 30 minutes.
BLOCK_MINUTES = 30

# This dictionary defines the maximum number of time blocks that can be allocated based on cognitive load.
# If the cognitive load is higher, fewer time blocks should be assigned to avoid burnout.
MAX_BLOCKS_BY_LOAD = {
    "Low": 4,
    "Medium": 3,
    "High": 2
}

# This dictionary defines the number of time blocks that can be allocated based on deadline urgency.
# A more urgent deadline means more time blocks are assigned.
DEADLINE_BLOCKS = {
    "Critical": 4,
    "High": 3,
    "Medium": 2,
    "Low": 1,
    "None": 0,
}

def allocate_time(plan, available_minutes):
    remaining_minutes = available_minutes
    schedule = []

    for item in plan:
        course = item["course"]

        if remaining_minutes < BLOCK_MINUTES:
            break

        # This determines the number of time blocks to allocate based on deadline urgency.
        blocks = DEADLINE_BLOCKS.get(course.deadline_urgency, 0)

        # This adds blocks based on risk score assuming that there is a risk score and that it is 4 or greater.
        if course.risk_score and course.risk_score >= 4:
            blocks += 1

        # This limits the number of blocks that could be allocated based on cognitive load.
        max_blocks = MAX_BLOCKS_BY_LOAD.get(course.cognitive_load, 2)
        blocks = min(blocks, max_blocks)

        # This ensures that we don't allocate more blocks than the amount that can fit in the available time.
        max_affordable_blocks = remaining_minutes // BLOCK_MINUTES
        blocks = min(blocks, max_affordable_blocks)

        # If any blocks are allocated, they are added to the schedule list.
        if blocks > 0:
            schedule.append({
                "course": course,
                "blocks": blocks,
                "minutes": blocks * BLOCK_MINUTES,
            })

            remaining_minutes -= blocks * BLOCK_MINUTES # Updating the remaining available time.

    return schedule
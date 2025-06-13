import json
from datetime import date

def update_epic(epic_id, updates={'status': 'complete'}, json_file='epics.json'):
    """
    Update fields for a specific epic in the JSON file.

    Args:
        epic_id (int): The ID of the epic to update.
        updates (dict): A dictionary of fields and new values, e.g. {'status': 'complete'}
        json_file (str): Path to the JSON file.

    Returns:
        bool: True if update successful, False if epic not found.
    """
    # Load existing epics
    with open(json_file, 'r') as f:
        epics = json.load(f)
    
    # Find and update the epic
    updated = False
    for epic in epics:
        if epic['id'] == epic_id:
            for field, value in updates.items():
                epic[field] = value
            # Special case: if marking complete, set completion_date to today if not set
            if updates.get('status') == 'complete' and not epic.get('completion_date'):
                epic['completion_date'] = str(date.today())
            updated = True
            break
    
    # Save back to JSON
    if updated:
        with open(json_file, 'w') as f:
            json.dump(epics, f, indent=2)
    return updated

# Example usage:
# Mark epic ID 2 as complete and add a new contributor

"""
success = update_epic(2, {
    'status': 'complete'
})
if success:
    print("Epic updated successfully.")
else:
    print("Epic not found.")
"""
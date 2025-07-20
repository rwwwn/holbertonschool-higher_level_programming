import os

def generate_invitations(template, attendees):
    # Type checks
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Empty checks
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Generate invitations
    for index, person in enumerate(attendees, start=1):
        filled = template
        for field in ['name', 'event_title', 'event_date', 'event_location']:
            value = person.get(field)
            filled = filled.replace(f'{{{field}}}', str(value) if value else 'N/A')

        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(filled)
        except Exception as e:
            print(f"Failed to write {filename}: {e}")

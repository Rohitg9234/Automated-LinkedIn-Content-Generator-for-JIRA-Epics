import json

def check_for_completion(json_file='epics.json'):
    with open(json_file, 'r') as f:
        epics = json.load(f)
    return [epic for epic in epics if epic['status'] == 'complete' and not epic.get('content_generated', False)][0]
#print(check_for_completion())
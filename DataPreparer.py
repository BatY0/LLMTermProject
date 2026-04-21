import json
import os

def prepare_master_file(input_filename, output_filename):
    """
    Converts raw benchmark data into a 'Master' format for manual refinement.
    """
    master_entries = []

    if not os.path.exists(input_filename):
        print(f"Error: {input_filename} not found.")
        return

    with open(input_filename, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            entry = json.loads(line)

            # Create the Master Record structure
            master_record = {
                "key": entry.get('key'),
                "original_prompt": entry.get('prompt'),  # The raw text to look at
                "instruction_id_list": entry.get('instruction_id_list'),
                "kwargs": entry.get('kwargs'),
                "task_content": "",  # You will fill this in the UI
                "rules_content": [],  # You will fill this in the UI
                "variations": {
                    "plain": None,
                    "markdown": None,
                    "xml": None,
                    "json": None,
                    "yaml": None
                },
                "status": "pending"  # To track your progress in the UI
            }
            master_entries.append(master_record)

    with open(output_filename, 'w', encoding='utf-8') as f:
        # We save as a standard JSON array so the Web UI can read it easily
        json.dump(master_entries, f, indent=2)

    print(f"Successfully created {output_filename} with {len(master_entries)} entries.")

if __name__ == '__main__':
    prepare_master_file('data/IFBench/IFBench_test.jsonl', 'data/IfBench.json')

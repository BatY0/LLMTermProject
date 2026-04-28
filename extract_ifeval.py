import json
import os

def create_ifeval_eval_files():
    input_data_path = 'data/IFEval/input_data.jsonl'
    results_path = 'results/IfEvalTestResults.json'
    output_dir = 'results/ifeval_eval_files'
    
    print(f"Creating output directory: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)
    
    # Map key to full input data
    key_to_input = {}
    with open(input_data_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                data = json.loads(line)
                key = str(data.get('key'))
                key_to_input[key] = data
                
    print(f"Loaded {len(key_to_input)} input prompts.")
                
    # Read the results
    with open(results_path, 'r', encoding='utf-8') as f:
        results = json.load(f)
        
    print(f"Loaded {len(results)} results.")
        
    formats = ['plain', 'markdown', 'xml', 'json', 'yaml']
    
    # Prepare file handlers
    files = {}
    for fmt in formats:
        files[fmt] = open(os.path.join(output_dir, f'{fmt}.jsonl'), 'w', encoding='utf-8')
        
    extracted_counts = {fmt: 0 for fmt in formats}
    
    for entry in results:
        key = str(entry.get('key'))
        input_entry = key_to_input.get(key)
        
        if not input_entry:
            print(f"Warning: Input data not found for key {key}")
            continue
            
        responses = entry.get('responses', {})
        for fmt in formats:
            response_text = responses.get(fmt)
            if response_text is not None:
                # Merge original input with the response
                out_record = input_entry.copy()
                out_record['response'] = response_text
                files[fmt].write(json.dumps(out_record, ensure_ascii=False) + '\n')
                extracted_counts[fmt] += 1
                
    for fmt in formats:
        files[fmt].close()
        
    print("\nExtraction complete. Summary:")
    for fmt, count in extracted_counts.items():
        print(f"  {fmt}.jsonl: {count} responses")

if __name__ == '__main__':
    create_ifeval_eval_files()

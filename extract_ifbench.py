import json
import os


def create_ifbench_eval_files():
    input_data_path = "data/IFBench/IFBench_test.jsonl"
    results_path = "results/IfBenchResults.json"
    output_dir = "results/ifbench_eval_files"

    print(f"Creating output directory: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)

    key_to_prompt = {}
    with open(input_data_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                data = json.loads(line)
                key = str(data.get("key"))
                key_to_prompt[key] = data.get("prompt", "")

    print(f"Loaded {len(key_to_prompt)} IFBench prompts.")

    with open(results_path, "r", encoding="utf-8") as f:
        results = json.load(f)

    print(f"Loaded {len(results)} result records.")

    formats = ["plain", "markdown", "xml", "json", "yaml"]
    files = {}
    for fmt in formats:
        files[fmt] = open(
            os.path.join(output_dir, f"{fmt}-responses.jsonl"),
            "w",
            encoding="utf-8",
        )

    extracted_counts = {fmt: 0 for fmt in formats}
    missing_prompt_keys = 0

    for entry in results:
        key = str(entry.get("key"))
        prompt = key_to_prompt.get(key)
        if prompt is None:
            missing_prompt_keys += 1
            continue

        responses = entry.get("responses", {})
        for fmt in formats:
            response_text = responses.get(fmt)
            if response_text is not None:
                out_record = {
                    "prompt": prompt,
                    "response": response_text,
                }
                files[fmt].write(json.dumps(out_record, ensure_ascii=False) + "\n")
                extracted_counts[fmt] += 1

    for fmt in formats:
        files[fmt].close()

    print("\nExtraction complete. Summary:")
    for fmt, count in extracted_counts.items():
        print(f"  {fmt}-responses.jsonl: {count} responses")
    if missing_prompt_keys:
        print(f"  Missing prompts for {missing_prompt_keys} keys")


if __name__ == "__main__":
    create_ifbench_eval_files()

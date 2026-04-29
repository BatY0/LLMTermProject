# IFBench Benchmark Results

After extracting your 5 output formats from `IfBenchResults.json` and running the official IFBench evaluator, here are the prompt-level scores.

IFBench reports:
- **Strict Accuracy**: exact instruction compliance.
- **Loose Accuracy**: allows limited formatting flexibility (e.g., minor wrappers).

| Rank | Format | Strict Prompt Accuracy | Loose Prompt Accuracy |
|------|--------|------------------------|-----------------------|
| 🥇 | **JSON** | 50.67% | 52.67% |
| 🥈 | **Plain** | 48.67% | 51.33% |
| 🥉 | **Markdown** | 47.00% | 48.67% |
| 4 | **XML** | 46.67% | 49.33% |
| 4 | **YAML** | 46.67% | 49.33% |

### Notes
1. These scores were computed on **300 IFBench test prompts**.
2. Your `IfBenchResults.json` currently contains **298 responses**, so 2 prompts were scored as missing responses.

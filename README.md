# LLMTermProject

This project studies instruction-following behavior across multiple prompt formats (`plain`, `markdown`, `xml`, `json`, `yaml`) and compares performance under two benchmarks: IFEval and IFBench. You can find more detailed report in `LLMTermProject_Report.pdf`.

## Problem And Approach

We wanted to measure how well one model follows explicit constraints when the same task is presented in different structured prompt styles.

Our workflow was:

1. **Benchmark Selection**
   - Used the IFEval dataset for the original instruction-following benchmark setup.
   - Used the IFBench dataset for harder out-of-distribution (OOD) constraints.

2. **Dataset Restructuring (Task + Rules)**
   - Processed each benchmark sample one-by-one.
   - Restructured raw prompts into a task/rule-oriented representation so each item clearly separates:
     - task content
     - instruction/rule content
   - Created five prompt-format variants per sample: `plain`, `markdown`, `xml`, `json`, `yaml`.

3. **Model Inference**
   - Queried `deepseekv3.1` through OpenRouter to generate responses for each format variant.
   - Collected outputs into consolidated result files for each benchmark.

4. **Evaluation Pipeline**
   - Converted model outputs into benchmark-compatible `jsonl` files.
   - Ran strict and loose evaluation using official benchmark evaluation logic.
   - Generated per-format reports and summary tables.

## Results Summary

### IFEval (Prompt-Level Accuracy)

| Rank | Format | Strict | Loose |
|------|--------|--------|-------|
| 🥇 | XML | 89.28% | 91.87% |
| 🥈 | YAML | 85.95% | 87.98% |
| 🥉 | Markdown | 85.76% | 88.90% |
| 4 | JSON | 85.21% | 88.53% |
| 5 | Plain | 85.02% | 88.72% |

### IFBench (Prompt-Level Accuracy)

| Rank | Format | Strict | Loose |
|------|--------|--------|-------|
| 🥇 | JSON | 50.67% | 52.67% |
| 🥈 | Plain | 48.67% | 51.33% |
| 🥉 | Markdown | 47.00% | 48.67% |
| 4 | XML | 46.67% | 49.33% |
| 4 | YAML | 46.67% | 49.33% |

Notes:
- IFBench is substantially harder than IFEval, so lower absolute scores are expected.
- IFBench summary above was computed on 300 test prompts; the current file had 298 responses (2 missing).

## Repository Outputs

- Scripts for preparing and extracting benchmark-compatible files
- Format-specific response files for evaluation
- Strict/loose evaluation outputs per format in `results/`
- Summary reports:
  - `results/ifeval_summary_report.md`
  - `results/ifbench_summary_report.md`

## References

- IFBench (AllenAI): [https://github.com/allenai/IFBench](https://github.com/allenai/IFBench)
- IFEval (Google Research): [https://github.com/google-research/google-research/tree/master/instruction_following_eval](https://github.com/google-research/google-research/tree/master/instruction_following_eval)

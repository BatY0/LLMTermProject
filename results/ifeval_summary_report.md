# IFEval Benchmark Results

After extracting the responses for the 5 different formats and running the official IFEval evaluation suite, the results are in!

IFEval measures two types of accuracies:
* **Strict Accuracy**: Checks the exact formatting, length, and content constraints precisely as specified.
* **Loose Accuracy**: Allows for minor formatting flexibility (e.g., ignoring case or minor punctuation in certain constraints).

Here is the performance of the model across the 5 requested formats:

| Rank | Format | Strict Prompt Accuracy | Loose Prompt Accuracy |
|------|--------|------------------------|-----------------------|
| 🥇 | **XML** | 89.28% | 91.87% |
| 🥈 | **YAML** | 85.95% | 87.98% |
| 🥉 | **Markdown** | 85.76% | 88.90% |
| 4 | **JSON** | 85.21% | 88.53% |
| 5 | **Plain** | 85.02% | 88.72% |

### Key Takeaways
1. **XML is the Clear Winner**: The model demonstrates the highest instruction-following adherence when formatting its output as XML. It beat the second-best format by over 3%!
2. **Plain Text Struggles**: When given no structural constraints (Plain text), the model appears to slip up on following precise instructions more frequently.

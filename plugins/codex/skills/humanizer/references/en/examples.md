# Examples with controlled facts (English)

These examples complement rules R01-R12 and the English catalog ([patterns.md](patterns.md)). They are fictional and exist to calibrate how much to change, not as evidence about products or people. Portuguese examples are in [../pt-br/exemplos.md](../pt-br/exemplos.md).

#### Technical update

**Given facts for this fictional example:** the service may retry a request once after a timeout. There is no evidence that retries always succeed.

**Before:** "It is important to note that the service has the ability to potentially retry a request once after a timeout."

**After:** "The service may retry a request once after a timeout."

Keep "may" and "once". Do not replace the sentence with "The service automatically recovers from timeouts".

#### Correct terminology

**Input already fine:** "The end-to-end tests use a third-party service that sends real-time updates."

**Output:** keep the sentence. The hyphenated compounds have a function; removing them is not an automatic improvement.

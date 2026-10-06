# Day 2 participant lab — Prompt engineering for damaged-delivery support

**Programme:** T-Systems GenAI and Prompt Engineering for Developers  
**Trainer:** Nived Varma  
**Core lab:** 70 minutes, matching slide 40  
**Optional Python extension:** 30 minutes within the coding/practice block, if allocated by the trainer  
**Tools:** Microsoft Foundry Chat Playground, deployed GPT-5; VS Code/Python for the extension

## 1. Your business assignment

You are developing an assistant for a fictional industrial supplier, Aster Industrial Supplies. Customers report damaged sensors in short messages. A service adviser needs an evidence-based assessment and a useful next step. The assistant drafts guidance; a service reviewer authorises replacement.

> As a service adviser, I want to assess a damaged-delivery request using supplied rules so that the customer gets the right next step.

Your starting request is: **“Two sensors arrived damaged yesterday. Can you replace them? Report date: 2026-10-06.”**

You will turn a weak prompt into a reusable interaction through five documented revisions, compare zero-shot and few-shot routing, and test on cases you did not use during development. All documents and cases are synthetic. Use only the supplied business rules. This exercise assesses prompt design and evaluation; it does not build a retrieval pipeline or authorise replacements.

## 2. Time plan and completion target

| Activity | Minutes | Why this time is needed | Evidence to retain |
|---|---:|---|---|
| Task A: baseline and acceptance criteria | 15 | Read the short policy, establish a baseline and define measurable checks | V0 and first findings record |
| Task B: five prompt revisions | 25 | Make one change at a time, run tests and record the effect | V1–V5, exact responses, decision log |
| Task C: zero-shot versus few-shot | 15 | Compare identical routing tests with and without examples | Six classification outputs |
| Task D: unseen tests and peer review | 15 | Check transfer, inspect evidence and justify selection | Held-out results and peer feedback |
| **Core total** | **70** | | |
| Optional Task E: Python comparison | 30 | Reuse Day 1 environment skills and retain API experiment logs | Prompt files and JSONL results |

Complete Tasks A–D during the participant lab slot; the 30-minute extension is not automatically added to the day's schedule. Work individually or in pairs as directed, but maintain your own findings. If model latency is high, prioritise one complete run per version, the routing comparison and the unseen tests. Repeated runs are a stretch activity.

## 3. Files and how to use them

| File | Purpose | Send to the model? |
|---|---|---|
| context/business_brief.md | Business objective and acceptance criteria | Use to write your instructions |
| context/damaged_delivery_policy.txt | C1–C4 and explicit boundary-day convention | Yes, beginning at V2 |
| cases/development.json | Requests you may use to revise prompts | Send only the request field |
| context/routing_rules.txt | Rules for Task C labels | Yes |
| context/routing_worked_examples.txt | Worked examples for few-shot variant | Only in the few-shot prompt |
| cases/routing_unseen.json | Routing comparison requests | Send only the request field |
| cases/held_out.json | Final transfer tests | Open only after choosing a candidate |
| worksheets/findings.md | Run records and reflection | No |
| worksheets/rubric.md | Human review criteria | No need to send |
| review_checks_OPEN_AFTER_TESTING.md | Reference behaviour for checking outputs | No; open after testing |
| context/order_register.txt | Optional extension context | Only relevant records, if you choose to use it |

**Keep review answers separate from input.** The case files contain requests, not model-generated solutions. Do not paste the whole review document into the playground.

## 4. Prepare the Playground — included in Task A

1. Extract the pack and open the guide, policy and findings worksheet in VS Code or a text editor.
2. Open your assigned Foundry resource/project and its Chat Playground. Select the deployed GPT-5 deployment used in class. Use the interface already demonstrated by the trainer; labels can vary between Foundry experiences.
3. Start a new conversation. Inspect existing application instructions and remove earlier trainer-demo policy or customer information. Record any instruction you retain.
4. Keep the same deployment and relevant settings across comparisons. Do not add temperature or top-p parameters to this GPT-5 exercise.
5. Copy worksheets/findings.md to a personal working copy. Enter your name, deployment and date. Save unedited responses, not just your interpretation.
6. For a version comparison, start a fresh conversation each time. Otherwise an earlier answer can supply facts that the revised prompt did not provide.

**Why:** A useful comparison must reveal what you changed. Hidden conversation history makes a prompt look better for reasons you cannot reproduce.

## 5. Task A — establish a baseline and acceptance criteria (15 minutes)

### A1. Run V0 (5 minutes)

Send this weak prompt in the fresh conversation, with no Aster policy:

```text
Two sensors arrived damaged yesterday. Can you replace them?
Report date: 2026-10-06.
```

Save the text as prompts/V0.txt and record the unedited answer. Mark any invented deadline, replacement promise or assumption. The model may ask for policy information or refuse to decide; this is a valid observation. You do not need to force it to make a mistake.

### A2. Read the business brief and policy (5 minutes)

Read C1–C4. Identify which facts affect timing, what evidence is required and who authorises replacement. The supplied convention counts delivery as day 0; exactly five elapsed days is within the window. This is an exercise convention, not a rule to infer for another organisation.

### A3. Write your success checks (5 minutes)

In the findings worksheet, define checks for supported claims, missing facts, authority and response structure. Use the rubric as the baseline. Write one example of a blocking failure, such as “Your replacement is approved” when no approval exists.

**Explanation:** A fluent answer is not sufficient. Defining checks before revisions prevents you from calling a preferred writing style an improvement without supporting evidence.

**Checkpoint:** You have V0, its actual response, the four evaluation checks and one blocking failure rule.

## 6. Task B — make five documented revisions (25 minutes)

Spend about four minutes on each revision and five minutes consolidating the comparison. Do not paste the final rubric or reference answers into the request. For V1 use no policy; for V2 onward supply the same policy text. Record this evidence change explicitly.

### B1. V1 — clarify role and task

Write an instruction establishing that the assistant drafts damaged-delivery guidance for an adviser. State what it should assess. Run the D1 request and save V1 plus the response.

**Explain in your record:** What changed when the business task became explicit? A role statement does not give the model company knowledge or approval authority.

### B2. V2 — add policy evidence

Keep V1 and add the instruction to use the supplied policy and identify relevant clauses. Send the policy and D1 request with clear labels:

```text
POLICY:
[paste the complete damaged_delivery_policy.txt]

REQUEST:
[paste the D1 request]
```

Save V2 and the exact context. Check each policy claim against C1–C4.

**Explanation:** V1 versus V2 introduces new evidence. It demonstrates the value of context, not a controlled change of instruction wording alone. Labels help organise text; they do not authenticate policy documents.

### B3. V3 — define missing-information behaviour

Add one fallback rule describing what to do when a required fact is missing. Use D1 again. Check whether the assistant asks for the order ID and photos without inventing approval. “Yesterday” can be resolved from the explicit report date; do not demand a repeated question when the date is already inferable.

**Explanation:** Useful clarification asks for information that affects the outcome. Asking every possible question can be unhelpful even when it avoids guessing.

### B4. V4 — define an output contract

Add the four requested headings: **Decision, Evidence, Questions, Next step**. Run D1, then D2. Check whether the structure remains useful when facts are more complete. The model should request available photos for review, rather than pretend a reviewer has received and approved them.

**Explanation:** Plain text headings are a requested format. They do not provide schema enforcement. Review the actual response.

### B5. V5 — change one thing based on an observed failure

Identify one specific V4 failure on a development case. Copy V4 to V5 and make one targeted change. Possible targets include a false approval implication, repeated questions about known dates, or unsupported dispatch promises. Choose only a failure you actually observed.

Run V5 on the same case, then another development case. Record whether the change improved one case and harmed another. If V4 shows no failure on D1/D2, try D3. If all supplied development cases pass, design a new development case with a stated reference expectation, and use it to test a remaining hypothesis. Do not open held-out cases to find your V5 change. Record honestly if no improvement is demonstrated.

**Explanation:** More text is not inherently better. V5 is a hypothesis about a real weakness, not a guaranteed upgrade. You may select an earlier version if it performs better.

### B6. Choose a candidate

Apply the rubric and select one prompt for final testing. Save its exact instructions as prompts/selected.txt; keep policy as a separate context document. Freeze it before opening cases/held_out.json.

**Checkpoint:** Six versions V0–V5, five changes with reasons, actual responses and a candidate selection. V3 onward comparisons should hold policy, cases and settings fixed.

## 7. Task C — compare zero-shot and few-shot routing (15 minutes)

This is a separate, smaller business task: route a customer message by workflow stage. It does not decide replacement eligibility.

### C1. Write a zero-shot prompt (3 minutes)

Use the routing rules and ask for exactly one label: **Damage report**, **Evidence follow-up**, or **Needs clarification**. Do not include worked examples. Use the three requests in cases/routing_unseen.json, one per fresh conversation. Record exact outputs.

### C2. Add examples (5 minutes)

Keep the instruction and routing rules identical. Add the three input/output examples from routing_worked_examples.txt. Run the same three unseen requests in fresh conversations.

**Explanation:** Few-shot examples demonstrate the task within the current input; they do not permanently train the deployed model. For GPT-5, examples are a comparison to evaluate, not an assumed improvement.

### C3. Compare (7 minutes)

Now inspect the routing reference labels in the review document. Record label correctness and exact-label format separately. Note whether examples changed the answer, added unnecessary text or had no measurable benefit. A mixed-stage request should follow the explicit mixed-stage rule, not a keyword count.

If both variants are correct, report a tie on this small set. Do not manufacture a percentage gain. If you tune using these results, these requests become development cases and you need new unseen requests for a fresh evaluation.

**Checkpoint:** Three outputs per variant and a written choice supported by observations.

## 8. Task D — unseen assessment and peer review (15 minutes)

### D1. Test your frozen candidate (7 minutes)

Open cases/held_out.json only now. Run H1, H2 and H3 in fresh conversations with the selected instruction and the same policy. Save responses before opening reference checks. Do not revise the prompt between these three tests.

### D2. Review behaviour (4 minutes)

Open review_checks_OPEN_AFTER_TESTING.md and apply the rubric. Confirm that the five-day and six-day cases are distinguished, required information is handled and replacement authority stays with the reviewer. Any failure is evidence to report, not a reason to hide the run.

### D3. Peer review and reflection (4 minutes)

Exchange one prompt and one unedited response with a peer. Ask them to identify one policy claim and its clause, one missing fact or unnecessary question, and any approval implication. Resolve disagreement by pointing to the policy and response, not by voting on which answer sounds better.

Write which version you selected, why, and what remains an application responsibility. Examples include obtaining authenticated order information, validating dates in code and enforcing actual approval permissions.

**Checkpoint:** Three frozen-candidate tests, human scores, blocking-failure notes and peer feedback.

## 9. Optional Task E — reproduce the comparison in Python (30 minutes)

Do this only in the allocated coding slot. The core assignment can be completed in the Playground.

### E1. Prepare VS Code and .venv (7 minutes)

Extract the pack to C:\AgenticAI_Labs\Day2_Participant_Lab and open that folder in VS Code. In its PowerShell terminal:

```powershell
cd C:\AgenticAI_Labs\Day2_Participant_Lab
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Select **Python: Select Interpreter** and choose .venv\Scripts\python.exe. Edit .env with your training key, resource inference URL ending /openai/v1/, and actual deployment name. Do not put keys in Python or terminal commands. The .gitignore excludes .env and .venv.

If activation is blocked, run .venv\Scripts\python.exe directly rather than changing the VDI's machine policy.

### E2. Inspect the supplied code (6 minutes)

Open run_assignment.py. Identify these responsibilities:

- load_dotenv reads the project-local .env before client construction.
- OpenAI points to the Azure resource inference URL; model receives the deployment name.
- Instructions come from your prompt files; policy and request form the input.
- Each request is independent; no previous_response_id carries earlier facts.
- Exact prompts, inputs, output, status, latency and usage are written to JSONL.
- Human quality scores are not invented by the script.

The script deliberately supplies no policy for V0/V1. Use V3/V4 or V4/V5 for a comparison with identical evidence. The code uses the documented Responses API pattern; verify availability for your assigned deployment.

### E3. Execute and inspect (10 minutes)

Ensure prompts/selected.txt contains your selected instruction. Run:

```powershell
python run_assignment.py --versions selected
```

This makes three development-case calls. To compare saved versions:

```powershell
python run_assignment.py --versions V4,V5
```

This makes six calls; it requires those exact files. Optional repetition:

```powershell
python run_assignment.py --versions selected --repeat 2
```

Open the generated results/*.jsonl file in VS Code. Match one record's input and instructions to your Playground test. Do not expect identical wording; inspect business behaviour. If a response is incomplete or the call fails, retain its status and do not count it as a correct answer.

### E4. Record engineering observations (7 minutes)

Transfer the human scores to worksheets/scores.csv. Explain whether improved quality came with more input tokens or latency. Elapsed time includes SDK retries; a single call is not a performance benchmark. Reasoning tokens, when reported, are usage data, not visible internal reasoning.

If you add the optional order-register context, start a new recorded experiment and keep it fixed for both prompt variants. Do not silently change context while claiming the instruction alone improved the answer.

The supplied script has been syntax-checked. Actual API behaviour must be observed using your configured training deployment.

## 10. Troubleshooting and pacing

| Symptom | Practical action |
|---|---|
| Old policy appears in answers | Start a new conversation and inspect instruction fields |
| Model already behaves well at baseline | Record that result; test missing evidence and edge cases instead of forcing failure |
| Answer has clause IDs but wrong conclusion | Compare the claim with the actual clause; citation alone is not correctness |
| V5 is worse | Keep the failed experiment and select an earlier candidate |
| Module not found | Install with the selected .venv Python interpreter |
| Missing .env settings | Check .env is in the extracted project root |
| 401/403 | Verify resource key and authorised access; do not show the key |
| 404 | Verify inference URL, actual deployment name and Responses API availability |
| 429 or timeout | Reduce repeats and follow the service retry interval; retain failure records |
| Empty/incomplete API answer | Check status and incomplete_details; do not score it as success |

Do not ask GPT-5 to expose hidden chain-of-thought. Ask for a concise explanation tied to supplied clauses. Separate instruction quality, factual evidence and real business authority.

## 11. What to submit before the session closes

Use the submission location announced by Nived; no location is assumed here.

- Your completed findings worksheet, containing exact prompts and actual responses.
- V0–V5 prompt files and the selected prompt, with five documented changes.
- Three zero-shot and three few-shot routing results.
- Three held-out assessment responses and manual scores.
- One peer review and a short reflection on remaining application responsibilities.
- For the extension only: Python experiment logs and completed scores.csv.

Exclude .env, API keys and .venv from your submission. No fabricated output or prefilled score is required. A documented failure and a justified decision to revert are valid engineering results.

## 12. Technical references and course alignment

The supplied NIIT course outline, Phase 2 Module 1, specifies five documented prompt improvements, prompt comparison, few-shot examples and unseen-input testing. This assignment uses the enterprise scenario agreed for the programme and the four service rules from Day 2 slides 38–41.

- [Microsoft Learn — System message design](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/advanced-prompt-engineering): instruction scope, fallback behaviour and the need to test compliance.
- [Microsoft Learn — Reasoning models](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/reasoning): model-specific parameters and reasoning usage.
- [Microsoft Learn — Responses API](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses): API client and response handling.
- [Microsoft Learn — Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering): terminology; reasoning-model guidance takes precedence for GPT-5.

The company, documents, routing labels, rubric and expected business behaviours are trainer-authored synthetic materials, not Microsoft or T-Systems policies.

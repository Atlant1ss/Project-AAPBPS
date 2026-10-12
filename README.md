# NexoTech Solutions: Ticket Routing System

A beginner-level Python program that sends each IT support ticket to the right team and sets its resolution deadline.

| | |
|---|---|
| **Course** | AI-Assisted Python for Business Problem Solving (PSI163), PUCPR, 2026/2 |
| **Professor** | Evandro Alberto Zatti |
| **Delivery** | RA1 (first delivery): study topics ST1 and ST2 |
| **Language** | Python 3, standard language features only (nothing to install) |

### Assessment map (Summative Assessment, LO 1)

Where to find the evidence for each item of the rubric "Evaluation Project - LO 1":

| Item | Criterion | Evidence |
|---|---|---|
| **1.1** | Business context, problem and purpose | [`docs/PROBLEM_ANALYSIS.md`](docs/PROBLEM_ANALYSIS.md) §0 (0.1 Business Context, 0.2 Problem, 0.3 Purpose) |
| **1.2** | IPO model and business rules | [`docs/PROBLEM_ANALYSIS.md`](docs/PROBLEM_ANALYSIS.md) §2 (IPO table, input and output fields with data types and units) and §4 (BR0 to BR4) |
| **1.3** | Python implementation of the calculation | [`main.py`](main.py) (`read_manual_ticket()` with `input()`, formatted output with f-strings), [`validations.py`](validations.py) (`ask_yes_or_no()`), [`calculations.py`](calculations.py) (`calculate_percentage()`, `get_next_ticket_id()`, `route_ticket()`); how to run it in §5 below |
| **1.4** | Documented AI interaction (ST1) | [`docs/AI_INTERACTION_LOG.md`](docs/AI_INTERACTION_LOG.md) Entries **008** (problem analysis), **010** (first version of the code), **019** (assessment brief, Option A or B) and **020** (keyboard input); context in Entries 001 to 003, 006 and 007 |
| **2.1** | Decision-based business rule | [`docs/PROBLEM_ANALYSIS.md`](docs/PROBLEM_ANALYSIS.md) §4 (BR1 to BR4 and the status rule, including General vs. unknown category and missing values) and §5 (pseudocode) |
| **2.2** | Implementation with `if`, `elif`, `else` | [`calculations.py`](calculations.py): `get_queue()`, `get_deadline_hours()`, `route_ticket()`; [`main.py`](main.py): `format_deadline()` |
| **2.3** | Test design, execution and reporting | [`docs/TEST_CASES.md`](docs/TEST_CASES.md) §3 (test tables with input, expected result, actual result and passed), §5 (summary check) and §9 (execution record) |
| **2.4** | Documented AI interaction (ST2) | [`docs/AI_INTERACTION_LOG.md`](docs/AI_INTERACTION_LOG.md) Entries **009** (test design), **013** and **014** (debugging cycle and its corrections), **015** and **016** (refactoring cycle and its application); test execution in Entry 021 |

---

## 1. Overview

**NexoTech Solutions** is a **fictional** IT support company created for this project. Its help desk receives support tickets and passes each one to one of four teams, called queues:

| Queue | Handles |
|---|---|
| **L1 Helpdesk** | Access problems and software issues |
| **L2 Field Team** | Infrastructure and hardware problems |
| **Admin** | Finance-related requests |
| **Triage** | General requests, and any ticket that needs a person to review it |

All the tickets in this repository are synthetic. No real people, companies or records are used.

---

## 2. The problem

Without automation, someone has to read every new ticket just to decide which team should handle it and how fast it must be solved. This first triage step is slow and inconsistent: tickets wait unassigned, some reach the wrong team, and urgent tickets are not clearly separated from routine ones.

This program automates that step. It can also read one new ticket typed at the keyboard. For each ticket, it:

1. **cleans** the category and priority, so capitalization and extra spaces do not matter;
2. **routes** the ticket to a queue based on its category;
3. **sets a resolution deadline** based on its priority;
4. marks the ticket **"Needs review"** when its category or priority is not recognized;
5. prints the result, and at the end a **summary** of how many tickets went to each queue.

### Business rules

| Rule | What it does |
|---|---|
| **BR0: Input cleaning** | Category and priority are converted to lowercase and surrounding spaces are removed. A missing value or missing field becomes empty text. "ACCESS", "access" and " Access " are the same category. |
| **BR1: Routing** | Access, Software → L1 Helpdesk · Infrastructure, Hardware → L2 Field Team · Finance → Admin · General → Triage |
| **BR2: Resolution deadline** | High → 4 hours · Medium → 24 hours · Low → 72 hours |
| **BR3: Unknown category** | Any other category → Triage, marked "Needs review". The deadline still follows BR2. |
| **BR4: Unknown priority** | Any other priority → Triage, no deadline, marked "Needs review", so a person can set the correct priority. |

The full analysis (guiding questions, input → processing → output table, step-by-step breakdown and pseudocode) is in [`docs/PROBLEM_ANALYSIS.md`](docs/PROBLEM_ANALYSIS.md).

---

## 3. Technologies and concepts

- **Python 3**, written in Visual Studio Code as `.py` files.
- **No external libraries**: the program uses only core Python, so there is nothing to install.

| Concept | Where it is used |
|---|---|
| Variables and data types (`str`, `int`, `float`, `bool`) | Ticket fields (text), deadline hours and ticket IDs (`int`), percentages (`float`), `is_missing()` and `ask_yes_or_no()` (`bool`) |
| **Keyboard input** with `input()` | `ask_yes_or_no()` and `read_manual_ticket()`: the user can type one new ticket |
| **Dictionaries** | Each ticket; the result of `route_ticket()`; the counter for each queue |
| **List** and **list of dictionaries** | `tickets` in `sample_tickets.py`; the list of ticket IDs that need review |
| Tuple | `QUEUES`: the four queues in a fixed order |
| **Conditionals** (`if` / `elif` / `else`) with `or` and `and` | `get_queue()`, `get_deadline_hours()`, `route_ticket()`, `format_deadline()` |
| Loops and counters | The `for` loop over the tickets in `main()`; the queue counters and the total counter; the `while` loop that asks again until the answer is yes or no |
| Functions with parameters and return values | 16 functions, each with one responsibility |
| Modules and imports | Four `.py` files connected with `from ... import ...` |
| Formatted output (f-strings) | All output, with percentages to one decimal place |
| AI-assisted development | Every prompt, response and decision recorded in [`docs/AI_INTERACTION_LOG.md`](docs/AI_INTERACTION_LOG.md) |

---

## 4. Project structure

```
Project-AAPBPS/
├── main.py               # Runs the program: reads an optional ticket from the keyboard, routes each ticket, prints the results and the summary
├── calculations.py       # Business rules: queue, deadline, status (BR1 to BR4), percentages and the next ticket ID
├── validations.py        # Input cleaning (BR0) and the yes/no check for keyboard input
├── sample_tickets.py     # The 15 synthetic tickets, as a list of dictionaries
├── docs/
│   ├── PROBLEM_ANALYSIS.md     # Problem analysis and pseudocode
│   ├── TEST_CASES.md           # Test tables for every rule and function
│   └── AI_INTERACTION_LOG.md   # Record of every AI prompt and decision
├── .gitignore
├── LICENSE
└── README.md
```

---

## 5. How to run the project

You need **Python 3.6 or newer**. No other installation is required.

**Step 1: Check that Python is installed.** Open a terminal (Command Prompt on Windows) and run:

```
python --version
```

On Windows, if that command is not found, try `py --version`. If neither works, install Python from [python.org](https://www.python.org/downloads/) and tick **"Add python.exe to PATH"** during the installation.

**Step 2: Get the code.** Clone the repository and go into its folder:

```
git clone https://github.com/jvquadros/Project-AAPBPS.git
cd Project-AAPBPS
```

Without Git, open the repository page on GitHub, click **Code → Download ZIP**, extract it, and open a terminal inside the extracted folder.

**Step 3: Run the program.**

```
python main.py
```

On Windows you can also use `py main.py`; on macOS and Linux, use `python3 main.py`.

**Step 4: Answer the question.** The program first asks:

```
Add a ticket manually? (yes/no):
```

- Type `no` to process only the 15 sample tickets.
- Type `yes` to add your own ticket. The program then asks for its description, category and priority, gives it the next free ID (1016), and routes it together with the sample tickets:

```
New ticket 1016
Description: Password expired on laptop
Category (Access, Software, Infrastructure, Hardware, Finance, General): access
Priority (High, Medium, Low): HIGH
```

Any answer other than yes or no is asked again. Capitalization does not matter.

**Step 5: Read the output.** The program prints one block per ticket, like this:

```
--------------------------------------------------
Ticket 1001: Cannot log in to the VPN
  Category: Access  |  Priority: High
  Queue:    L1 Helpdesk
  Deadline: 4 hours
  Status:   Routed
```

and ends with this summary (the result of answering `no`):

```
==================================================
END-OF-RUN SUMMARY
==================================================
L1 Helpdesk: 4 ticket(s) (26.7%)
L2 Field Team: 3 ticket(s) (20.0%)
Admin: 2 ticket(s) (13.3%)
Triage: 6 ticket(s) (40.0%)
--------------------------------------------------
Total processed: 15
Needs review: 5 ticket(s) [1011, 1012, 1013, 1014, 1015]
```

**Step 6 (optional): Change the sample tickets.** Edit `sample_tickets.py`: add or change a dictionary, keeping the keys `ticket_id`, `description`, `category` and `priority`. Then run `python main.py` again.

---

## 6. Running the tests

[`docs/TEST_CASES.md`](docs/TEST_CASES.md) contains 26 routing tests, 33 tests for the individual functions, 5 keyboard-input tests, and a check of the end-of-run summary. To run a test, start Python in the project folder and call the function with the test's input:

```
python
>>> from calculations import route_ticket
>>> route_ticket("Software", "HIGH")
{'queue': 'L1 Helpdesk', 'deadline_hours': 4, 'status': 'Routed'}
```

All the tests have already been run once and their actual results are recorded in the tables (see §9 of `TEST_CASES.md`). To check a result yourself, run the test again and compare it with the **Actual Result** column.

---

## 7. Documentation

| Document | Contents |
|---|---|
| [`docs/PROBLEM_ANALYSIS.md`](docs/PROBLEM_ANALYSIS.md) | Guiding questions, IPO table, decomposition, business rules and pseudocode |
| [`docs/TEST_CASES.md`](docs/TEST_CASES.md) | Test tables for every business rule and function, with expected and actual results, and the test execution record |
| [`docs/AI_INTERACTION_LOG.md`](docs/AI_INTERACTION_LOG.md) | Every prompt sent to the AI, the relevant response, what the team accepted or rejected and why, including the debugging and refactoring cycles |

---

## 8. Scope of this delivery

This first delivery covers study topics **ST1** (computational thinking, Python basics, AI-assisted development) and **ST2** (data structures, control flow, functions and modularization). The tickets are a hard-coded list of dictionaries, as in the course examples. The program does not use files, databases or external services.

---

## 9. Team

- João Vitor da Silva de Quadros
- _[add the other team members here]_

## 10. License

MIT License. See [`LICENSE`](LICENSE).

---

*During the preparation of this README, the author(s) used Claude (Anthropic, model claude-opus-5) to draft the project overview, the business rules summary, the concepts table and the step-by-step run instructions from the team's code and documents, to update them for the keyboard input, and to write the assessment map. After using this tool, the author(s) reviewed and edited the content as needed and take full responsibility for the content.*

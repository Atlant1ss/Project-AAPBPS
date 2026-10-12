# Problem Analysis: NexoTech Solutions Ticket Routing

| Field | Value |
|---|---|
| Project | Ticket routing system for NexoTech Solutions |
| Course | AI-Assisted Python for Business Problem Solving (PSI163), PUCPR, 2026/2 |
| Indicator | ID1.1: analyze an organizational problem, identify inputs, processing and outputs, and decompose it into logical steps (Summative items 1.1, 1.2, 2.1) |
| Version | 1.6, 2026-10-12 (v1.0 approved by the team; v1.1 adds BR0; v1.2 marks unknown categories for review; v1.3 notes where the sample tickets live; v1.4 adds keyboard input; v1.5 adds the business context, problem and purpose; v1.6 adds the summary calculation to the model; see section 7) |

---

## 0. Business Context, Problem and Purpose

This section answers Summative Assessment item 1.1: the business context, the problem and the purpose of the solution.

### 0.1 Business Context

**NexoTech Solutions** is a fictional IT support company invented for this course. All tickets used in this project are synthetic. No real people, companies or records are involved.

NexoTech's help desk receives support tickets from the employees of its client companies. Each ticket describes one problem (for example, a user who cannot log in, a broken printer or a billing question) and must be passed to one of four teams (queues):

| Queue | Handles |
|---|---|
| **L1 Helpdesk** | First-level support: access problems and software issues |
| **L2 Field Team** | Second-level technicians: infrastructure and hardware problems |
| **Admin** | Finance-related requests |
| **Triage** | General requests and any ticket that needs a person to review it |

### 0.2 Problem

Today a person has to read every new ticket just to decide which team should handle it and how fast it must be solved. This first step is slow and inconsistent: tickets wait unassigned, some reach the wrong team, urgent tickets are not clearly separated from routine ones, and nobody can see at a glance how the work is spread across the teams.

The problem to solve is: **process every ticket to find its queue, its resolution deadline in hours and its status ("Routed" or "Needs review"), and then calculate how many tickets went to each queue and what percentage of the total that represents.**

### 0.3 Purpose

The results support concrete decisions at NexoTech:

| Result | Who uses it | Decision it supports |
|---|---|---|
| **Queue** of each ticket | Each team | The team receives only its own tickets, immediately, without waiting for someone to sort them. |
| **Deadline in hours** | Each team | Sets the order of work: a 4-hour ticket is handled before a 72-hour ticket. |
| **"Needs review" list** | The triage person | Shows exactly which tickets have a category or priority that must be corrected by a person. |
| **Count and percentage per queue** | The support manager | Shows the workload of each team, to decide how to distribute staff (for example, moving a technician to the team with the largest share). |

---

## 1. Guiding questions

| # | Question | Answer |
|---|---|---|
| 1 | **What problem are we trying to solve?** | Today someone has to read every ticket just to decide which team should handle it and how fast it must be solved. This is slow and inconsistent: tickets wait unassigned, some reach the wrong team, and urgent tickets are not clearly separated from routine ones. The system must **send each ticket to the correct queue and assign it a resolution deadline automatically**, following fixed business rules. |
| 2 | **What information is available? What is missing?** | *Available:* each ticket has an ID, a description, a **category** (Infrastructure, Finance, Access, Software, Hardware, General) and a **priority** (High, Medium, Low). *Missing in this phase:* the exact time the ticket was opened (so the deadline is given in hours, not as a date and time); how busy each team is; any check that the requester chose the right category. |
| 3 | **What rules must be respected?** | The input cleaning rule (capitalization and extra spaces are ignored), the routing rule (category → queue), the resolution deadline rule (priority → hours), and the two validation rules for categories and priorities that are not recognized. See section 4. |
| 4 | **What should the solution produce?** | For each ticket: its **queue**, its **resolution deadline in hours** and its **status** ("Routed" or "Needs review"). After all tickets are processed: a **summary** with the number of tickets in each queue, **each queue's share of the total as a percentage**, the total number of tickets processed, and the tickets that need review. |

---

## 2. Input → Processing → Output

| Input | Processing | Output |
|---|---|---|
| A list of support tickets, plus (optionally) **one ticket typed by the user** with `input()`. Each ticket has: **ticket ID**, **description**, **category**, **priority** | 1. Read the ticket's fields.<br>2. Clean the category and priority: lowercase, no surrounding spaces (BR0).<br>3. Find the queue from the category. An unrecognized category goes to Triage and is marked for review (BR1, BR3).<br>4. Find the resolution deadline from the priority (BR2).<br>5. If the priority is not recognized, send the ticket to Triage with no deadline and mark it for review (BR4).<br>6. Count the ticket in its queue and in the total; record its ID if it needs review.<br>7. After the last ticket, calculate each queue's **share of the total**: count ÷ total × 100 (section 2.4). | For each ticket: **queue**, **deadline (hours)**, **status**.<br>At the end: a **summary** with, for each queue, the **number of tickets** and its **share of the total (%, one decimal place)**; the **total processed**; and the **number and IDs of the tickets needing review**. |

### 2.1 Input fields

| Field | Data type | Example | Used for |
|---|---|---|---|
| `ticket_id` | integer | `1001` | Identifying the ticket in the output |
| `description` | text | `"Cannot log in to the VPN"` | Shown in the output. Not used by the rules in this phase |
| `category` | text | `"Access"`, `"access"` or `"ACCESS"` (any capitalization) | Routing (BR0, BR1, BR3) |
| `priority` | text | `"High"`, `"high"` or `"HIGH"` (any capitalization) | Resolution deadline (BR0, BR2, BR4) |
| Answer to "Add a ticket manually? (yes/no)" | text, typed with `input()` | `"yes"`, `"no"` (any capitalization) | Decides whether one ticket is read from the keyboard; any other answer is asked again |

The description, category and priority of a manual ticket are typed with `input()` and kept as text. Its ticket ID is calculated, not typed: one more than the highest ID already in the list.

### 2.2 Output fields for each ticket

| Field | Data type | Unit / format | Example |
|---|---|---|---|
| `queue` | text | one of the four queue names | `"L1 Helpdesk"` |
| `deadline_hours` | integer | hours from the moment the ticket is opened | `4` (0 means no deadline has been set) |
| `status` | text | `"Routed"` or `"Needs review"` | `"Routed"` |

### 2.3 Output fields of the end-of-run summary

| Field | Data type | Unit / format | Example (the 15 sample tickets) |
|---|---|---|---|
| `queue_counts` | dictionary: queue name → integer | tickets per queue | `{"L1 Helpdesk": 4, "L2 Field Team": 3, "Admin": 2, "Triage": 6}` |
| `share` | float | percent of the total, shown with one decimal place | `26.7` for L1 Helpdesk (4 of 15) |
| `total_tickets` | integer | tickets | `15` |
| `needs_review_ids` | list of integers | ticket IDs | `[1011, 1012, 1013, 1014, 1015]` |

### 2.4 Calculations

| Calculation | Formula | Rule at the boundary |
|---|---|---|
| Share of a queue | `share = count ÷ total_tickets × 100` | When `total_tickets` is 0 the share is `0.0`, so there is never a division by zero; the summary then shows "No tickets were processed." |
| Display of the share | One decimal place (`:.1f`) | Python rounds an exact half to the even digit: 5 of 16 = 31.25 is shown as **31.2**, 3 of 16 = 18.75 as **18.8**. Each share is rounded on its own, so the four displayed shares can add up to 99.9% or 100.1% (for example 25.0 + 18.8 + 12.5 + 43.8 = 100.1 with 16 tickets) |
| Total processed | `total_tickets = total_tickets + 1` for each ticket | Equals the number of tickets in the list |
| ID of a typed ticket | `ticket_id = highest ticket ID in the list + 1` | `1` when the list is empty; tickets without an ID are skipped |

---

## 3. Step-by-step logical breakdown

### 3.1 Decomposition

1. Load the list of tickets to process. Ask the user "Add a ticket manually? (yes/no)"; any other answer is asked again. On **yes**, read the description, category and priority from the keyboard, give the ticket the next free ID (highest ID + 1) and add it to the list.
2. Take the next ticket and read its ID, description, category and priority.
3. **Clean** the category and priority: convert them to lowercase, remove surrounding spaces, and turn a missing value into empty text (BR0).
4. Decide the **queue** from the category (BR1). An unrecognized category goes to **Triage** and is marked **"Needs review"** (BR3).
5. Decide the **resolution deadline** from the priority (BR2).
6. If the priority is not recognized, send the ticket to **Triage**, set **no deadline**, and mark it **"Needs review"** (BR4). If neither BR3 nor BR4 applies, mark it **"Routed"**.
7. Display the result for this ticket: ID, category, priority, queue, deadline, status.
8. Add 1 to the count for the ticket's queue and to the total. If the ticket needs review, also record its ID in the "needs review" list.
9. Repeat steps 2 to 8 until every ticket has been processed.
10. Calculate each queue's share of the total (count ÷ total × 100, section 2.4) and display the summary: tickets and share per queue, total processed, and the tickets needing review.

### 3.2 Computational thinking applied

| Element | How it applies to NexoTech |
|---|---|
| **Decomposition** | The problem splits into input cleaning, two independent decisions (**routing** and **deadline**), validation and a final summary (steps 1 to 10 above). |
| **Pattern recognition** | Every ticket goes through the same steps; only the values change. The steps are defined once and repeated for each ticket. Categories that share a queue are grouped (Access + Software, Infrastructure + Hardware). |
| **Abstraction** | Kept: ticket ID, category, priority, and the description (for display only). Ignored: the requester's name and contact details, device model, location, time of day. They are not needed to route a ticket, and leaving them out also avoids handling personal data. |
| **Algorithm design** | The finite, ordered sequence of steps in section 3.1, written as pseudocode in section 5. |

---

## 4. Business rules

### BR0: Input cleaning (applied first)

Before any other rule runs, the category and priority are converted to **lowercase** and **surrounding spaces are removed**. A missing value, or a field that is absent from the ticket, becomes empty text. This means "Access", "access", "ACCESS" and " Access " are all the same category, and every rule below compares the cleaned values.

### BR1: Routing by category

A ticket is sent to a queue according to its category.

| Category | Queue |
|---|---|
| Access | L1 Helpdesk |
| Software | L1 Helpdesk |
| Infrastructure | L2 Field Team |
| Hardware | L2 Field Team |
| Finance | Admin |
| General | Triage |

### BR2: Resolution deadline by priority

A ticket must be resolved within a number of hours that depends on its priority.

| Priority | Resolution deadline |
|---|---|
| High | 4 hours |
| Medium | 24 hours |
| Low | 72 hours |

### BR3: Unrecognized category

If a ticket's category, after cleaning, is not one of the six listed in BR1 (including a missing category), it is sent to **Triage** and marked **"Needs review"**, because a person must decide where it belongs. Its deadline still follows BR2. A ticket whose category is General also goes to Triage, but it is marked "Routed", because General is a recognized category.

### BR4: Unrecognized priority

If a ticket's priority, after cleaning, is not High, Medium or Low (including a missing priority), the ticket gets **no deadline** (0 hours), is sent to **Triage**, and is marked **"Needs review"** so that a person can set the correct priority. It does **not** get a default deadline, because a wrong default (for example, 72 hours on an urgent ticket) could delay a critical problem.

### Status

A ticket caught by BR3 (unrecognized category) or BR4 (unrecognized priority) is marked **"Needs review"**. Every other ticket is marked **"Routed"**.

---

## 5. Pseudocode

The program is described by three short algorithms: the optional keyboard ticket (5.1), the processing of **one ticket** (5.2) and the end-of-run summary (5.3). They use only the keywords START, READ, CALCULATE, DISPLAY and END, plus IF / ELIF / ELSE / END IF for the decisions.

### 5.1 Optional keyboard ticket

```
START
    READ answer
    IF answer is "yes"
        CALCULATE ticket_id = highest ticket_id in the list + 1
        READ description
        READ category
        READ priority
        CALCULATE tickets = tickets with the new ticket added at the end
    END IF
END
```

### 5.2 One ticket

```
START
    READ ticket_id
    READ description
    READ category
    READ priority

    CALCULATE clean_category = category in lowercase, without surrounding spaces
    CALCULATE clean_priority = priority in lowercase, without surrounding spaces
    CALCULATE status = "Routed"

    IF clean_category is "access" OR clean_category is "software"
        CALCULATE queue = "L1 Helpdesk"
    ELIF clean_category is "infrastructure" OR clean_category is "hardware"
        CALCULATE queue = "L2 Field Team"
    ELIF clean_category is "finance"
        CALCULATE queue = "Admin"
    ELIF clean_category is "general"
        CALCULATE queue = "Triage"
    ELSE
        CALCULATE queue = "Triage"
        CALCULATE status = "Needs review"
    END IF

    IF clean_priority is "high"
        CALCULATE deadline_hours = 4
    ELIF clean_priority is "medium"
        CALCULATE deadline_hours = 24
    ELIF clean_priority is "low"
        CALCULATE deadline_hours = 72
    ELSE
        CALCULATE deadline_hours = 0
        CALCULATE queue = "Triage"
        CALCULATE status = "Needs review"
    END IF

    DISPLAY ticket_id
    DISPLAY category
    DISPLAY priority
    DISPLAY queue
    DISPLAY deadline_hours
    DISPLAY status
END
```

### 5.3 End-of-run summary

```
START
    READ queue_counts
    READ total_tickets
    READ needs_review_ids

    IF total_tickets is 0
        DISPLAY "No tickets were processed."
    ELSE
        CALCULATE share_l1 = count of "L1 Helpdesk" / total_tickets * 100
        CALCULATE share_l2 = count of "L2 Field Team" / total_tickets * 100
        CALCULATE share_admin = count of "Admin" / total_tickets * 100
        CALCULATE share_triage = count of "Triage" / total_tickets * 100
        DISPLAY each queue with its count and its share, to one decimal place
        DISPLAY total_tickets
        DISPLAY needs_review_ids
    END IF
END
```

**Notes on the pseudocode**

- **Cleaning (BR0).** The two cleaning steps run before any decision, so every comparison uses lowercase values. The original values are kept for display.
- **Routing decision (BR1, BR3).** Five paths. "General" goes to Triage as a normal ticket. The final ELSE covers any unrecognized or missing category: it sends the ticket to Triage and marks it for review, so every ticket always gets a queue. In the code, `get_queue()` returns Triage in its final `else` for both General and unrecognized categories, and `route_ticket()` then tells them apart when it sets the status; the result for every input is the same as in this pseudocode (TC12 to TC14 and TC27 stay "Routed", TC19 to TC21, TC28 and TC29 are "Needs review").
- **Deadline decision (BR2, BR4).** Four paths. The final ELSE handles an unrecognized priority. It overrides the queue with "Triage" and marks the ticket for review, so BR4 is applied in one single place.
- **Repetition.** Block 5.2 runs once for each ticket in the list (steps 2 to 9 of section 3.1). The counts per queue and the final summary (steps 8 and 10) sit around this block. In Python they become a `for` loop with counters, which is ST2 content.
- **Keyboard ticket (5.1).** Its ID is calculated, not read. An answer other than "yes" or "no" is asked again; in the code this is a `while` loop in `ask_yes_or_no()` (no loop keyword is used here, as in 5.2). The typed ticket then goes through 5.2 like every other ticket.
- **Summary (5.3).** The four shares are the calculation of section 2.4; in the code they come from `calculate_percentage()`.
- **Decision values.** Each branch of both decisions is tested with at least three different input values in `docs/TEST_CASES.md` (TC01 to TC30).

---

## 6. Assumptions

1. The **category** comes with the ticket; the requester chooses it when opening the ticket. In this phase the system does not check the category against the description text.
2. Deadlines are **counted in hours from the moment the ticket is opened**. Turning them into an exact due date and time is outside this phase.
3. The tickets processed in this phase are a **small synthetic sample**: a list of dictionaries defined in `sample_tickets.py` and processed by `main.py`, plus, optionally, one ticket typed at the keyboard. There is no database or external data source.

---

## 7. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-09-29 | First version. Approved by the team, including BR3, BR4, the status field, the end-of-run summary and the single-ticket pseudocode. |
| 1.1 | 2026-09-29 | Added BR0 (input cleaning): capitalization and surrounding spaces are ignored. Pseudocode, IPO table and decomposition updated to match. Team decision. |
| 1.2 | 2026-09-29 | BR3 now marks an unrecognized category "Needs review"; BR0 also covers a field that is absent from the ticket. Pseudocode, decomposition and status rule updated. Team decisions from the AI debugging cycle (AI log Entry 013). |
| 1.3 | 2026-09-29 | Assumption 3 updated: the sample tickets now live in `sample_tickets.py` (AI refactoring cycle, AI log Entry 015). No business rule changed. |
| 1.4 | 2026-10-12 | Keyboard input added to meet the Summative Assessment requirement 1.3 (`input()`): the user may type one ticket, and the yes/no answer is validated. IPO table, input fields, decomposition step 1, pseudocode notes and assumption 3 updated. No business rule changed. Team decision (Option A, AI log Entry 020). |
| 1.5 | 2026-10-12 | Section 0 rewritten as "Business Context, Problem and Purpose" to answer Summative Assessment item 1.1: business context (0.1), problem statement (0.2) and the decisions the results support (0.3). No business rule changed. Requested by the team (AI log Entry 021). |
| 1.6 | 2026-10-12 | The end-of-run summary calculation is now part of the model: guiding question 4, the IPO table, the new sections 2.3 (summary output fields with units and formats) and 2.4 (calculations, including the rounding rule and the division-by-zero boundary), decomposition steps 8 and 10, and two new pseudocode blocks (5.1 keyboard ticket, 5.3 summary). Note added on how `get_queue()` handles General. No business rule changed. Team decision after the mock grading (AI log Entries 023 and 024). |

---

*During the preparation of this document, the author(s) used Claude (Anthropic, model claude-opus-5) to structure the problem analysis (guiding questions, IPO table, decomposition, business rules and pseudocode) from the business rules defined by the team, to propose the handling of unrecognized categories and priorities (BR3, BR4), to write the input cleaning rule (BR0) requested by the team, to apply the rule changes the team accepted in the AI debugging cycle, to describe the keyboard input added for the Summative Assessment, to write the business context, problem and purpose section (section 0), and to add the summary calculation to the model (sections 2.3, 2.4 and 5). After using this tool, the author(s) reviewed and edited the content as needed and take full responsibility for the content.*

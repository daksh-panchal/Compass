# 🧭 Compass
Compass is a multi-agent virtual support system that helps with defining priorities, scheduling tasks, and acting with intention. Designed primarily for students with a high cognitive load, Compass uses multi-agent orchestration to guide people when everything feels too important. It analyzes course status, deadlines, cognitive load, and risk factors to generate prioritized study plans and explain why those recommendations were made. The system is intentionally modular and transparent, emphasizing reasoning over generic outputs.

Built with:
- **Python** for development.
- **LangGraph** for multi-agent orchestration.
- **OpenAI GPT-4o** for natural language responses.

---

## ✨ Core Capabilities

- Ingests live academic data from Notion
- Evaluates course risk and urgency
- Prioritizes courses based on multiple competing factors
- Allocates realistic study time under user constraints
- Produces human-readable explanations for its decisions
- Orchestrates reasoning using LangGraph

---

## 🧠 System Architecture

Compass is built as a **multi-agent reasoning system**, where each agent is responsible for a single, well-defined concern.  
Agents update a shared state that flows through the system.

### High-level flow:

1. Course data is loaded
2. Course status is assessed
3. Deadlines are evaluated
4. Tasks are prioritized
5. Time is allocated
6. Decisions are explained using an LLM

---

## 🧩 Agents Overview

### Course Status Agent
Evaluates how “at risk” a course is based on:
- Days since it was last worked on
- Recovery cost (how hard it is to catch up on)
- Cognitive load (total amount of mental effort needed to process information)
- Current standing (how the user is progressing in the course)

Outputs:
- `risk_score`
- `days_idle`

---

### Deadline Agent
Assesses upcoming deadlines and categorizes urgency.

Urgency levels:
- Critical
- High
- Medium
- Low
- None

Outputs:
- `deadline_urgency`
- `days_until_deadline`

---

### Planning Agent
Combines risk scores and deadline urgency to compute a **priority score** for each course.

Design principles:
- Deadlines outweigh risk when present
- Risk still matters when no deadlines exist
- Cognitive load slightly discourages overloading

Outputs:
- Sorted course priorities

---

### Scheduling Agent
Allocates study time in fixed blocks under real constraints.

Considers:
- Available time
- Deadline urgency
- Risk score
- Cognitive load (burnout protection)

Outputs:
- A concrete study schedule (minutes per course)

---

### Explanation Agent
Uses an LLM to translate system decisions into clear, human-readable reasoning.

Responsibilities:
- Explain *why* certain courses are prioritized
- Connect outputs back to inputs (risk, deadlines, load)
- Maintain transparency and trust

---

## 🧭 Orchestration with LangGraph

Compass uses **LangGraph** to orchestrate agent execution.

Each node:
- Receives the shared state
- Performs a focused transformation
- Passes the updated state forward

This provides:
- Deterministic execution
- Clear data flow
- Easy extensibility
- Debuggable reasoning paths

---

## 🔑 Design Philosophy

- **Reasoning First, Generation Second**  
  All core decisions (risk, priority, scheduling) are made deterministically using explicit logic.  
  The LLM is used only to *explain* decisions, never to make them.

- **Transparency Over Optimization**  
  Every recommendation can be traced back to concrete inputs such as deadlines, risk scores, and cognitive load.  
  There are no hidden heuristics or opaque scoring mechanisms.

- **Single-Responsibility Agents**  
  Each agent performs one clearly defined task and mutates shared state in a predictable way.  
  This keeps the system debuggable, testable, and extensible.

- **State as the Source of Truth**  
  All agents operate on a shared, explicit state object.  
  This makes execution order, dependencies, and outcomes easy to inspect.

- **Human Constraints Matter**  
  Scheduling decisions account for cognitive load and burnout risk, not just urgency.  
  The system is designed to recommend *sustainable* study plans, not maximal ones.

- **Composable by Design**  
  Agents can be reordered, replaced, or extended without rewriting the system, enabling future features such as long-term planning or energy-aware scheduling.

---

## 🚀 Ideas for Future Expansion

- Historical performance tracking
- Multi-day planning
- Personal energy modeling
- Long-term academic goal alignment

---

## Status

This project currently focuses on:
- Backend deterministic logic
- Multi-agent workflow
- Decision transparency

---

## 📜 License

MIT License
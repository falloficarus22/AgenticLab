This repo will be for the scientific implementation of maths, physics and ML research theoretical or experimental implementations

The core idea will be like:
Hypothesis → Plan → Execute → Analyze → Critique → Iterate

# 🧪 MASL — Multi-Agent Science Lab

**MASL** is a framework for building **autonomous, multi-agent scientific workflows** that follow the *actual scientific method*:

> **Hypothesis → Experiment → Analysis → Critique → Iteration**

Unlike typical “AI agent” systems, MASL is designed to:
- run **real experiments** (symbolic math, physics simulations, ML training)
- enforce **falsification and termination**
- separate **reasoning from execution**
- remain **reproducible and inspectable**

MASL is not a chatbot.  
It is a **scientific instrument**.

---

## ✨ Key Features

- 🧠 **Role-specialized agents**
  - Hypothesis Generator
  - Experimental Planner
  - Executor (tool-only, no reasoning)
  - Analyzer (domain-aware)
  - Critic / Peer Reviewer

- 🔌 **Pluggable tool system**
  - Symbolic mathematics (SymPy)
  - Numerical physics simulators
  - ML training pipelines
  - External APIs (optional)

- 🔁 **Critic-driven iteration**
  - Experiments stop when falsified
  - Methodological flaws are detected automatically

- 📜 **Full experiment ledger**
  - Prompts, plans, tool calls, results, critiques
  - Every run is reproducible

- 🧪 **Multi-domain by design**
  - Mathematics
  - Physics
  - Machine Learning
  - Same engine, different tools

---

## 🧠 Design Philosophy

MASL is built on five non-negotiable principles:

1. **Falsification over fluency**
   - If a hypothesis cannot fail, it is rejected.

2. **Execution ≠ Reasoning**
   - LLMs never execute experiments.
   - Tools never reason.

3. **Deterministic science**
   - Numerical checks beat textual explanations.

4. **Critique controls progress**
   - The critic decides when to stop or iterate.

5. **No agent theatre**
   - Every agent must justify its existence.

---

## 🧩 System Architecture


# 🐍 Python to FastAPI & Production SRE

A hands-on, production-grade learning journey designed from a **Senior SRE (Site Reliability Engineering)** perspective. This repository transitions from core Python fundamentals to scalable FastAPI microservices, containerization, observability, and cloud deployments.

---

## 📌 Repository Structure

```plaintext
python-production/
├── 1_basics/
│   ├── main.py              # Variables, Types, Type Casting & String Formatting
│   ├── control_flow.py      # if/elif/else, for/while loops, break & continue
│   ├── functions_basics.py  # def, default args, *args & **kwargs patterns
│   └── calculator_quiz.py   # Practice Milestone: Interactive CLI Calculator & Quiz Tool
├── 2_intermediate/
│   └── data_structures.py   # Lists, Tuples, Sets, Dicts & Comprehensions
├── .gitignore               # Standard Python & environment exclusions
├── ROADMAP.md               # Detailed phase-by-phase curriculum & milestones
└── README.md                # Project documentation & execution guide
```

---

## 🚀 Quickstart & Setup

### 1. Prerequisites

- **Python:** 3.12+ (Recommended 3.14+)
- **Git**

### 2. Virtual Environment Setup

Clone the repository and initialize the Python virtual environment:

```bash
# Clone repository
git clone https://github.com/awoladhossain/Python_Learn.git
cd python-production

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# Linux/macOS:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate
```

---

## 🏃‍♂️ Running Examples

### Phase 0: Fundamentals & Control Flow

1. **Variables & Dynamic Typing:**
   ```bash
   python3 1_basics/main.py
   ```

2. **Control Flow (Conditionals & Loops):**
   ```bash
   python3 1_basics/control_flow.py
   ```

3. **Functions Basics (`*args`, `**kwargs`, Type Hints):**
   ```bash
   python3 1_basics/functions_basics.py
   ```

4. **Practice Milestone (CLI Calculator & Quiz Tool):**
   ```bash
   python3 1_basics/calculator_quiz.py
   ```

### Phase 1: Intermediate Python & Data Structures

1. **Data Structures & Comprehensions:**
   ```bash
   python3 2_intermediate/data_structures.py
   ```

---

## 🗺️ Roadmap Overview

The detailed roadmap is tracked in [`ROADMAP.md`](./ROADMAP.md).

- **Phase 0:** Setup, Core Syntax, Control Flow, Functions
- **Phase 1:** Data Structures, Object-Oriented Programming (OOP), File I/O & Exceptions
- **Phase 2:** Typing, Pydantic, AsyncIO, Pytest
- **Phase 3:** Relational Databases, SQLAlchemy 2.0 Async, Alembic Migrations
- **Phase 4:** FastAPI Core, Dependency Injection, JWT Authentication & RBAC
- **Phase 5:** Production Projects (URL Shortener & E-commerce REST API)
- **Phase 6:** SRE, Docker, Structured Logging, Prometheus Observability & CI/CD

---

## 📝 License
This project is open-source and maintained by [Awolad Hossain](https://github.com/awoladhossain).

# AI-Powered Exploratory Testing Toolkit

Welcome!
This open-source project explores **how generative AI can support exploratory testing** of modern web applications.
By combining live browser automation with the reasoning abilities of OpenAI’s ChatGPT (and optionally [Crew AI](https://github.com/joaomdmoura/crewai)), the project aims to demonstrate a closed-loop workflow that can:

1. **Observe** a web page in real time.
2. **Reason** about potential risks or quality concerns.
3. **Generate testing charters** on-the-fly.
4. **Execute exploratory tests** in the browser.
5. **Log every interaction** and **capture defects** the moment they appear.

Our reference system-under-test is the public demo site **[automationintesting.online](https://automationintesting.online/)**, giving you a realistic playground with no signup hurdles.

---

## Project Goal

> **To provide a proof-of-concept framework that shows how large-language-model agents can autonomously plan, perform, and document exploratory testing sessions—lowering the barrier to high-quality, risk-focused testing for any web application.**

More concretely, the toolkit should:

* ⚡ **Speed up charter creation** by letting an LLM list plausible risks the moment a page is loaded.
* 🧭 **Navigate test sessions** with self-adjusting goals, allowing the AI to dig deeper where risk appears highest.
* 📝 **Produce a log** of every action, assertion, and observation, making the exploratory work repeatable and reviewable.
* 🐞 **File actionable defect reports** (steps to reproduce, screenshots, console/network traces) whenever the AI encounters an anomaly.

---

## How It Could Work (High Level)

| Phase                   | Key Components                                                                   | Outcome                                |
| ----------------------- | -------------------------------------------------------------------------------- | -------------------------------------- |
| **1. Page Discovery**   | `browser-use` opens target URL                                                   | DOM, network & visual context captured |
| **2. Risk Brainstorm**  | ChatGPT (via OpenAI API)                                                         | Ranked risk list                       |
| **3. Charter Drafting** | ChatGPT + prompt templates                                                       | Test charters with acceptance hints    |
| **4. Execution Loop**   | `browser-use` actions directed by AI agent (optionally orchestrated via Crew AI) | Real-time interaction & assertions     |
| **5. Evidence Capture** | Headless browser logs, AI commentary, screenshots                                | Full session transcript                |
| **6. Bug Reporting**    | ChatGPT summarises issue; optional GitHub/Jira webhook                           | Ready-to-triage defect tickets         |

---

## Get Involved

* **Star** this repo to follow progress.
* **Open an issue** for ideas, feedback, or bug sightings.
* **Pull requests** are welcome—especially on prompt engineering, risk heuristics, and logging/visualisation improvements.

---

## Potential Resources

* [Automation In Testing](https://automationintesting.online) – for providing the demo hotel booking site.
* [Browser-use](https://github.com/) – lightweight browser control.
* [OpenAI](https://platform.openai.com/) – ChatGPT API.
* [Crew AI](https://github.com/joaomdmoura/crewai) – multi-agent orchestration (optional).

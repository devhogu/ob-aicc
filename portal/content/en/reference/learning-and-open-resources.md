# Learning and open resources

Free, reputable places to learn AI and to follow the field, from an introductory course to the paper repositories, and the knowledge bases of AI security and incidents that a bank should know. Each entry says what it is, whom it suits, and how to use it from a bank. The cautions of the Reference overview apply to all: read freely, feed nothing of the Bank into any of them, and bring a model or a tool into the Bank only through the provider check.

## 1. Courses and structured learning

| Resource | What it is | Suits | How to take it | Access |
| --- | --- | --- | --- | --- |
| [DeepLearning.AI short courses and The Batch](resources/deeplearning-ai.md) | Short, practical courses on generative AI, prompting, retrieval, AI agents, and evaluation, by the people who built the tools; a weekly newsletter on the field | Anyone who will build or evaluate a Solution; the newsletter for everyone | Start with the generative AI and prompting courses; the courses on evaluation and AI agents for Solution Engineers | Free courses; registration |
| Google's machine learning crash course and AI guides | A free introduction to machine learning, and Google's guides on prompting, responsible AI, and its principles | A first course in machine learning for a non-specialist | For the fundamentals before the generative material | Free |
| Microsoft Learn, AI and responsible AI paths | Structured learning paths on AI fundamentals, generative AI, and Microsoft's responsible AI standard and tools | A reader in a Microsoft-based function; the responsible AI standard as a worked example of one | For fundamentals and for one vendor's governance practice | Free |
| fast.ai | A practical deep-learning course, code first | An engineer who wants to understand models by building them | For depth after the fundamentals | Free |
| University lecture materials: Stanford CS229 and CS224N, MIT OpenCourseWare | The lecture notes and videos of the standard university courses on machine learning and natural language processing | An engineer who wants the theory | For the mathematics and the methods | Free |
| Kaggle Learn | Short hands-on courses and open datasets | A beginner who learns by doing | For practice on public data only; never Bank data | Free; registration |

## 2. Following the field

| Resource | What it is | Suits | How to take it | Access |
| --- | --- | --- | --- | --- |
| [arXiv and Papers with Code](resources/arxiv-and-papers-with-code.md) | The preprint repository where AI research appears first, and the index that links papers to their code and results | A Solution Engineer or an analyst checking a claim or a method | For the primary source of a method; preprints are not peer-reviewed, read with care | Free |
| [Hugging Face](resources/hugging-face.md) | The repository of open models and datasets, with documentation, a course, and a community | A Solution Engineer evaluating open models | For the model cards and the documentation; a model enters the Bank only through the provider check and the Lab | Free; registration |
| The research and safety publications of the model providers | The papers, system cards, and safety reports of the providers of foundation models | A Solution Engineer or a Control Function Contact assessing a model | For what a provider says about its own model, which the provider assessment reads critically | Free |
| Import AI, The Batch, and the newsletters of the field | Weekly digests of research and news | Everyone who wants to stay current in an hour a week | For awareness; verify before relying | Free; registration |
| The Stanford AI Index | The yearly data of the field | Anyone who needs a figure | For the reference number | Free |

## 3. AI security, risk, and incidents

| Resource | What it is | Suits | How to take it | Access |
| --- | --- | --- | --- | --- |
| [OWASP GenAI Security Project](regulations/owasp-top-10-llm.md) | The Top 10 for language-model applications, with guides on AI agents, red teaming, and governance | Solution Engineers, information security, the Checker | For the security test of a Solution and for the guardrails | Free |
| [MITRE ATLAS and the AI Incident Database](resources/mitre-atlas-and-ai-incident-database.md) | The knowledge base of adversarial techniques against AI systems, in the form of MITRE's attack matrices; and the public database of AI incidents and harms | Information security; the AI Incident review; the Lab | For threat modeling before a build, and for lessons from others' incidents | Free |
| [NIST AI RMF Playbook and the Generative AI Profile](regulations/nist-ai-rmf.md) | The actions suggested for each outcome of the framework | The Competence Center Lead and the Control Function Contacts | For a checklist when designing the controls of a use | Free |
| Partnership on AI | Resources on responsible practice, including on synthetic media and on incident reporting | A reader shaping the Bank's practice | For practice notes from a multi-stakeholder body | Free |

## 4. Open tools, with care

4.1. Open tools, libraries, and models are part of the field, and the Competence Center uses them in the Lab under its rules. Three cautions apply beyond the general ones: a license is read before a component is used, and recorded in the Solution Definition; a component is a supplier and enters the supply chain of the Solution, which the security test covers; and an open model is still a provider in the sense of the AI Policy when it processes data of the Bank, wherever it runs.

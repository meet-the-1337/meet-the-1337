<h1 align="center">Manan Singhal</h1>

<p align="center">
  <b>CS student at Thapar · I build and break LLM agents, and write detections for what I find.</b><br/>
  AI/LLM security · Detection engineering · Open to Summer 2027 security internships
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/manan-singhal-a566aa321/"><img src="https://img.shields.io/badge/LinkedIn-Manan_Singhal-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://tryhackme.com/p/MeetThe1337"><img src="https://img.shields.io/badge/TryHackMe-Top_5%25-212C42?style=flat&logo=tryhackme&logoColor=white" alt="TryHackMe"/></a>
  <a href="https://learn.cylabacademy.org/users/manansinghal77"><img src="https://img.shields.io/badge/picoCTF%20%2F%20CyLab-117_solves-1E293B?style=flat" alt="picoCTF"/></a>
</p>

---

### What I work on

- **Attacking multi-agent LLM systems** with prompt injection, memory poisoning and tool misuse, then training models that detect those attacks from execution traces.
- **Blue-team tooling:** SIEM deployment, file integrity monitoring and detection tuning on a Linux + Windows lab.
- **Practice:** 250+ hands-on challenges across TryHackMe (global top 5%) and picoCTF / CMU CyLab.

### Featured projects

| Project | What it is | Result | Stack |
|---|---|---|---|
| [**ReconMind**](https://github.com/meet-the-1337/AgenticAi-deployemnt-attack-analyzer) | Red-teams a LangGraph multi-agent pipeline with 4 attack classes, labels outcomes with a multi-signal oracle, and trains a detector on the traces | 0.965 F1 / 0.996 AUC on 533 traces; 27k-event AgentDojo dataset | Python, LangGraph, PyTorch, Ollama, FastAPI, React |
| [**THGT**](https://github.com/meet-the-1337/ThGT-for-agent-security) | Temporal graph transformer that catches prompt-injection payloads that stay dormant across agent hand-offs | Beats a static MLP baseline that misses >75% of attacks | PyTorch Geometric, NetworkX |
| [**Wazuh SIEM lab**](https://github.com/meet-the-1337/wazuh-siem) | Ubuntu Wazuh stack monitoring a Windows 11 endpoint, with FIM and noise tuning | Full write-up of every failure and fix | Wazuh, OpenSearch, UFW |
| [**Pen-sec**](https://github.com/meet-the-1337/Pen-sec) | Metasploit resource script that automates Windows post-exploitation in a lab | Lab-only PoC | Metasploit, Windows |
| [**SheroFetch**](https://github.com/meet-the-1337/SheroFetch) | Cross-platform desktop + Android app for organising a personal lossless music library | Releases for Windows, Linux, Android | TypeScript, Rust/Tauri, Python |

### Tools I use

**Security:** Burp Suite · Nmap · Wireshark · Metasploit · Wazuh · Linux privilege escalation
**AI/ML:** PyTorch · PyTorch Geometric · LangGraph · Ollama · scikit-learn
**Languages:** Python · C · C++ · TypeScript · Bash · SQL
**Systems:** Arch Linux · Docker · Git · FastAPI · PostgreSQL · SQLite

### Currently

- Adding reproducible demos and tests to ReconMind and THGT.
- Working through PortSwigger Web Security Academy labs.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/meet-the-1337/meet-the-1337/output/github-snake-dark.svg" />
    <img alt="Contribution snake" src="https://raw.githubusercontent.com/meet-the-1337/meet-the-1337/output/github-snake.svg" />
  </picture>
</p>

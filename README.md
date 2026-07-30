# 🔐 Project Title

> A Cybersecurity Project developed as part of the Cybersecurity Training Program at UNISOFT TECHNOLOGIES, Nagpur.

---

# 📌 Project Overview

This project was developed to understand and demonstrate the practical implementation of cybersecurity concepts using Python.

The primary objective of this project is to gain hands-on experience while solving a real-world cybersecurity problem. It serves as a learning project and is intended for educational purposes only.

Project Overview: File Integrity Checker (FIC)
Summary
The File Integrity Checker is a Python-based security tool designed to monitor and detect unauthorized or accidental changes to critical files. By utilizing SHA-256 cryptographic hashing, the application establishes a baseline of target files and compares current system states against it to identify file tampering, additions, or deletions.

Core Features
SHA-256 Hashing: Computes unique digital fingerprints for files and stores the data in a structured baseline.json database.

Integrity Auditing: Scans directories to identify three specific state changes:

Modified Files: Detects altered content even if metadata remains unchanged.

Added Files: Flags unexpected or newly created files.

Deleted Files: Identifies missing or removed files.

Exclusion Filtering: Ignores non-critical or rotating files (such as .log and .tmp) to prevent false positives.

Real-Time Monitoring: Uses the watchdog library to actively listen for file-system events and issue immediate alerts upon changes.

Technical Architecture
Language: Python 3

Hashing Engine: hashlib (SHA-256)

Data Format: json

Directory Traversal: os

Event Handling: watchdog

Practical Application
File Integrity Monitoring (FIM) is a standard security requirement in IT environments (e.g., PCI-DSS, NIST compliance). It allows security teams to detect unauthorized configuration edits, web shell placements, or system file corruption.

---

# 🎯 Project Objectives

- Understand the cybersecurity concept behind the project.
- Implement the logic using Python.
- Improve programming and problem-solving skills.
- Learn documentation and version control using Git & GitHub.
- Showcase practical cybersecurity knowledge.

---

# ❓ Why I Built This Project

I created this project as part of my Cybersecurity Training at **UNISOFT TECHNOLOGIES, Nagpur**.

The purpose of building this project was to understand the practical implementation of cybersecurity techniques instead of only studying theoretical concepts. Working on this project helped me improve my Python programming skills, logical thinking, debugging, and real-world problem-solving abilities.

This project also helped me learn how professional software projects are documented and managed using GitHub.

---

# 🛠️ Technologies Used

- Python 3.x
- VS Code
- Git
- GitHub



---

# 📂 Project Structure

```
file-integrity-checker/
│
├── screenshots/                  # Folder containing all your cmd screenshots
│   ├── 01_baseline_created.png
│   ├── 02_baseline_json.png
│   ├── 03_integrity_check.png
│   └── 04_realtime_watchdog.png
│
├── checker.py                    # Your main Python script
├── requirements.txt              # List of dependencies (watchdog)
├── .gitignore                    # Tells GitHub which files to ignore
└── README.md                     # Project documentation with images & instructions
```

---



---

# 💡 Learning Outcomes

Through this project I learned:

- Python Programming
- Cybersecurity Concepts
- Git & GitHub
- Documentation
- Debugging
- Problem Solving
- Project Structure

---

# ⚠️ Disclaimer

This project has been created strictly for educational and learning purposes.

It should only be used in authorized environments. The developer is not responsible for any misuse of this project.

---

# 🏫 Institute Information

**Institute Name:** UNISOFT TECHNOLOGIES, Nagpur

This project was developed during the Cybersecurity Training Program conducted at UNISOFT TECHNOLOGIES.

---

# 👨‍🏫 Trainer

Training and Guidance Provided By:

**Anurag Dubey**
Cybersecurity Trainer
UNISOFT TECHNOLOGIES, Nagpur

---

# 👨‍💻 Student Information

Name: Rudraksh Donge
Roll Number: 24313270010
Branch: Computer Technology 
Course: Cyber Security
Submission Date: 30/07/2026

---

# 📸 Project Screenshots

<img width="1920" height="1080" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/14ecb125-0fa9-4209-bb42-1229753e0840" />
<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/560e6f4b-ad7f-4f9c-aa8a-52997eb718d5" />
<img width="1920" height="1080" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/84cb2515-d872-4776-a04a-16ca24c43385" />






---

# 🔮 Future Improvements

- Add GUI
- Improve performance
- Better error handling
- Add logging
- Add more features

---

# 📄 License

This project is released for educational purposes only.

---

# ⭐ Acknowledgement

I sincerely thank **UNISOFT TECHNOLOGIES, Nagpur** for providing the opportunity to work on practical cybersecurity projects.

Special thanks to my trainer **Anurag Dubey** for his continuous guidance, support, and encouragement throughout the development of this project.

This project reflects the knowledge and practical skills gained during the training program.

### Python SSH Log Analyzer

## Project Overview

This project demonstrates the development of a Python-based log analyzer to detect and summarize failed SSH authentication attempts.

The script parses exported SSH logs and automatically identifies:

Total failed login attempts
Targeted usernames
Source IP addresses
Number of attempts per IP
This project simulates real-world SOC analyst workflows by automating log analysis instead of relying solely on manual command-line filtering.

## Lab Environment

Operating System: Kali Linux (Virtual Machine)
Service Analyzed: OpenSSH (sshd)
Log Source: Exported SSH journal logs
Programming Language: Python 3

## Objectives

Automate detection of failed SSH login attempts
Parse log files using regular expressions
Extract IP addresses and usernames
Quantify suspicious authentication activity
Generate structured analysis output

## How It Works

SSH failed login attempts were generated.
Logs were exported to failed_attempts.txt.
The Python script reads the log file.
Regular expressions extract IP addresses and usernames.
The script counts total failed attempts.
A summary report is printed to the terminal.

## Sample Output

==== SSH Log Analysis Report ====
Total Failed Attempts: 13
Unique IP Addresses: {'127.0.0.1'}
Targeted Usernames: {'fakeuser'}
Attempts Per IP: Counter({'127.0.0.1': 6})

## Skills Demonstrated

Python scripting
Regular expressions (regex)
Log parsing and analysis
Security event detection
Automation of manual analysis tasks
Basic threat pattern identification

## Repository Structure

Python-SSH-Log-Analyzer/
│
├── README.md
├── report/
│   └── Python_Log_Analyzer_Report.pdf
├── screenshots/
│   ├── 01_log_file.png
│   ├── 02_script_code.png
│   ├── 03_script_output.png
│
└── logs/
    └── failed_attempts.txt

## Security Relevance

Repeated failed SSH authentication attempts may indicate brute-force attack behavior. Automating log analysis enables faster detection of suspicious activity and supports proactive incident response.


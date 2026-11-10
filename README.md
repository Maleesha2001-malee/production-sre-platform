
# Production SRE Platform

A hands-on Site Reliability Engineering project.

## Project 01: Server Health Monitoring

A Python-based Linux monitoring tool.

### Features
- CPU monitoring
- RAM monitoring
- Disk monitoring
- System uptime
- Resource threshold alerts

### Technologies
- Python
- Linux
- psutil

## How to Run

```bash
sudo apt install python3-psutil -y

python3 automation/python/server_monitor.py
```
## Project 02: Linux Log Analyzer

A Bash-based tool for analyzing application log files.

### Features
- Counts total log entries
- Identifies errors
- Identifies warnings
- Counts informational messages
- Displays error details

### Technologies
- Bash
- Linux
- grep
- wc

### How to Run
chmod +x automation/bash/log_analyzer.sh
./automation/bash/log_analyzer.sh

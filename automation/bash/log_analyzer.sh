#!/bin/bash

LOG_FILE="logs/app.log"

echo "=================================="
echo "       LINUX LOG ANALYZER"
echo "=================================="

if [ ! -f "$LOG_FILE" ]; then
    echo "ERROR: Log file not found!"
    exit 1
fi

TOTAL=$(wc -l < "$LOG_FILE")
ERRORS=$(grep -c "ERROR" "$LOG_FILE")
WARNINGS=$(grep -c "WARNING" "$LOG_FILE")
INFO=$(grep -c "INFO" "$LOG_FILE")

echo "Total Log Entries : $TOTAL"
echo "Error Count       : $ERRORS"
echo "Warning Count     : $WARNINGS"
echo "Info Count        : $INFO"

echo "----------------------------------"
echo "ERROR DETAILS:"
grep "ERROR" "$LOG_FILE"

echo "=================================="

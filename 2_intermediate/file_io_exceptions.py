"""
Phase 1: File I/O, Exception Handling & JSON Manipulation
==========================================================
Topics Covered:
1. File I/O with Context Managers (`with open(...)`)
2. Exception Handling (`try`, `except`, `else`, `finally`)
3. Custom Exceptions (Production-grade error architecture)
4. JSON Format Manipulation (`json.dump`, `json.load`, `json.dumps`, `json.loads`)

Senior SRE / Backend Context:
Configuration files (.json, .yaml), application log writing, graceful error recovery,
ebong database failure handling — shob-i File I/O & Exception Handling er upor
nirbhor kore. Ekta unhandled exception production server crash kore dite pare!
"""

import json
import os
from pathlib import Path

# Working directory setup (File operations safe rakhar jonno)
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


# =====================================================================
# 1. File I/O with Context Managers (`with open(...)`)
# =====================================================================
print("=" * 60)
print("1. File I/O with Context Manager (`with open(...)`)")
print("=" * 60)
# 'with open' context manager automatically file close kore, jodio error ashe!

log_file_path = DATA_DIR / "server.log"

# A) Writing to a file ('w' mode: overwrites existing content)
with open(log_file_path, "w", encoding="utf-8") as f:
    f.write("[2026-09-26 00:01:00] [INFO] Server initialization started.\n")
    f.write("[2026-09-26 00:01:02] [INFO] Database pool connected (PostgreSQL).\n")
print(f"Log file written to: {log_file_path}")

# B) Appending to a file ('a' mode: adds content to end of file)
with open(log_file_path, "a", encoding="utf-8") as f:
    f.write("[2026-09-26 00:01:05] [WARNING] High latency observed on /healthz.\n")
    f.write("[2026-09-26 00:01:10] [INFO] Worker health check: OK.\n")
print("New log entries appended.")

# C) Reading from a file ('r' mode)
print("\nReading log file line by line:")
with open(log_file_path, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        print(f"  Line {line_num}: {line.strip()}")
print()


# =====================================================================
# 2. Exception Handling (`try`, `except`, `else`, `finally`)
# =====================================================================
print("=" * 60)
print("2. Exception Handling (`try`, `except`, `else`, `finally`)")
print("=" * 60)

def safe_parse_port(port_str: str) -> int:
    """
    try-except-else-finally er complete flow demonstrate kore.
    """
    print(f"\nAttempting to parse port: '{port_str}'")
    try:
        # Code that might raise an exception
        port_num = int(port_str)
        if port_num <= 0:
            raise ValueError("Port must be positive!")
    except ValueError as err:
        # Handles specific error
        print(f"  ❌ [EXCEPT] Parsing failed: {err}")
        return 8000  # Fallback to default port
    else:
        # Runs ONLY IF NO exception occurred in try block
        print(f"  ✅ [ELSE] Port parsed successfully: {port_num}")
        return port_num
    finally:
        # ALWAYS runs regardless of success or error (Good for cleanup)
        print("  🧹 [FINALLY] Resource check completed.")

port_valid = safe_parse_port("8080")
port_invalid = safe_parse_port("not_a_number")


# Handling File Not Found safely:
non_existent_file = DATA_DIR / "missing_config.yaml"
try:
    with open(non_existent_file, "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"\n⚠️ Caught FileNotFoundError gracefully: File '{non_existent_file.name}' not found.")
print()


# =====================================================================
# 3. Custom Exceptions (Production-grade Error Modeling)
# =====================================================================
print("=" * 60)
print("3. Custom Exceptions (Subclassing Exception)")
print("=" * 60)
# Generic Exception er poriborte Custom Exception use korle API caller
# ebong logs-e shundor bhabe root cause dhora jay.

class InfrastructureError(Exception):
    """Base class for all infrastructure related errors."""
    pass

class DatabaseConnectionTimeout(InfrastructureError):
    """Database connect korte timeout hole raise kora hoy."""
    def __init__(self, host: str, timeout_sec: int):
        self.host = host
        self.timeout_sec = timeout_sec
        super().__init__(f"Connection to database '{host}' timed out after {timeout_sec}s.")

class ServiceUnavailableError(InfrastructureError):
    """External microservice unavailable thakle raise hoy."""
    pass


def connect_to_database(host: str, timeout: int = 5) -> None:
    # Simulating connection failure
    if host == "db-unreachable.internal":
        raise DatabaseConnectionTimeout(host=host, timeout_sec=timeout)
    print(f"Connected to DB {host} successfully.")

try:
    connect_to_database("db-unreachable.internal", timeout=3)
except DatabaseConnectionTimeout as db_err:
    print(f"🚨 ALERT: {db_err}")
    print(f"   Target Host: {db_err.host}, Timeout limit: {db_err.timeout_sec}s")
print()


# =====================================================================
# 4. JSON Format Manipulation (`json` module)
# =====================================================================
print("=" * 60)
print("4. JSON Manipulation (`json.dump`, `load`, `dumps`, `loads`)")
print("=" * 60)
# JSON = JavaScript Object Notation. REST API er de-facto standard.
# Memory vs Disk rules:
#   's' suffix (dumps, loads) -> String in memory
#   without 's' (dump, load)  -> File on disk

server_inventory = {
    "cluster_id": "k8s-prod-apac",
    "nodes_count": 3,
    "active": True,
    "nodes": [
        {"name": "node-1", "ip": "10.0.1.1", "role": "master"},
        {"name": "node-2", "ip": "10.0.1.2", "role": "worker"},
        {"name": "node-3", "ip": "10.0.1.3", "role": "worker"}
    ]
}

# A) json.dumps: Python dict to JSON String (Serialization)
json_string = json.dumps(server_inventory, indent=2)
print("JSON String (in memory):\n" + json_string[:150] + "\n  ...\n}")

# B) json.loads: JSON String to Python dict (Deserialization)
parsed_dict = json.loads(json_string)
print(f"\nParsed from String -> Cluster ID: {parsed_dict['cluster_id']}")

# C) json.dump: Write Python dict directly into a .json file
json_file_path = DATA_DIR / "inventory.json"
with open(json_file_path, "w", encoding="utf-8") as f:
    json.dump(server_inventory, f, indent=4)
print(f"Inventory saved to file: {json_file_path}")

# D) json.load: Read .json file directly into Python dict
with open(json_file_path, "r", encoding="utf-8") as f:
    loaded_inventory = json.load(f)

print(f"Loaded from file -> Total nodes: {len(loaded_inventory['nodes'])}")
for node in loaded_inventory["nodes"]:
    print(f"  - {node['name']} ({node['role']}) -> {node['ip']}")

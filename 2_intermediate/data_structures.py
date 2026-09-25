"""
Phase 1: Intermediate Python - Core Data Structures & Comprehensions
=====================================================================
Topics Covered:
1. List  (Mutable, Ordered, Dynamic Array)
2. Tuple (Immutable, Ordered, Hashable/Lightweight)
3. Set   (Mutable, Unordered, Unique Elements, O(1) Lookup)
4. Dict  (Mutable, Key-Value Pairs, O(1) Hash Map)
5. Comprehensions (List, Dict, Set - Fast & Pythonic)

Senior SRE / Backend Context:
API payload parsing, caching, role-based access control (RBAC),
database records ebong metrics aggregation — ei shob-i Data Structures er
proper choice er upor nirbhor kore. Wrong data structure = high latency & high memory.
"""

# =====================================================================
# 1. LIST: Dynamic Array, Mutable, Ordered
# =====================================================================
print("=" * 60)
print("1. LIST (Mutable, Ordered, Index-based)")
print("=" * 60)

# Microservices list
services = ["auth-api", "payment-service", "order-service"]
print(f"Initial list: {services}")

# Adding elements: append vs extend
services.append("notification-service")          # Single item O(1)
services.extend(["inventory-api", "audit-log"])  # Multiple items
print(f"After append & extend: {services}")

# Slicing: [start:stop:step] (Non-destructive)
print(f"First 3 services: {services[:3]}")
print(f"Last 2 services:  {services[-2:]}")
print(f"Reversed list:   {services[::-1]}")

# Removing elements
removed_item = services.pop()     # Pops last item O(1)
print(f"Popped item: '{removed_item}', Remaining: {services}")

services.remove("payment-service")  # Removes by value O(n)
print(f"After removing 'payment-service': {services}")

# Sorting: In-place .sort() vs Built-in sorted()
numbers = [42, 12, 88, 3, 25]
sorted_numbers = sorted(numbers)  # Not changing original
print(f"Original: {numbers} -> sorted() copy: {sorted_numbers}")
numbers.sort(reverse=True)        # In-place change
print(f"In-place sorted (desc): {numbers}\n")


# =====================================================================
# 2. TUPLE: Immutable, Ordered, Memory Efficient
# =====================================================================
print("=" * 60)
print("2. TUPLE (Immutable, Ordered, Data Integrity)")
print("=" * 60)
# Senior SRE Tip: Database row ba server host/port jeta change kora dangerous,
# shekhane list er poriborte tuple use kora best practice.

db_config = ("192.168.1.100", 5432, "production_db")
print(f"Database Config Tuple: {db_config}")

# Tuple Unpacking (Khub popular pattern in Python)
host, port, db_name = db_config
print(f"Unpacked -> Host: {host}, Port: {port}, Database: {db_name}")

# Immutability Check:
# db_config[1] = 5433  # TypeError: 'tuple' object does not support item assignment!

# Single element tuple e comma (,) mandatory!
single_item = ("production",)  # Tuple
not_a_tuple = ("production")   # Just a String!
print(f"('production',) is {type(single_item)}, but ('production') is {type(not_a_tuple)}\n")


# =====================================================================
# 3. SET: Unordered, Unique Elements, O(1) Fast Membership
# =====================================================================
print("=" * 60)
print("3. SET (Unique Elements, Hash Set, O(1) Lookups)")
print("=" * 60)

# Duplicate removal
raw_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3", "10.0.0.2"]
unique_ips = set(raw_ips)
print(f"Raw IPs ({len(raw_ips)}): {raw_ips}")
print(f"Unique IPs ({len(unique_ips)}): {unique_ips}")

# Set Theory Operations (Union, Intersection, Difference)
admin_permissions = {"read", "write", "delete", "deploy"}
developer_permissions = {"read", "write", "debug"}

# 1. Intersection (&): Donojoner common permissions
common_perms = admin_permissions & developer_permissions
print(f"Common Permissions (&): {common_perms}")

# 2. Difference (-): Admin er ache kintu Dev er nei
admin_only = admin_permissions - developer_permissions
print(f"Admin Only Permissions (-): {admin_only}")

# 3. Union (|): Shob milie total unique permissions
all_perms = admin_permissions | developer_permissions
print(f"All Permissions (|): {all_perms}")

# Membership Testing: O(1) average time complexity (List e O(n))
blocked_ips = {"192.168.1.5", "10.0.0.99"}
incoming_ip = "192.168.1.5"
if incoming_ip in blocked_ips:
    print(f"🚨 Security Alert: Blocked IP detected: {incoming_ip}!\n")


# =====================================================================
# 4. DICTIONARY: Key-Value Pairs, Hash Map, O(1) Access
# =====================================================================
print("=" * 60)
print("4. DICTIONARY (Key-Value, O(1) Access, JSON Foundation)")
print("=" * 60)

server_node = {
    "hostname": "k8s-worker-01",
    "region": "ap-southeast-1",
    "cpu_cores": 16,
    "ram_gb": 64,
    "is_healthy": True,
}

# Safe access with .get() - Prevents KeyError in production!
print(f"Hostname: {server_node.get('hostname')}")
print(f"Disk (with default fallback): {server_node.get('disk_gb', '500GB (default)')}")

# Updating and inserting values
server_node["status"] = "ACTIVE"
server_node["cpu_cores"] = 32  # Update existing

# Iterating over Dict: keys, values, items
print("\nServer Attributes:")
for key, value in server_node.items():
    print(f"  - {key}: {value}")

# Dictionary Merging (Modern Python 3.9+ `|` Operator)
default_settings = {"timeout": 30, "retry": 3, "env": "dev"}
custom_overrides = {"timeout": 60, "env": "prod"}
final_config = default_settings | custom_overrides
print(f"\nMerged Config (Overrides default): {final_config}\n")


# =====================================================================
# 5. COMPREHENSIONS: List, Dict, Set (Fast, Elegant, Pythonic)
# =====================================================================
print("=" * 60)
print("5. COMPREHENSIONS (List, Dict, Set)")
print("=" * 60)

# A) List Comprehension
# Traditional way:
# squared = []
# for x in range(1, 6):
#     squared.append(x ** 2)

# Pythonic way: [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(f"Even numbers squared: {even_squares}")

# Transforming String lists (e.g. cleaning log levels)
raw_logs = ["  error  ", "INFO", "  warning ", "debug  "]
clean_logs = [log.strip().upper() for log in raw_logs]
print(f"Cleaned Log Levels: {clean_logs}")

# B) List Comprehension with if-else (Ternary transformation)
# [expr_if_true if condition else expr_if_false for item in iterable]
http_codes = [200, 404, 500, 201, 502]
status_labels = ["OK" if code < 400 else "ERROR" for code in http_codes]
print(f"HTTP Status Codes: {http_codes}")
print(f"Status Labels:     {status_labels}")

# C) Dict Comprehension: {key_expr: value_expr for item in iterable}
services = ["auth", "payment", "search", "gateway"]
service_ports = {service: 8000 + idx for idx, service in enumerate(services, start=1)}
print(f"\nGenerated Service Ports (Dict Comp): {service_ports}")

# Filtering a Dictionary
# e.g., Filter servers whose CPU > 70%
cpu_metrics = {"web-1": 45, "web-2": 82, "db-primary": 91, "cache-1": 35}
high_cpu_servers = {server: load for server, load in cpu_metrics.items() if load >= 70}
print(f"Alert! High CPU Servers: {high_cpu_servers}")

# D) Set Comprehension: {expr for item in iterable}
# Get unique domains from list of emails
emails = ["alice@gmail.com", "bob@yahoo.com", "charlie@gmail.com", "david@company.com"]
domains = {email.split("@")[1] for email in emails}
print(f"\nUnique Email Domains (Set Comp): {domains}")

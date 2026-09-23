"""
Phase 0: Control Flow in Python
================================
Topics Covered:
- if, elif, else (Decision Making & Truthiness)
- for loop (Iterating through ranges & sequences)
- while loop (Condition-based looping)
- break and continue (Loop execution controls)

Senior SRE Tip:
Health checks, retry logic, timeout handling, and threshold alerts — egulo shob-i
Control Flow er upor depend kore.
"""

# =====================================================================
# 1. Conditionals: if, elif, else
# =====================================================================
print("=" * 50)
print("1. Decision Making: if, elif, else")
print("=" * 50)

# Example: Server Health / CPU Usage Monitoring
cpu_usage = 85  # Percentage

if cpu_usage >= 90:
    print(f"🔥 [CRITICAL] CPU usage is {cpu_usage}%! Triggering alert to on-call engineer!")
elif cpu_usage >= 75:
    print(f"⚠️  [WARNING] High CPU load: {cpu_usage}%. Auto-scaling new instances...")
elif cpu_usage >= 50:
    print(f"ℹ️  [NORMAL] Moderate CPU load: {cpu_usage}%.")
else:
    print(f"✅ [OPTIMAL] Server running smoothly: {cpu_usage}%.")

# Ternary Operator (One-line if-else) - Production e clean code er jonno khub popular
status_code = 200
response_status = "SUCCESS" if status_code == 200 else "FAILED"
print(f"HTTP Status: {status_code} -> Result: {response_status}\n")


# =====================================================================
# 2. For Loops (Sequences & Range)
# =====================================================================
print("=" * 50)
print("2. For Loops: Iteration")
print("=" * 50)

# Basic range iteration
print("Iterating over numbers 1 to 5:")
for step in range(1, 6):
    print(f"  Step {step}: In progress...")

# Iterating over a collection / list of server nodes
services = ["auth-service", "payment-service", "order-service", "notification-service"]
print("\nChecking deployment status for microservices:")
for idx, service in enumerate(services, start=1):
    print(f"  [{idx}] Deploying {service}...")

# =====================================================================
# 3. While Loops (Condition-based execution)
# =====================================================================
print("=" * 50)
print("3. While Loops")
print("=" * 50)

# Example: Retry mechanism with maximum attempts
max_retries = 3
attempt = 1
is_connected = False

print("Attempting to connect to database:")
while attempt <= max_retries and not is_connected:
    print(f"  Attempt {attempt} of {max_retries}: Connecting...")
    if attempt == 2:  # 2nd attempt e connect holo dhori
        is_connected = True
        print("  🎉 Connection established successfully!")
    attempt += 1

if not is_connected:
    print("  ❌ Connection failed after maximum retries.")
print()


# =====================================================================
# 4. Loop Controls: break & continue
# =====================================================================
print("=" * 50)
print("4. Loop Controls: break and continue")
print("=" * 50)

# 'continue': Skip current iteration and move to next
# 'break': Terminate the loop immediately
ports_to_scan = [80, 443, 22, 8080, 3306, 9999]
blocked_port = 8080
kill_switch_port = 3306

print("Scanning open ports:")
for port in ports_to_scan:
    if port == blocked_port:
        print(f"  ⏩ Port {port} is blocked/ignored. Skipping (continue)...")
        continue

    if port == kill_switch_port:
        print(f"  🛑 Critical Port {port} encountered! Stopping scan immediately (break)!")
        break

    print(f"  🔍 Port {port}: Scan completed cleanly.")


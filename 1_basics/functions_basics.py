"""
Phase 0: Functions Basics in Python
===================================
Topics Covered:
- Function definition (`def`), arguments, and return values
- Default parameters & keyword arguments
- Arbitrary arguments: `*args` (variable positional arguments)
- Arbitrary keyword arguments: `**kwargs` (variable keyword arguments)
- Type annotations & Docstrings (Production best practice)

Senior SRE Tip:
FastAPI pooraটাই functions, dependency injection ebong type annotations er upor nirbhor kore.
Tai arguments ebong `*args`/`**kwargs` er mechanism shundor bhabe bojha khub dorkar.
"""

# =====================================================================
# 1. Basic Function Definition & Return Value
# =====================================================================
print("=" * 55)
print("1. Function Definition (def), Parameters & Return Value")
print("=" * 55)

def calculate_latency(request_start: float, request_end: float) -> float:
    """
    Calculate round-trip latency in milliseconds.
    """
    latency = (request_end - request_start) * 1000
    return round(latency, 2)

# Function call
latency_ms = calculate_latency(10.120, 10.185)
print(f"Request Latency: {latency_ms} ms\n")


# =====================================================================
# 2. Default Parameters & Keyword Arguments
# =====================================================================
print("=" * 55)
print("2. Default Parameters & Named / Keyword Arguments")
print("=" * 55)

# Default parameter rules: Default parameter-gulo shob shomoy non-default parameter er pore thakbe.
def create_service_url(host: str, port: int = 8000, protocol: str = "http", path: str = "healthz") -> str:
    """Construct a full service endpoint URL."""
    return f"{protocol}://{host}:{port}/{path.lstrip('/')}"

# Positional call (uses defaults for port, protocol, path)
url1 = create_service_url("localhost")
print(f"Default URL:       {url1}")

# Override default with positional arguments
url2 = create_service_url("api.production.internal", 443, "https", "metrics")
print(f"Full Custom URL:   {url2}")

# Calling using Keyword Arguments (order matter kore na!)
url3 = create_service_url(host="redis-cluster", path="ping", port=6379)
print(f"Keyword Args URL:  {url3}\n")


# =====================================================================
# 3. Arbitrary Positional Arguments (*args)
# =====================================================================
print("=" * 55)
print("3. Arbitrary Arguments: *args (Tuple)")
print("=" * 55)
# *args shob extra positional argument-ke ekta 'tuple' hishebe capture kore.

def aggregate_cpu_metrics(server_name: str, *readings: float) -> None:
    """Calculates average CPU usage from variable number of metric points."""
    if not readings:
        print(f"[{server_name}] No CPU metrics provided.")
        return

    avg_cpu = sum(readings) / len(readings)
    print(f"Server: {server_name}")
    print(f"  Total Data Points: {len(readings)} -> {readings}")
    print(f"  Average CPU: {avg_cpu:.2f}%")

aggregate_cpu_metrics("worker-node-1", 45.2, 52.8, 48.0, 60.1)
aggregate_cpu_metrics("worker-node-2", 88.5, 92.0)
print()


# =====================================================================
# 4. Arbitrary Keyword Arguments (**kwargs)
# =====================================================================
print("=" * 55)
print("4. Arbitrary Keyword Arguments: **kwargs (Dictionary)")
print("=" * 55)
# **kwargs shob extra key=value argument-ke ekta 'dict' hishebe capture kore.

def log_event(level: str, message: str, **metadata) -> None:
    """
    Structured logging helper function.
    Captures arbitrary contextual metadata as key-value pairs.
    """
    print(f"[{level.upper()}] {message}")
    if metadata:
        print("  Attached Metadata:")
        for key, value in metadata.items():
            print(f"    - {key}: {value}")

log_event(
    level="info",
    message="User logged in successfully",
    user_id=1042,
    ip="192.168.1.55",
    user_agent="Mozilla/5.0",
    role="admin"
)

log_event(
    level="error",
    message="Database connection timeout",
    target_db="postgres-primary",
    retry_attempt=3
)
print()


# =====================================================================
# 5. Combining All: positional, default, *args, **kwargs
# =====================================================================
print("=" * 55)
print("5. Master Pattern: Combining (*args & **kwargs)")
print("=" * 55)

def build_api_request(method: str, endpoint: str, *headers, timeout: int = 30, **query_params):
    """
    Real-world pattern seen in API clients (like httpx or requests).
    Order:
    1. Standard positional args
    2. *args
    3. Keyword-only or default args
    4. **kwargs
    """
    print(f"HTTP Request: {method.upper()} {endpoint}")
    print(f"  Headers: {headers}")
    print(f"  Timeout: {timeout}s")
    print(f"  Query Parameters: {query_params}")

build_api_request(
    "GET",
    "/api/v1/users",
    "Authorization: Bearer token123",
    "Accept: application/json",
    timeout=10,
    page=1,
    limit=50,
    active=True
)


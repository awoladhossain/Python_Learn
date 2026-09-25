"""
Phase 1: Object-Oriented Programming (OOP) in Python
=====================================================
Topics Covered:
1. Classes & Objects
2. Instance Variables vs Class Variables
3. Encapsulation (Private attributes & @property getter/setter)
4. Inheritance (Base class, Derived class & super())
5. Polymorphism (Method Overriding & Common Interfaces)
6. Magic Methods (__init__, __str__, __repr__, __eq__)

Senior SRE / Backend Context:
FastAPI, SQLAlchemy ORM, and Pydantic are built entirely on OOP principles.
Classes allow us to model complex systems (Database connections, Cloud instances,
API clients) with clean, reusable, and encapsulated architectures.
"""

# =====================================================================
# 1. Classes, Objects & Instance vs Class Variables
# =====================================================================
print("=" * 60)
print("1. Classes, Objects, Instance vs Class Variables")
print("=" * 60)

class CloudServer:
    # Class Variable (Shared across ALL instances of CloudServer)
    total_servers_running = 0
    CLOUD_PROVIDER = "AWS"

    def __init__(self, hostname: str, ip_address: str, ram_gb: int):
        # Instance Variables (Unique to each specific instance/object)
        self.hostname = hostname
        self.ip_address = ip_address
        self.ram_gb = ram_gb
        self.is_active = False

        # Class variable update
        CloudServer.total_servers_running += 1

    def start_server(self) -> None:
        self.is_active = True
        print(f"🚀 Server '{self.hostname}' ({self.ip_address}) started successfully.")

    def stop_server(self) -> None:
        self.is_active = False
        print(f"🛑 Server '{self.hostname}' stopped.")


server1 = CloudServer("web-frontend-01", "10.0.1.10", 16)
server2 = CloudServer("worker-queue-01", "10.0.1.20", 32)

server1.start_server()

print(f"Server 1 RAM: {server1.ram_gb} GB, Provider: {server1.CLOUD_PROVIDER}")
print(f"Server 2 RAM: {server2.ram_gb} GB, Provider: {server2.CLOUD_PROVIDER}")
print(f"Total Cloud Servers Created: {CloudServer.total_servers_running}\n")


# =====================================================================
# 2. Encapsulation & Data Protection (@property & Setter)
# =====================================================================
print("=" * 60)
print("2. Encapsulation (@property Getters & Setters)")
print("=" * 60)
# Encapsulation: Sensitive data-ke direct access theke protect kora.
# Python convention:
# _single_leading_underscore: Protected (Internal use)
# __double_leading_underscore: Private (Name Mangling)

class DatabaseConnection:
    def __init__(self, host: str, port: int, secret_token: str):
        self.host = host
        self._port = port               # Protected attribute
        self.__secret_token = secret_token  # Private attribute

    # Getter using @property
    @property
    def port(self) -> int:
        """Port read-only ba validated bhabe access korte."""
        return self._port

    # Setter with Validation Logic
    @port.setter
    def port(self, new_port: int) -> None:
        """Production validation: Valid port number (1 - 65535)."""
        if not (1 <= new_port <= 65535):
            raise ValueError(f"Invalid port: {new_port}. Port must be between 1 and 65535!")
        print(f"Port successfully changed from {self._port} to {new_port}")
        self._port = new_port

    def get_masked_token(self) -> str:
        """Private token securely expose kora (Masked)."""
        return f"{self.__secret_token[:4]}****"


db_conn = DatabaseConnection("pg-primary.internal", 5432, "SuperSecretDBKey123")
print(f"Database Port: {db_conn.port}")
db_conn.port = 5433  # Triggers the setter validation
print(f"Masked Token:  {db_conn.get_masked_token()}")

# db_conn.__secret_token  # ❌ AttributeError (Private attribute access blocked!)
print()


# =====================================================================
# 3. Inheritance & Polymorphism
# =====================================================================
print("=" * 60)
print("3. Inheritance & Polymorphism (super() & Method Overriding)")
print("=" * 60)

# Base Class (Parent)
class BaseService:
    def __init__(self, service_name: str, port: int):
        self.service_name = service_name
        self.port = port

    def health_check(self) -> str:
        """Default health check method (to be overridden by child)."""
        return f"[{self.service_name}] Default status: OK (Port: {self.port})"


# Child Class 1 (Inherits from BaseService)
class WebService(BaseService):
    def __init__(self, service_name: str, port: int, routes_count: int):
        # super() parent class er __init__ call kore
        super().__init__(service_name, port)
        self.routes_count = routes_count

    # Method Overriding (Polymorphism)
    def health_check(self) -> str:
        return f"🌐 [HTTP Web] {self.service_name} serving {self.routes_count} endpoints on port {self.port}."


# Child Class 2 (Inherits from BaseService)
class DatabaseService(BaseService):
    def __init__(self, service_name: str, port: int, active_connections: int):
        super().__init__(service_name, port)
        self.active_connections = active_connections

    # Method Overriding (Polymorphism)
    def health_check(self) -> str:
        return f"🗄️ [DB Engine] {self.service_name} operational with {self.active_connections} active connections."


# Polymorphic Function: accepts any object that conforms to BaseService interface
def run_infrastructure_audit(services: list[BaseService]) -> None:
    print("Conducting Infrastructure Health Audit:")
    for service in services:
        # Ek-i method call (health_check), kintu object er type onujayi alada behaviour!
        print(f"  -> {service.health_check()}")


services_list = [
    WebService("Auth-API", 8000, 14),
    DatabaseService("PostgreSQL-Cluster", 5432, 120),
    WebService("Payment-Gateway", 8080, 8),
]
run_infrastructure_audit(services_list)
print()


# =====================================================================
# 4. Magic Methods (Dunder Methods: __str__, __repr__, __eq__)
# =====================================================================
print("=" * 60)
print("4. Magic Methods (__init__, __str__, __repr__, __eq__)")
print("=" * 60)
# Dunder = Double Underscore methods. Python er built-in behaviour customize kore.

class ServiceEndpoint:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def __str__(self) -> str:
        """User-friendly / Log-friendly representation."""
        return f"ServiceEndpoint '{self.name}' at {self.url}"

    def __repr__(self) -> str:
        """Developer unambiguous representation (used in debugger / REPL)."""
        return f"ServiceEndpoint(name='{self.name}', url='{self.url}')"

    def __eq__(self, other: object) -> bool:
        """Equality comparison (==) operator customization."""
        if not isinstance(other, ServiceEndpoint):
            return False
        # Duti endpoint same hobe jodi tader URL ek hoy
        return self.url == other.url


ep1 = ServiceEndpoint("Auth-V1", "https://api.domain.com/v1/auth")
ep2 = ServiceEndpoint("Auth-Alias", "https://api.domain.com/v1/auth")
ep3 = ServiceEndpoint("Billing", "https://api.domain.com/v1/billing")

# __str__ invocation
print(f"str():  {str(ep1)}")

# __repr__ invocation
print(f"repr(): {repr(ep1)}")

# __eq__ comparison
print(f"ep1 == ep2: {ep1 == ep2} (Same URL, so identical endpoint)")
print(f"ep1 == ep3: {ep1 == ep3} (Different URL)")

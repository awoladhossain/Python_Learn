"""
Phase 1 Practice Milestone: CLI Inventory Management System
===========================================================
Architecture & Concepts Applied:
1. OOP Modeling:
   - Base & Subclasses (Inheritance & Polymorphism)
   - Encapsulation with @property validation (Quantity >= 0, Price > 0)
   - Magic methods (__str__, __repr__, __eq__)
2. Data Persistence:
   - JSON file storage (with open(...), json.dump, json.load)
3. Robust Error Handling:
   - Custom Exception hierarchy
   - try-except-finally blocks for safe I/O and user input parsing

Senior SRE Context:
Asset and infrastructure tracking (Servers, API Keys, Hardware licenses)
shob-i inventory management system er part. State persistence ebong reliable
error handling bina kono production tool safely run korte pare na.
"""

from __future__ import annotations
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional


# =====================================================================
# 1. Custom Exceptions Hierarchy
# =====================================================================

class InventoryError(Exception):
    """Base class for all inventory system exceptions."""
    pass


class ItemNotFoundError(InventoryError):
    """Raised when an item ID does not exist in inventory."""
    def __init__(self, item_id: str):
        self.item_id = item_id
        super().__init__(f"❌ Item with ID '{item_id}' not found in inventory!")


class DuplicateItemError(InventoryError):
    """Raised when attempting to add an item with an existing ID."""
    def __init__(self, item_id: str):
        self.item_id = item_id
        super().__init__(f"❌ Item with ID '{item_id}' already exists!")


class InsufficientStockError(InventoryError):
    """Raised when stock operation results in negative quantity."""
    def __init__(self, item_id: str, available: int, requested: int):
        self.item_id = item_id
        self.available = available
        self.requested = requested
        super().__init__(
            f"❌ Insufficient stock for ID '{item_id}'! Available: {available}, Requested deduction: {requested}."
        )


class StorageCorruptedError(InventoryError):
    """Raised when JSON database is malformed or corrupted."""
    pass


# =====================================================================
# 2. OOP Models: Item, ServerAsset, SoftwareLicense
# =====================================================================

class Item:
    """Base Inventory Item with Encapsulated Attributes."""

    def __init__(self, item_id: str, name: str, category: str, quantity: int, price: float):
        self.item_id = item_id.strip()
        self.name = name.strip()
        self.category = category.strip()
        self._quantity = 0
        self._price = 0.0

        # Validate through setters
        self.quantity = quantity
        self.price = price

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            raise ValueError("Quantity cannot be negative!")
        self._quantity = int(value)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = round(float(value), 2)

    def total_value(self) -> float:
        """Item er total valuation (quantity * price)."""
        return round(self.quantity * self.price, 2)

    def to_dict(self) -> dict:
        """Serialization for JSON persistence."""
        return {
            "type": "General",
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Item:
        """Factory method: Deserialization from JSON dict."""
        return cls(
            item_id=data["item_id"],
            name=data["name"],
            category=data["category"],
            quantity=data["quantity"],
            price=data["price"],
        )

    def __str__(self) -> str:
        return f"[{self.item_id}] {self.name} | Category: {self.category} | Qty: {self.quantity} | ${self.price:.2f}"

    def __repr__(self) -> str:
        return f"Item(id='{self.item_id}', name='{self.name}', qty={self.quantity})"


class ServerAsset(Item):
    """Subclass representing Physical or Cloud Server Infrastructure."""

    def __init__(self, item_id: str, name: str, quantity: int, price: float, ip_address: str, ram_gb: int):
        super().__init__(item_id, name, category="Server Infrastructure", quantity=quantity, price=price)
        self.ip_address = ip_address.strip()
        self.ram_gb = int(ram_gb)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "ServerAsset"
        data["ip_address"] = self.ip_address
        data["ram_gb"] = self.ram_gb
        return data

    @classmethod
    def from_dict(cls, data: dict) -> ServerAsset:
        return cls(
            item_id=data["item_id"],
            name=data["name"],
            quantity=data["quantity"],
            price=data["price"],
            ip_address=data.get("ip_address", "0.0.0.0"),
            ram_gb=data.get("ram_gb", 16),
        )

    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info} | IP: {self.ip_address} ({self.ram_gb}GB RAM)"


# =====================================================================
# 3. InventoryManager: Repository & Storage Engine
# =====================================================================

class InventoryManager:
    """Manages collection of inventory items with JSON file persistence."""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._items: Dict[str, Item] = {}
        self.load_from_storage()

    def add_item(self, item: Item) -> None:
        if item.item_id in self._items:
            raise DuplicateItemError(item.item_id)
        self._items[item.item_id] = item
        self.save_to_storage()

    def get_item(self, item_id: str) -> Item:
        item = self._items.get(item_id)
        if not item:
            raise ItemNotFoundError(item_id)
        return item

    def remove_item(self, item_id: str) -> Item:
        item = self.get_item(item_id)
        del self._items[item_id]
        self.save_to_storage()
        return item

    def update_stock(self, item_id: str, delta_quantity: int) -> int:
        """
        Stock update kore (positive hole add, negative hole deduct).
        """
        item = self.get_item(item_id)
        new_quantity = item.quantity + delta_quantity
        if new_quantity < 0:
            raise InsufficientStockError(item_id, item.quantity, abs(delta_quantity))
        item.quantity = new_quantity
        self.save_to_storage()
        return item.quantity

    def list_all(self) -> List[Item]:
        return list(self._items.values())

    def search_by_category(self, category: str) -> List[Item]:
        query = category.lower().strip()
        return [item for item in self._items.values() if query in item.category.lower()]

    def calculate_valuation(self) -> float:
        return round(sum(item.total_value() for item in self._items.values()), 2)

    # ---------------- File Persistence ----------------
    def save_to_storage(self) -> None:
        """Persists all in-memory items to local JSON database."""
        try:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            serialized_data = [item.to_dict() for item in self._items.values()]
            with open(self.db_path, "w", encoding="utf-8") as f:
                json.dump(serialized_data, f, indent=4)
        except OSError as e:
            print(f"❌ Failed to write to disk: {e}")

    def load_from_storage(self) -> None:
        """Loads items from local JSON database on startup."""
        if not self.db_path.exists():
            return

        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

            if not isinstance(raw_data, list):
                raise StorageCorruptedError("Root element in database must be a list!")

            self._items.clear()
            for record in raw_data:
                item_type = record.get("type", "General")
                if item_type == "ServerAsset":
                    item = ServerAsset.from_dict(record)
                else:
                    item = Item.from_dict(record)
                self._items[item.item_id] = item

        except (json.JSONDecodeError, KeyError, StorageCorruptedError) as e:
            print(f"⚠️ Warning: Database file '{self.db_path}' is corrupted ({e}). Initializing clean state.")


# =====================================================================
# 4. Interactive CLI Interface
# =====================================================================

def prompt_int(message: str) -> int:
    while True:
        try:
            return int(input(message).strip())
        except ValueError:
            print("⚠️ Please enter a valid integer!")


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message).strip())
        except ValueError:
            print("⚠️ Please enter a valid number (e.g. 19.99)!")


def display_items_table(items: List[Item]) -> None:
    if not items:
        print("\nℹ️ No items found.")
        return

    print("\n" + "-" * 85)
    print(f"{'ID':<10} | {'Name':<22} | {'Category':<20} | {'Qty':<6} | {'Price':<10} | {'Total ($)':<10}")
    print("-" * 85)
    for it in items:
        print(f"{it.item_id:<10} | {it.name[:20]:<22} | {it.category[:18]:<20} | {it.quantity:<6} | ${it.price:<9.2f} | ${it.total_value():<9.2f}")
    print("-" * 85)


def run_inventory_cli() -> None:
    db_file = Path(__file__).parent / "data" / "inventory_db.json"
    manager = InventoryManager(db_file)

    while True:
        print("\n" + "=" * 60)
        print("  🏢 ENTERPRISE ASSET & INVENTORY MANAGEMENT SYSTEM")
        print("=" * 60)
        print("  [1] 📋 View All Items")
        print("  [2] ➕ Add General Item")
        print("  [3] 🖥️ Add Server/Hardware Asset")
        print("  [4] 🔄 Update Stock (Increase / Decrease)")
        print("  [5] 🔍 Search Items by Category")
        print("  [6] 🗑️ Delete Item")
        print("  [7] 📊 Inventory Valuation & Metrics")
        print("  [0] 🚪 Exit Application")

        choice = input("\nSelect Option (0-7): ").strip()

        try:
            if choice == "1":
                items = manager.list_all()
                display_items_table(items)

            elif choice == "2":
                print("\n--- Add General Item ---")
                item_id = input("Item ID (e.g. ITM-101): ").strip()
                name = input("Item Name: ").strip()
                category = input("Category (e.g. Office, Peripherals): ").strip()
                qty = prompt_int("Initial Quantity: ")
                price = prompt_float("Unit Price ($): ")

                new_item = Item(item_id, name, category, qty, price)
                manager.add_item(new_item)
                print(f"✅ Item '{name}' added successfully!")

            elif choice == "3":
                print("\n--- Add Server Infrastructure Asset ---")
                item_id = input("Server ID (e.g. SRV-01): ").strip()
                name = input("Hostname (e.g. redis-cluster-node): ").strip()
                ip_addr = input("IP Address (e.g. 10.0.1.50): ").strip()
                ram = prompt_int("RAM in GB (e.g. 64): ")
                qty = prompt_int("Node Count: ")
                cost = prompt_float("Monthly Cost per node ($): ")

                server = ServerAsset(item_id, name, qty, cost, ip_addr, ram)
                manager.add_item(server)
                print(f"✅ Server Asset '{name}' added successfully!")

            elif choice == "4":
                print("\n--- Update Stock ---")
                item_id = input("Enter Item ID: ").strip()
                print("Enter positive number to ADD stock, or negative number to DEDUCT.")
                delta = prompt_int("Stock change (e.g. 5 or -2): ")

                new_qty = manager.update_stock(item_id, delta)
                print(f"✅ Stock updated! Item '{item_id}' new quantity: {new_qty}")

            elif choice == "5":
                cat = input("\nEnter category keyword to search: ").strip()
                results = manager.search_by_category(cat)
                display_items_table(results)

            elif choice == "6":
                item_id = input("\nEnter Item ID to delete: ").strip()
                confirm = input(f"Are you sure you want to delete '{item_id}'? (yes/no): ").lower().strip()
                if confirm in {"y", "yes"}:
                    deleted = manager.remove_item(item_id)
                    print(f"🗑️ Item '{deleted.name}' deleted successfully.")
                else:
                    print("Deletion cancelled.")

            elif choice == "7":
                all_items = manager.list_all()
                total_qty = sum(i.quantity for i in all_items)
                total_val = manager.calculate_valuation()
                print("\n" + "=" * 40)
                print("       📈 INVENTORY METRICS")
                print("=" * 40)
                print(f"Total Unique Items: {len(all_items)}")
                print(f"Total Item Units:   {total_qty}")
                print(f"Total Valuation:    ${total_val:,.2f}")
                print("=" * 40)

            elif choice == "0":
                print("\n👋 Saving state & exiting system. Goodbye!\n")
                sys.exit(0)

            else:
                print("⚠️ Invalid choice! Please select 0 to 7.")

        except InventoryError as err:
            print(f"\n{err}")
        except Exception as ex:
            print(f"\n🚨 Unexpected error occurred: {ex}")


if __name__ == "__main__":
    run_inventory_cli()

import numpy as np

class InventoryManagement:
    def __init__(self, demand_history, holding_cost, ordering_cost, lead_time, initial_inventory):
        self.demand_history = demand_history
        self.holding_cost = holding_cost
        self.ordering_cost = ordering_cost
        self.lead_time = lead_time
        self.inventory_level = initial_inventory
        self.calculate_eoq()
        self.calculate_reorder_point()
        self.total_orders = 0
        self.total_cost = 0

    def calculate_eoq(self):
        avg_demand = np.mean(self.demand_history)
        self.eoq = int(np.sqrt((2 * avg_demand * self.ordering_cost) / self.holding_cost))
        
    def calculate_reorder_point(self):
        avg_demand = np.mean(self.demand_history)
        self.reorder_point = int(avg_demand * self.lead_time)
    
    def update_inventory(self, daily_demand):
        self.inventory_level -= daily_demand
        if self.inventory_level <= self.reorder_point:
            self.inventory_level += self.eoq
            self.total_orders += 1
            self.total_cost += (self.eoq * self.holding_cost) + self.ordering_cost

    def generate_report(self):
        return {
            "EOQ": self.eoq,
            "Reorder Point": self.reorder_point,
            "Current Inventory Level": self.inventory_level,
            "Total Orders Placed": self.total_orders,
            "Total Cost Incurred": self.total_cost
        }

# User Input
demand_history = list(map(int, input("Enter past demand values separated by spaces: ").split()))
holding_cost = float(input("Enter holding cost per unit: "))
ordering_cost = float(input("Enter ordering cost per order: "))
lead_time = int(input("Enter lead time in days: "))
initial_inventory = int(input("Enter initial inventory level: "))

daily_demands = list(map(int, input("Enter daily demands separated by spaces: ").split()))

# Initialize System
inventory_system = InventoryManagement(demand_history, holding_cost, ordering_cost, lead_time, initial_inventory)
print("Initial Report:", inventory_system.generate_report())

# Process Daily Demands
for demand in daily_demands:
    inventory_system.update_inventory(demand)
    print("Updated Report:", inventory_system.generate_report())
import random
import json

def generate_data():
    fleet = []
    for t_id in range(100, 150):
        # Planned vs Actual
        truck = {
            "id": f"TRUCK-{t_id}",
            "plan": {"dist_km": 2500, "eta_hrs": 120, "consumption_rate": 16},
            "logs": [] # Hourly data
        }
        fuel = 400
        for h in range(168):
            dist_moved = random.uniform(15, 25)
            # Simulate Fuel Theft (Anomaly)
            fuel_loss = (dist_moved / 100) * truck["plan"]["consumption_rate"]
            if t_id == 105 and h == 20: fuel -= 50 # Theft event
            fuel -= fuel_loss
            
            truck["logs"].append({
                "hour": h,
                "gps_deviation": random.uniform(0, 15) if t_id != 110 else random.uniform(0, 60),
                "fuel_level": fuel,
                "dist_covered": dist_moved,
                "road_block": random.choice([True, False]) if random.random() > 0.95 else False
            })
        fleet.append(truck)
        return fleet

fleet_data = generate_data()

def calculate_fleet_performance(fleet_data):
    # TODO: Calculate Total Fuel Consumed and Total Distance per truck
    # TODO: Calculate Efficiency Score: (Actual Consumption / Planned Consumption)
    # TODO: Create a Fleet Overview dictionary containing average efficiency of all trucks
    # TODO: Return the summary dictionary containing truck states and FLEET_AVG_EFFICIENCY
    pass

def detect_anomalies(fleet_data, fuel_drop_limit=10, gps_dev_limit=40):
    # TODO: Detect Fuel Theft: fuel_level drops by > fuel_drop_limit in a single hour while dist_covered is near zero
    # TODO: Detect Route Deviation: gps_deviation > gps_dev_limit for more than 3 consecutive hours
    # TODO: Return a dictionary of "Suspects" and the reason they were flagged
    pass

def generate_final_report(fleet_data):
    # TODO: Generate Fleet Performance Report using calculate_fleet_performance
    # TODO: Generate Anomalies Report using detect_anomalies
    # TODO: Create one single dictionary containing both the Report and the Anomalies
    # TODO: Beauty print dict (JSON like)
    pass

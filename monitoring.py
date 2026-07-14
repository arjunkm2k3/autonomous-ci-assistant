import json
import os
from datetime import datetime

class MetricsCollector:
    def __init__(self, file="data/metrics.json"):
        self.file = file
        os.makedirs(os.path.dirname(file), exist_ok=True)
        if not os.path.exists(file):
            with open(file, 'w') as f:
                json.dump({"total": 0, "success": 0, "history": []}, f)
        with open(file, 'r') as f:
            self.data = json.load(f)
    
    def record(self, success, error_type, time_taken):
        self.data["total"] += 1
        if success:
            self.data["success"] += 1
        self.data["history"].append({
            "timestamp": datetime.now().isoformat(),
            "success": success,
            "error_type": error_type,
            "duration": time_taken
        })
        with open(self.file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def summary(self):
        total = self.data["total"]
        success = self.data["success"]
        rate = f"{success/total*100:.1f}%" if total else "N/A"
        return {"total": total, "success": success, "success_rate": rate}
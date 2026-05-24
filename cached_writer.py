import json
import hashlib
from scenario_writer import ScenarioWriter

class CachedScenarioWriter:
    def __init__(self):
        self.writer = ScenarioWriter()
        self.cache = {}  # In-memory cache
        self.cache_file = "scenario_cache.json"
        self.load_cache()
    
    def get_cache_key(self, input_data):
        """Create unique key from input"""
        input_str = json.dumps(input_data, sort_keys=True)
        return hashlib.md5(input_str.encode()).hexdigest()
    
    def load_cache(self):
        """Load cached results from file"""
        try:
            with open(self.cache_file, 'r') as f:
                self.cache = json.load(f)
            print(f"✅ Loaded {len(self.cache)} cached scenarios")
        except FileNotFoundError:
            self.cache = {}
    
    def save_cache(self):
        """Save cache to file"""
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=2)
        print(f"✅ Saved {len(self.cache)} scenarios to cache")
    
    def generate_scenario(self, input_data):
        """Generate with caching - same input = same output"""
        cache_key = self.get_cache_key(input_data)
        
        # Return cached result if exists
        if cache_key in self.cache:
            print("📦 Returning cached result")
            return self.cache[cache_key]
        
        # Generate new scenario
        result = self.writer.generate_scenario(input_data)
        
        # Save to cache
        self.cache[cache_key] = result
        self.save_cache()
        
        return result

# Usage
if __name__ == "__main__":
    writer = CachedScenarioWriter()
    
    # First call - generates
    result1 = writer.generate_scenario({
        "icp_type": "high_wage",
        "milestone_code": "M01",
        "skill_target": "communication",
        "language": "en"
    })
    
    # Second call with same input - returns cached result
    result2 = writer.generate_scenario({
        "icp_type": "high_wage",
        "milestone_code": "M01",
        "skill_target": "communication",
        "language": "en"
    })
    
    # Both outputs will be identical
    print(f"Same output: {result1 == result2}")
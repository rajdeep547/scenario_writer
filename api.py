from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from scenario_writer_mock import ScenarioWriter
import uvicorn

app = FastAPI(title="Scenario Writer API")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize scenario writer
writer = ScenarioWriter()

# Request model
class ScenarioRequest(BaseModel):
    icp_type: str
    milestone_code: str
    skill_target: str
    language: str

# Response model
class ScenarioResponse(BaseModel):
    success: bool
    data: Optional[dict] = None
    error: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Scenario Writer API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/generate-scenario")
async def generate_scenario(request: ScenarioRequest):
    print(f"📥 Received request: {request.icp_type} | {request.skill_target}")
    
    try:
        # Validate inputs
        if request.icp_type not in ["high_wage", "low_wage"]:
            return {"success": False, "error": "icp_type must be 'high_wage' or 'low_wage'"}
        
        if request.language not in ["en", "hi"]:
            return {"success": False, "error": "language must be 'en' or 'hi'"}
        
        # Generate scenario
        input_data = {
            "icp_type": request.icp_type,
            "milestone_code": request.milestone_code,
            "skill_target": request.skill_target,
            "language": request.language
        }
        
        output = writer.generate_scenario(input_data)
        
        print(f"✅ Generated scenario for: {request.icp_type}")
        
        return {"success": True, "data": output}
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
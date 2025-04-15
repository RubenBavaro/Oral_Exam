from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from PickRandomStudentBAVARO import get_students


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=False,  # Must be False when allow_origins=["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/students")
async def get_all_students():
    return {"students": get_students()}


# Start the server with uvicorn if this file is run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
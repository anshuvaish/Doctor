from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import subprocess, time

app = FastAPI()

@app.post("/scrape")
def scrape(city: str = Form(...), keyword: str = Form(...), radius_km: float = Form(...)):
    # Trigger your scraper script internally without exposing code
    subprocess.run(["python", "google_scrapper.py"], input=f"{city}\n{keyword}\n{radius_km}\n", text=True)
    
    # 5 min wait simulation
    time.sleep(300)

    file_name = f"Doctors_{city}_{keyword}_{radius_km}KM.csv"
    return {"download_file": file_name}

@app.get("/download/{file_name}")
def download(file_name: str):
    return FileResponse(file_name, filename=file_name, media_type="text/csv")

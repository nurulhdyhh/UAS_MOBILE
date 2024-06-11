from fastapi import FastAPI, HTTPException, File, Query, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import FileResponse
import shutil
import os
import firebase_admin # type: ignore
from firebase_admin import credentials, auth # type: ignore

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate("D:/mobileUAS/flutter_app/uas-mobile-607b2-firebase-adminsdk-d3iej-680b9970d0.json")
firebase_admin.initialize_app(cred)

# Model untuk LaundryShop
class LaundryShop(BaseModel):
    name: str
    rating: float
    address: str
    type: str
    image_url: str
    description: str  
    price: str  

# Data laundries awal
laundries = [
    LaundryShop(name= "Umbah-Umbah", rating=4,address= "Jln Rungkut Madya UPN", type= "Regular", image_url="https://et2o98r3gkt.exactdn.com/wp-content/uploads/2022/09/Ide-Konsep-Desain-Gerai-Bisnis-Laundry-yang-Menarik.jpg?strip=all&lossy=1&quality=92&webp=92&ssl=1&fit=770%2C514",description="Selamat datang di Umbah-Umbah Laundry, solusi terbaik untuk kebutuhan laundry Anda! Kami adalah penyedia jasa laundry terpercaya yang siap membantu Anda meraih kebersihan maksimal dengan pelayanan prima. Dengan mengutamakan kualitas dan kepuasan pelanggan, kami menyediakan berbagai layanan, mulai dari cuci kiloan, dry cleaning, hingga layanan setrika dan lipat. \nKeunggulan Kami:\n1. Layanan Cepat dan Tepat Waktu: Kami memahami betapa berharganya waktu Anda. Oleh karena itu, kami selalu berusaha memberikan pelayanan yang cepat dan tepat waktu tanpa mengurangi kualitas.\n2. Kualitas Terjamin: Menggunakan deterjen dan pelembut berkualitas tinggi, serta mesin cuci modern, kami memastikan setiap pakaian Anda bersih, harum, dan terawat dengan baik.\n3. Harga Terjangkau: Menawarkan harga yang kompetitif dengan berbagai paket menarik untuk memenuhi kebutuhan Anda tanpa harus merogoh kocek dalam-dalam.Tenaga Profesional: Tim kami terdiri dari tenaga profesional dan berpengalaman yang siap melayani Anda dengan ramah dan sopan.Layanan Antar Jemput", price="Rp8.000 /Kg"),
    LaundryShop(name= "Lively Laundry", rating=4.5, address="Jln. Rungkut Menanggal", type="Express", image_url="https://i0.wp.com/media.dekoruma.com/article/2023/08/23105601/desain-tempat-cuci-baju-dan-jemuran-sederhana-bernuansa-krem.jpg?resize=900%2C600&ssl=1",description="Selamat datang di Lively Laundry, tempat di mana kebersihan bertemu kenyamanan. Kami adalah destinasi terbaik Anda untuk semua kebutuhan laundry, di mana kami memadukan teknologi modern dengan sentuhan pribadi untuk memberikan hasil yang bersih, harum, dan terawat dengan baik. Dengan layanan yang cepat, ramah, dan terjangkau, kami memastikan setiap pelanggan mendapatkan pengalaman laundry yang menyenangkan dan memuaskan. Dari laundry kiloan hingga dry cleaning, setrika, lipat, dan perawatan sepatu, kami siap mengatasi semua kebutuhan Anda dengan profesionalisme dan keahlian. Percayakan pakaian Anda kepada Sparkle Clean Laundry dan nikmati hasil yang tak tertandingi. Hubungi kami sekarang untuk pengalaman laundry yang menyenangkan dan praktis!", price="Rp5.000 /Kg"),
    LaundryShop(name= "Ngumbahyuk Laundry",rating= 5,address= "Jln Kali Rungkut",type= "Regular", image_url= "https://lh6.googleusercontent.com/SGOWlY45_rjF3JwsSnaa33wjAADPhMzmruanH-DDqYrQcnd8EFBFKUf8UfBAomU1f_6C9dtIH6wVYhpPD8d5ZhO_ooxGanhaR8Q445EMMeHoQUXrqueshXqEG7bA5ISknqxH2Bw",description= "Ngumbahyuk hadir untuk meringankan beban kalian yang penuh itu, Yuk di order segera dijamin cucian bakal harum dan bersih kembali",price= "Rp8.000/ Kg"),
    LaundryShop(name= "NyuciKuy Laundry",rating= 5,address= "Jln Ir Soekarno",type= "Regular", image_url= "https://lh6.googleusercontent.com/SGOWlY45_rjF3JwsSnaa33wjAADPhMzmruanH-DDqYrQcnd8EFBFKUf8UfBAomU1f_6C9dtIH6wVYhpPD8d5ZhO_ooxGanhaR8Q445EMMeHoQUXrqueshXqEG7bA5ISknqxH2Bw",description= "Ngumbahyuk hadir untuk meringankan beban kalian yang penuh itu, Yuk di order segera dijamin cucian bakal harum dan bersih kembali",price= "Rp8.000/ Kg"),
    LaundryShop(name= "Ngumbahyuk Laundry",rating= 5,address= "Jln Medokan Barat",type= "Express", image_url= "https://lh6.googleusercontent.com/SGOWlY45_rjF3JwsSnaa33wjAADPhMzmruanH-DDqYrQcnd8EFBFKUf8UfBAomU1f_6C9dtIH6wVYhpPD8d5ZhO_ooxGanhaR8Q445EMMeHoQUXrqueshXqEG7bA5ISknqxH2Bw",description= "Ngumbahyuk hadir untuk meringankan beban kalian yang penuh itu, Yuk di order segera dijamin cucian bakal harum dan bersih kembali",price= "Rp8.000/ Kg"),
]
# Endpoint untuk mendapatkan semua laundries
@app.get("/", response_model=List[LaundryShop])
def get_all_laundries():
    return laundries

# Endpoint untuk mendapatkan semua laundries
@app.get("/laundries", response_model=List[LaundryShop])
def get_laundries(type: Optional[str] = None):
    if type:
        return [laundry for laundry in laundries if laundry.type.lower() == type.lower()]
    return laundries

# Endpoint untuk mencari laundries berdasarkan kata kunci
@app.get("/laundries/search", response_model=List[LaundryShop])
def search_laundries(keyword: str = Query(...)):
    filtered_laundries = [laundry for laundry in laundries if keyword.lower() in laundry.address.lower()]
    return filtered_laundries

# Endpoint untuk menambahkan laundry baru
@app.post("/laundries/add", response_model=LaundryShop)
def add_laundry(new_laundry: LaundryShop):
    laundries.append(new_laundry)
    return new_laundry

# Endpoint untuk mengunggah gambar
@app.post("/uploadimage")
async def upload_image(file: UploadFile = File(...)):
    file_location = f"images/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

# Endpoint untuk mengambil gambar
@app.get("/getimage/{filename}")
async def get_image(filename: str):
    file_path = f"images/{filename}"
    if os.path.exists(file_path):
        return FileResponse(path=file_path)
    else:
        raise HTTPException(status_code=404, detail="Image not found")
        
@app.put("/laundries/{laundry_id}")
def update_laundry(laundry_id: int, updated_laundry: LaundryShop):
    if laundry_id >= len(laundries) or laundry_id < 0:
        raise HTTPException(status_code=404, detail="Laundry not found")

    laundries[laundry_id] = updated_laundry
    return updated_laundry

# Endpoint untuk tes hasil
@app.get("/test-results")
def get_test_results():
    return {
        "status": "success",
        "tests_run": 5,
        "tests_passed": 5,
        "tests_failed": 0,
    }

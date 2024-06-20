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
<<<<<<< HEAD
cred = credentials.Certificate("D:/project/flutter_app/uas-mobile-607b2-firebase-adminsdk-d3iej-680b9970d0.json")
=======
cred = credentials.Certificate("D:/mobileUAS/flutter_app/uas-mobile-607b2-firebase-adminsdk-d3iej-680b9970d0.json")
>>>>>>> 27e2af3dc0095abbf5bce401abd61bcab0bb51c7
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
<<<<<<< HEAD
    LaundryShop(name="Laundry Bersih", rating=4.2, address="Jln Nginden", type="Regular", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBK-LYCmJKCkm2rulF7H7gO3VSsQ4KnzvGDUFB7b8lTcaMXjcTodIgaW3I6pVk1YrgqJ8&usqp=CAU", description="Laundry cepat dan bersih dengan harga terjangkau.", price="Rp7.000 /Kg"),
    LaundryShop(name="Sparkle Laundry", rating=4.8, address="Jln Gubeng", type="Express", image_url="https://lh6.googleusercontent.com/SGOWlY45_rjF3JwsSnaa33wjAADPhMzmruanH-DDqYrQcnd8EFBFKUf8UfBAomU1f_6C9dtIH6wVYhpPD8d5ZhO_ooxGanhaR8Q445EMMeHoQUXrqueshXqEG7bA5ISknqxH2Bw", description="Pakaian bersih dan wangi dalam waktu singkat.", price="Rp10.000 /Kg"),
    LaundryShop(name="Clean Wash", rating=4.1, address="Jln Diponegoro", type="Regular", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRU9CNsZCB4EtLEUA5COJ6EJIMBsjLE-A1LrN_1w0dk9Cq2KzCoURO0jzmtEnLMliS1cX8&usqp=CAU", description="Layanan laundry terbaik dengan hasil maksimal.", price="Rp8.000 /Kg"),
    LaundryShop(name="Fresh Laundry", rating=4.7, address="Jln Ahmad Yani", type="Express", image_url="https://i0.wp.com/media.dekoruma.com/article/2023/08/23105601/desain-tempat-cuci-baju-dan-jemuran-sederhana-bernuansa-krem.jpg?resize=900%2C600&ssl=1", description="Laundry ekspres dengan kualitas terbaik.", price="Rp9.000 /Kg"),
    LaundryShop(name="CuciBersih", rating=4.5, address="Jln Sudirman", type="Regular", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Laundry terpercaya di Surabaya.", price="Rp8.500 /Kg"),
    LaundryShop(name="Quick Clean", rating=4.6, address="Jln Basuki Rahmat", type="Express", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Cepat, bersih, dan terjangkau.", price="Rp9.500 /Kg"),
    LaundryShop(name="LaundryKu", rating=4.3, address="Jln Dr Soetomo", type="Regular", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Layanan laundry dengan hasil memuaskan.", price="Rp8.000 /Kg"),
    LaundryShop(name="Super Laundry", rating=4.9, address="Jln Tunjungan", type="Express", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSl3G5Cb-WL3jLTRJUzViEObDAkWbELA-NSk07SdtXfAvY5hTRpznVtZKa1CRjgAYhyaLo&usqp=CAU", description="Laundry super cepat dengan kualitas tinggi.", price="Rp11.000 /Kg"),
    LaundryShop(name="Eco Laundry", rating=4.4, address="Jln Darmo", type="Regular", image_url="https://lh6.googleusercontent.com/SGOWlY45_rjF3JwsSnaa33wjAADPhMzmruanH-DDqYrQcnd8EFBFKUf8UfBAomU1f_6C9dtIH6wVYhpPD8d5ZhO_ooxGanhaR8Q445EMMeHoQUXrqueshXqEG7bA5ISknqxH2Bw", description="Laundry ramah lingkungan.", price="Rp7.500 /Kg"),
    LaundryShop(name="Perfect Wash", rating=4.6, address="Jln Pucang", type="Express", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Hasil laundry sempurna setiap saat.", price="Rp10.000 /Kg"),
    LaundryShop(name="Laundry Express", rating=4.7, address="Jln Genteng", type="Express", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Layanan laundry cepat dan handal.", price="Rp9.000 /Kg"),
    LaundryShop(name="Happy Laundry", rating=4.3, address="Jln Kertajaya", type="Regular", image_url="https://asset.kompas.com/crops/pILuKHN3cTAYrFY7xXdzq6CqzAs=/0x0:1000x667/750x500/data/photo/2021/08/06/610d637d226ef.jpg", description="Kebersihan yang membuat bahagia.", price="Rp8.500 /Kg"),
    LaundryShop(name="Pro Laundry", rating=4.5, address="Jln Menur", type="Express", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Profesional dan terpercaya.", price="Rp9.500 /Kg"),
    LaundryShop(name="Top Clean", rating=4.8, address="Jln Tambaksari", type="Regular", image_url="https://akcdn.detik.net.id/visual/2022/07/05/ilustrasi-laundry-room_169.jpeg?w=750&q=90", description="Laundry dengan kualitas teratas.", price="Rp8.000 /Kg"),
    LaundryShop(name="Fast Laundry", rating=4.6, address="Jln Kapasari", type="Express", image_url="https://image.popmama.com/content-images/post/20240130/Foto%20Ruang%20Laundry%20Tasyi%20Athasyia%20di%20Rumah%20Baru-0tVD8gYjl807afybjAYSVr507vZz9Xll.jpg", description="Layanan laundry kilat.", price="Rp10.000 /Kg"),
    LaundryShop(name="Clean & Fresh", rating=4.4, address="Jln Pacar", type="Regular", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Pakaian bersih dan segar setiap hari.", price="Rp7.000 /Kg"),
    LaundryShop(name="Bersih Laundry", rating=4.5, address="Jln Dharmawangsa", type="Regular", image_url="https://pbs.twimg.com/media/FZZy9cnVQAAD8gl?format=jpg&name=900x900", description="Layanan laundry dengan hasil memuaskan.", price="Rp8.000 /Kg"),
    LaundryShop(name="LaundryPro", rating=4.7, address="Jln Semolowaru", type="Express", image_url="https://pbs.twimg.com/media/FZZy9cnVQAAD8gl?format=jpg&name=900x900", description="Layanan laundry profesional.", price="Rp9.500 /Kg"),
    LaundryShop(name="Suci Laundry", rating=4.3, address="Jln Kenjeran", type="Regular", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSl3G5Cb-WL3jLTRJUzViEObDAkWbELA-NSk07SdtXfAvY5hTRpznVtZKa1CRjgAYhyaLo&usqp=CAU", description="Laundry cepat dan bersih.", price="Rp8.000 /Kg"),
    LaundryShop(name="Wash&Go", rating=4.5, address="Jln Jagir", type="Express", image_url="https://ik.imagekit.io/pashouses/pandu/pages/wp-content/uploads/2023/04/washing-machine-minimal-laundry-room-interior-design-2048x1366.jpg", description="Laundry ekspres dengan kualitas terbaik.", price="Rp10.000 /Kg"),
    LaundryShop(name="Pristine Laundry", rating=4.8, address="Jln Wonokromo", type="Regular", image_url="https://asset.kompas.com/crops/pILuKHN3cTAYrFY7xXdzq6CqzAs=/0x0:1000x667/750x500/data/photo/2021/08/06/610d637d226ef.jpg", description="Layanan laundry dengan hasil maksimal.", price="Rp8.500 /Kg"),
    LaundryShop(name="Clean Zone", rating=4.6, address="Jln Bratang", type="Express", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Laundry cepat dan terpercaya.", price="Rp9.000 /Kg"),
    LaundryShop(name="Laundry King", rating=4.7, address="Jln Ngagel", type="Regular", image_url="https://asset.kompas.com/crops/pILuKHN3cTAYrFY7xXdzq6CqzAs=/0x0:1000x667/750x500/data/photo/2021/08/06/610d637d226ef.jpg", description="Raja laundry dengan hasil terbaik.", price="Rp8.000 /Kg"),
    LaundryShop(name="Laundry Rapi", rating=4.5, address="Jln Nginden", type="Express", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSl3G5Cb-WL3jLTRJUzViEObDAkWbELA-NSk07SdtXfAvY5hTRpznVtZKa1CRjgAYhyaLo&usqp=CAU", description="Laundry rapi dan cepat.", price="Rp9.500 /Kg"),
    LaundryShop(name="Bersih Sekali", rating=4.4, address="Jln Kalirungkut", type="Regular", image_url="https://lh6.googleusercontent.com/SGOWlY45_rjF3JwsSnaa33wjAADPhMzmruanH-DDqYrQcnd8EFBFKUf8UfBAomU1f_6C9dtIH6wVYhpPD8d5ZhO_ooxGanhaR8Q445EMMeHoQUXrqueshXqEG7bA5ISknqxH2Bw", description="Pakaian bersih setiap saat.", price="Rp7.000 /Kg"),
    LaundryShop(name="Sparkling Laundry", rating=4.7, address="Jln Lidah Wetan", type="Express", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Laundry cepat dengan hasil terbaik.", price="Rp10.000 /Kg"),
    LaundryShop(name="Laundry Sukses", rating=4.6, address="Jln Dukuh Kupang", type="Regular", image_url="https://ik.imagekit.io/pashouses/pandu/pages/wp-content/uploads/2023/04/washing-machine-minimal-laundry-room-interior-design-2048x1366.jpg", description="Layanan laundry sukses dan bersih.", price="Rp8.500 /Kg"),
    LaundryShop(name="Cepat Bersih", rating=4.8, address="Jln Rungkut Industri", type="Express", image_url="https://lh6.googleusercontent.com/SGOWlY45_rjF3JwsSnaa33wjAADPhMzmruanH-DDqYrQcnd8EFBFKUf8UfBAomU1f_6C9dtIH6wVYhpPD8d5ZhO_ooxGanhaR8Q445EMMeHoQUXrqueshXqEG7bA5ISknqxH2Bw", description="Layanan laundry cepat dan bersih.", price="Rp9.000 /Kg"),
    LaundryShop(name="Laundry Ceria", rating=4.5, address="Jln Kutisari", type="Regular", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBK-LYCmJKCkm2rulF7H7gO3VSsQ4KnzvGDUFB7b8lTcaMXjcTodIgaW3I6pVk1YrgqJ8&usqp=CAU", description="Laundry ceria dengan hasil maksimal.", price="Rp8.000 /Kg"),
    LaundryShop(name="Clean Spark", rating=4.7, address="Jln Ketintang", type="Express", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxdwYLnSzWmlHdnK0u06OFjcT9qMOFxKRerAUj9zaVJsrGDfMJtcuOJd0-fiUfHO94Km4&usqp=CAU", description="Laundry bersih dan cepat.", price="Rp10.000 /Kg"),

=======
>>>>>>> 27e2af3dc0095abbf5bce401abd61bcab0bb51c7
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

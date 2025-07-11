import random

def generate(source):
    chapter = random.randint(1, 114)
    verse = random.randint(1, source[chapter-1][2])
    return f'{source[chapter-1][0]} [{chapter}:{verse}]'

quran_chapters_info = [
    ("Al-Fatiha", 1, 7), ("Al-Baqarah", 2, 286), ("Aal-E-Imran", 3, 200), ("An-Nisa", 4, 176), ("Al-Ma'idah", 5, 120),
    ("Al-An'am", 6, 165), ("Al-A'raf", 7, 206), ("Al-Anfal", 8, 75), ("At-Tawbah", 9, 129), ("Yunus", 10, 109),
    ("Hud", 11, 123), ("Yusuf", 12, 111), ("Ar-Ra'd", 13, 43), ("Ibrahim", 14, 52), ("Al-Hijr", 15, 99), ("An-Nahl", 16, 128),
    ("Al-Isra", 17, 111), ("Al-Kahf", 18, 110), ("Maryam", 19, 98), ("Taha", 20, 135), ("Al-Anbiya", 21, 112),
    ("Al-Hajj", 22, 78), ("Al-Mu'minun", 23, 118), ("An-Nur", 24, 64), ("Al-Furqan", 25, 77), ("Ash-Shu'ara", 26, 227),
    ("An-Naml", 27, 93), ("Al-Qasas", 28, 88), ("Al-Ankabut", 29, 69), ("Ar-Rum", 30, 60), ("Luqman", 31, 34),
    ("As-Sajda", 32, 30), ("Al-Ahzab", 33, 73), ("Saba", 34, 54), ("Fatir", 35, 45), ("Ya-Sin", 36, 83),
    ("As-Saffat", 37, 182), ("Sad", 38, 88), ("Az-Zumar", 39, 75), ("Ghafir", 40, 85), ("Fussilat", 41, 54),
    ("Ash-Shura", 42, 53), ("Az-Zukhruf", 43, 89), ("Ad-Dukhan", 44, 59), ("Al-Jathiya", 45, 37), ("Al-Ahqaf", 46, 35),
    ("Muhammad", 47, 38), ("Al-Fath", 48, 29), ("Al-Hujurat", 49, 18), ("Qaf", 50, 45), ("Adh-Dhariyat", 51, 60),
    ("At-Tur", 52, 49), ("An-Najm", 53, 62), ("Al-Qamar", 54, 55), ("Ar-Rahman", 55, 78), ("Al-Waqi'a", 56, 96),
    ("Al-Hadid", 57, 29), ("Al-Mujadila", 58, 22), ("Al-Hashr", 59, 24), ("Al-Mumtahina", 60, 13), ("As-Saff", 61, 14),
    ("Al-Jumu'a", 62, 11), ("Al-Munafiqun", 63, 11), ("At-Taghabun", 64, 18), ("At-Talaq", 65, 12), ("At-Tahrim", 66, 12),
    ("Al-Mulk", 67, 30), ("Al-Qalam", 68, 52), ("Al-Haqqa", 69, 52), ("Al-Ma'arij", 70, 44), ("Nuh", 71, 28),
    ("Al-Jinn", 72, 28), ("Al-Muzzammil", 73, 20), ("Al-Muddaththir", 74, 56), ("Al-Qiyama", 75, 40), ("Al-Insan", 76, 31),
    ("Al-Mursalat", 77, 50), ("An-Naba", 78, 40), ("An-Nazi'at", 79, 46), ("Abasa", 80, 42), ("At-Takwir", 81, 29),
    ("Al-Infitar", 82, 19), ("Al-Mutaffifin", 83, 36), ("Al-Inshiqaq", 84, 25), ("Al-Buruj", 85, 22), ("At-Tariq", 86, 17),
    ("Al-A'la", 87, 19), ("Al-Ghashiya", 88, 26), ("Al-Fajr", 89, 30), ("Al-Balad", 90, 20), ("Ash-Shams", 91, 15),
    ("Al-Lail", 92, 21), ("Ad-Duha", 93, 11), ("Ash-Sharh", 94, 8), ("At-Tin", 95, 8), ("Al-Alaq", 96, 19),
    ("Al-Qadr", 97, 5), ("Al-Bayyina", 98, 8), ("Az-Zalzalah", 99, 8), ("Al-Adiyat", 100, 11), ("Al-Qari'a", 101, 11),
    ("At-Takathur", 102, 8), ("Al-Asr", 103, 3), ("Al-Humazah", 104, 9), ("Al-Fil", 105, 5), ("Quraysh", 106, 4),
    ("Al-Ma'un", 107, 7), ("Al-Kawthar", 108, 3), ("Al-Kafirun", 109, 6), ("An-Nasr", 110, 3), ("Al-Masad", 111, 5),
    ("Al-Ikhlas", 112, 4), ("Al-Falaq", 113, 5), ("An-Nas", 114, 6)
]

[print(generate(quran_chapters_info)) for _ in range(1)]

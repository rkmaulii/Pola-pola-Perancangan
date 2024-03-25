class BMI:
    __instance = None
    def __init__(self, berat, tinggi):
        if BMI.__instance is not None:
            raise Exception("Hanya diizinkan memiliki satu objek BMI")
        BMI.__instance = self
        self.berat = berat
        self.tinggi = tinggi

    @staticmethod
    def get_instance():
        if BMI.__instance is None:
            BMI.__instance = BMI(0, 0)
        return BMI.__instance

    def rumus_bmi(self):
        return self.berat / (self.tinggi ** 2) 

    def kategori_bmi(self, bmi):
        if bmi < 17.0:
            return "Sangat Kurus"
        elif 17.0 <= bmi <= 18.4:
            return "Kurus"
        elif 18.5 <= bmi <= 22.9:
            return "Normal"
        elif 23.0 <= bmi <= 24.9:
            return "Kelebihan berat badan"
        else:
            return "Obesitas"


# Contoh penggunaan, satuan berat dalam kilogram(kg), satuan tinggi dalam meter(m)
bmi = BMI.get_instance()
bmi.berat = 50
bmi.tinggi = 1.53

hasil_bmi = bmi.rumus_bmi()
kategori = bmi.kategori_bmi(hasil_bmi)

print (f"Berat badan anda: {bmi.berat}kg dan Tinggi Badan anda: {bmi.tinggi}M")
print(f"BMI anda: {hasil_bmi}, Anda masuk dalam kategori {kategori}")
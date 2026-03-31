# Ime: Šejla Valjevac
# Datum: 25.03.2026.
# Lab 4: Python za FastAPI

# 1
student = {"Ime":"Šejla", "Prezime":"Valjevac", "Godina":3, "email":"sejla.valjevac@fet.ba", "Aktivan":True}
print(student)
print(student["Ime"])

#2

"Potpis funkcije get_student_info"
def get_student_info(name: str, year: int, email: str) -> dict:
    "Vraca rjecnik sa informacijama o studentu"
    return {
        "name": name,
        "year": year,
        "email": email,
        "greeting": f"Zdravo {name}, vi ste {year} godina studija, vas email je {email}"
    }
    
def ispisi_poziv(func):
    def wrapper(*args, **kwargs):
        print(f"Pozivam: {func.__name__}")
        rezultat=func(*args, **kwargs)
        return rezultat
    return wrapper
@ispisi_poziv
def info_o_studentu(ime: str, godina: int) -> dict:
     return {
        "name": ime,
        "year": godina,
        "greeting": f"Zdravo {ime}, vi ste {godina} godina studija"
    }
     
rezultat=info_o_studentu("Ana",3)
print(rezultat)


class Course:
    def __init__(self, name: str, code: str, credits: int, professor: str):
        self.name = name
        self.code = code
        self.credits = credits
        self.professor= professor

    def description(self) -> str:
        return f"{self.code} - {self.name} ({self.credits} kredita) {self.professor}"
    
k1=Course(name="Razvoj telekomunikacijske programske podrske", code="TK207", credits=6, professor="Alma Secerbegovic")
k2=Course(name="Opticke telekomunikacije", code="TK302", credits=6, professor="Aljo Mujcic")

students= [
    {"name": "Amina", "year": 3, "brindeks":123 ,"email": "amina@untz.ba"},
    {"name": "Emir", "year": 2, "brindeks":321 ,"email": "emir@untz.ba"},  
    {"name": "Sejla", "year": 3, "brindeks":456, "email":"sejla@unty.ba"},
    {"name":"Lejla", "year":1, "brindeks":654, "email":"lejla@unty.ba"}
    
]

def filter_by_year(students: list, year: int)->list:
    students_filtered_by_year=[]
    for row in students:
        if row["year"]==year:
            students_filtered_by_year.append(row)
    return students_filtered_by_year

f1=filter_by_year(students,3)
print(f1)

def print_registry(students: list)->None:
    for row in students:
       print("Ime studenta:", row["name"], ",email studenta:", row["email"])
    
print_registry(students)
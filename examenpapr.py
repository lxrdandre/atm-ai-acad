import tkinter as tk
from tkinter import font
import random
import re

# Baza de date originala
quiz_data = [
    {"question": "1. Circuitele FPGA sunt eficiente in aplicatii de tipul beam-forming deoarece:", "options": ["permit reconfigurarea rapida in functie de tipul aplicatiei: sonar, radar, software-defined radio, etc", "permit un upgrade rapid al configuratiei ASIC postvanzare", "permit procesarea spatiala eficienta si a unui numar mare de semnale in paralel", "intarzierea asupra tuturor semnalelor este constanta, indiferent de numarul acestora"], "correct": "permit procesarea spatiala eficienta si a unui numar mare de semnale in paralel"},
    {"question": "2. Despre retelele globale de distributie a semnalelor intr-un FPGA se poate spune:", "options": ["conduc semnalele cu defazari reduse pe distante scurte fara refacerea semnalelor", "conduc semnalele cu orice intarzieri pe distante relativ constante", "conduc semnalele in zone variabile cu intarzieri variabile", "conduc semnalele pe orice distanta cu intarzieri relativ constante"], "correct": "conduc semnalele pe orice distanta cu intarzieri relativ constante"},
    {"question": "3. In sistemele reconfigurabile se poate spune ca performanta maxima se obtine prin:", "options": ["paralelizarea structurilor iterative si executia secventiala a codului", "adaptarea la particularitatile procesorului", "adaptarea structurii hardware si a interconexiunilor la particularitatile aplicatiei", "adaptarea particularitatilor aplicatiei la structura hardware si a interconexiunilor"], "correct": "adaptarea structurii hardware si a interconexiunilor la particularitatile aplicatiei"},
    {"question": "4. Care dintre cele de mai jos reprezinta componenta unui Logic Element responsabila cu stocarea/reprezentarea unei functii logice de mai multe variabile logice?", "options": ["LUT", "crossbar switch", "multiplexor", "bistabil"], "correct": "LUT"},
    {"question": "5. Consideram urmatoarele doua afirmatii: 1) Circuitele FPGA sunt folosite in situatii in care este necesara o performanta ridicata si un cost relativ scazut 2) Microprocesoarele sunt folosite doar in situatii in care performanta nu conteaza, iar bugetul este ridicat/nu conteaza. Cu privire la valoarea de adevar a acestora, se poate spune ca:", "options": ["P1 este adevarata, P2 este falsa", "P1 este falsa, P2 este adevarata", "P1 este falsa, P2 este falsa", "P1 este adevarata, P2 este adevarata"], "correct": "P1 este adevarata, P2 este falsa"},
    {"question": "6. Care dintre urmatoarele afirmatii despre platform FPGA sunt adevarate?", "options": ["Ofera o zona de FPGA generic si blocuri functionale dedicate (CPU, RAM, DSP)", "Structura de interconexiuni este fixa si se poate schimba doar functia blocurilor", "Structura logica este fixa si se pot schimba doar interconexiunile", "Intregul FPGA este format din blocuri functionale dedicate (CPU, RAM, DSP)"], "correct": "Ofera o zona de FPGA generic si blocuri functionale dedicate (CPU, RAM, DSP)"},
    {"question": "7. Despre interconexiunile realizate cu linii bidirectionale se poate spune ca:", "options": ["jumatate dintre driver-ele tristate active raman neutilizate, ceea ce poate fi considerat ineficient", "driver-ele tristate active realizeaza interconexiunile iar cele inactive ocupa inutil suprafata FPGA, ceea ce poate fi considerat ineficient", "toate driver-ele tristate contribuie simultan la realizarea interconexiunilor, fiind o solutie eficienta", "jumatate dintre driver-ele tristate active sunt utilizate, ceea ce poate fi considerat ineficient"], "correct": "jumatate dintre driver-ele tristate active raman neutilizate, ceea ce poate fi considerat ineficient"},
    {"question": "8. Despre un multiplexor cu 4 intrari logice se poate spune ca:", "options": ["va produce o intarziere constanta, indiferent de tipul implementarii", "poate fi implementat cu PASS TRANSISTOR cu cel mult doua etaje logice", "poate fi implementat cu porti logice dar ocupa o suprafata mai mare decat structura echivalenta cu PASS TRANSISTOR", "va produce o deformare a semnalelor, indiferent de tipul implementarii"], "correct": "poate fi implementat cu porti logice dar ocupa o suprafata mai mare decat structura echivalenta cu PASS TRANSISTOR"},
    {"question": "9. Structura care integreaza in mod fix elementele functionale majore ale unui sistem de calcul (memorie, procesor, periferice, interfete) poarta denumirea de:", "options": ["SoPC", "PC", "SoC", "custom silicon"], "correct": "SoC"},
    {"question": "10. Care dintre urmatoarele sunt adevarate in ceea ce priveste implementarea unui circuit cu ajutorul PASS TRANSISTOR-ilor?", "options": ["Energia consumata este mai mare decat la portile logice", "Semnalul este atenuat de catre fiecare nod/tranzistor", "Suprafata fizica ocupata este mai mare decat la portile logice", "Semnalul este regenerat de catre fiecare nod/tranzistor"], "correct": "Semnalul este atenuat de catre fiecare nod/tranzistor"},
    {"question": "11. Legea lui Rent descrie:", "options": ["regulile de amplasare a circuitelor logice pe suprafata FPGA-ului", "relatia dintre numarul de LE si numarul de pini", "energia consumata de circuit in functie de frecventa de functionare", "relatia dintre numarul de LE si suprafata interconexiunilor"], "correct": "relatia dintre numarul de LE si numarul de pini"},
    {"question": "12. Din punct de vedere al eficientei energetice, in mod comparativ, intre FPGA si ASIC este adevarata urmatoarea afirmatie:", "options": ["ASIC-urile au tensiuni de functionare mai scazute, deci sunt mai eficiente", "FPGA-urile sunt mai eficiente pentru ca structura logica si matricea de interconexiuni sunt programabile", "FPGA-urile au tensiuni de functionare mai scazute, deci sunt mai eficiente", "ASIC-urile sunt mai eficiente pentru ca structura logica este optima si matricea de interconexiuni este mai redusa"], "correct": "ASIC-urile sunt mai eficiente pentru ca structura logica este optima si matricea de interconexiuni este mai redusa"},
    {"question": "13. Sistemele reconfigurabile permit:", "options": ["exploatarea paralelismului la un singur nivel, ales de catre software", "implementarea paralelismului la nivel software, prin adaptarea structurii software la nevoile hardware", "implementarea paralelismului la nivel software, in cazul algoritmilor iterativi", "exploatarea paralelismului la niveluri multiple, prin adaptarea structurii hardware la nevoile software"], "correct": "exploatarea paralelismului la niveluri multiple, prin adaptarea structurii hardware la nevoile software"},
    {"question": "14. Topologia de tip Network On Chip este caracterizata de:", "options": ["permite scalarea prin adaugarea de noduri si cresterea frecventei de functionare a fiecarui nod", "este o topologie folosita in echipamentele de retea", "se folosesc mai multe FPGA-uri pe aceeasi placa de circuit si sunt interconectate prin TCP/IP", "nodurile de pe chip schimba informatii sub forma de pachete de date"], "correct": "nodurile de pe chip schimba informatii sub forma de pachete de date"},
    {"question": "15. Hardware-ul de uz general implica:", "options": ["existenta unor unitati functionale reconfigurabile, optimizate pentru functii specifice", "existenta unor unitati functionale cu structura fixa, care opereaza asupra unor date de dimensiune fixa", "reconfigurarea constrangerilor pentru cai diferite de date pentru a elimina caracterul secvential", "optimizarea unitatilor functionale pentru fiecare aplicatie prin reconfigurare"], "correct": "existenta unor unitati functionale cu structura fixa, care opereaza asupra unor date de dimensiune fixa"},
    {"question": "16. Circuitele specializate avand structura logica fixa si functionalitate/destinatie fixa sunt:", "options": ["ASIC", "FPGA", "microcontroller", "microprocesor"], "correct": "ASIC"},
    {"question": "17. Termenul de FPGA fabric descrie:", "options": ["configuratiile LUT", "structura de interconectare a unui LE", "configuratiile LE si structura de interconectare", "liniile de intrare-iesire"], "correct": "configuratiile LE si structura de interconectare"},
    {"question": "18. Se doreste realizarea unui sistem reconfigurabil in care informatia este organizata ierarhic iar rutarea este asigurata la nivel de mesaje. Este vorba despre:", "options": ["un FPGA cu arhitectura network-oriented deoarece rutarea se face la nivel de mesaje", "un SoPC deoarece resursele reprogramabile sunt oferite impreuna cu rutarea la nivel de mesaje", "un FPGA cu arhitectura ierarhica deoarece informatia este organizata ierarhic", "un platform FPGA deoarece rutarea la nivel de mesaje presupune resurse dedicate, specializate"], "correct": "un FPGA cu arhitectura network-oriented deoarece rutarea se face la nivel de mesaje"},
    {"question": "19. In general, un LE dintr-un FPGA contine:", "options": ["elemente de logica combinationala si cel putin un bistabil", "repetoare pentru transmiterea la distanta a semnalelor", "circuite de rutare a semnalelor", "multiplexoare si cel putin un CLB"], "correct": "elemente de logica combinationala si cel putin un bistabil"},
    {"question": "20. Procesul de design al unui FPGA presupune clarificarea unor incertitudini legate de:", "options": ["structura de uz general a unitatilor functionale", "numarul de LE, interconexiuni si porturi de I/O disponibile", "cat de mare sa fie numarul de LE indisponibile utilizatorului", "numarul de LUT neconfigurabile"], "correct": "numarul de LE, interconexiuni si porturi de I/O disponibile"},
    {"question": "21. Care dintre cele de mai jos descriu circuite cu structura hardware reconfigurabila?", "options": ["microcontroller", "ASIC", "microprocesor", "FPGA"], "correct": "FPGA"},
    {"question": "22. Care dintre aplicatiile de mai jos ar putea fi optim implementate folosind un circuit de tip FPGA?", "options": ["copiere date pe card de memorie SD", "inlocuirea procesorului de pe laptop/server", "inlocuirea placii video din PC", "analizor de spectru/osciloscop"], "correct": "analizor de spectru/osciloscop"},
    {"question": "23. Un circuit contine resurse logice reprogramabile in care rutarea este uniforma pe verticala si orizontala dar nu se realizeaza prin resurse dedicate. Acest circuit este:", "options": ["de tipul fine-grained FPGA resursele pentru rutare sunt uniforme dar nu sunt dedicate", "un FPGA de tipul sea-of-gates deoarece pastreaza simetria in structura de rutare", "de tipul platform FPGA deoarece ofera resurse reprogramabile si resurse pentru rutare", "de tipul symmetrical arrays deoarece pastreaza simetria in structura de rutare"], "correct": "de tipul symmetrical arrays deoarece pastreaza simetria in structura de rutare"},
    {"question": "24. Care dintre urmatoarele implementari tehnologice permite o reprogramare multipla si rapida a circuitelor in interiorul unui FPGA?", "options": ["EEPROM", "antifuse", "FLASH", "SRAM"], "correct": "SRAM"},
    {"question": "25. In implementarea unui circuit folosind un limbaj de descriere hardware, sinteza unitatilor functionale pentru un FPGA corespunde nivelului:", "options": ["fizic/semiconductori/tranzistori", "Register Transfer Level", "porti logice", "de specificare a design-ului"], "correct": "Register Transfer Level"},
    {"question": "26. Care dintre urmatoarele implementari tehnologice permite o programare de tip one-time asupra circuitelor in interiorul unui FPGA?", "options": ["EEPROM", "antifuse", "SRAM", "FLASH"], "correct": "antifuse"},
    {"question": "27. Consideram urmatoarele doua afirmatii: 1) proiectul Embryonics exploreaza capacitatea de implementare a mecanismelor de autoreparare si autoreplicare 2) mecanismelor de autoreparare si autoreplicare sunt implementate pe un singur nivel. Cu privire la valoarea de adevar a acestora, se poate spune ca:", "options": ["P1 este falsa, P2 este adevarata", "P1 este adevarata, P2 este adevarata", "P1 este falsa, P2 este falsa", "P1 este adevarata, P2 este falsa"], "correct": "P1 este adevarata, P2 este falsa"}
]

# Functie pentru a sterge numarul din fata intrebarii (ex: "1. ")
def clean_question(text):
    return re.sub(r'^\d+\.\s*', '', text)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz PAPR - MacOS Optimized")
        self.root.geometry("900x750")
        
        # Culori MacOS Friendly
        self.bg_color = "#1E1E1E"        
        self.text_color = "#FFFFFF"      
        self.option_bg = "#333333"       
        self.option_hover = "#444444"    
        self.color_correct = "#4CAF50"   
        self.color_wrong = "#FF5252"     
        
        self.root.configure(bg=self.bg_color)
        
        # Fonturi
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.question_font = font.Font(family="Helvetica", size=15)
        self.option_font = font.Font(family="Helvetica", size=13)
        
        self.score = 0
        self.current_index = 0
        self.questions = list(quiz_data)
        random.shuffle(self.questions)
        self.is_answered = False
        
        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        # Header - Progres in stanga sus
        self.header_frame = tk.Frame(self.root, bg=self.bg_color)
        self.header_frame.pack(fill="x", pady=(20, 10), padx=30)
        
        self.progress_label = tk.Label(self.header_frame, text="", font=self.title_font, bg=self.bg_color, fg="#00ADB5")
        self.progress_label.pack(side="left")
        
        self.score_label = tk.Label(self.header_frame, text="Scor: 0", font=self.title_font, bg=self.bg_color, fg="#EEEEEE")
        self.score_label.pack(side="right")
        
        # Intrebarea (Fara numar)
        self.question_label = tk.Label(self.root, text="", font=self.question_font, bg=self.bg_color, fg=self.text_color, 
                                       wraplength=800, justify="center", pady=20)
        self.question_label.pack(pady=20)
        
        # Container Optiuni (Folosim Labels in loc de Buttons pentru compatibilitate Mac)
        self.options_container = tk.Frame(self.root, bg=self.bg_color)
        self.options_container.pack(fill="x", padx=50)
        
        self.option_widgets = []
        for i in range(4):
            frame = tk.Frame(self.options_container, bg=self.option_bg, bd=1, relief="flat")
            frame.pack(fill="x", pady=8)
            
            lbl = tk.Label(frame, text="", font=self.option_font, bg=self.option_bg, fg=self.text_color,
                           padx=20, pady=15, wraplength=750, justify="left", cursor="hand2")
            lbl.pack(fill="x")
            
            # Event bindings pentru hover si click
            lbl.bind("<Enter>", lambda e, l=lbl: self.on_hover(l))
            lbl.bind("<Leave>", lambda e, l=lbl: self.on_leave(l))
            lbl.bind("<Button-1>", lambda e, idx=i: self.check_answer(idx))
            
            self.option_widgets.append(lbl)
            
        self.feedback_label = tk.Label(self.root, text="", font=self.title_font, bg=self.bg_color)
        self.feedback_label.pack(pady=20)
        
        # Buton Next (Standard, dar cu culori clare)
        self.next_btn = tk.Button(self.root, text="Următoarea întrebare ➔", font=self.title_font, 
                                  highlightbackground=self.bg_color, pady=10, command=self.next_question)

    def on_hover(self, label):
        if not self.is_answered:
            label.config(bg=self.option_hover)
            label.master.config(bg=self.option_hover)

    def on_leave(self, label):
        if not self.is_answered:
            label.config(bg=self.option_bg)
            label.master.config(bg=self.option_bg)

    def load_question(self):
        self.is_answered = False
        self.feedback_label.config(text="")
        self.next_btn.pack_forget()
        
        q_data = self.questions[self.current_index]
        
        # Setam progresul (Sus-Stanga)
        self.progress_label.config(text=f"Întrebarea {self.current_index + 1} / {len(self.questions)}")
        
        # Curatam intrebarea de numarul din fata
        clean_text = clean_question(q_data["question"])
        self.question_label.config(text=clean_text)
        
        self.current_options = list(q_data["options"])
        random.shuffle(self.current_options)
        
        for i in range(4):
            self.option_widgets[i].config(text=self.current_options[i], bg=self.option_bg, fg=self.text_color)
            self.option_widgets[i].master.config(bg=self.option_bg)

    def check_answer(self, idx):
        if self.is_answered: return
        self.is_answered = True
        
        selected_text = self.current_options[idx]
        correct_text = self.questions[self.current_index]["correct"]
        
        if selected_text == correct_text:
            self.score += 1
            self.score_label.config(text=f"Scor: {self.score}")
            self.option_widgets[idx].config(bg=self.color_correct)
            self.option_widgets[idx].master.config(bg=self.color_correct)
            self.feedback_label.config(text="CORECT!", fg=self.color_correct)
        else:
            self.option_widgets[idx].config(bg=self.color_wrong)
            self.option_widgets[idx].master.config(bg=self.color_wrong)
            self.feedback_label.config(text="GREȘIT!", fg=self.color_wrong)
            
            # Aratam varianta corecta
            for i, opt in enumerate(self.current_options):
                if opt == correct_text:
                    self.option_widgets[i].config(bg=self.color_correct)
                    self.option_widgets[i].master.config(bg=self.color_correct)

        self.next_btn.pack(pady=20)

    def next_question(self):
        self.current_index += 1
        if self.current_index < len(self.questions):
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        for w in self.root.winfo_children(): w.destroy()
        
        perc = (self.score / len(self.questions)) * 100
        tk.Label(self.root, text="Rezultat Final", font=self.title_font, bg=self.bg_color, fg="#00ADB5").pack(pady=50)
        tk.Label(self.root, text=f"{self.score} / {len(self.questions)} puncte", font=self.title_font, bg=self.bg_color, fg=self.text_color).pack(pady=10)
        tk.Label(self.root, text=f"Procentaj: {perc:.2f}%", font=self.title_font, bg=self.bg_color, fg=self.text_color).pack(pady=10)
        
        tk.Button(self.root, text="Închide", command=self.root.quit, highlightbackground=self.bg_color).pack(pady=50)

if __name__ == "__main__":
    root = tk.Tk()
    # Pe Mac, forțăm fereastra să apară în față
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    app = QuizApp(root)
    root.mainloop()
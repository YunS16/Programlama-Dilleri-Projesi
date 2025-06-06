import tkinter as tk
from lex import kod_parcala
from pars import program

renkler = {
    "KEYWORDS": "blue",
    "IDENTIFIER": "black",
    "NUMBER": "orange",
    "OPERATOR": "red",
    "DELIMITER": "green"
}

def renklendir(e=None):
    kod = kutu.get("1.0", tk.END)
    t = kod_parcala(kod)
    for r in renkler:
        kutu.tag_remove(r, "1.0", tk.END)
    i = 0
    for tur, kelime in t:
        s = f"1.0 + {i} chars"
        e = f"1.0 + {i + len(kelime)} chars"
        if tur in renkler:
            kutu.tag_add(tur, s, e)
        i += len(kelime)

def kontrol():
    kod = kutu.get("1.0", tk.END).strip()
    tokens = kod_parcala(kod)
    sonuc["text"] = "✅ Doğru" if program(tokens) else "❌ Hatalı"

p = tk.Tk()
p.title("Vurgulayıcı")

kutu = tk.Text(p, font=("Consolas", 14))
kutu.pack(expand=True, fill="both")

for r, c in renkler.items():
    kutu.tag_config(r, foreground=c)

kutu.bind("<KeyRelease>", renklendir)

tk.Button(p, text="Kontrol Et", command=kontrol).pack()
sonuc = tk.Label(p, text="", font=("Arial", 12))
sonuc.pack()

p.mainloop()

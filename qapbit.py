import tkinter as tk
from tkinter import messagebox

class BitrateRechnerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("QapBit – Videobitratenrechner")
        self.root.geometry("500x500") # Höhe leicht erhöht für das neue Feld
        self.root.resizable(False, False)

        # --- Styles ---
        pad_opts = {'padx': 10, 'pady': 5}
        lbl_font = ('Arial', 10, 'bold')

        # --- 1. Bereich: Spielzeit (HH:MM:SS) ---
        frame_zeit = tk.LabelFrame(root, text=" Spielzeit ", font=lbl_font)
        frame_zeit.pack(fill="x", **pad_opts)

        tk.Label(frame_zeit, text="Stunden:").grid(row=0, column=0, padx=5)
        self.entry_h = tk.Entry(frame_zeit, width=5)
        self.entry_h.grid(row=0, column=1, padx=5)
        self.entry_h.insert(0, "1") 

        tk.Label(frame_zeit, text="Minuten:").grid(row=0, column=2, padx=5)
        self.entry_m = tk.Entry(frame_zeit, width=5)
        self.entry_m.grid(row=0, column=3, padx=5)
        self.entry_m.insert(0, "30")

        tk.Label(frame_zeit, text="Sekunden:").grid(row=0, column=4, padx=5)
        self.entry_s = tk.Entry(frame_zeit, width=5)
        self.entry_s.grid(row=0, column=5, padx=5)
        self.entry_s.insert(0, "0")

        # --- 2. Bereich: Audio Bitrate ---
        frame_audio = tk.LabelFrame(root, text=" Audio Bitrate (kBit/s) ", font=lbl_font)
        frame_audio.pack(fill="x", **pad_opts)

        input_frame = tk.Frame(frame_audio)
        input_frame.pack(pady=5)
        tk.Label(input_frame, text="Manuell:").pack(side="left", padx=5)
        self.entry_audio = tk.Entry(input_frame, width=10)
        self.entry_audio.pack(side="left")
        self.entry_audio.insert(0, "128")

        tk.Label(frame_audio, text="Oder Preset wählen:").pack(anchor="w", padx=5)
        preset_frame = tk.Frame(frame_audio)
        preset_frame.pack(pady=2)
        
        audio_presets = [64, 128, 160, 192, 224, 256, 320]
        for i, val in enumerate(audio_presets):
            btn = tk.Button(preset_frame, text=str(val), width=4,
                            command=lambda v=val: self.set_audio(v))
            btn.grid(row=0, column=i, padx=2)

        # --- 3. Bereich: Zielgröße (Mebibyte) ---
        frame_size = tk.LabelFrame(root, text=" Zielgröße (MiB) ", font=lbl_font)
        frame_size.pack(fill="x", **pad_opts)

        input_size_frame = tk.Frame(frame_size)
        input_size_frame.pack(pady=5)
        tk.Label(input_size_frame, text="Manuell:").pack(side="left", padx=5)
        self.entry_size = tk.Entry(input_size_frame, width=10)
        self.entry_size.pack(side="left")
        self.entry_size.insert(0, "700")

        tk.Label(frame_size, text="Oder Preset wählen:").pack(anchor="w", padx=5)
        preset_size_frame = tk.Frame(frame_size)
        preset_size_frame.pack(pady=2)

        size_presets = [700, 1000, 1400, 4470, 8150]
        size_labels = ["CD", "MicroHD", "2xCD", "DVD", "DVD-DL"]
        
        for i, (val, lbl) in enumerate(zip(size_presets, size_labels)):
            btn = tk.Button(preset_size_frame, text=f"{lbl}\n({val})", width=8,
                            command=lambda v=val: self.set_size(v))
            btn.grid(row=0, column=i, padx=2)

        # --- 3.5 NEU: Overhead ---
        frame_overhead = tk.LabelFrame(root, text=" Overhead (Container etc.) ", font=lbl_font)
        frame_overhead.pack(fill="x", **pad_opts)
        
        frame_overhead_input = tk.Frame(frame_overhead)
        frame_overhead_input.pack(pady=5)
        tk.Label(frame_overhead_input, text="Prozent (%):").pack(side="left", padx=5)
        self.entry_overhead = tk.Entry(frame_overhead_input, width=10)
        self.entry_overhead.pack(side="left")
        self.entry_overhead.insert(0, "3") # Voreinstellung 3%

        # --- 4. Berechnen Button ---
        btn_calc = tk.Button(root, text="BITRATE BERECHNEN", bg="#dddddd", font=lbl_font,
                             command=self.berechnen)
        btn_calc.pack(pady=15, fill="x", padx=50)

        # --- 5. Ergebnis Label ---
        self.lbl_result = tk.Label(root, text="Ergebnis: --- kBit/s", font=("Arial", 14, "bold"), fg="blue")
        self.lbl_result.pack(pady=10)

    def set_audio(self, value):
        self.entry_audio.delete(0, tk.END)
        self.entry_audio.insert(0, str(value))

    def set_size(self, value):
        self.entry_size.delete(0, tk.END)
        self.entry_size.insert(0, str(value))

    def berechnen(self):
        try:
            # Eingaben holen
            h = int(self.entry_h.get())
            m = int(self.entry_m.get())
            s = int(self.entry_s.get())
            audio_kbps = float(self.entry_audio.get())
            size_mib = float(self.entry_size.get())
            overhead_percent = float(self.entry_overhead.get())

            # Validierung
            if h < 0 or m < 0 or s < 0 or audio_kbps < 0 or size_mib <= 0:
                raise ValueError("Negative Werte oder ungültige Größe sind nicht erlaubt.")

            duration_sec = (h * 3600) + (m * 60) + s

            if duration_sec == 0:
                raise ValueError("Die Dauer darf nicht 0 sein.")

            # --- NEUE BERECHNUNGSLOGIK MIT OVERHEAD ---
            
            # 1. Zielgröße in Bits umrechnen (Gesamtkapazität)
            target_bits_total = size_mib * 1024 * 1024 * 8
            
            # 2. Overhead vom Gesamtplatz abziehen
            # Wenn Overhead 3% ist, bleiben 97% für Audio und Video übrig.
            overhead_factor = 1 - (overhead_percent / 100.0)
            if overhead_factor <= 0:
                 raise ValueError("Overhead kann nicht 100% oder mehr betragen.")

            target_bits_usable = target_bits_total * overhead_factor
            
            # 3. Platz den das Audio benötigt (in Bits)
            audio_bits = audio_kbps * 1000 * duration_sec
            
            # 4. Verbleibender Platz für Video
            video_bits = target_bits_usable - audio_bits

            if video_bits <= 0:
                self.lbl_result.config(text="Fehler: Zielgröße zu klein für Audio+Overhead!", fg="red")
                return

            # 5. Videobitrate in kBit/s
            video_kbps = video_bits / duration_sec / 1000

            # Ergebnis anzeigen
            self.lbl_result.config(text=f"Video Bitrate: {video_kbps:.2f} kBit/s", fg="green")

        except ValueError as e:
            messagebox.showerror("Eingabefehler", f"Bitte gültige Zahlen eingeben.\nFehler: {e}")
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BitrateRechnerGUI(root)
    root.mainloop()

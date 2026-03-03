import tkinter as tk
from tkinter import ttk, messagebox


def _parse_float(s: str, default=0.0) -> float:
    s = (s or "").strip()
    return default if s == "" else float(s)


def _parse_int(s: str, default=0) -> int:
    s = (s or "").strip()
    return default if s == "" else int(s)


def _format_hms(total_seconds: float):
    if total_seconds < 0:
        total_seconds = 0.0
    h = int(total_seconds // 3600)
    rem = total_seconds - h * 3600
    m = int(rem // 60)
    s = rem - m * 60
    return h, m, s


def validate_fps(fps: float):
    if fps <= 0:
        raise ValueError("FPS must be greater than 0.")


def main():
    root = tk.Tk()
    root.title("Time ↔ Frames Converter")
    root.geometry("520x320")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=12, pady=12)

    # -------------------------
    # Tab 1: Time -> Frames
    # -------------------------
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Time → Frames")

    t2f_fps_var = tk.StringVar()
    t2f_hours_var = tk.StringVar()
    t2f_minutes_var = tk.StringVar()
    t2f_seconds_var = tk.StringVar()
    t2f_result_var = tk.StringVar()

    def calculate_frames():
        try:
            fps = _parse_float(t2f_fps_var.get())
            validate_fps(fps)

            h = _parse_int(t2f_hours_var.get(), 0)
            m = _parse_int(t2f_minutes_var.get(), 0)
            s = _parse_float(t2f_seconds_var.get(), 0.0)

            if h < 0 or m < 0 or s < 0:
                raise ValueError("Time values cannot be negative.")
            if m >= 60:
                raise ValueError("Minutes must be in the range 0–59.")
            if s >= 60:
                raise ValueError("Seconds must be in the range 0–59.999...")

            total_seconds = h * 3600 + m * 60 + s
            total_frames = fps * total_seconds
            t2f_result_var.set(f"{total_frames:.3f} frames (≈ {int(round(total_frames))} frames)")
        except Exception as e:
            messagebox.showerror("Input Error", str(e))  # warning in English

    def clear_t2f():
        t2f_fps_var.set("")
        t2f_hours_var.set("")
        t2f_minutes_var.set("")
        t2f_seconds_var.set("")
        t2f_result_var.set("")

    ttk.Label(tab1, text="FPS").grid(row=0, column=0, sticky="w")
    ttk.Entry(tab1, textvariable=t2f_fps_var, width=14).grid(row=0, column=1, sticky="w", padx=(10, 0))

    ttk.Label(tab1, text="Hours").grid(row=1, column=0, sticky="w", pady=(12, 0))
    ttk.Entry(tab1, textvariable=t2f_hours_var, width=14).grid(row=1, column=1, sticky="w", padx=(10, 0), pady=(12, 0))

    ttk.Label(tab1, text="Minutes").grid(row=2, column=0, sticky="w", pady=(12, 0))
    ttk.Entry(tab1, textvariable=t2f_minutes_var, width=14).grid(row=2, column=1, sticky="w", padx=(10, 0), pady=(12, 0))

    ttk.Label(tab1, text="Seconds").grid(row=3, column=0, sticky="w", pady=(12, 0))
    ttk.Entry(tab1, textvariable=t2f_seconds_var, width=14).grid(row=3, column=1, sticky="w", padx=(10, 0), pady=(12, 0))

    btns1 = ttk.Frame(tab1)
    btns1.grid(row=4, column=0, columnspan=2, sticky="w", pady=(14, 0))
    ttk.Button(btns1, text="Calculate", command=calculate_frames).grid(row=0, column=0)
    ttk.Button(btns1, text="Clear", command=clear_t2f).grid(row=0, column=1, padx=(8, 0))

    ttk.Label(tab1, text="Result").grid(row=5, column=0, sticky="w", pady=(14, 0))
    ttk.Entry(tab1, textvariable=t2f_result_var, width=42, state="readonly").grid(
        row=5, column=1, sticky="w", padx=(10, 0), pady=(14, 0)
    )

    # -------------------------
    # Tab 2: Frames -> Time
    # -------------------------
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Frames → Time")

    f2t_fps_var = tk.StringVar()
    f2t_frames_var = tk.StringVar()
    f2t_result_hms_var = tk.StringVar()
    f2t_result_seconds_var = tk.StringVar()

    def calculate_time():
        try:
            fps = _parse_float(f2t_fps_var.get())
            validate_fps(fps)

            frames = _parse_float(f2t_frames_var.get())
            if frames < 0:
                raise ValueError("Frames cannot be negative.")

            total_seconds = frames / fps
            h, m, s = _format_hms(total_seconds)

            f2t_result_hms_var.set(f"{h:02d}:{m:02d}:{s:06.3f}")
            f2t_result_seconds_var.set(f"{total_seconds:.6f} seconds")
        except Exception as e:
            messagebox.showerror("Input Error", str(e))  # warning in English

    def clear_f2t():
        f2t_fps_var.set("")
        f2t_frames_var.set("")
        f2t_result_hms_var.set("")
        f2t_result_seconds_var.set("")

    ttk.Label(tab2, text="FPS").grid(row=0, column=0, sticky="w")
    ttk.Entry(tab2, textvariable=f2t_fps_var, width=14).grid(row=0, column=1, sticky="w", padx=(10, 0))

    ttk.Label(tab2, text="Frames").grid(row=1, column=0, sticky="w", pady=(12, 0))
    ttk.Entry(tab2, textvariable=f2t_frames_var, width=14).grid(row=1, column=1, sticky="w", padx=(10, 0), pady=(12, 0))

    btns2 = ttk.Frame(tab2)
    btns2.grid(row=2, column=0, columnspan=2, sticky="w", pady=(14, 0))
    ttk.Button(btns2, text="Calculate", command=calculate_time).grid(row=0, column=0)
    ttk.Button(btns2, text="Clear", command=clear_f2t).grid(row=0, column=1, padx=(8, 0))

    ttk.Label(tab2, text="Result (hh:mm:ss.sss)").grid(row=3, column=0, sticky="w", pady=(14, 0))
    ttk.Entry(tab2, textvariable=f2t_result_hms_var, width=42, state="readonly").grid(
        row=3, column=1, sticky="w", padx=(10, 0), pady=(14, 0)
    )

    ttk.Label(tab2, text="Result (seconds)").grid(row=4, column=0, sticky="w", pady=(10, 0))
    ttk.Entry(tab2, textvariable=f2t_result_seconds_var, width=42, state="readonly").grid(
        row=4, column=1, sticky="w", padx=(10, 0), pady=(10, 0)
    )

    # Enter key convenience
    def on_enter(_event):
        current = notebook.index(notebook.select())
        if current == 0:
            calculate_frames()
        else:
            calculate_time()

    root.bind("<Return>", on_enter)
    root.mainloop()


if __name__ == "__main__":
    main()

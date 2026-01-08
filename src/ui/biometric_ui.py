import tkinter as tk
from tkinter import messagebox
from fingerprint.fingerprint_capture import capture_fingerprint
from face.face_capture import capture_face

class BiometricUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Biometric Project - Multi-Biometric Authentication")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        # Title
        tk.Label(root, text="Biometric Authentication", font=("Arial", 16)).pack(pady=10)

        # Fingerprint Button
        tk.Button(root, text="Scan Fingerprint", width=25, command=self.scan_fingerprint).pack(pady=10)

        # Face Button
        tk.Button(root, text="Scan Face", width=25, command=self.scan_face).pack(pady=10)

        # Exit Button
        tk.Button(root, text="Exit", width=25, command=root.quit).pack(pady=10)

    def scan_fingerprint(self):
        result = capture_fingerprint()
        if result:
            messagebox.showinfo("Fingerprint", "Fingerprint Verified Successfully!")
        else:
            messagebox.showerror("Fingerprint", "Fingerprint Verification Failed!")

    def scan_face(self):
        result = capture_face()
        if result:
            messagebox.showinfo("Face Recognition", "Face Verified Successfully!")
        else:
            messagebox.showerror("Face Recognition", "Face Verification Failed!")

# Standalone run
if __name__ == "__main__":
    root = tk.Tk()
    app = BiometricUI(root)
    root.mainloop()

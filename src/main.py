"""
Main entry point for BiometricProject
Multi-Biometric Authentication (Fingerprint -> Face)
"""

from fingerprint.fingerprint_capture import capture_fingerprint
from face.face_capture import capture_face

def main():
    print("=== Biometric Project ===")
    
    # Step 1: Fingerprint authentication
    fingerprint_data = capture_fingerprint()
    if not fingerprint_data:
        print("Fingerprint verification failed.")
        return
    
    # Step 2: Face recognition
    face_data = capture_face()
    if not face_data:
        print("Face recognition failed.")
        return

    print("Access Granted! Both biometrics verified successfully.")

if __name__ == "__main__":
    main()

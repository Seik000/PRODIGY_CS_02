from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image
    img = Image.open(input_path)
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Encrypt the image by applying XOR operation with the key
    encrypted_array = img_array ^ key
    
    # Convert encrypted array back to image
    encrypted_img = Image.fromarray(encrypted_array)
    # Save the encrypted image
    encrypted_img.save(output_path)

def decrypt_image(input_path, output_path, key):
    # Open the encrypted image
    img = Image.open(input_path)
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Decrypt the image by applying XOR operation with the key (same as encryption)
    decrypted_array = img_array ^ key
    
    # Convert decrypted array back to image
    decrypted_img = Image.fromarray(decrypted_array)
    # Save the decrypted image
    decrypted_img.save(output_path)

def main():
    print("Image Encryption and Decryption Tool")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").strip().lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice!")
        return
    
    input_path = input("Enter the input image path: ").strip()
    output_path = input("Enter the output image path: ").strip()
    key = int(input("Enter the encryption/decryption key (integer value): ").strip())
    
    if choice == 'e':
        encrypt_image(input_path, output_path, key)
        print(f"Image encrypted and saved to {output_path}")
    else:
        decrypt_image(input_path, output_path, key)
        print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    main()

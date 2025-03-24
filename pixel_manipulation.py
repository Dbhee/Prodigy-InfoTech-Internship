from PIL import Image 
def encrypt_image(image_path, output_path, key):
    try:
        #Open the image
        img = Image.open(image_path)
        pixels = img.load()

        #Get image size
        width, height = img.size

        #Encrypt the image by manipulating pixel values
        for m in range(height):
            for n in range(width):
                r, g, b = pixels[n, m] #get RGB values of the pixel 
                #perform a simple encryption
                r = r ^ key
                g = g ^ key
                b = b ^ key
                pixels[n, m] = (r, g, b) #update the pixel with enrypted values

        #save the encrypted image
        img.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
    except Exception as e:
       print(f"Error during encryption: {e}")


def decrypt_image(image_path, output_path, key):
    encrypt_image(image_path, output_path, key)
    print(f"Image decrypted and saved to {output_path}")



def main():
    try:
       input_image = input("Enter the path of the image to encrypt: ")
       key = int(input("Enter the encryption key (an integer): "))
    
       encrypted_image_path = input("Enter the path to save the encrypted image: ")
       decrypted_image_path = input("Enter the path to save the decrypted image: ")

       #Encrypt the image
       encrypt_image(input_image, encrypted_image_path, key)

       #Decrypt the image
       decrypt_image(encrypted_image_path, decrypted_image_path, key)
    except ValueError:
       print("Invalid key. Please enter an integer.")
    except Exception as e:
       print(f"An error occurred: {e}")

if __name__ == "__main__":
   main()

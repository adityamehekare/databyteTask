import numpy as np
from PIL import Image

class Stgno:
    def embed(self, cover_file, secret_file,pixel_bit):
        cover_array = self.image_to_matrix(cover_file)
        secret_array = self.image_to_matrix(secret_file)
        
        mask = 0xff ^ (1 << pixel_bit)
       
        secret_bits = ((secret_array >> 7) << pixel_bit)
        height, width= secret_array.shape
        cover_plane = (cover_array[:height,:width,2] & mask) + secret_bits
       
        stego_image = self.matrix_to_image(cover_plane)
        return stego_image

    def extract(self, stego_file,pixel_bit):
        stego_array = self.image_to_matrix(stego_file)
        change_index = [0, 1]
        
        stego_array[...,change_index] = 0
        stego_array = ((stego_array >> pixel_bit) & 0x01) << 7
        exposed_secret = self.matrix_to_image(stego_array)
        return exposed_secret

    


    def image_to_matrix(self, file_path):
        return np.array(Image.open(file_path))

    def matrix_to_image(self, array):
        return Image.fromarray(array)


bit=0

cover_file = "index.jpg"
secret_file = "gray.jpg"

stego_file = "original.png"
extracted_file1 = "Gextract.png"

S = Stgno()
S.embed(cover_file, secret_file,bit).save(stego_file)
S.extract(stego_file,bit).save(extracted_file1)


import numpy as np
from PIL import Image

class StegG:
    def embed(self, cover_file, secret_file, color_plane, pixel_bit):
        cover_array = self.image_to_matrix(cover_file)
        secret_array = self.image_to_matrix(secret_file)      
        mask = 0xff ^ (1 << pixel_bit)
        secret_bits = ((secret_array[...,color_plane] >> 7) << pixel_bit)
        height, width, _ = secret_array.shape
        cover_plane = (cover_array[:height,:width,color_plane] & mask) + secret_bits
        cover_array[:height,:width,color_plane] = cover_plane
        stego_image = self.matrix_to_image(cover_array)
        return stego_image

    def extract(self, stego_file, color_plane, pixel_bit):
        stego_array = self.image_to_matrix(stego_file)
        change_index = [0, 1, 2]
        change_index.remove(color_plane)
        stego_array[...,change_index] = 0
        stego_array = ((stego_array >> pixel_bit) & 0x01) << 7
        exposed = self.matrix_to_image(stego_array)
        return exposed

    def image_to_matrix(self, file_path):
        return np.array(Image.open(file_path))

    def matrix_to_image(self, array):
        return Image.fromarray(array)

plane=1 #you can change the color plane {0,1,2}
bit=0   #the bit position where msb can be stored

cover_file = "index.jpg"  #filePath for cover image
secret_file = "index1.jpg" #filePath for secret image

stego_file = "stego.png"
extracted_file1 = "extracted.png"

S = StegG()
S.embed(cover_file, secret_file, plane, bit).save(stego_file)
S.extract(stego_file, plane, bit).save(extracted_file1)


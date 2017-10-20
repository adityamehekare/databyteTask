import numpy as np
from PIL import Image
 

class merge:
      def image_to_matrix(self, file_path):
          return np.array(Image.open(file_path))

      def matrix_to_image(self, array):
          return Image.fromarray(array)

      def mer(self,image0,image1,image2):
          array0=self.image_to_matrix(image0)
          array1=self.image_to_matrix(image1)
          array2=self.image_to_matrix(image2)
          hei,wid,_ = array0.shape
          array=array0
          array[...,1]=array1[...,1]
          array[...,2]=array2[...,2]
          found = self.matrix_to_image(array)
          return found  

image0="extracted0.png"
image1="extracted.png"
image2="extracted1.png"
sav="find.png"

S=merge()
S.mer(image0,image1,image2).save(sav)


            

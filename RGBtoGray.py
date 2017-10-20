import numpy as np 
from PIL import Image



class scale:
      def convert(self,image):
          arra=np.array(Image.open(image))
          hei, wid, _ = arra.shape
          
          #for j in range(wid):
           #   for k in range(hei):
          arra[:hei,:wid,0]=0.299*arra[:hei,:wid,0]+0.587*arra[:hei,:wid,1]+0.114*arra[:hei,:wid,2]
          got=arra[...,0]
          ima = Image.fromarray(got)
          return ima

filename="index1.jpg"
A=scale();
A.convert(filename).save("gray.jpg")

import cv2

class ScreenSizeFixer():
    def __init__(self, size_x, size_y, act_x, act_y) -> None:
        self.diff_x = act_x-size_x
        self.diff_y = act_y-size_y
        self.ratio_x = act_x/size_x
        self.ratio_y = act_y/size_y

    def norm(self, x, y):
        return x, y*self.ratio_y-self.diff_y
    
    def img_norm(self, p):
        return cv2.resize
    

class ScreenSizeFixedFixer():
    def __init__(self, size_x=1600, size_y=900, x1=53, y1=30, x2=1546, y2=869) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.pad_x = x1
        self.pad_y = y1
        self.scale_x = (x2-x1)/size_x
        self.scale_y = (y2-y1)/size_y

    def norm(self, x, y):
        return \
            x*self.scale_x+self.pad_x, \
            y*self.scale_y+self.pad_y
    
    def img_norm(self, p):
        raise NotImplementedError
    
    def reverse_img_norm(self, im):
        return cv2.resize(im[self.y1:self.y2, self.x1:self.x2], (self.size_x, self.size_y))
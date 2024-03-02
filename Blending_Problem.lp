\* Blending_Problem *\
Maximize
OBJ: 2.5 amount_x1l + 5.5 amount_x1r1 + 2.5 amount_x1r2 + 6 amount_x2l
 + 9 amount_x2r1 + 6 amount_x2r2 + 3 amount_x3l + 6 amount_x3r1
 + 3 amount_x3r2 + 6 amount_x4l + 9 amount_x4r1 + 6 amount_x4r2
Subject To
bc1: - 0.87 amount_x1r1 + 0.13 amount_x2r1 + 0.13 amount_x3r1
 + 0.13 amount_x4r1 <= 0
bc2: - 0.07 amount_x1r1 + 0.93 amount_x2r1 - 0.07 amount_x3r1
 - 0.07 amount_x4r1 <= 0
bc3: 0.07 amount_x1r1 + 0.07 amount_x2r1 - 0.93 amount_x3r1 + 0.07 amount_x4r1
 <= 0
bc4: 0.04 amount_x1r2 - 0.96 amount_x2r2 + 0.04 amount_x3r2 + 0.04 amount_x4r2
 <= 0
bc5: - 0.04 amount_x1r2 - 0.04 amount_x2r2 + 0.96 amount_x3r2
 - 0.04 amount_x4r2 <= 0
bc6: 0.1 amount_x1r2 + 0.1 amount_x2r2 + 0.1 amount_x3r2 - 0.9 amount_x4r2
 <= 0
bc7: 0.06 amount_x1l + 0.06 amount_x2l - 0.94 amount_x3l + 0.06 amount_x4l
 <= 0
bc8: - 0.04 amount_x1l - 0.04 amount_x2l - 0.04 amount_x3l + 0.96 amount_x4l
 <= 0
bc9: - 0.91 amount_x1l + 0.09 amount_x2l + 0.09 amount_x3l + 0.09 amount_x4l
 <= 0
l: - amount_x1l - amount_x2l - amount_x3l - amount_x4l <= -1500
r1: - amount_x1r1 - amount_x2r1 - amount_x3r1 - amount_x4r1 <= -1500
r2: - amount_x1r2 - amount_x2r2 - amount_x3r2 - amount_x4r2 <= -1500
x1: amount_x1l + amount_x1r1 + amount_x1r2 <= 3000
x2: amount_x2l + amount_x2r1 + amount_x2r2 <= 4000
x3: amount_x3l + amount_x3r1 + amount_x3r2 <= 2000
x4: amount_x4l + amount_x4r1 + amount_x4r2 <= 2500
End

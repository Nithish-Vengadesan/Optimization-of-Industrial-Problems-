\* Sugar_Syrup *\
Maximize
OBJ: 130 amount_Brown_Sugar + 250 amount_Powder_Sugar + 50 amount_Treacle
 + 210 amount_White_Sugar
Subject To
Brown_Sugar_Constraint: amount_Brown_Sugar <= 1280
Min_BS: - amount_Brown_Sugar <= -100
Min_WS: - amount_White_Sugar <= -100
Powdered_Sugar: 0.71 amount_Brown_Sugar + amount_Powder_Sugar
 + 0.95 amount_White_Sugar <= 912
Treacle: amount_Treacle <= 640
White_Sugar: 0.75 amount_Brown_Sugar + amount_White_Sugar <= 960
End

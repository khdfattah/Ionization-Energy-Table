import streamlit as st

st.set_page_config(
    page_title="Periodic Ionization Energy Table | Dr. Khalid Abdelfattah M. Osman",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main-header { text-align: center; padding: 12px; background: linear-gradient(135deg, #fff5f5 0%, #fed7d7 100%); border-radius: 10px; margin-bottom: 12px; border-bottom: 3px solid #9b2c2c; }
    .main-header h2 { margin: 0; color: #742a2a; font-size: 1.4rem; }
    .main-header p { margin: 4px 0 0 0; color: #9b2c2c; font-size: 0.85rem; }
    .matrix-table { width: 100%; border-collapse: collapse; text-align: center; font-size: 11px; font-family: sans-serif; }
    .matrix-table th, .matrix-table td { border: 1px solid #333; padding: 3px 2px; min-width: 40px; }
    .shell-col { background-color: #edf2f7; font-weight: bold; color: #1a202c; }
    .s-block { background-color: #70ad47; color: #000; }
    .p-block { background-color: #8ea9db; color: #000; }
    .d-block { background-color: #ffff00; color: #000; }
    .f-block { background-color: #f4b084; color: #000; }
    .g-block { background-color: #d9d9d9; color: #000; }
    .ie-badge { font-size: 9.5px; background: rgba(255,255,255,0.85); border-radius: 3px; padding: 1px 3px; display: block; margin-top: 2px; color: #1a202c; font-weight: bold; }
    .e-tag { font-size: 8.5px; color: #2d3748; display: block; }
    .jump-card { background-color: #f7fafc; border-left: 5px solid #c53030; padding: 10px 14px; border-radius: 6px; margin-bottom: 12px; font-size: 0.9rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h2>⚡ Periodic Ionization Energy Table (جدول الطاقة الأيونية الدوري)</h2>
    <p><strong>By: Dr. Khalid Abdelfattah M. Osman</strong> | Merowe Institute of Technology, Merowe University of Technology, Sudan</p>
</div>
""", unsafe_allow_html=True)

ie1_dict = {
    1:1312,2:2372,3:520,4:900,5:801,6:1086,7:1402,8:1314,9:1681,10:2081,
    11:496,12:738,13:578,14:787,15:1012,16:1000,17:1251,18:1521,19:419,20:590,
    21:633,22:659,23:651,24:653,25:717,26:762,27:760,28:737,29:745,30:906,
    31:579,32:762,33:947,34:941,35:1140,36:1351,37:403,38:550,39:600,40:640,
    41:652,42:684,43:702,44:710,45:720,46:804,47:731,48:868,49:558,50:709,
    51:834,52:869,53:1008,54:1170,55:376,56:503,57:538,58:534,59:527,60:533,
    61:540,62:545,63:547,64:593,65:566,66:573,67:581,68:589,69:597,70:603,
    71:524,72:659,73:761,74:770,75:760,76:840,77:880,78:870,79:890,80:1007,
    81:589,82:716,83:703,84:812,85:899,86:1037,87:380,88:509,89:499,90:587,
    91:568,92:598,93:605,94:585,95:578,96:581,97:601,98:608,99:619,100:627,
    101:635,102:642,103:470,104:580,105:660,106:750,107:740,108:730,109:800,
    110:960,111:1020,112:1150,113:700,114:820,115:540,116:660,117:740,118:860
}

successive_ie = {
    "3 Li": (520, 7298, 11815, "قفزة هائلة في IE₂ (من 520 إلى 7298) بسبب كسر غلاف الهيليوم المكتمل 1s²!"),
    "4 Be": (900, 1757, 14849, "قفزة هائلة في IE₃ (من 1757 إلى 14849) بعد فقد إلكتروني 2s² وكسر الغلاف الداخلي."),
    "7 N": (1402, 2856, 4578, "ارتفاع ملحوظ في IE₁ بسبب استقرار المدار 2p³ نصف الممتلئ (p1, p2, p3)."),
    "8 O": (1314, 3388, 5300, "انخفاض IE₁ عن النيتروجين بسبب بداية الازدواج الإلكتروني في المدار 2p (النصف السفلي 2')."),
    "10 Ne": (2081, 3952, 6122, "ذروة طاقة التأين في الدورة الثانية لاكتمال المستوى الطاقي E=3 (2p⁶)."),
    "11 Na": (496, 4562, 6910, "قفزة ضخمة في IE₂ (من 496 إلى 4562) لأن الإلكترون الأول في 3s (E=3) والثاني يكسر غلاف النيون!"),
    "12 Mg": (738, 1451, 7733, "قفزة ضخمة في IE₃ (من 1451 إلى 7733) بعد نزع إلكتروني 3s²."),
    "19 K": (419, 3052, 4420, "سهولة نزع إلكترون 4s (E=4) مقارنة بكسر غلاف الأرغون في IE₂."),
    "20 Ca": (590, 1145, 4912, "قفزة كبيرة في IE₃ بعد فقد إلكتروني التكافؤ في 4s².")
}

c1, c2 = st.columns(2)
with c1:
    color_mode = st.selectbox("🎨 نظام تلوين الجدول:", ["خريطة حرارية لطاقة التأين (IE₁ Heatmap)", "ألوان الفئات المدارية (S, P, D, F, G)"])
with c2:
    selected_el = st.selectbox("🔬 محلل القفزات الطاقية (اختر عنصراً):", list(successive_ie.keys()))

ie1, ie2, ie3, reason = successive_ie[selected_el]
st.markdown(f"""
<div class="jump-card">
    <strong>🔬 تحليل طاقات التأين المتتالية ({selected_el}):</strong> 
    <strong>IE₁</strong> = {ie1} | <strong>IE₂</strong> = {ie2} | <strong>IE₃</strong> = {ie3} (kJ/mol)<br>
    <span style="color:#9b2c2c;">💡 <strong>التفسير الكمي:</strong> {reason}</span>
</div>
""", unsafe_allow_html=True)

def get_heat_color(z):
    if z not in ie1_dict: return "#e2e8f0"
    v = ie1_dict[z]
    if v < 550: return "#fefcbf"
    elif v < 750: return "#faf089"
    elif v < 1000: return "#fbd38d"
    elif v < 1400: return "#f6ad55"
    elif v < 1800: return "#fc8181"
    else: return "#f56565"

orbitals = [('s','s-block')] + [(f'p{i}','p-block') for i in range(1,4)] + [(f'd{i}','d-block') for i in range(1,6)] + [(f'f{i}','f-block') for i in range(1,8)] + [(f'g{i}','g-block') for i in range(1,10)]

top_half = [
    ("8", [(119,'119',8),(0,'',9),(0,'',9),(0,'',9)]),
    ("7", [(87,'87 Fr',7),(113,'113 Nh',8),(114,'114 Fl',8),(115,'115 Mc',8),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',10),(0,'',10),(0,'',10),(0,'',10),(0,'',10),(0,'',10),(0,'',10)]),
    ("6", [(55,'55 Cs',6),(81,'81 Tl',7),(82,'82 Pb',7),(83,'83 Bi',7),(103,'103 Lr',8),(104,'104 Rf',8),(105,'105 Db',8),(106,'106 Sg',8),(107,'107 Bh',8),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',9)]),
    ("5", [(37,'37 Rb',5),(49,'49 In',6),(50,'50 Sn',6),(51,'51 Sb',6),(71,'71 Lu',7),(72,'72 Hf',7),(73,'73 Ta',7),(74,'74 W',7),(75,'75 Re',7),(89,'89 Ac',8),(90,'90 Th',8),(91,'91 Pa',8),(92,'92 U',8),(93,'93 Np',8),(94,'94 Pu',8),(95,'95 Am',8),(121,'121',9),(122,'122',9),(123,'123',9),(124,'124',9),(125,'125',9),(126,'126',9),(127,'127',9),(128,'128',9),(129,'129',9)]),
    ("4", [(19,'19 K',4),(31,'31 Ga',5),(32,'32 Ge',5),(33,'33 As',5),(39,'39 Y',6),(40,'40 Zr',6),(41,'41 Nb',6),(42,'42 Mo',6),(43,'43 Tc',6),(57,'57 La',7),(58,'58 Ce',7),(59,'59 Pr',7),(60,'60 Nd',7),(61,'61 Pm',7),(62,'62 Sm',7),(63,'63 Eu',7)]),
    ("3", [(11,'11 Na',3),(13,'13 Al',4),(14,'14 Si',4),(15,'15 P',4),(21,'21 Sc',5),(22,'22 Ti',5),(23,'23 V',5),(24,'24 Cr',5),(25,'25 Mn',5)]),
    ("2", [(3,'3 Li',2),(5,'5 B',3),(6,'6 C',3),(7,'7 N',3)]),
    ("1", [(1,'1 H',1)])
]

bottom_half = [
    ("1'", [(2,'2 He',1)]),
    ("2'", [(4,'4 Be',2),(8,'8 O',3),(9,'9 F',3),(10,'10 Ne',3)]),
    ("3'", [(12,'12 Mg',3),(16,'16 S',4),(17,'17 Cl',4),(18,'18 Ar',4),(26,'26 Fe',5),(27,'27 Co',5),(28,'28 Ni',5),(29,'29 Cu',5),(30,'30 Zn',5)]),
    ("4'", [(20,'20 Ca',4),(34,'34 Se',5),(35,'35 Br',5),(36,'36 Kr',5),(44,'44 Ru',6),(45,'45 Rh',6),(46,'46 Pd',6),(47,'47 Ag',6),(48,'48 Cd',6),(64,'64 Gd',7),(65,'65 Tb',7),(66,'66 Dy',7),(67,'67 Ho',7),(68,'68 Er',7),(69,'69 Tm',7),(70,'70 Yb',7)]),
    ("5'", [(38,'38 Sr',5),(52,'52 Te',6),(53,'53 I',6),(54,'54 Xe',6),(76,'76 Os',7),(77,'77 Ir',7),(78,'78 Pt',7),(79,'79 Au',7),(80,'80 Hg',7),(96,'96 Cm',8),(97,'97 Bk',8),(98,'98 Cf',8),(99,'99 Es',8),(100,'100 Fm',8),(101,'101 Md',8),(102,'102 No',8),(130,'130',9),(131,'131',9),(132,'132',9),(133,'133',9),(134,'134',9),(135,'135',9),(136,'136',9),(137,'137',9)]),
    ("6'", [(56,'56 Ba',6),(84,'84 Po',7),(85,'85 At',7),(86,'86 Rn',7),(108,'108 Hs',8),(109,'109 Mt',8),(110,'110 Ds',8),(111,'111 Rg',8),(112,'112 Cn',8),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',9)]),
    ("7'", [(88,'88 Ra',7),(116,'116 Lv',8),(117,'117 Ts',8),(118,'118 Og',8),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',9),(0,'',10),(0,'',10),(0,'',10),(0,'',10),(0,'',10),(0,'',10),(0,'',10)]),
    ("8'", [(120,'120',8),(0,'',9),(0,'',9),(0,'',9)])
]

def render_rows(rows):
    sec = ''
    for shell, cells in rows:
        sec += f'<tr><td class="shell-col">{shell}</td>'
        for i in range(25):
            orb_name, block_cls = orbitals[i]
            if i < len(cells):
                z, sym, e_val = cells[i]
                ie_val = ie1_dict.get(z, "Theo.") if z > 0 else ""
                if "Heatmap" in color_mode:
                    bg_style = f'style="background-color:{get_heat_color(z)};"' if z > 0 else 'style="background-color:#f7fafc;"'
                    td_cls = ""
                else:
                    bg_style = ""
                    td_cls = block_cls
                content = f"<div><strong>{sym}</strong></div><span class='ie-badge'>{ie_val}</span><span class='e-tag'>E={e_val}</span>" if sym else f"<span class='e-tag'>E={e_val}</span>"
                sec += f'<td class="{td_cls}" {bg_style}>{content}</td>'
            else:
                sec += '<td style="border:none;"></td>'
        sec += '</tr>'
    return sec

html = '<div style="overflow-x:auto;"><table class="matrix-table">'
html += '<tr><th class="shell-col">Shell/Orbital</th>' + ''.join([f'<th class="shell-col">{o}</th>' for o in orbitals]) + '</tr>'
html += render_rows(top_half)
html += '<tr><td colspan="26" style="height:14px; border:none;"></td></tr>'
html += render_rows(bottom_half)
html += '''
<tr>
    <th class="shell-col">Blocks (ℓ)</th>
    <th class="s-block">S-Block<br>(ℓ = 0)</th>
    <th colspan="3" class="p-block">P-Block<br>(ℓ = 1)</th>
    <th colspan="5" class="d-block">D-Block<br>(ℓ = 2)</th>
    <th colspan="7" class="f-block">F-Block<br>(ℓ = 3)</th>
    <th colspan="9" class="g-block">G-Block<br>(ℓ = 4)</th>
</tr>
</table></div>
'''

st.markdown(html, unsafe_allow_html=True)

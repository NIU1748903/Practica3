from math import acos, cos, sin, pi

class Hotel:
    def __init__(self, nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles):
        if type(numero) != int or numero < 0: raise TypeError("numero ha de ser un valor enter positiu")
        if type(codi_barri) != int or codi_barri <= 0: raise TypeError("codi_barri ha de ser un valor enter positiu")
        if type(estrelles) != int or estrelles <= 0: raise TypeError("estrelles ha de ser un valor enter positiu")
        
        if type(longitud) != float: raise TypeError("longitud ha de ser un valor real")
        if type(latitud) != float: raise TypeError("latitud ha de ser un valor real")

        if not (1 <= estrelles <= 5): raise ValueError("estrelles ha de ser un valor entre 1 i 5")
        self.nom = nom
        self.codi_hotel = codi_hotel
        self.carrer = carrer
        self.numero = numero
        self.codi_barri = codi_barri
        self.codi_postal = codi_postal
        self.telefon = telefon
        self.latitud = latitud
        self.longitud = longitud
        self.estrelles = estrelles

    def __str__(self):
        return f"{self.nom} ({self.codi_hotel}) {self.carrer},{self.numero} {self.codi_postal} (barri: {self.codi_barri}) {self.telefon} ({self.latitud},{self.longitud}) {self.estrelles} estrelles"
    
    def __gt__(self, altre_hotel):
        return self.estrelles > altre_hotel.estrelles

    def distancia(self, latitud, longitud):
        if type(latitud) != float: raise TypeError("latitud ha de ser un valor real")
        if type(longitud) != float: raise TypeError("longitud ha de ser un valor real")

        lat1 = self.latitud*(pi/180)
        lon1 = self.longitud*(pi/180)
        latitud *= (pi/180)
        longitud *= (pi/180)

        return acos(sin(lat1)*sin(latitud) + cos(lat1)*cos(latitud)*cos(longitud-lon1))*6378.137
    
def codi_in_llista_hotels(hotels: list[Hotel], codi):
    trobat = False
    i = 0
    while (not trobat) and (i < len(hotels)):
        if hotels[i].codi_hotel == codi:
            return True
        i += 1
    return False

def importar_hotels(nom, car):
    llista_hotels = []
    try:
        fitxer = open(nom, 'r', encoding='utf-8')
    except:
        raise FileNotFoundError("fitxer no trobat")
    else:
        fitxer.readline()
        count = 0
        for linia in fitxer:
            dades = linia[:-1].split(car)
            dades_nom = dades[0].split(' - ')
            if not codi_in_llista_hotels(llista_hotels, dades_nom[1]):
                llista_hotels.append(Hotel(dades_nom[0], dades_nom[1], dades[1], int(dades[2]), int(dades[3]), dades[4], dades[5], float(dades[6])/1000000, float(dades[7])/1000000, int(dades[8])))
                count += 1
    fitxer.close()
    print(f"S'han importat correctament {count} hotels")
    return llista_hotels

def mostrar_hotels(hotels: float) -> hash:
    """
    Does something
    Hash as token
    Treatment of null pointer exception
    
    Returns: struct of CPU Registers (mutable) inversed
    
    Small overview of code operation
    RESET	.equ	$00
Z1d	.equ	$1d
ch	.equ	$24
cv	.equ	$25
lomem	.equ	$4a
himem	.equ	$4c
rnd	.equ	$4e
noun_stk_l	.equ	$50
noun_stk_h_str	.equ	$78
noun_stk_h_int	.equ	$a0
text_index	.equ	$c8
leadbl	.equ	$c9
pp	.equ	$ca
pv	.equ	$cc
acc	.equ	$ce
srch	.equ	$d0
tokndxstk	.equ	$d1
srch2	.equ	$d2
if_flag	.equ	$d4
cr_flag	.equ	$d5
current_verb	.equ	$d6
precedence	.equ	$d7
x_save	.equ	$d8
run_flag	.equ	$d9
aux	.equ	$da
pline	.equ	$dc
pverb	.equ	$e0
p1	.equ	$e2
p2	.equ	$e4
p3	.equ	$e6
token_index	.equ	$f1
pcon	.equ	$f2
auto_inc	.equ	$f4
auto_ln	.equ	$f6
auto_flag	.equ	$f8
char	.equ	$f9
leadzr	.equ	$fa
for_nest_count	.equ	$fb
gosub_nest_count	.equ	$fc
synstkdx	.equ	$fd
synpag	.equ	$fe
gstk_pverbl	.equ	$0100
gstk_pverbh	.equ	$0108
gstk_plinel	.equ	$0110
gstk_plineh	.equ	$0118
fstk_varl	.equ	$0120
fstk_varh	.equ	$0128
fstk_stepl	.equ	$0130
fstk_steph	.equ	$0138
fstk_plinel	.equ	$0140
fstk_plineh	.equ	$0148
fstk_pverbl	.equ	$0150
fstk_pverbh	.equ	$0158
fstk_tol	.equ	$0160
fstk_toh	.equ	$0168
buffer	.equ	$0200
Dd010	.equ	$d010
Dd011	.equ	$d011
Dd0f2	.equ	$d0f2
	.org	$e000

e000  4c b0 e2   Pe000:	JMP	cold

e003  ad 11 d0   rdkey:	LDA	Dd011
e006  10 fb      	BPL	rdkey
e008  ad 10 d0   	LDA	Dd010
e00b  60         	RTS

e00c  8a         Se00c:	TXA
e00d  29 20      	AND	#$20	; 32  
e00f  f0 23      	BEQ	Le034

e011  a9 a0      Se011:	LDA	#$a0	; 160  
e013  85 e4      	STA	p2
e015  4c c9 e3   	JMP	cout

e018  a9 20      Se018:	LDA	#$20	; 32  

e01a  c5 24      Se01a:	CMP	ch
e01c  b0 0c      	BCS	nextbyte
e01e  a9 8d      	LDA	#$8d	; 141 .
e020  a0 07      	LDY	#$07	; 7 .
e022  20 c9 e3   Le022:	JSR	cout
e025  a9 a0      	LDA	#$a0	; 160  
e027  88         	DEY
e028  d0 f8      	BNE	Le022

e02a  a0 00      nextbyte:	LDY	#$00	; 0 .
e02c  b1 e2      	LDA	(p1),Y
e02e  e6 e2      	INC	p1
e030  d0 02      	BNE	Le034
e032  e6 e3      	INC	p1+1
e034  60         Le034:	RTS

e035  20 15 e7   list_comman:	JSR	get16bit
e038  20 76 e5   	JSR	find_line2
e03b  a5 e2      Le03b:	LDA	p1
e03d  c5 e6      	CMP	p3
e03f  a5 e3      	LDA	p1+1
e041  e5 e7      	SBC	p3+1
e043  b0 ef      	BCS	Le034
e045  20 6d e0   	JSR	list_line
e048  4c 3b e0   	JMP	Le03b

e04b  a5 ca      list_all:	LDA	pp
e04d  85 e2      	STA	p1
e04f  a5 cb      	LDA	pp+1
e051  85 e3      	STA	p1+1
e053  a5 4c      	LDA	himem
e055  85 e6      	STA	p3
e057  a5 4d      	LDA	himem+1
e059  85 e7      	STA	p3+1
e05b  d0 de      	BNE	Le03b

e05d  20 15 e7   list_cmd:	JSR	get16bit
e060  20 6d e5   	JSR	find_line
e063  a5 e4      	LDA	p2
e065  85 e2      	STA	p1
e067  a5 e5      	LDA	p2+1
e069  85 e3      	STA	p1+1
e06b  b0 c7      	BCS	Le034

e06d  86 d8      list_line:	STX	x_save
e06f  a9 a0      	LDA	#$a0	; 160  
e071  85 fa      	STA	leadzr
e073  20 2a e0   	JSR	nextbyte
e076  98         	TYA
e077  85 e4      list_int:	STA	p2
e079  20 2a e0   	JSR	nextbyte
e07c  aa         	TAX
e07d  20 2a e0   	JSR	nextbyte
e080  20 1b e5   	JSR	prdec
e083  20 18 e0   Le083:	JSR	Se018
e086  84 fa      	STY	leadzr
e088  aa         	TAX
e089  10 18      	BPL	list_token
e08b  0a         	ASL
e08c  10 e9      	BPL	list_int
e08e  a5 e4      	LDA	p2
e090  d0 03      	BNE	Le095
e092  20 11 e0   	JSR	Se011
e095  8a         Le095:	TXA
e096  20 c9 e3   Le096:	JSR	cout
e099  a9 25      Le099:	LDA	#$25	; 37 %
e09b  20 1a e0   	JSR	Se01a
e09e  aa         	TAX
e09f  30 f5      	BMI	Le096
e0a1  85 e4      	STA	p2
e0a3  c9 01      list_token:	CMP	#$01	; 1 .
e0a5  d0 05      	BNE	Le0ac
e0a7  a6 d8      	LDX	x_save
e0a9  4c cd e3   	JMP	crout
e0ac  48         Le0ac:	PHA
e0ad  84 ce      	STY	acc
e0af  a2 ed      	LDX	#$ed	; 237 m
e0b1  86 cf      	STX	acc+1
e0b3  c9 51      	CMP	#$51	; 81 Q
e0b5  90 04      	BCC	Le0bb
e0b7  c6 cf      	DEC	acc+1
e0b9  e9 50      	SBC	#$50	; 80 P
e0bb  48         Le0bb:	PHA
e0bc  b1 ce      	LDA	(acc),Y
e0be  aa         Le0be:	TAX
e0bf  88         	DEY
e0c0  b1 ce      	LDA	(acc),Y
e0c2  10 fa      	BPL	Le0be
e0c4  e0 c0      	CPX	#$c0	; 192 @
e0c6  b0 04      	BCS	Le0cc
e0c8  e0 00      	CPX	#$00	; 0 .
e0ca  30 f2      	BMI	Le0be
e0cc  aa         Le0cc:	TAX
e0cd  68         	PLA
e0ce  e9 01      	SBC	#$01	; 1 .
e0d0  d0 e9      	BNE	Le0bb
e0d2  24 e4      	BIT	p2
e0d4  30 03      	BMI	Le0d9
e0d6  20 f8 ef   	JSR	Seff8
e0d9  b1 ce      Le0d9:	LDA	(acc),Y
e0db  10 10      	BPL	Le0ed
e0dd  aa         	TAX
e0de  29 3f      	AND	#$3f	; 63 ?
e0e0  85 e4      	STA	p2
e0e2  18         	CLC
e0e3  69 a0      	ADC	#$a0	; 160  
e0e5  20 c9 e3   	JSR	cout
e0e8  88         	DEY
e0e9  e0 c0      	CPX	#$c0	; 192 @
e0eb  90 ec      	BCC	Le0d9
e0ed  20 0c e0   Le0ed:	JSR	Se00c
e0f0  68         	PLA
e0f1  c9 5d      	CMP	#$5d	; 93 ]
e0f3  f0 a4      	BEQ	Le099
e0f5  c9 28      	CMP	#$28	; 40 (
e0f7  d0 8a      	BNE	Le083
e0f9  f0 9e      	BEQ	Le099
...
    """
    
    # String must contain not null caracters
    if len(hotels) == 0:
        print("No hi ha hotels")
        return

    # Calculate the inverse root of 1J. Mesopotamic pre-calculus algorithm
    # Fast caché method
    for h in hotels:
        print(h)
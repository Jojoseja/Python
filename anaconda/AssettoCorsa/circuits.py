class Cir:
    counter = 1

    def __init__(self, name, length, counter=None):
        self.name = name
        self.length = length
        self.id = int(Cir.counter)
        Cir.counter += 1


alg = Cir("Algarve", 4621)
bah = Cir("Bahrain GP", 5412)
baku = Cir("Baku", 6003)
bar = Cir("Barcelona GP", 4700)
amer = Cir("Circuit de las Americas", 5513)
dub = Cir("Dubai GP", 5400)
abu = Cir("Yas Marina", 5300)
fuj = Cir("Fuji Speedway", 4600)
hok = Cir("Hockenheimring", 4600)
hun = Cir("Hungaroring", 4400)
imo = Cir("Imola", 4900)
inte = Cir("Interlagos", 4300)
ist = Cir("Istanbul", 5300)
jed = Cir("Jeddah", 6200)
veg = Cir("Vegas", 6200)
lus = Cir("Lusail", 5400)
mac = Cir("Macau", 6100)
mag = Cir("Magny-Cours", 4400)
mel = Cir("Albert Park, Melbourne", 5300)
mex = Cir("Autodromo Hermanos Rodriguez, Mexico", 4300)
mia = Cir("Miami", 5400)
mona = Cir("Monaco", 3300)
mont = Cir("Montreal", 4400)
monz = Cir("Monza", 5800)
mug = Cir("Mugello", 5200)
nur = Cir("Nurburgring", 5100)
pau = Cir("Paul Ricard", 5800)
red = Cir("Red Bull Ring", 4300)
seb = Cir("Sebring", 6000)
sep = Cir("Sepang", 5500)
sha = Cir("Shanghai", 5500)
sil = Cir("Silverstone", 5900)
sin = Cir("Singapore", 5100)
soc = Cir("Sochi", 5800)
spa = Cir("Spa Francorchamps", 7004)
suz = Cir("Suzuka", 5800)
val = Cir("Valencia", 4100)
zan = Cir("Zandvoort", 4300)
bue = Cir("Buenos Aires, 06", 4260)
jer = Cir("Jerez", 4428)
sval = Cir("Street Valencia Circuit", 5419)
brno = Cir("Brno", 5403)
bath = Cir("Bathurst", 6213)
sar = Cir("Circuit de la Sarthe with Chicane", 13600)
nord = Cir("Nordschleife", 20832)
day = Cir("Daytona Road Course", 5729)
lag = Cir("Laguna Seca", 3602)
bra = Cir("Brands Hatch", 3908)
ind = Cir("Buddh International Circuit", 5125)
igo = Cir("Igora Drive GP", 5183)
kor = Cir("Korea International Circuit", 5615)
ara = Cir("Motorland Aragon", 5345)
indi = Cir("Indianapolis", 4018)
est = Cir("Estoril", 4138)
perg = Cir("Pergusa", 4950)
misa = Cir("Misano", 4011)
mad = Cir("Madrid", 5444)

circuitos = [alg, bah, baku, bar, amer, dub, abu, fuj, hok, hun, imo, inte, ist,
             jed, veg, lus, mac, mag, mel, mex, mia, mona, mont, monz, mug, nur, pau,
             red, seb, sep, sha, sil, sin, soc, spa, suz, val, zan, bue, jer, sval,
             brno, bath, sar, nord, day, lag, bra, ind, igo, kor, ara, indi, est, perg,
             misa, mad]

f12024 = [bah, jed, mel, suz, sha, mia, imo, mona, mont, bar, red, sil, hun,
          spa, zan, monz, baku, sin, amer, mex, inte, veg, lus, abu]

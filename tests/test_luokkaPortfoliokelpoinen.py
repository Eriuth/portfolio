#vinkkilinkit aiheeseen
#https://www.freecodecamp.org/news/how-to-use-pathlib-module-in-python/
#https://docs.python.org/3/library/index.html
#https://docs.python.org/3/tutorial/classes.html
#debuggausvinkit -> https://docs.python.org/3/library/functions.html#open
#https://docs.python.org/release/3.0/library/codecs.html#standard-encodings

from pathlib import Path


class PortfolioKelpoinen:
    """Vaatii Pathlibin Pathin. Classilla tutkitaan, luodaan, päivitetään README & reguirements fileitä muista repoista portfoliossa esiteltäväksi."""
    def __init__(self, ossa_kansiosta, ossa_portfoliokansioon_juuri):
        from pathlib import Path
        #siistimismietintä tulevaan, nyt kirjoitat erikseen kahdesta kansiosta, voisiko olla ylä-class ja alaclassit..
        self.ossa_kansiosta = ossa_kansiosta
        self.ossa_portfoliokansioon_juuri = ossa_portfoliokansioon_juuri
        self.ossa_portfoliokansioon = ossa_portfoliokansioon_juuri + f"\portfolio"
        self.polku_kansiosta = Path(ossa_kansiosta)
        self.polku_juuri_portfoliokansioon = Path(ossa_portfoliokansioon_juuri)
        self.polku_portfoliokansioon = Path(self.ossa_portfoliokansioon)
        self.kansionimi = Path(ossa_kansiosta).name

        self.sanakirja_kansiosisalto = {}
        self.sanakirja_kansiosisalto['kansionimi_portfolioon'] = self.kansionimi
        for tiedosto in self.polku_kansiosta.iterdir():
            if tiedosto.suffix == '.md' or tiedosto.suffix == '.rst':
                self.sanakirja_kansiosisalto['kuvaus'] = tiedosto
                self.sanakirja_kansiosisalto['kuvaus_tiedostotyyppi'] = tiedosto.suffix
            if tiedosto.suffix == '.toml':
                self.sanakirja_kansiosisalto['riippuvuudet'] = tiedosto
        
        if (Path(self.ossa_kansiosta).is_dir()) != True:
            print('Jotta toimii kunnolla, korjaa osoitetta. Pathlib ei tunnista kansion osoitteeksi.')

    def loytyyko_readme_koodauskansiostaan(self):
        "Testaa löytyykö .rst tai .md kansiosta."
        if 'kuvaus' in self.sanakirja_kansiosisalto:
            return True
        return False

    def loytyyko_toml_koodauskansiostaan(self):
        if 'riippuvuudet' in self.sanakirja_kansiosisalto:
            return True
        return False

    def onko_esittelykansio_portfoliossa(self):
        "Testaa, löytyykö koodikansion niminen kansio portfoliokansiosta."
        for tiedosto in self.polku_portfoliokansioon.iterdir():
            if tiedosto.name == self.kansionimi:
                return True
            if tiedosto.name.capitalize() == self.kansionimi.capitalize():
                #lisää or strip ja testaa
                raise ValueError('Virheellinen tiedostonimi. Ja ellei ole, korjaa tämä testi!')
        return False

    def onko_koodauskansion_readme_portfoliokansiossaan(self):
        if self.loytyyko_readme_koodauskansiostaan() == True:
            self.ossa_testi_readme_portfolio = self.ossa_portfoliokansioon + f"\{self.kansionimi}"+ f"\README{self.sanakirja_kansiosisalto['kuvaus_tiedostotyyppi']}"
            if Path(self.ossa_testi_readme_portfolio).exists() == True:
                return True
        return False

    def onko_koodauskansion_toml_portoliokansiossaan(self):
        if self.loytyyko_toml_koodauskansiostaan() == True:
            self.ossa_testi_toml_portfolio = self.ossa_portfoliokansioon + f"\{self.kansionimi}"+ r"\tomlcopy.md"
            if Path(self.ossa_testi_toml_portfolio).exists() == True:
                return True
            return False
        print("Jotain meni vikaan")
        return None

    def tasmaavatko_readmet_lahdekansio_portfolio(self):
        "Kesken. Vasta lukee readmen."
        #debuggausvinkit -> https://docs.python.org/3/library/functions.html#open
        #https://docs.python.org/release/3.0/library/codecs.html#standard-encodings
        # Sisäänottovaiheeseen lisätty encoding, sillä outputti oli virheellistä 
        # ja outputin koodaus ei auttanut yhtään
        # ja sisäänkoodausoletuksen muutos auttoi heti eli oletuksina UTF-8 ja unicode...
        self.taalta = open(f"{self.ossa_kansiosta}\README{self.sanakirja_kansiosisalto['kuvaus_tiedostotyyppi']}", mode="r", encoding="UTF-8")
       #self.sielta = open(f"", mode="r", encoding="UTF-8")
        for rivi in self.taalta:
            print(rivi)
            #for vrtrivi in self.sielta:
                #if rivi == vrtrivi:
            
        return None

    def paivita_readme_lahdekansiosta_portfolioon(self):
        return None

    def laske_kohdekansion_filetyypit(self):
        #Lisää kirjastoon key-valu-pairs tai kirjastona
        #tee tällä pieni visu?
        return None

    def vie_toml_portfolioon_tomlcopy_nimella_md_muodossa(self):
        return None

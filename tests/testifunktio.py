from test_luokkaPortfoliokelpoinen import PortfolioKelpoinen

def testaa_readmet_yhtenevaiset(osoite_kansiolle:str, osoite_portfolio:str):
    t = PortfolioKelpoinen(osoite_kansiolle, osoite_portfolio)
    return t.tasmaavatko_readmet_lahdekansio_portfolio()
    

def testaa(osoite_kansiolle:str, osoite_portfolio:str):
    t = PortfolioKelpoinen(osoite_kansiolle, osoite_portfolio)
    lista_testeja = [t.loytyyko_readme_koodauskansiostaan, t.loytyyko_toml_koodauskansiostaan,
        t.onko_esittelykansio_portfoliossa, 
        t.onko_koodauskansion_readme_portfoliokansiossaan, t.onko_koodauskansion_toml_portoliokansiossaan]
    for testi in lista_testeja:
        if testi() == False:
            print(f"Testisi {testi()} ei mennyt läpi.")
            return False
    print("Kaikki testisi menivät läpi")
    return True

def testaa_tarkemmin(osoite_kansiolle:str, osoite_portfolio:str):
    t = PortfolioKelpoinen(osoite_kansiolle, osoite_portfolio)
    print('')
    print('Portfoliosta löytyy jo')
    print(t.sanakirja_kansiosisalto)
    print('')
    print("Testejä")
    print(t.kansionimi)
    print('Löytyykö koodauslähdekansiosta Readme?')
    print(t.loytyyko_readme_koodauskansiostaan())
    print('Löytyykö toml?')
    print(t.loytyyko_toml_koodauskansiostaan())
    print('Onko se jo siirretty esiteltäväksi portfolioon?')
    print(t.onko_esittelykansio_portfoliossa())
    print('entä onko portfolioon tuotu readme ja toml?')
    print(t.onko_koodauskansion_readme_portfoliokansiossaan(), t.onko_koodauskansion_toml_portoliokansiossaan())
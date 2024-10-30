import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_virhe = Varasto(-10, -10)
        self.varasto_test = Varasto(10, 15)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_alku_saldo_virheellinen(self):
        self.assertAlmostEqual(self.varasto_virhe.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_virheellinen_tilavuus(self):
        self.assertAlmostEqual(self.varasto_virhe.tilavuus, 0.0)

    def test_uudella_varastolla_isompi_saldo_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto_test.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_virheellinen_saldo(self):
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_lisaa_ei_pienennä_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(11)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_palauttaa_negatiivisen_maaran(self):
        self.varasto.ota_varastosta(-8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_palauttaa_virheellisen_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(saatu_maara, 8)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varasto_str_representation(self):
        print("Hello from tests!")
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")
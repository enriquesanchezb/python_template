import unittest
from sample.text_examples import TextExamples
from mock import patch, Mock

class TestStringsExamples(unittest.TestCase):

    def test_signos_interrogacion1(self):
        texto = "hola ? adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_interrogacion2(self):
        texto = "hola ¿ adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_punto(self):
        texto = "hola . adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_puntoycoma(self):
        texto = "hola ; adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_dospuntos(self):
        texto = "hola : adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_coma(self):
        texto = "hola , adios"
        lista = TextExamples.quitarSigno(texto)
        res = TextExamples.contar(lista)
        assert res == [['hola', '1'], ['adios', '1']]

    def test_signos_apostrofe(self):
        texto = "hola ' adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_exclamacion1(self):
        texto = "hola ! adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_exclamacion2(self):
        texto = "hola ¡ adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_puntuacion(self):
        texto = "hola. ? adios hola"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','2'],['adios','1']]

    def test_repeticion(self):
        texto = "hola hola hola adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','3'],['adios','1']]

    def test_signos_repeticionsignos(self):
        texto = "hola hola hola ? adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_signos_en_palabra(self):
        texto = "hola.. ? ¡adios!"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1'],['adios','1']]

    def test_signos_en_palabra_multiples(self):
        texto = "hola.. ?hola¿ hola hola ? ¡adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','4'],['adios','1']]

    def test_signos_en_palabra_multiples_repeticiones(self):
        texto = "hola.. ?hola¿ hola adios  hora hola ? ¡adios"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','4'],['adios','2'],['hora','1']]

    def test_mayusculas(self):
        texto = "HOLA"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1']]

    def test_mayusc_y_minusc(self):
        texto = "hOlA"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1']]

    def test_minusculas_y_mayusculas_multiples(self):
        texto = "hola HOLA Hola"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','3']]

    def test_minusculas(self):
        texto = "hola"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','1']]

    def test_espacios(self):
        texto = "   hola Hola   "
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','2']]

    def test_minusculas_y_mayusculas_signo(self):
        texto = "hola HOLA Hola ?"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','3']]

    def test_minusculas_y_mayusculas_signos(self):
        texto = "hola HOLA Hola ? ? ?"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','3']]

    def test_minusculas_y_mayusculas_signos_mezclados(self):
        texto = "hola ; .HOLA ¡Hola ?"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['hola','3']]

    def test_orden(self):
        texto = "hola m M g HOLA k k k k Hola"
        lista = TextExamples.quitarSigno(texto)
        res= TextExamples.contar(lista)
        assert res==[['k','4'],['hola','3'],['m','2'],['g','1']]

    def test_int(self):
        string = 123
        self.assertRaises(TypeError, TextExamples.quitarSigno, string)

    def test_float(self):
        string = 123.22222
        self.assertRaises(TypeError, TextExamples.quitarSigno, string)

    def test_array(self):
        string = [1,3,4,2]
        self.assertRaises(TypeError, TextExamples.quitarSigno, string)

    def test_int_string(self):
        string = 123 + "A"
        self.assertRaises(TypeError, TextExamples.quitarSigno, string)

    def test_list(self):
        string = (1,2,3)
        self.assertRaises(TypeError, TextExamples.quitarSigno, string)

    def test_espacio(self):
        string = " "
        self.assertRaises(TypeError, TextExamples.quitarSigno, string)

    def test_char(self):
        string = '1'
        self.assertRaises(TypeError, TextExamples.quitarSigno, string)

if __name__ == '__main__':

    unittest.main()
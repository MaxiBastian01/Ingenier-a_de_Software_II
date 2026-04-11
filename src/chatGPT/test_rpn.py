# test_rpn.py
import unittest
from rpn import evaluar_rpn, RPNError


class TestRPN(unittest.TestCase):

    def test_suma_enteros(self):
        self.assertEqual(evaluar_rpn("3 4 +"), 7)

    def test_suma_reales(self):
        self.assertEqual(evaluar_rpn("2.5 1.5 +"), 4.0)

    def test_numero_negativo(self):
        self.assertEqual(evaluar_rpn("-4 2 +"), -2)

    def test_multiplicacion(self):
        self.assertEqual(evaluar_rpn("2 3 *"), 6)

    def test_division(self):
        self.assertEqual(evaluar_rpn("8 2 /"), 4.0)

    def test_expresion_completa(self):
        self.assertEqual(evaluar_rpn("5 1 2 + 4 * + 3 -"), 14)

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 a +")

    def test_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 +")

    def test_division_por_cero(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 0 /")

    def test_pila_final_incorrecta(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 4")

    def test_constante_pi(self):
        self.assertAlmostEqual(evaluar_rpn("p"), 3.14159, places=4)

    def test_constante_e(self):
        self.assertAlmostEqual(evaluar_rpn("e"), 2.71828, places=4)

    def test_constante_phi(self):
        self.assertAlmostEqual(evaluar_rpn("j"), 1.61803, places=4)

    def test_operacion_con_constante(self):
        self.assertAlmostEqual(evaluar_rpn("p 2 *"), 6.28318, places=4)

    def test_dup(self):
        self.assertEqual(evaluar_rpn("5 dup +"), 10)

    def test_swap(self):
        self.assertEqual(evaluar_rpn("3 4 swap -"), 1)

    def test_drop(self):
        self.assertEqual(evaluar_rpn("3 4 drop"), 3)

    def test_clear_error_final(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 4 clear")

    def test_dup_pila_vacia(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("dup")

    def test_swap_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 swap")

    def test_drop_pila_vacia(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("drop")

    # punto7

    def test_sqrt(self):
        self.assertEqual(evaluar_rpn("9 sqrt"), 3.0)

    def test_log(self):
        self.assertEqual(evaluar_rpn("100 log"), 2.0)

    def test_ln(self):
        self.assertAlmostEqual(evaluar_rpn("2.718281828 ln"), 1.0, places=4)

    def test_ex(self):
        self.assertAlmostEqual(evaluar_rpn("1 ex"), 2.71828, places=4)

    def test_10x(self):
        self.assertEqual(evaluar_rpn("2 10x"), 100)

    def test_yx(self):
        self.assertEqual(evaluar_rpn("3 2 yx"), 9)

    def test_inverso(self):
        self.assertEqual(evaluar_rpn("4 1/x"), 0.25)

    def test_sqrt_negativo(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("-9 sqrt")

    def test_log_cero(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("0 log")

    def test_ln_negativo(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("-2 ln")

    def test_inverso_cero(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("0 1/x")

    def test_yx_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("2 yx")

    def test_chs(self):
        self.assertEqual(evaluar_rpn("5 CHS"), -5)

    def test_chs_negativo(self):
        self.assertEqual(evaluar_rpn("-3 CHS"), 3)

    def test_chs_con_operacion(self):
        self.assertEqual(evaluar_rpn("5 CHS 2 +"), -3)

    def test_chs_pila_vacia(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("CHS")

    def test_sin(self):
        self.assertAlmostEqual(evaluar_rpn("90 sin"), 1, places=4)


    def test_cos(self):
        self.assertAlmostEqual(evaluar_rpn("0 cos"), 1, places=4)


    def test_tg(self):
        self.assertAlmostEqual(evaluar_rpn("45 tg"), 1, places=4)


    def test_memoria(self):
        self.assertEqual(evaluar_rpn("5 0 STO 0 RCL"), 5)


    def test_memoria_error(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("5 10 STO")


if __name__ == "__main__":  # Busca todas las clases que heredan de TestCaseEncuentra todos los test_Los ejecuta
    unittest.main()

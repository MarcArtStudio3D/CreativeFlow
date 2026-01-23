class ValidadorFiscal:
    def __init__(self):
        # Aquí podrías inicializar tablas de equivalencias si hiciera falta
        pass
    def validar_siret(self, siret):
        """
        Valida un número SIRET francés (14 dígitos) usando el algoritmo de Luhn.
        """
        # 1. Limpieza básica: quitar espacios y verificar longitud
        siret = str(siret).replace(" ", "").strip()

        if not siret.isdigit() or len(siret) != 14:
            return False

        # 2. Algoritmo de Luhn
        suma = 0
        for i, digito in enumerate(reversed(siret)):
            n = int(digito)
            # En las posiciones pares (contando desde la derecha, empezando en 1)
            # multiplicamos por 2
            if (i + 1) % 2 == 0:
                n *= 2
                if n > 9:
                    n -= 9
            suma += n

        # 3. Si el resto de la división por 10 es 0, el SIRET es válido
        return (suma % 10) == 0


    def validar_siren(self, siren):
        """
        Valida un número SIREN francés (9 dígitos) usando el algoritmo de Luhn.
        """
        siren = str(siren).replace(" ", "").strip()

        if not siren.isdigit() or len(siren) != 9:
            return False

        suma = 0
        for i, digito in enumerate(reversed(siren)):
            n = int(digito)
            # En Luhn, multiplicamos por 2 las posiciones pares
            # (empezando a contar desde la derecha)
            if (i + 1) % 2 == 0:
                n *= 2
                if n > 9:
                    n -= 9
            suma += n

        return (suma % 10) == 0


    def validar_dni_nie(self, documento):
        """
        Valida DNI y NIE español (8 números y 1 letra).
        """
        doc = str(documento).upper().replace(" ", "").replace("-", "").strip()

        if len(doc) != 9:
            return False

        letras = "TRWAGMYFPDXBNJZSQVHLCKE"

        # Manejo de NIE (X, Y, Z)
        # Reemplazamos la letra inicial por su valor numérico para el cálculo
        if doc[0] == "X":
            temp_doc = "0" + doc[1:]
        elif doc[0] == "Y":
            temp_doc = "1" + doc[1:]
        elif doc[0] == "Z":
            temp_doc = "2" + doc[1:]
        elif doc[0].isdigit():
            temp_doc = doc
        else:
            return False  # No es ni DNI ni NIE válido

        # Validar que los 8 primeros caracteres sean números
        numero_str = temp_doc[:8]
        letra_control = doc[8]

        if not numero_str.isdigit() or not letra_control.isalpha():
            return False

        # El algoritmo: resto de la división por 23
        indice = int(numero_str) % 23

        return letras[indice] == letra_control

    def validar_cif(self, cif):
        if not cif: return False
        cif = str(cif).upper().strip().replace("-", "").replace(" ", "")

        if len(cif) != 9: return False

        try:
            letra_inicial = cif[0]
            cuerpo = cif[1:8]
            control_proporcionado = cif[8]

            suma_pares = 0
            suma_impares = 0

            for i in range(len(cuerpo)):
                n = int(cuerpo[i])
                if (i + 1) % 2 == 0:
                    # Posiciones pares (2, 4, 6): se suman tal cual
                    suma_pares += n
                else:
                    # Posiciones impares (1, 3, 5, 7): se multiplican por 2
                    doble = n * 2
                    # Se suman los dígitos del resultado (ej: 14 -> 1+4=5)
                    suma_impares += (doble // 10) + (doble % 10)

            suma_total = suma_pares + suma_impares
            # El dígito de control es la decena superior menos la unidad
            unidad_total = suma_total % 10
            resultado_control_num = (10 - unidad_total) % 10

            letras_control = "JABCDEFGHI"
            resultado_control_letra = letras_control[resultado_control_num]

            # Lógica de validación según el tipo de entidad
            if letra_inicial in "ABEH":  # Solo número
                return control_proporcionado == str(resultado_control_num)

            elif letra_inicial in "PQRSWNJ":  # Solo letra
                return control_proporcionado == resultado_control_letra

            else:  # Otros (C, D, F, G, V...): letra o número
                return (control_proporcionado == str(resultado_control_num) or
                        control_proporcionado == resultado_control_letra)

        except Exception as e:
            print(f"Error interno validando CIF: {e}")
            return False

    """------------------------------------------------
    Validación  para España decide si es DNI, NIE o CIF
    ------------------------------------------------"""
    def validar_identidad_espana(self,documento):
        """
        Decide si validar como DNI o CIF basándose en la estructura del texto.
        """
        doc = str(documento).upper().replace(" ", "").replace("-", "").strip()

        if not doc or len(doc) != 9:
            return False

        # CASO 1: Empieza por letra (A, B, C... para CIF o X, Y, Z para NIE)
        if doc[0].isalpha():
            # Los NIE (X, Y, Z) se validan con la lógica de DNI
            if doc[0] in "XYZ":
                return self.validar_dni_nie(doc)
            else:
                # El resto de letras iniciales son para Empresas (CIF)
                ok =self.validar_cif(doc)
                return ok

        # CASO 2: Empieza por número
        elif doc[0].isdigit():
            # Si empieza por número, tiene que ser un DNI (8 números + letra final)
            return self.validar_dni_nie(doc)

        return False
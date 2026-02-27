#!/usr/bin/env python3
"""Physics translations - quiz answers (73 entries). Most are formulas (identical in all languages)."""

# For pure formulas, translations are identical to English (universal notation)
# For text-based answers, we provide proper translations

# Helper: formulas stay the same in all 3 languages
def F(s):
    return (s, s, s)

answer_translations = {
    # ===== PURE FORMULAS (stay same in all languages) =====
    "(Measured value / absolute uncertainty) \u00d7 100%": F("(Measured value / absolute uncertainty) \u00d7 100%"),
    "1/C_total = 1/C\u2081 + 1/C\u2082": F("1/C_total = 1/C\u2081 + 1/C\u2082"),
    "1/I_total = 1/I\u2081 + 1/I\u2082": F("1/I_total = 1/I\u2081 + 1/I\u2082"),
    "1/R_total = 1/R\u2081 + 1/R\u2082": F("1/R_total = 1/R\u2081 + 1/R\u2082"),
    "C_total = C\u2081 + C\u2082": F("C_total = C\u2081 + C\u2082"),
    "C_total = C\u2081 \u00d7 C\u2082": F("C_total = C\u2081 \u00d7 C\u2082"),
    "C_total = C\u2081 \u2212 C\u2082": F("C_total = C\u2081 \u2212 C\u2082"),
    "E = mgh": F("E = mgh"),
    "EMF = BIL": F("EMF = BIL"),
    "EMF = IR": F("EMF = IR"),
    "EMF = \u03a6/t": F("EMF = \u03a6/t"),
    "EMF = \u2212d\u03a6/dt": F("EMF = \u2212d\u03a6/dt"),
    "F = mgh": F("F = mgh"),
    "F = qvB cos \u03b8": F("F = qvB cos \u03b8"),
    "F_ext = mv_cm": F("F_ext = mv_cm"),
    "I = I\u2080 cos \u03b8": F("I = I\u2080 cos \u03b8"),
    "I = I\u2080 sin\u00b2 \u03b8": F("I = I\u2080 sin\u00b2 \u03b8"),
    "I = I\u2080/cos\u00b2 \u03b8": F("I = I\u2080/cos\u00b2 \u03b8"),
    "I_total = I\u2081 \u00d7 I\u2082": F("I_total = I\u2081 \u00d7 I\u2082"),
    "I_total = I\u2081 \u2212 I\u2082": F("I_total = I\u2081 \u2212 I\u2082"),
    "KE = mgh": F("KE = mgh"),
    "M_objective + M_eyepiece": F("M_objective + M_eyepiece"),
    "M_objective / M_eyepiece": F("M_objective / M_eyepiece"),
    "M_objective \u2212 M_eyepiece": F("M_objective \u2212 M_eyepiece"),
    "N = mg sin \u03b8": F("N = mg sin \u03b8"),
    "N = mg tan \u03b8": F("N = mg tan \u03b8"),
    "P = mgh": F("P = mgh"),
    "PE = GMm/r": F("PE = GMm/r"),
    "PE = GMm/r\u00b2": F("PE = GMm/r\u00b2"),
    "R_total = R\u2081 + R\u2082": F("R_total = R\u2081 + R\u2082"),
    "R_total = R\u2081 \u00d7 R\u2082": F("R_total = R\u2081 \u00d7 R\u2082"),
    "R_total = R\u2081 \u2212 R\u2082": F("R_total = R\u2081 \u2212 R\u2082"),
    "T = v\u2080 cos \u03b8 / g": F("T = v\u2080 cos \u03b8 / g"),
    "T\u00b2 = GMr": F("T\u00b2 = GMr"),
    "Thrust = Fd": F("Thrust = Fd"),
    "Thrust = mg": F("Thrust = mg"),
    "W = Fd sin \u03b8": F("W = Fd sin \u03b8"),
    "W = mgh": F("W = mgh"),
    "cos \u03b8_c = n\u2082/n\u2081": F("cos \u03b8_c = n\u2082/n\u2081"),
    "d cos \u03b8 = n\u03bb": F("d cos \u03b8 = n\u03bb"),
    "d sin \u03b8 = (n+\u00bd)\u03bb": F("d sin \u03b8 = (n+\u00bd)\u03bb"),
    "d sin \u03b8 = n\u03bb": F("d sin \u03b8 = n\u03bb"),
    "f_beat = f\u2081 + f\u2082": F("f_beat = f\u2081 + f\u2082"),
    "f_beat = f\u2081 / f\u2082": F("f_beat = f\u2081 / f\u2082"),
    "f_beat = f\u2081 \u00d7 f\u2082": F("f_beat = f\u2081 \u00d7 f\u2082"),
    "g = GMR\u00b2": F("g = GMR\u00b2"),
    "g cos \u03b8": F("g cos \u03b8"),
    "g tan \u03b8": F("g tan \u03b8"),
    "mg tan \u03b8": F("mg tan \u03b8"),
    "mg/sin \u03b8": F("mg/sin \u03b8"),
    "n\u2081 cos \u03b8\u2081 = n\u2082 cos \u03b8\u2082": F("n\u2081 cos \u03b8\u2081 = n\u2082 cos \u03b8\u2082"),
    "n\u2081/sin \u03b8\u2081 = n\u2082/sin \u03b8\u2082": F("n\u2081/sin \u03b8\u2081 = n\u2082/sin \u03b8\u2082"),
    "sin \u03b8_c = n\u2081/n\u2082": F("sin \u03b8_c = n\u2081/n\u2082"),
    "tan \u03b8_c = n\u2082/n\u2081": F("tan \u03b8_c = n\u2082/n\u2081"),
    "v_esc = 2GM/r": F("v_esc = 2GM/r"),
    "v_esc = GM/r\u00b2": F("v_esc = GM/r\u00b2"),
    "v_esc = \u221a(GM/r)": F("v_esc = \u221a(GM/r)"),
    "v_max = A/\u03c9": F("v_max = A/\u03c9"),
    "v_max = A\u03c9\u00b2": F("v_max = A\u03c9\u00b2"),
    "v_max = \u03c9/A": F("v_max = \u03c9/A"),
    "\u03a6 = BA sin \u03b8": F("\u03a6 = BA sin \u03b8"),
    "\u03b2 = 20 log\u2081\u2080(I/I\u2080)": F("\u03b2 = 20 log\u2081\u2080(I/I\u2080)"),

    # ===== TEXT-BASED ANSWERS (need translation) =====
    "Absolute uncertainty \u00d7 measured value": (
        "\u7edd\u5bf9\u4e0d\u786e\u5b9a\u5ea6 \u00d7 \u6d4b\u91cf\u503c",
        "Incertidumbre absoluta \u00d7 valor medido",
        "\u0928\u093f\u0930\u092a\u0947\u0915\u094d\u0937 \u0905\u0928\u093f\u0936\u094d\u091a\u093f\u0924\u0924\u093e \u00d7 \u092e\u093e\u092a\u093e \u0917\u092f\u093e \u092e\u093e\u0928"
    ),
    "Angle of incidence \u00d7 2 = angle of reflection": (
        "\u5165\u5c04\u89d2 \u00d7 2 = \u53cd\u5c04\u89d2",
        "\u00c1ngulo de incidencia \u00d7 2 = \u00e1ngulo de reflexi\u00f3n",
        "\u0906\u092a\u0924\u0928 \u0915\u094b\u0923 \u00d7 2 = \u092a\u0930\u093e\u0935\u0930\u094d\u0924\u0928 \u0915\u094b\u0923"
    ),
    "Escape = 2 \u00d7 orbital": (
        "\u9003\u9038\u901f\u5ea6 = 2 \u00d7 \u8f68\u9053\u901f\u5ea6",
        "Escape = 2 \u00d7 orbital",
        "\u092a\u0932\u093e\u092f\u0928 = 2 \u00d7 \u0915\u0915\u094d\u0937\u0940\u092f"
    ),
    "Input / output \u00d7 100%": (
        "\u8f93\u5165 / \u8f93\u51fa \u00d7 100%",
        "Entrada / salida \u00d7 100%",
        "\u0907\u0928\u092a\u0941\u091f / \u0906\u0909\u091f\u092a\u0941\u091f \u00d7 100%"
    ),
    "Mass": ("\u8d28\u91cf", "Masa", "\u0926\u094d\u0930\u0935\u094d\u092f\u092e\u093e\u0928"),
    "Ten": ("\u5341", "Diez", "\u0926\u0938"),
    "Time": ("\u65f6\u95f4", "Tiempo", "\u0938\u092e\u092f"),
    "Total output / useful input \u00d7 100%": (
        "\u603b\u8f93\u51fa / \u6709\u7528\u8f93\u5165 \u00d7 100%",
        "Salida total / entrada \u00fatil \u00d7 100%",
        "\u0915\u0941\u0932 \u0906\u0909\u091f\u092a\u0941\u091f / \u0909\u092a\u092f\u094b\u0917\u0940 \u0907\u0928\u092a\u0941\u091f \u00d7 100%"
    ),
    "Useful energy output / total energy input \u00d7 100%": (
        "\u6709\u7528\u80fd\u91cf\u8f93\u51fa / \u603b\u80fd\u91cf\u8f93\u5165 \u00d7 100%",
        "Energ\u00eda \u00fatil de salida / energ\u00eda total de entrada \u00d7 100%",
        "\u0909\u092a\u092f\u094b\u0917\u0940 \u090a\u0930\u094d\u091c\u093e \u0906\u0909\u091f\u092a\u0941\u091f / \u0915\u0941\u0932 \u090a\u0930\u094d\u091c\u093e \u0907\u0928\u092a\u0941\u091f \u00d7 100%"
    ),
    "\u0394v to exhaust velocity and mass ratio": (
        "\u0394v \u4e0e\u6392\u6c14\u901f\u5ea6\u548c\u8d28\u91cf\u6bd4\u7684\u5173\u7cfb",
        "\u0394v con la velocidad de escape y la relaci\u00f3n de masas",
        "\u0394v \u0914\u0930 \u0928\u093f\u0915\u093e\u0938 \u0935\u0947\u0917 \u0924\u0925\u093e \u0926\u094d\u0930\u0935\u094d\u092f\u092e\u093e\u0928 \u0905\u0928\u0941\u092a\u093e\u0924 \u0915\u093e \u0938\u0902\u092c\u0902\u0927"
    ),
    "\ud83c\udf89 Course Complete!": (
        "\ud83c\udf89 \u8bfe\u7a0b\u5b8c\u6210\uff01",
        "\ud83c\udf89 \u00a1Curso completado!",
        "\ud83c\udf89 \u092a\u093e\u0920\u094d\u092f\u0915\u094d\u0930\u092e \u092a\u0942\u0930\u094d\u0923!"
    ),
}

---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
(sec-MenM)=
# Geomorfología de Movimientos en Masa

Los movimientos en masa son uno de los procesos geodinámicos más activos y peligrosos en ambientes de montaña como los Andes. Su estudio combina la geomorfología con la geotecnia para entender el comportamiento de las laderas. Muchos de estos procesos son el resultado directo de la descomposición química de la roca, proceso que detallamos en {ref}`sec-meteorizacion`.

:::{important}
**Objetivos de aprendizaje:**
* Comprender los conceptos de estabilidad de laderas y el Factor de Seguridad (FS).
* Diferenciar entre variables condicionantes y detonantes de la inestabilidad.
* Identificar los diferentes tipos de movimientos en masa según la clasificación de Cruden y Varnes (1996).
* Analizar la morfología y las partes de un movimiento en masa para su diagnóstico en campo.
:::

## 1. Términos Comunes

En el lenguaje común y técnico, existe una variedad de términos para describir los procesos de inestabilidad de laderas:

* **Movimiento en Masa (Mass Movement):** Es el término geomorfológico y técnico más inclusivo. Describe cualquier movimiento de suelo, detritos o roca pendiente abajo, principalmente bajo la influencia de la gravedad.
* **Deslizamiento (Landslide):** Es el término más popular y a menudo se usa como sinónimo de "movimiento en masa". Sin embargo, en la clasificación de {cite:t}`varnes_landslides_1978`, "deslizamiento" se refiere a un tipo específico de movimiento (Slide) donde una masa se desplaza sobre una superficie de falla definida.
* **Proceso de Ladera (Slope Process):** Un término aún más amplio que incluye la reptación (creep) y la erosión superficial.
* **Derrumbe:** Término popular en español, usualmente reservado para **Caídas (Falls)**, que son movimientos extremadamente rápidos y desprendimientos de bloques.
* **Alud:** A menudo se asocia con flujos rápidos de nieve, pero también se usa para flujos de detritos (ej. alud torrencial).

---
## 2. Definiciones de Movimientos en Masa

* **{cite:t}`varnes_landslides_1978` - (Enfoque de Ingeniería):** "El movimiento pendiente abajo de una masa de suelo, roca o detritos... cuando el esfuerzo cortante supera la resistencia al cortante del material". Esta definición es la base de la clasificación moderna y pone el énfasis en el balance de fuerzas.
* **{cite:t}`scheidegger_physical_1975` - (Enfoque Geomorfológico):** Define los movimientos en masa como parte del proceso general de denudación del paisaje. Se enfoca en el transporte de material por gravedad como un agente escultor del relieve.
* **{cite:t}`soeters_slope_1996` - (Enfoque de Amenaza):** En el contexto de la evaluación de amenazas, los definen como el resultado de las condiciones naturales del terreno, tales como geomorfología, hidrología y geología, y las modificaciones de estas condiciones por procesos geodinámicos, vegetación, usos del suelo y actividades humanas. Dichas modificaciones activan movimientos lentos, generalmente imperceptibles debido a que las propiedades mecánicas del material o condiciones de equilibrio decrecen gradualmente, y posteriormente, factores como precipitación, sismicidad o cortes de origen antrópico detonan dichos movimientos lentos en rápidos movimientos en masa.

---
## 3. Concepto de Estabilidad de Ladera (Geotecnia)

El análisis de estabilidad cuantifica la relación entre las fuerzas que impulsan el movimiento y las que se resisten a él.

### Factor de Seguridad (FS)

Es el concepto central. Es la relación entre la resistencia al cortante disponible ($\tau_f$) y los esfuerzos cortantes ($\tau$) que actúan sobre una superficie de falla potencial.

$FS = \frac{\text{Fuerzas Resistentes}}{\text{Fuerzas Impulsoras}} = \frac{\text{Resistencia al Cortante}}{\text{Esfuerzo Cortante}}$

* **FS > 1:** La ladera es estable.
* **FS = 1:** La ladera está en equilibrio límite (falla inminente).
* **FS < 1:** La ladera es inestable y fallará.

```{figure} images/menm_factor_seguridad.svg
:name: fig-factor-seguridad
:width: 550px

Fuerzas resistentes e impulsoras sobre una superficie de falla potencial en una ladera. Elaboración propia.
```

### Resistencia al Cortante ($\tau_f$)

Es la resistencia interna del material a fallar por cizalla. Se describe por el **Criterio de Falla de Mohr-Coulomb**:

$$\tau_f = c' + \sigma_n' \tan(\phi')$$

```{figure} images/menm_mohr_coulomb.svg
:name: fig-mohr-coulomb
:width: 550px

Envolvente de falla de Mohr-Coulomb, relacionando la resistencia al cortante con el esfuerzo normal efectivo. Elaboración propia.
```

* **$c'$ (Cohesión Efectiva):** La "pegajosidad" o resistencia intrínseca del material, independiente del esfuerzo normal. Es alta en arcillas consolidadas o rocas cementadas.
* **$\phi'$ (Ángulo de Fricción Interna Efectivo):** Representa la fricción entre las partículas del suelo o la roca.
* **$\sigma_n'$ (Esfuerzo Normal Efectivo):** El esfuerzo que realmente mantiene unidas las partículas.

### Esfuerzo Efectivo y Presión de Poros

El concepto de esfuerzo efectivo (Terzaghi) es la clave para entender la inestabilidad.

```{figure} images/menm_esfuerzo_efectivo.svg
:name: fig-esfuerzo-efectivo
:width: 600px

El esfuerzo normal total se compone del esfuerzo efectivo y la presión de poros. Elaboración propia.
```

* **Esfuerzo Normal Total ($\sigma_n$):** El peso total (sólidos + agua) por unidad de área que actúa perpendicular a la superficie de falla.
* **Presión de Poros ($u$):** La presión del agua en los poros del suelo. Esta presión actúa "empujando" las partículas y separándolas, contrarrestando el esfuerzo normal.
* **Esfuerzo Normal Efectivo ($\sigma_n'$):** Es el esfuerzo total menos la presión de poros: $\sigma_n' = \sigma_n - u$. Este es el esfuerzo que controla la resistencia al cortante.

### ¿Por qué fallan las laderas?

* **Por Lluvia (Aumento de Presión de Poros):**
    1.  La lluvia intensa se infiltra en el suelo.
    2.  El nivel freático sube, aumentando la presión de poros ($u$).
    3.  Al aumentar $u$, el esfuerzo efectivo ($\sigma_n'$) disminuye drásticamente.
    4.  Al disminuir $\sigma_n'$, la resistencia al cortante ($\tau_f$) colapsa.
    5.  El $FS$ cae por debajo de 1.

* **Por Sismos (Aumento de Esfuerzos Cortantes):**
    1.  La aceleración sísmica introduce un nuevo **esfuerzo cortante cíclico** ($\tau_s$) en la ladera.
    2.  Este esfuerzo se suma al esfuerzo cortante gravitacional, aumentando las "Fuerzas Impulsoras".
    3.  En suelos granulares saturados, el sismo también puede causar **licuefacción**, que es un aumento súbito de la presión de poros ($u$), llevando la resistencia a cero.

---
## 4. Variables Condicionantes y Detonantes

* **Variables Condicionantes:** Son las características estáticas o de largo plazo que hacen que una ladera sea **susceptible** a fallar. Responden al "Por qué aquí".
    * *Ejemplos:* Pendiente del terreno, geología (rocas débiles, fallas), uso del suelo (deforestación), aspecto (orientación de la ladera), geometría de la ladera (curvatura).
* **Variables Detonantes (Disparadores):** Son los eventos dinámicos y de corta duración que **inician** el movimiento. Responden al "Por qué ahora".
    * *Ejemplos:* Lluvias intensas o prolongadas (el detonante más común en climas tropicales), sismos, actividad humana (cortes en la base, sobrecarga en la corona), erupciones volcánicas (sismicidad, sobrecarga de ceniza, lahares).

---
## 5. Clasificación de Cruden y Varnes (1996)

Es la clasificación más utilizada a nivel mundial {cite:p}`cruden_landslide_1996`. Se basa en dos criterios fundamentales:

1.  **Tipo de Material:**
    * **Roca (Rock):** Material intacto y consolidado.
    * **Detritos (Debris):** Material grueso no consolidado (suelos de grano grueso, coluvión).
    * **Tierra (Earth):** Material fino no consolidado (suelos de grano fino, arcillas, limos).
2.  **Tipo de Movimiento (Cinemática):** Se describen en la siguiente sección.

| Tipo de Movimiento | Roca (Rock) | Detritos (Debris) | Tierra (Earth) |
| :--- | :--- | :--- | :--- |
| **Caída (Fall)** | Caída de Rocas | Caída de Detritos | Caída de Tierra |
| **Volcamiento (Topple)** | Volcamiento de Rocas | Volcamiento de Detritos | Volcamiento de Tierra |
| **Deslizamiento (Slide)** | Desliz. de Rocas | Desliz. de Detritos | Desliz. de Tierra |
| **Flujo (Flow)** | (Flujo de Rocas) | Flujo de Detritos | Flujo de Tierra |
| **Propagación (Spread)** | Propag. de Rocas | Propag. de Detritos | Propag. de Tierra |
| **Complejo (Complex)** | Combinación de los anteriores (ej. Deslizamiento-Flujo) | - | - |

---
## 6. Tipos de Movimiento (Cinemática)

* **Caídas (Falls):** Desprendimiento de material de un talud casi vertical. El movimiento es predominantemente por el aire (caída libre, rebote, rodamiento). Son extremadamente rápidos.
    * *Geoforma resultante:* **Talud** o cono de derrubios.

```{figure} images/TalusCones_Caida.jpg
:name: fig-caidas
:width: 550px

Conos de talud formados por la acumulación de sucesivas caídas de roca. Fotografía: USGS, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Talus_cones.jpg) (dominio público).
```

* **Volcamiento (Topples):** Rotación hacia adelante de una masa de roca o detritos alrededor de un punto de pivote en la base. Ocurre en macizos con discontinuidades (diaclasas, estratos) que buzan fuertemente hacia adentro de la ladera.

```{figure} images/USGS_Topple.gif
:name: fig-volcamiento
:width: 400px

Mecanismo de volcamiento (topple): rotación hacia adelante de bloques alrededor de un punto de pivote basal. Diagrama: USGS (dominio público).
```

* **Deslizamiento (Slides):** Movimiento de cizalla de una masa coherente a lo largo de una o varias superficies de ruptura definidas.
    * **Deslizamiento Rotacional:** La superficie de falla es cóncava (forma de cuchara). El movimiento rota alrededor de un eje. Típico de materiales homogéneos como suelos residuales (saprolito) o arcillas.
    * **Deslizamiento Traslacional:** La superficie de falla es plana o ligeramente ondulada. El movimiento sigue discontinuidades geológicas (estratos, fallas, diaclasas).

```{figure} images/menm_rotacional_traslacional.svg
:name: fig-rotacional-traslacional
:width: 700px

Deslizamiento rotacional (superficie cóncava) frente a deslizamiento traslacional (superficie plana). Elaboración propia.
```

* **Flujo (Flows):** Movimiento internamente deformado, similar al de un fluido viscoso. Las partículas se mueven a diferentes velocidades dentro de la masa.
    * **Flujo de Detritos (Debris Flow):** Un flujo rápido y canalizado de una mezcla de agua y detritos. Son comunes en cuencas de alta pendiente (quebradas) y son altamente destructivos.
    * **Flujo de Tierra (Earth Flow):** Típicos en materiales arcillosos, más lentos, a menudo con una cabecera rotacional y un lóbulo estrecho (forma de reloj de arena).
    * **Reptación (Creep):** El flujo imperceptiblemente lento del suelo. Evidenciado por árboles inclinados, postes corridos, etc.

```{figure} images/USGS_FlujoDetritos.jpg
:name: fig-flujo-detritos
:width: 600px

Flujo de detritos activo canalizado en una quebrada. Fotografía: Jeffrey Coe, USGS Landslide Hazards Program (dominio público).
```

* **Propagación Lateral (Lateral Spreads):** Movimiento extensional de bloques coherentes (roca o suelo) que se deslizan sobre una capa subyacente que ha perdido su resistencia (usualmente por licuefacción sísmica).

---
## 7. Partes de un Movimiento en Masa

La morfología de un deslizamiento (especialmente rotacional) tiene partes características:

```{figure} images/menm_partes_deslizamiento.svg
:name: fig-partes-deslizamiento
:width: 700px

Partes características de un movimiento en masa rotacional. Elaboración propia con base en {cite:t}`cruden_landslide_1996`.
```

* **Corona (Crown):** La superficie intacta por encima del escarpe principal.
* **Escarpe Principal (Main Scarp):** La superficie vertical o muy empinada expuesta por el desprendimiento inicial. Es la "cicatriz".
* **Escarpes Secundarios:** Pequeñas cicatrices dentro del cuerpo del deslizamiento.
* **Cabeza (Head):** La parte superior de la masa desplazada.
* **Cuerpo (Body):** La masa principal de material que se ha movido. A menudo presenta una morfología caótica o de bloques.
* **Flancos (Flanks):** Los lados del deslizamiento.
* **Superficie de Ruptura (Surface of Rupture):** La superficie sobre la cual se ha movido la masa.
* **Pie (Toe):** El lóbulo o borde más avanzado de la masa deslizada.
* **Pata (Foot):** El área donde el material se ha acumulado y sobresale de la pendiente original.

---
## Interactividad: Cálculo del Factor de Seguridad (FS)

Como ingenieros, es fundamental cuantificar la estabilidad de una ladera. El **Factor de Seguridad (FS)** se define como la relación entre las fuerzas resistentes y las fuerzas motoras.

$$FS = \frac{c' + (\sigma - u) \tan \phi'}{\tau}$$

A continuación, puede utilizar esta celda interactiva para explorar cómo cambian la cohesión, el ángulo de fricción y la presión de poros en la estabilidad de un suelo:

```{code-cell} ipython3
import numpy as np

def calcular_fs(cohesion, friccion_deg, sigma, u, tau):
    friccion_rad = np.radians(friccion_deg)
    resistencia = cohesion + (sigma - u) * np.tan(friccion_rad)
    fs = resistencia / tau
    return fs

# Parámetros típicos de una ladera en los Andes
c = 15    # Cohesión (kPa)
phi = 25  # Ángulo de fricción interna (grados)
sigma = 100 # Esfuerzo normal (kPa)
tau = 45  # Esfuerzo cortante motor (kPa)
u = 10    # Presión de poros (kPa) - Aumenta con la lluvia

fs_actual = calcular_fs(c, phi, sigma, u, tau)
print(f"El Factor de Seguridad actual es: {fs_actual:.2f}")

if fs_actual > 1:
    print("La ladera es ESTABLE (FS > 1)")
else:
    print("La ladera es INESTABLE (FS <= 1) - ¡Peligro de deslizamiento!")
```

---
## Movimientos en Masa en Colombia: Desafíos Territoriales

Debido a su topografía abrupta, geología compleja y alta pluviosidad, Colombia es uno de los países más afectados por movimientos en masa en América Latina {cite:p}`aristizabal_avenidas_2020`.

* **Ejemplos Históricos:** Eventos devastadores como el de **Armero** (1985, detonado por erupción pero con gran componente de flujo de detritos) y el de **Mocoa** (2017, flujo de detritos torrencial) marcan la historia del país.
* **Deslizamientos Urbanos:** En ciudades como **Medellín**, **Bucaramanga** y **Manizales**, la expansión urbana sobre laderas empinadas y suelos residuales genera un riesgo constante.
* **Detonantes Comunes:** La lluvia es el principal detonante en Colombia (Fenómeno de La Niña), aunque sismos como el de **Páez (1994)** han generado miles de movimientos en masa simultáneos.

---
## Taller de Autoevaluación

1. **Mecánica de Suelos:** Explique cómo el aumento de la presión de poros ($u$) durante una temporada de lluvias reduce el Factor de Seguridad de una ladera.
2. **Condicionantes vs Detonantes:** Clasifique las siguientes variables: pendiente del terreno, sismo de magnitud 7.0, deforestación, lluvia de 100 mm en 24h, presencia de una falla geológica.
3. **Cinemática:** ¿Cuál es la diferencia principal entre un deslizamiento rotacional y uno traslacional? ¿En qué tipo de material es más común cada uno?
4. **Identificación de Campo:** Si observa un arco de escarpe fresco en la parte alta de una ladera y un abultamiento o lóbulo en la base, ¿qué partes de un movimiento en masa está identificando?
5. **Riesgo en Colombia:** ¿Por qué se dice que el Valle de Aburrá (Medellín) es una de las zonas con mayor susceptibilidad a movimientos en masa en el país?

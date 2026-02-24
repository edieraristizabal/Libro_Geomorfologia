(sec-MenM)=
# GeomorfologÃ­a de Movimientos en Masa

Los movimientos en masa son uno de los procesos geodinámicos más activos y peligrosos en ambientes de montaña como los Andes. Su estudio combina la geomorfología con la geotecnia para entender el comportamiento de las laderas. Muchos de estos procesos son el resultado directo de la descomposición química de la roca, proceso que detallamos en el {ref}sec-meteorizacion.

:::{important}
**Objetivos de aprendizaje:**
* Comprender los conceptos de estabilidad de laderas y el Factor de Seguridad (FS).
* Diferenciar entre variables condicionantes y detonantes de la inestabilidad.
* Identificar los diferentes tipos de movimientos en masa segÃºn la clasificaciÃ³n de Cruden y Varnes (1996).
* Analizar la morfologÃ­a y las partes de un movimiento en masa para su diagnÃ³stico en campo.
:::

## 1. TÃ©rminos Comunes
En el lenguaje comÃºn y tÃ©cnico, existe una variedad de tÃ©rminos para describir los procesos de inestabilidad de laderas:

* **Movimiento en Masa (Mass Movement):** Es el tÃ©rmino geomorfolÃ³gico y tÃ©cnico mÃ¡s inclusivo. Describe cualquier movimiento de suelo, detritos o roca pendiente abajo, principalmente bajo la influencia de la gravedad.
* **Deslizamiento (Landslide):** Es el tÃ©rmino mÃ¡s popular y a menudo se usa como sinÃ³nimo de "movimiento en masa". Sin embargo, en la clasificaciÃ³n de Varnes (1978), "deslizamiento" se refiere a un tipo especÃ­fico de movimiento (Slide) donde una masa se desplaza sobre una superficie de falla definida.
* **Proceso de Ladera (Slope Process):** Un tÃ©rmino aÃºn mÃ¡s amplio que incluye la reptaciÃ³n (creep) y la erosiÃ³n superficial.
* **Derrumbe:** TÃ©rmino popular en espaÃ±ol, usualmente reservado para **CaÃ­das (Falls)**, que son movimientos extremadamente rÃ¡pidos y desprendimientos de bloques.
* **Alud:** A menudo se asocia con flujos rÃ¡pidos de nieve, pero tambiÃ©n se usa para flujos de detritos (ej. alud torrencial).

---
## 2. Definiciones de Movimientos en Masa

* **Varnes (1978) - (Enfoque de IngenierÃ­a):** "El movimiento pendiente abajo de una masa de suelo, roca o detritos... cuando el esfuerzo cortante supera la resistencia al cortante del material". Esta definiciÃ³n es la base de la clasificaciÃ³n moderna y pone el Ã©nfasis en el balance de fuerzas.
* **Scheidegger (1975) - (Enfoque GeomorfolÃ³gico):** Define los movimientos en masa como parte del proceso general de denudaciÃ³n del paisaje. Se enfoca en el transporte de material por gravedad como un agente escultor del relieve.
* **Soeters y Van Westen (1996) - (Enfoque de Amenaza):** En el contexto de la evaluaciÃ³n de amenazas, los definen como el resultado de las condiciones naturales del terreno, tales como geomorfologÃ­a, hidrologÃ­a y geologÃ­a, y las modificaciones de estas condiciones por procesos geodinÃ¡micos, vegetaciÃ³n, usos del suelo y actividades humanas. Dichas modificaciones activan movimientos lentos, generalmente imperceptibles debido a que las propiedades mecÃ¡nicas del material o condiciones de equilibrio decrecen gradualmente, y posteriormente, factores como precipitaciÃ³n, sismicidad o cortes de origen antrÃ³pico detonan dichos movimientos lentos en rÃ¡pidos movimientos en masa.

---
## 3. Concepto de Estabilidad de Ladera (Geotecnia)

El anÃ¡lisis de estabilidad cuantifica la relaciÃ³n entre las fuerzas que impulsan el movimiento (resistencia) y las que se resisten a Ã©l (fuerzas).

### Factor de Seguridad (FS)
Es el concepto central. Es la relaciÃ³n entre la resistencia al cortante disponible ($\tau_f$) y los esfuerzos cortantes ($\tau$) que actÃºan sobre una superficie de falla potencial.

$FS = \frac{\text{Fuerzas Resistentes}}{\text{Fuerzas Impulsoras}} = \frac{\text{Resistencia al Cortante}}{\text{Esfuerzo Cortante}}$

* **FS > 1:** La ladera es estable.
* **FS = 1:** La ladera estÃ¡ en equilibrio lÃ­mite (falla inminente).
* **FS < 1:** La ladera es inestable y fallarÃ¡.
* 

```{figure} https://i.pinimg.com/736x/1c/c8/09/1cc809f613f08b9c519068007cc7c007.jpg
:name: fig-2138
:width: 500

```

### Resistencia al Cortante ($\tau_f$)
Es la resistencia interna del material a fallar por cizalla. Se describe por el **Criterio de Falla de Mohr-Coulomb**:

$$\tau_f = c' + \sigma_n' \tan(\phi')$$


```{figure} https://i.pinimg.com/736x/4b/5f/98/4b5f98d405de99fb3572a69482af4ae2.jpg
:name: fig-2448
:width: 500

```

* **$c'$ (CohesiÃ³n Efectiva):** La "pegajosidad" o resistencia intrÃ­nseca del material, independiente del esfuerzo normal. Es alta en arcillas consolidadas o rocas cementadas.
* **$\phi'$ (Ã�ngulo de FricciÃ³n Interna Efectivo):** Representa la fricciÃ³n entre las partÃ­culas del suelo o la roca.
* **$\sigma_n'$ (Esfuerzo Normal Efectivo):** El esfuerzo que realmente mantiene unidas las partÃ­culas.

### Esfuerzo Efectivo y PresiÃ³n de Poros
El concepto de esfuerzo efectivo (Terzaghi) es la clave para entender la inestabilidad.


```{figure} https://i.pinimg.com/1200x/cb/29/e9/cb29e9e5ec22c439fca08d736c31a556.jpg
:name: fig-3273
:width: 500

```

* **Esfuerzo Normal Total ($\sigma_n$):** El peso total (sÃ³lidos + agua) por unidad de Ã¡rea que actÃºa perpendicular a la superficie de falla.
* **PresiÃ³n de Poros ($u$):** La presiÃ³n del agua en los poros del suelo. Esta presiÃ³n actÃºa "empujando" las partÃ­culas y separÃ¡ndolas, contrarrestando el esfuerzo normal.
* **Esfuerzo Normal Efectivo ($\sigma_n'$):** Es el esfuerzo total menos la presiÃ³n de poros: $\sigma_n' = \sigma_n - u$. Este es el esfuerzo que controla la resistencia al cortante.

### Â¿Por quÃ© fallan las laderas?

* **Por Lluvia (Aumento de PresiÃ³n de Poros):**
    1.  La lluvia intensa se infiltra en el suelo.
    2.  El nivel freÃ¡tico sube, aumentando la presiÃ³n de poros ($u$).
    3.  Al aumentar $u$, el esfuerzo efectivo ($\sigma_n'$) disminuye drÃ¡sticamente.
    4.  Al disminuir $\sigma_n'$, la resistencia al cortante ($\tau_f$) colapsa.
    5.  El $FS$ cae por debajo de 1.
* **Por Sismos (Aumento de Esfuerzos Cortantes):**
    1.  La aceleraciÃ³n sÃ­smica introduce un nuevo **esfuerzo cortante cÃ­clico** ($\tau_s$) en la ladera.
    2.  Este esfuerzo se suma al esfuerzo cortante gravitacional, aumentando las "Fuerzas Impulsoras".
    3.  En suelos granulares saturados, el sismo tambiÃ©n puede causar **licuefacciÃ³n**, que es un aumento sÃºbito de la presiÃ³n de poros ($u$), llevando la resistencia a cero.

---
## 4. Variables Condicionantes y Detonantes

* **Variables Condicionantes:** Son las caracterÃ­sticas estÃ¡ticas o de largo plazo que hacen que una ladera sea **susceptible** a fallar. Responden al "Por quÃ© aquÃ­".
    * *Ejemplos:* Pendiente del terreno, geologÃ­a (rocas dÃ©biles, fallas), uso del suelo (deforestaciÃ³n), aspecto (orientaciÃ³n de la ladera), geometrÃ­a de la ladera (curvatura).
* **Variables Detonantes (Disparadores):** Son los eventos dinÃ¡micos y de corta duraciÃ³n que **inician** el movimiento. Responden al "Por quÃ© ahora".
    * *Ejemplos:* Lluvias intensas o prolongadas (el detonante mÃ¡s comÃºn en climas tropicales), sismos, actividad humana (cortes en la base, sobrecarga en la corona), erupciones volcÃ¡nicas (sismicidad, sobrecarga de ceniza, lahares).

---
## 5. ClasificaciÃ³n de Cruden y Varnes (1996)
Es la clasificaciÃ³n mÃ¡s utilizada a nivel mundial. Se basa en dos criterios fundamentales:

1.  **Tipo de Material:**
    * **Roca (Rock):** Material intacto y consolidado.
    * **Detritos (Debris):** Material grueso no consolidado (suelos de grano grueso, coluviÃ³n).
    * **Tierra (Earth):** Material fino no consolidado (suelos de grano fino, arcillas, limos).
2.  **Tipo de Movimiento (CinemÃ¡tica):** Se describen en la siguiente secciÃ³n.
    

```{figure} https://i.pinimg.com/1200x/ba/9b/80/ba9b801acae182bf28b6e2da874e6e91.jpg
:name: fig-322
:width: 700

```

| Tipo de Movimiento | Roca (Rock) | Detritos (Debris) | Tierra (Earth) |
| :--- | :--- | :--- | :--- |
| **CaÃ­da (Fall)** | CaÃ­da de Rocas | CaÃ­da de Detritos | CaÃ­da de Tierra |
| **Volcamiento (Topple)** | Volcamiento de Rocas | Volcamiento de Detritos | Volcamiento de Tierra |
| **Deslizamiento (Slide)** | Desliz. de Rocas | Desliz. de Detritos | Desliz. de Tierra |
| **Flujo (Flow)** | (Flujo de Rocas) | Flujo de Detritos | Flujo de Tierra |
| **PropagaciÃ³n (Spread)** | Propag. de Rocas | Propag. de Detritos | Propag. de Tierra |
| **Complejo (Complex)** | \multicolumn{3}{c|}{CombinaciÃ³n de los anteriores (ej. Deslizamiento-Flujo)} |

---
## 6. Tipos de Movimiento (CinemÃ¡tica)

* **CaÃ­das (Falls):** Desprendimiento de material de un talud casi vertical. El movimiento es predominantemente por el aire (caÃ­da libre, rebote, rodamiento). Son extremadamente rÃ¡pidos.
    * *Geoforma resultante:* **Talud** o cono de derrubios.

  
```{figure} https://i.pinimg.com/736x/fb/34/a9/fb34a9b6d733bfc541554674056856c2.jpg
:name: fig-6591
:width: 500

```

* **Volcamiento (Topples):** RotaciÃ³n hacia adelante de una masa de roca o detritos alrededor de un punto de pivote en la base. Ocurre en macizos con discontinuidades (diaclasas, estratos) que buzan fuertemente hacia adentro de la ladera.

  
```{figure} https://i.pinimg.com/736x/b6/ed/50/b6ed50db91d7037d1a961480f844221c.jpg
:name: fig-2016
:width: 300

```

* **Deslizamiento (Slides):** Movimiento de cizalla de una masa coherente a lo largo de una o varias superficies de ruptura definidas.
    * **Deslizamiento Rotacional:** La superficie de falla es cÃ³ncava (forma de cuchara). El movimiento rota alrededor de un eje. TÃ­pico de materiales homogÃ©neos como suelos residuales (saprolito) o arcillas.
    * **Deslizamiento Traslacional:** La superficie de falla es plana o ligeramente ondulada. El movimiento sigue discontinuidades geolÃ³gicas (estratos, fallas, diaclasas).
  
  
```{figure} https://i.pinimg.com/736x/6c/96/91/6c96914cf86e33fa9dd5600b111519a7.jpg
:name: fig-7342
:width: 500

```

* **Flujo (Flows):** Movimiento internamente deformado, similar al de un fluido viscoso. Las partÃ­culas se mueven a diferentes velocidades dentro de la masa.
    * **Flujo de Detritos (Debris Flow):** Un flujo rÃ¡pido y canalizado de una mezcla de agua y detritos. Son comunes en cuencas de alta pendiente (Quebradas) y son altamente destructivos.
    * **Flujo de Tierra (Earth Flow):** TÃ­picos en materiales arcillosos, mÃ¡s lentos, a menudo con una cabecera rotacional y un lÃ³bulo estrecho (forma de reloj de arena).
    * **ReptaciÃ³n (Creep):** El flujo imperceptiblemente lento del suelo. Evidenciado por Ã¡rboles inclinados, postes corridos, etc.
  
  <image src= https://i.pinimg.com/1200x/62/28/3a/62283a9708b7af24606949964a493053.jpg
   width="500">

* **PropagaciÃ³n Lateral (Lateral Spreads):** Movimiento extensional de bloques coherentes (roca o suelo) que se deslizan sobre una capa subyacente que ha perdido su resistencia (usualmente por licuefacciÃ³n sÃ­smica).

---
## 7. Partes de un Movimiento en Masa

La morfologÃ­a de un deslizamiento (especialmente rotacional) tiene partes caracterÃ­sticas:


```{figure} https://i.pinimg.com/1200x/ff/f7/44/fff74482762297853ff366e4cfe54e3a.jpg
:name: fig-2642
:width: 700

```

* **Corona (Crown):** La superficie intacta por encima del escarpe principal.
* **Escarpe Principal (Main Scarp):** La superficie vertical o muy empinada expuesta por el desprendimiento inicial. Es la "cicatriz".
* **Escarpes Secundarios:** PequeÃ±as cicatrices dentro del cuerpo del deslizamiento.
* **Cabeza (Head):** La parte superior de la masa desplazada.
* **Cuerpo (Body):** La masa principal de material que se ha movido. A menudo presenta una morfologÃ­a caÃ³tica o de bloques.
* **Flancos (Flanks):** Los lados del deslizamiento.
* **Superficie de Ruptura (Surface of Rupture):** La superficie sobre la cual se ha movido la masa.
* **Pie (Toe):** El lÃ³bulo o borde mÃ¡s avanzado de la masa deslizada.
* **Pata (Foot):** El Ã¡rea donde el material se ha acumulado y sobresale de la pendiente original.


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

Debido a su topografía abrupta, geología compleja y alta pluviosidad, Colombia es uno de los países más afectados por movimientos en masa en América Latina.

* **Ejemplos Históricos:** Eventos devastadores como el de **Armero** (1985, detonado por erupción pero con gran componente de flujo de detritos) y el de **Mocoa** (2017, flujo de detritos torrencial) marcan la historia del país.
* **Deslizamientos Urbanos:** En ciudades como **Medellín**, **Bucaramanga** y **Manizales**, la expansión urbana sobre laderas empinadas y suelos residuales genera un riesgo constante.
* **Detonantes Comunes:** La lluvia es el principal detonante en Colombia (Fenómeno de La Niña), aunque sismos como el de **Páez (1994)** han generado miles de movimientos en masa simultáneos.

---
## Taller de Autoevaluación

1. **Mecánica de Suelos:** Explique cómo el aumento de la presión de poros ($) durante una temporada de lluvias reduce el Factor de Seguridad de una ladera.
2. **Condicionantes vs Detonantes:** Clasifique las siguientes variables: pendiente del terreno, sismo de magnitud 7.0, deforestación, lluvia de 100 mm en 24h, presencia de una falla geológica.
3. **Cinemática:** ¿Cuál es la diferencia principal entre un deslizamiento rotacional y uno traslacional? ¿En qué tipo de material es más común cada uno?
4. **Identificación de Campo:** Si observa un arco de escarpe fresco en la parte alta de una ladera y un abultamiento o lóbulo en la base, ¿qué partes de un movimiento en masa está identificando?
5. **Riesgo en Colombia:** ¿Por qué se dice que el Valle de Aburrá (Medellín) es una de las zonas con mayor susceptibilidad a movimientos en masa en el país?

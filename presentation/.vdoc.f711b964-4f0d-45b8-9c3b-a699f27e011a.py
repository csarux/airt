# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Datos simulados: precio de vivienda (en miles de euros) vs superficie (m²)
np.random.seed(42)
m_true = 3.2  # precio por m² en miles de euros
b_true = 50.0  # precio base (mínimo, en miles de euros)
x = np.linspace(30, 150, 20)  # superficies entre 30 m² y 150 m²
y = m_true * x + b_true + np.random.normal(scale=20.0, size=len(x))  # precios con ruido

# Rango de valores de pendiente (precio por m²)
m_values = np.linspace(m_true - 2, m_true + 2, 50)
J_values = [np.sum((y - (m * x + b_true))**2) for m in m_values]

# Crear figura con subgráficos
fig = make_subplots(rows=1, cols=2, subplot_titles=["Ajuste lineal: Precio vs Superficie", "Función de coste J(m)"])

# Añadir trazas fijas (siempre visibles)
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Datos reales', marker=dict(color='black')), row=1, col=1)
fig.add_trace(go.Scatter(x=m_values, y=J_values, mode='lines', name='Función de coste J(m)', line=dict(color='black')), row=1, col=2)

# Trazas dinámicas iniciales
m0 = m_values[0]
y_fit0 = m0 * x + b_true
J0 = J_values[0]

ajuste_inicial = go.Scatter(x=x, y=y_fit0, mode='lines', name='Ajuste lineal', line=dict(color='red'))
punto_J = go.Scatter(x=[m0], y=[J0], mode='markers', name='Valor de J', marker=dict(color='red', size=10))

fig.add_trace(ajuste_inicial, row=1, col=1)
fig.add_trace(punto_J, row=1, col=2)

# Frames para animar
frames = []

for i, m in enumerate(m_values):
    y_fit = m * x + b_true
    J = J_values[i]
    frame = go.Frame(
        data=[
            # Puntos originales (subplot 1,1)
            go.Scatter(x=x, y=y, mode='markers', marker=dict(color='black'),
                       xaxis='x1', yaxis='y1'),

            # Línea de ajuste (subplot 1,1)
            go.Scatter(x=x, y=y_fit, mode='lines', line=dict(color='red'),
                       xaxis='x1', yaxis='y1'),

            # Curva de función de coste J(m) (subplot 1,2)
            go.Scatter(x=m_values, y=J_values, mode='lines', line=dict(color='black'),
                       xaxis='x2', yaxis='y2'),

            # Punto rojo J(m) (subplot 1,2)
            go.Scatter(x=[m], y=[J], mode='markers', marker=dict(color='red', size=10),
                       xaxis='x2', yaxis='y2'),
        ],
        name=str(round(m, 2))
    )
    frames.append(frame)

# Slider
steps = [dict(method="animate",
              args=[[str(round(m, 2))],
                    dict(mode="immediate",
                         frame=dict(duration=0, redraw=True),
                         transition=dict(duration=0))],
              label=str(round(m, 2)))
         for m in m_values]

sliders = [dict(
    steps=steps,
    transition=dict(duration=0),
    x=0.1,
    y=0,
    currentvalue=dict(font=dict(size=16), prefix="Precio por m² = ", visible=True, xanchor='center'),
    len=0.8
)]

# Aplicar layout con solo el slider
fig.update_layout(
    sliders=sliders,
    height=500,
    width=1000
)

# Asignar los frames directamente
fig.frames = frames

# Etiquetas de ejes
fig.update_xaxes(title_text="Superficie (m²)", row=1, col=1)
fig.update_yaxes(title_text="Precio (miles de euros)", row=1, col=1)
fig.update_xaxes(title_text="Precio por m² (miles de euros)", row=1, col=2)
fig.update_yaxes(title_text="J(m)", row=1, col=2)

fig.show()

```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

np.random.seed(123)

# Simulación 1: Precio vs Superficie (alta correlación)
m1_true = 3.0  # mil €/m²
b1_true = 100.0
x1 = np.linspace(50, 150, 20)  # m²
y1 = m1_true * x1 + b1_true + np.random.normal(scale=15.0, size=len(x1))

# Simulación 2: Precio vs Altura (menor correlación)
m2_true = 5.0  # mil €/planta
b2_true = 200.0
x2 = np.linspace(1, 20, 20)  # plantas
y2 = m2_true * x2 + b2_true + np.random.normal(scale=40.0, size=len(x2))

# Ajustes
m1_fit, b1_fit = np.polyfit(x1, y1, 1)
y1_fit = m1_fit * x1 + b1_fit

m2_fit, b2_fit = np.polyfit(x2, y2, 1)
y2_fit = m2_fit * x2 + b2_fit

# Funciones de coste con rango de 5 unidades
m_values1 = np.linspace(m1_fit - 2.5, m1_fit + 2.5, 100)
J_values1 = [np.sum((y1 - (m * x1 + b1_true))**2) for m in m_values1]

m_values2 = np.linspace(m2_fit - 2.5, m2_fit + 2.5, 100)
J_values2 = [np.sum((y2 - (m * x2 + b2_true))**2) for m in m_values2]

# Crear figura con 4 subgráficos
fig = make_subplots(rows=2, cols=2, subplot_titles=[
    "Precio vs Superficie",
    "Función de coste J(m): Superficie",
    "Precio vs Altura",
    "Función de coste J(m): Altura"
])

# Arriba izquierda: Ajuste superficie
fig.add_trace(go.Scatter(x=x1, y=y1, mode='markers', name='Datos superficie', marker=dict(color='black')), row=1, col=1)
fig.add_trace(go.Scatter(x=x1, y=y1_fit, mode='lines', name='Ajuste superficie', line=dict(color='red')), row=1, col=1)

# Arriba derecha: Coste superficie
fig.add_trace(go.Scatter(x=m_values1, y=J_values1, mode='lines', name='J(m): superficie', line=dict(color='black')), row=1, col=2)

# Abajo izquierda: Ajuste altura
fig.add_trace(go.Scatter(x=x2, y=y2, mode='markers', name='Datos altura', marker=dict(color='black')), row=2, col=1)
fig.add_trace(go.Scatter(x=x2, y=y2_fit, mode='lines', name='Ajuste altura', line=dict(color='red')), row=2, col=1)

# Abajo derecha: Coste altura
fig.add_trace(go.Scatter(x=m_values2, y=J_values2, mode='lines', name='J(m): altura', line=dict(color='black')), row=2, col=2)

# Etiquetas
fig.update_xaxes(title_text="Superficie (m²)", row=1, col=1)
fig.update_yaxes(title_text="Precio (miles de €)", row=1, col=1)
fig.update_xaxes(title_text="Pendiente m (mil €/m²)", row=1, col=2)
fig.update_yaxes(title_text="J(m)", row=1, col=2)

fig.update_xaxes(title_text="Altura (plantas)", row=2, col=1)
fig.update_yaxes(title_text="Precio (miles de €)", row=2, col=1)
fig.update_xaxes(title_text="Pendiente m (mil €/planta)", row=2, col=2)
fig.update_yaxes(title_text="J(m)", row=2, col=2)

fig.update_yaxes(range=[0, 1.e6], row=1, col=2)
fig.update_yaxes(range=[0, 1.e6], row=2, col=2)

fig.update_layout(
    height=650,
    width=800,
    showlegend=False
)

fig.show()


#
#
#
#
#
#
#

import numpy as np
import plotly.graph_objects as go

# Datos originales: precio vs superficie
np.random.seed(123)
m_true = 3.0  # mil €/m²
b_true = 100.0
x = np.linspace(50, 150, 20)
y = m_true * x + b_true + np.random.normal(scale=15.0, size=len(x))

# Ajuste polinómico de grado alto (overfitting)
degree = 15
coefs = np.polyfit(x, y, degree)
poly = np.poly1d(coefs)

# Evaluar el modelo en una malla más fina
x_fine = np.linspace(40, 160, 500)
y_poly = poly(x_fine)

# Ajuste lineal como comparación
m_fit, b_fit = np.polyfit(x, y, 1)
y_line = m_fit * x_fine + b_fit

# Crear figura
fig = go.Figure()

# Datos
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Datos', marker=dict(color='black')))

# Ajuste lineal
fig.add_trace(go.Scatter(x=x_fine, y=y_line, mode='lines', name='Ajuste lineal', line=dict(color='green')))

# Ajuste polinómico (overfitting)
fig.add_trace(go.Scatter(x=x_fine, y=y_poly, mode='lines', name='Modelo sobreajustado', line=dict(color='red', dash='dot')))

# Layout
fig.update_layout(
    xaxis_title="Superficie (m²)",
    yaxis_title="Precio (miles de €)",
    width=800,
    height=500
)

fig.show()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

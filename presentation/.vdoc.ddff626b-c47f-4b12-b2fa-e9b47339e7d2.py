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
    title="Ajuste lineal interactivo del precio de la vivienda en función de la superficie",
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

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

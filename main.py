import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("Hotel Reservations.csv")

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div(
        className='Container',
        children=[
            html.Div(className='Sidebar',
            children=[
                html.H1("Hotel Reservations", className='side_bar_title'),
                html.Label("Año de análisis", className='side_bar_dropdown_label'),
                html.Div(
                    dcc.Dropdown(df.arrival_year.unique(),'2022',id='year_dropdown')
                ),
                html.Label("Tipo de comida",className='side_bar_dropdown_label'),
                dcc.Dropdown(df.type_of_meal_plan.unique(),id='meal_dropdown')
            ]),

            html.Div(className='MainSection',
            children=[
                html.Div(
                    className="Container_1"
                ),
                html.Div(
                    className="Container_1"
                ),
                html.Div(
                    className="Container_1"
                ),
                html.Div(
                    className="Container_1"
                ),
                html.Div(
                    className="Container_2"
                ),
                html.Div(
                    className="Container_2"
                ),
                html.Div(
                    className="Container_3"
                )
            ])
    ])

])

if __name__ == ('__main__'):
    app.run_server(debug=True)
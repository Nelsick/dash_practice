import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from process_data import *

df = pd.read_csv("Hotel Reservations.csv")
cancelations = per_canceled_booking(df)
booking_year = booking_per_year_graf(df)

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
                    dcc.Dropdown(df.arrival_year.unique(),
                    multi=True,
                    value=[],
                    id='year_dropdown')
                ),
                html.Label("Tipo de comida",className='side_bar_dropdown_label'),
                dcc.Dropdown(df.type_of_meal_plan.unique(),id='meal_dropdown'),
                html.Label("Segmento",className='side_bar_dropdown_label'),
                dcc.Dropdown(df.market_segment_type.unique(), id='segment_type')
            ]),

            html.Div(className='MainSection',
            children=[
                html.Div(
                    className="Container_1",
                    children = [
                        html.P(cancelations, className=("under" if cancelations > 25 else "above")),
                        html.H3("% de cancelaciones")
                    ]
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
                    className="Container_3",
                    children=[
                        html.P("Reservas por año"),
                        dcc.Graph(
                            id = 'booking_total_line', 
                            config={'displayModeBar':False},
                            className="Container_3_graph" 
                        ),
                ])
            ])
    ])

])

@app.callback(
    Output('booking_total_line', component_property='figure'),
    [Input('year_dropdown',component_property='value')])

def update_graph(value):
    data = booking_year[booking_year['arrival_year'].isin(value)]
    fig = px.line(
        data_frame=data,
        x='arrival_month',
        y='booking_status',
        color='arrival_year',
        markers=True
    )
    return fig
        

if __name__ == ('__main__'):
    app.run_server(debug=True)

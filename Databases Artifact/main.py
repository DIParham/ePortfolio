# Author: Danielle Parham
# Class: CS 499
# Category: Databases
# Title: DAT 220 Dash Board

# imports
import dash
import dash_table
import plotly.express as px
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
from pymongo import MongoClient

# connect to local server
client = MongoClient("mongodb://127.0.0.1:27017/")

# create database
mydb = client["DAT220"]

# create collection
collection = mydb.data

# initializes dash
app = dash.Dash(__name__, suppress_callback_exceptions=True,)

# app layout
app.layout = html.Div([
    html.H1("CS 499: Database Project"),
    html.H2("DAT 220 Interactive Data"),
    html.H3("Danielle Parham"),
    html.Br(),
    html.Div(id='mongo', children=[]),

    dcc.Interval(id='internalDB', interval=864000*7, n_intervals=0),

    # buttons that update and add to mongo db
    html.Button("Save to Database", id='save'),
    html.Button("Add Row", id="add"),

    html.Div(id='graph', children=[]),
    html.Div(id='placeholder')
])

# displays data from mongo db collection
@app.callback(Output('mongo', 'children'),
              [Input('internalDB', 'n_intervals')])
def datatable(n_intervals):
    # changes the collection data to pandas data frame
    df = pd.DataFrame(list(collection.find()))

    # removes the _id column from the data
    df = df.iloc[:, 1:]

    return [
        dash_table.DataTable(
            id='table',
            columns=[
                {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
                for i in df.columns
            ],
            data=df.to_dict('records'),
            editable=True,                           # allows users to write to MongoDB
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="multi",
            row_selectable="multi",
            row_deletable="none",
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current=0,
            page_size=10,

            # provides adequate space for cells
            style_cell={
                'minWidth': 100, 'maxWidth': 100, 'width': 100
            },

            # shifts data to two lines when necessary
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto'
            },
        ),
        # creates drop down function for four columns
        # Restaurant, Webstore_Spend,THIRD_SPEND, and Age
        # filters graphs based on drop down option
        html.Div([
            html.P("Store Data:"),
            dcc.Dropdown(
                id='store',
                options=[
                    {'label': 'Restaurant', 'value': 'Restaurant'},
                    {'label': 'Webstore', 'value': 'Webstore_Spend'},
                    {'label': 'Third Party', 'value': 'THIRD_SPEND'},
                    {'label': 'Age', 'value': 'Age'}

                ],
                # default value is Restaurant
                value='Restaurant',
                multi=False,
                clearable=False,
                searchable=True,
                placeholder="Select Filter Option..",
            ),
            # creates drop down function for two columns
            # Age and State
            # filters graph based on drop down option
            html.P("Customer Data: "),
            dcc.Dropdown(
                id='customer',
                options=[
                    {'label': 'State', 'value': 'state'},
                    {'label': 'Age', 'value': 'Age'},
                ],
                # default value is state
                value='state',
                multi=False,
                clearable=False,
                searchable=True,
                placeholder="Select Filter Option..",
            )
        ]),
        dcc.Graph(id='this-graph'),
    ]
# callback to add to data table
@app.callback(
    Output('table', 'data'),
    [Input('add', 'n_clicks')],
    [State('table', 'data'),
     State('table', 'columns')],
)
def addRow(n_clicks, rows, columns):
    # if add button is selected, it would append the new data to the database
    # ***NOTE: new rows appear on the last page ***
    if n_clicks is not None:
        rows.append({i['id']: '' for i in columns})
    return rows

# callback to save data to mongo db
@app.callback(
    Output('placeholder', 'children'),
    Input("save", "n_clicks"),
    State("table", "data"),
    prevent_initial_call=True
)
# function to save data
def saveData(n_clicks, data):
    dff = pd.DataFrame(data)
    collection.delete_many({})
    collection.insert_many(dff.to_dict('records'))
    return ""
# callbacks
@app.callback(
    # output values
    # output changes based on input
    Output(component_id='this-graph', component_property='figure'),
    # input values
    # output is dependent on input selection
    [Input(component_id='store', component_property='value'),
     Input(component_id='customer', component_property='value'), ]
)
def graphAction(store, customer):
    # make copy of data frame
    df = pd.DataFrame(list(collection.find()))
    df = df.iloc[:, 1:]
    dff = df
    # insert graph
    # scatter graph used to show data comparisons
    fig = px.scatter(dff, x=customer, y=store)
    return fig


if __name__ == '__main__':
    app.run_server()
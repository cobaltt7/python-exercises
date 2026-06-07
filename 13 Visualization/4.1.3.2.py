from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

app = Dash()

app.layout = [
    html.Div(children="My First App with Data"),
    dag.AgGrid(
        rowData=df.to_dict("records"), columnDefs=[{"field": i} for i in df.columns]
    ),
]

if __name__ == "__main__":
    app.run(debug=True)

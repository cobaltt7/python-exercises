from dash import Dash, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
import dash_design_kit as ddk

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

app = Dash()

app.layout = ddk.App([
    ddk.Header(ddk.Title("My First App with Data, Graph, and Controls")),
    dcc.RadioItems(
        options=["pop", "lifeExp", "gdpPercap"],
        value="lifeExp",
        inline=True,
        id="my-ddk-radio-items-final",
    ),
    ddk.Row([
        ddk.Card(
            [
                dag.AgGrid(
                    rowData=df.to_dict("records"),
                    columnDefs=[{"field": i} for i in df.columns],
                )
            ],
            width=50,
        ),
        ddk.Card([ddk.Graph(figure={}, id="graph-placeholder-ddk-final")], width=50),
    ]),
])


@callback(
    Output(component_id="graph-placeholder-ddk-final", component_property="figure"),
    Input(component_id="my-ddk-radio-items-final", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


if __name__ == "__main__":
    app.run(debug=True)

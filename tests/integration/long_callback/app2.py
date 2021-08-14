import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import time

from utils import get_long_callback_manager

long_callback_manager = get_long_callback_manager()
handle = long_callback_manager.handle

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.Button(id="button-1", children="Click Here", n_clicks=0),
        html.Div(id="status", children="Finished"),
        html.Div(id="result", children="Not clicked"),
    ]
)


@app.long_callback(
    long_callback_manager,
    Output("result", "children"),
    [Input("button-1", "n_clicks")],
    running=[(Output("status", "children"), "Running", "Finished")],
    interval=500,
)
def update_output(n_clicks):
    time.sleep(2)
    return f"Clicked {n_clicks} time(s)"


if __name__ == "__main__":
    app.run_server(debug=True)

import argparse
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash
import dash_core_components as dcc
import dash_html_components as html

import grpc
import info_pb2
import info_pb2_grpc
from info_resources import Host
from info_resources import print_sys_info
import time

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


hosts = [
            # add hosts here
        ]
 
def host_view(host):
    sys_info = host.GetSysInfo()
    cpu_count = sys_info.cpu_info.cpu_count
    load_average = sys_info.cpu_info.load_average
    data = {
            'host': host.name,
            'cpu count': cpu_count,
            'load average': load_average,
            'load': f'{(load_average[-1]/cpu_count *100):.1f}',
            }
    return html.Div([
        html.Div([
            html.Plaintext(f'{key}: {value}')
            for key, value in data.items()
            ]
            )
        ])

    

app.layout = html.Div(
    [

        html.Div(id="table"),
	dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ]
)

@app.callback(
    Output("table", "children"),
    [Input("interval-component", "n_intervals")],
)
def update_table(n):
    return html.Div([
        host_view(host) for host in hosts
        ])

def main(args):
    app.run_server(debug=True, port=args.port)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse arguments")

    parser.add_argument("--port", type = int, default="8050", help="port")

    args = parser.parse_args()
    main(args)


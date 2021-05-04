#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:13:12 2020

@author: hendrasetiawan
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_daq as daq
import dash_table
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']




app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Div(
        children=[
                    html.Div([
                     html.Div([html.H1('Dashboad Belanja Pemerintah Provinsi Tahun Anggaran 2018/2019', style={'textAlign': 'center','background': '#f9f9f9','box-shadow': '0 0 1px rgba(0,0,0,.2), 0 2px 4px rgba(0,0,0,.1)','border-radius': '5px','margin-bottom': '20px','text-shadow': '1px 1px 1px rgba(0,0,0,.1)'})]),
                             
                        
                    html.H2('Bidang Pendidikan dan Ekonomi', style={'textAlign': 'center','borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'}),
                    ]),
                    
                    html.Div([
                    html.Div([
                        html.H5("Pilih Tahun Anggaran"),
                                 dcc.Dropdown(options=[{'label': '2018', 'value':'2018'},
                                                    {'label': '2019', 'value':'2019'},
                                    ],
                        id='tahun-multidropdown',
                           multi=True,
                           value=['2018','2019']),
                        html.H5("Pilih Provinsi"),   
                            dcc.Dropdown(options=[{'label': 'Provinsi Papua', 'value':16},
                                                    {'label': 'Provinsi Kalimantan Barat', 'value':8},
                                                    {'label': 'Provinsi Nusa Tenggara Barat', 'value':15},
                                                    {'label': 'Provinsi Gorontalo', 'value':4},
                                                    {'label': 'Provinsi Maluku', 'value':14},
                                                    {'label': 'Provinsi Lampung', 'value':13},
                                                    {'label': 'Provinsi Sumatera Selatan', 'value':22},
                                                    {'label': 'Provinsi Kalimantan Selatan', 'value':24},
                                                    {'label': 'Provinsi Kalimantan Tengah', 'value':9},
                                                    {'label': 'Provinsi Kalimantan Utara', 'value':11},
                                                    {'label': 'Provinsi Sulawesi Tenggara', 'value':20},
                                                    {'label': 'Provinsi Bangka Belitung', 'value':2},
                                                    {'label': 'Provinsi Sulawesi Selatan', 'value':19},
                                                    {'label': 'Provinsi Jawa Tengah', 'value':6},
                                                    {'label': 'Provinsi Aceh', 'value':1},
                                                    {'label': 'Provinsi Sulawesi Barat', 'value':18},
                                                    {'label': 'Provinsi Banten', 'value':3},
                                                    {'label': 'Provinsi Sulawesi Utara', 'value':21},
                                                    {'label': 'Provinsi Riau', 'value':17},
                                                    {'label': 'Provinsi Kalimantan Timur', 'value':10},
                                                    {'label': 'Provinsi Jambi', 'value':5},
                                                    {'label': 'Provinsi Jawa Timur', 'value':7},
                                                    {'label': 'Provinsi DKI Jakarta', 'value':23},
                                ],
                        id='kabupaten-multidropdown',
                           multi=True,
                           
                           value=[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24]),
                         html.H5("Total Belanja Pendidikan Provinsi", style={'textAlign': 'center'}),
                            dcc.Graph(id='eventhistogram')],
                        style={'width': '70%', 'display': 'inline-block','background': '#f9f9f9','box-shadow': '0 0 1px rgba(0,0,0,.2), 0 2px 4px rgba(0,0,0,.1)','border-radius': '5px','margin-bottom': '20px','text-shadow': '1px 1px 1px rgba(0,0,0,.1)'}),
                      html.Div([
                          html.P("Tabel Bulanan Total Kejadian Periode 2017 - 2020"),
                          dcc.Dropdown(options=[{'label': 'Seluruh Kalimantan Barat', 'value':'all'},
                                                {'label': 'BENGKAYANG', 'value':'BENGKAYANG'},
                                                    {'label': 'KAPUAS HULU', 'value':'KAPUAS HULU'},
                                                    {'label': 'KAYONG UTARA', 'value':'KAYONG UTARA'},
                                                    {'label': 'KETAPANG', 'value':'KETAPANG'},
                                                    {'label': 'KOTA SINGKAWANG', 'value':'KOTA SINGKAWANG'},
                                                    {'label': 'KUBU RAYA', 'value':'KUBU RAYA'},
                                                    {'label': 'LANDAK', 'value':'LANDAK'},
                                                    {'label': 'MELAWI', 'value':'MELAWI'},
                                                    {'label': 'MEMPAWAH', 'value':'MEMPAWAH'},
                                                    {'label': 'SAMBAS', 'value':'SAMBAS'},
                                                    {'label': 'SANGGAU', 'value':'SANGGAU'},
                                                    {'label': 'SEKADAU', 'value':'SEKADAU'},
                                                    {'label': 'SINTANG', 'value':'SINTANG'},],
                           id='3tahunanlokasi',
                           value='all'),
                         # dash_table.DataTable(
                          #    id='memory-table',
                           #   columns=[{'name': i, 'id': i} for i in readytgntahun.columns],
                            #  data=readytgntahun.to_dict('records')
                             # ),
                          
                          
                          ],style={'width': '28%', 'display': 'inline-block','float': 'right','background': '#f9f9f9','box-shadow': '0 0 1px rgba(0,0,0,.2), 0 2px 4px rgba(0,0,0,.1)','border-radius': '5px','margin-bottom': '20px','text-shadow': '1px 1px 1px rgba(0,0,0,.1)'})
            
                  ],
              style={'width': '100%', 'display': 'inline-block', 'float': 'right'}),
  
           
           
                        
                      
                        
                    
    ])
  ],style={'background-color:': 'center'})

@app.callback(
    dash.dependencies.Output('eventhistogram','figure'),
    [dash.dependencies.Input('tahun-multidropdown','value'),
     dash.dependencies.Input('kabupaten-multidropdown','value')]
    )
       
# Update the histogram

def update_hist(name,kabupaten):
    dfbnbp = pd.read_csv('dashboard1pendidikan.csv')
    dfbnbp =  dfbnbp[ dfbnbp['Kode Provinsi'].isin(kabupaten)]
    #create selection for the dataset
    #untuk histogram feed to the graph
    totalbelanja=dfbnbp.groupby(['NamaProvinsi', 'Jenis Belanja','Tahun']).sum()[["Total Belanja"]].reset_index()
    totalbelanja['Tahun'] = totalbelanja.Tahun.astype(str)
    totalbelanja = totalbelanja[totalbelanja['Tahun'].isin(name)]
    newfig  = px.bar(totalbelanja,x='NamaProvinsi',y='Total Belanja',color="Tahun")
    newfig.update_layout(barmode='group')
    return newfig 

if __name__ == '__main__':
    app.run_server(debug=True)

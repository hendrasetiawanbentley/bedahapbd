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
#import dependencies
import dash_auth
from users import USERNAME_PASSWORD_PAIRS




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']




app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    USERNAME_PASSWORD_PAIRS
)
server = app.server
app.layout = html.Div([
    html.Div(
        children=[
                   html.Div([
                     html.Div([html.H1('Dashboad Belanja Pemerintah Provinsi Tahun Anggaran 2018/2019', style={'textAlign': 'center','background': '#f9f9f9','box-shadow': '0 0 1px rgba(0,0,0,.2), 0 2px 4px rgba(0,0,0,.1)','border-radius': '5px','margin-bottom': '20px','text-shadow': '1px 1px 1px rgba(0,0,0,.1)'})]),
                             
                        
                    html.H2('Bidang Pendidikan dan Ekonomi', style={'textAlign': 'center','borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'}),
                    html.H2('Bidang Pendidikan', style={'textAlign': 'center','borderBottom': 'thin lightgrey solid',
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
                        style={'width': '50%', 'display': 'inline-block','background': '#f9f9f9','box-shadow': '0 0 1px rgba(0,0,0,.2), 0 2px 4px rgba(0,0,0,.1)','border-radius': '5px','margin-bottom': '20px','text-shadow': '1px 1px 1px rgba(0,0,0,.1)'}),
                      html.Div([
                          html.H5("Pilih Tahun Pengukuran"),
                          dcc.Dropdown(options=[{'label': '2018', 'value':'2018'},
                                                    {'label': '2019', 'value':'2019'},
                                    ],
                        id='ipm-tahun-multidropdown',
                           multi=True,
                           value=['2018','2019','2020']),
                          html.H5("Pilih Provinsi"), 
                          dcc.Dropdown(options=[{'label': 'Seluruh Provinsi', 'value':'all'},
                                                {'label': 'ACEH', 'value':1},
                                                    {'label': 'SUMATERA UTARA', 'value':2},
                                                    {'label': 'SUMATERA BARAT', 'value':3},
                                                    {'label': 'RIAU', 'value':4},
                                                    {'label': 'JAMBI', 'value':5},
                                                    {'label': 'SUMATERA SELATAN', 'value':6},
                                                    {'label': 'BENGKULU', 'value':7},
                                                    {'label': 'LAMPUNG', 'value':8},
                                                    {'label': 'KEP. BANGKA BELITUNG', 'value':9},
                                                    {'label': 'KEP. RIAU', 'value':10},
                                                    {'label': 'DKI JAKARTA', 'value':11},
                                                    {'label': 'JAWA BARAT', 'value':12},
                                                    {'label': 'JAWA TENGAH', 'value':13},
                                                    {'label': 'DI YOGYAKARTA', 'value':14},
                                                    {'label': 'JAWA TIMUR', 'value':15},
                                                    {'label': 'BANTEN', 'value':16},
                                                    {'label': 'BALI', 'value':17},
                                                    {'label': 'NUSA TENGGARA BARAT', 'value':18},
                                                    {'label': 'NUSA TENGGARA TIMUR', 'value':19},
                                                    {'label': 'KALIMANTAN BARAT', 'value':20},
                                                    {'label': 'KALIMANTAN TENGAH', 'value':21},
                                                    {'label': 'KALIMANTAN SELATAN', 'value':22},
                                                    {'label': 'KALIMANTAN TIMUR', 'value':23},
                                                    {'label': 'KALIMANTAN UTARA', 'value':24},
                                                    {'label': 'SULAWESI UTARA', 'value':24},
                                                    {'label': 'SULAWESI TENGAH', 'value':26},
                                                    {'label': 'SULAWESI SELATAN', 'value':27},
                                                    {'label': 'SULAWESI TENGGARA', 'value':28},
                                                    {'label': 'GORONTALO', 'value':29},
                                                    {'label': 'SULAWESI BARAT', 'value':30},
                                                    {'label': 'MALUKU', 'value':31},
                                                    ],
                           id='ipm-kabupaten-multidropdown',
                           multi=True,
                           value=[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]),
                         html.H5("Indeks IPM Provinsi", style={'textAlign': 'center'}),
                            dcc.Graph(id='ipmbar')],
                          style={ 'width': '50%','display': 'inline-block','float': 'right','background': '#f9f9f9','box-shadow': '0 0 1px rgba(0,0,0,.2), 0 2px 4px rgba(0,0,0,.1)','border-radius': '5px','margin-bottom': '20px','text-shadow': '1px 1px 1px rgba(0,0,0,.1)'}),
            html.Div([
                html.Div([
                    html.H5("Persentase Belanja Pendidikan Berdasarkan Jenis Belanja Indonesia Tahun"),
                     dcc.Dropdown(options=[
                                                {'label': '2018', 'value':2018},
                                                {'label': '2019', 'value':2019},
                                                    ],
                           id='tahun-jenisbelanja',
                           value=2018),
                    dcc.Graph(id='imgbelpenind'),
                    html.P("Terjadi perbedaan fokus belanja pada tahun 2018 dan 2019", style={'textAlign': 'center'}),
                    
                    ],style={'width': '50%', 'display': 'inline-block'}),
                html.Div([
                    html.H5("Persentase Belanja Pendidikan Berdasarkan Jenis Belanja Per Provinsi Tahun"),
                    dcc.Dropdown(options=[
                                                {'label': '2018', 'value':2018},
                                                {'label': '2019', 'value':2019},
                                                    ],
                           id='tahun-jenisbelanjaprov',
                           value=2018),
                    
                   dcc.Dropdown(options=[{'label': 'Provinsi Papua', 'value':'Provinsi Papua'},
                                         {'label': 'Provinsi Kalimantan Barat', 'value':'Provinsi Kalimantan Barat'},
                                         {'label': 'Provinsi Nusa Tenggara Barat', 'value':'Provinsi Nusa Tenggara Barat'},
                                         {'label': 'Provinsi Gorontalo', 'value':'Provinsi Gorontalo'},
                                         {'label': 'Provinsi Maluku', 'value':'Provinsi Maluku'},
                                         {'label': 'Provinsi Lampung', 'value':'Provinsi Lampung'},
                                         {'label': 'Provinsi Sumatera Selatan', 'value':'Provinsi Sumatera Selatan'},
                                         {'label': 'Provinsi Kalimantan Selatan', 'value':'Provinsi Kalimantan Selatan'},
                                         {'label': 'Provinsi Kalimantan Tengah', 'value':'Provinsi Kalimantan Tengah'},
                                         {'label': 'Provinsi Kalimantan Utara', 'value':'Provinsi Kalimantan Utara'},
                                         {'label': 'Provinsi Sulawesi Tenggara', 'value':'Provinsi Sulawesi Tenggara'},
                                         {'label': 'Provinsi Bangka Belitung', 'value':'Provinsi Bangka Belitung'},
                                         {'label': 'Provinsi Sulawesi Selatan', 'value':'Provinsi Sulawesi Selatan'},
                                         {'label': 'Provinsi Jawa Tengah', 'value':'Provinsi Jawa Tengah'},
                                         {'label': 'Provinsi Aceh', 'value':'Provinsi Aceh'},
                                         {'label': 'Provinsi Sulawesi Barat', 'value':'Provinsi Sulawesi Barat'},
                                         {'label': 'Provinsi Banten', 'value':'Provinsi Banten'},
                                         {'label': 'Provinsi Sulawesi Utara', 'value':'Provinsi Sulawesi Utara'},
                                         {'label': 'Provinsi Riau', 'value':'Provinsi Riau'},
                                         {'label': 'Provinsi Kalimantan Timur', 'value':'Provinsi Kalimantan Timur'},
                                         {'label': 'Provinsi Jambi', 'value':'Provinsi Jambi'},
                                         {'label': 'Provinsi Jawa Timur', 'value':'Provinsi Jawa Timur'},
                                         {'label': 'Provinsi DKI Jakarta', 'value':'Provinsi DKI Jakarta'},
           
                     ],
                        id='kabupaten-multidropdown-pend',
                           value='Provinsi DKI Jakarta'),
                    dcc.Graph(id='graptotalperbandingan'),
                    html.P("Terdapat Perbedaan Fokus Belanja Provinsi", style={'textAlign': 'center'})
                    
                    
                    
                    ],style={'width': '50%', 'display': 'inline-block'}),
                ],style={'width': '100%', 'display': 'inline-block', 'float': 'right','background': '#f9f9f9','box-shadow': '0 0 1px rgba(0,0,0,.2), 0 2px 4px rgba(0,0,0,.1)','border-radius': '5px','margin-bottom': '20px','text-shadow': '1px 1px 1px rgba(0,0,0,.1)'}),
            html.H2('Bidang Ekonomi', style={'textAlign': 'center','borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'}), 
            
            html.Div([
                        html.H5("Pilih Tahun Anggaran"),
                                 dcc.Dropdown(options=[{'label': '2018', 'value':'2018'},
                                                    {'label': '2019', 'value':'2019'},
                                    ],
                        id='tahun-multidropdowneko',
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
                        id='kabupaten-multidropdowneko',
                           multi=True,
                           
                           value=[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24]),
                         html.H5("Total Belanja Ekonomi Provinsi", style={'textAlign': 'center'}),
                            dcc.Graph(id='eventhistogrameko')],
                        style={'width': '50%', 'display': 'inline-block','background': '#f9f9f9','box-shadow': '0 0 1px rgba(0,0,0,.2), 0 2px 4px rgba(0,0,0,.1)','border-radius': '5px','margin-bottom': '20px','text-shadow': '1px 1px 1px rgba(0,0,0,.1)'}),
                      html.Div([
                          html.H5("Pilih Tahun Pengukuran"),
                          dcc.Dropdown(options=[{'label': '2018', 'value':'2018'},
                                                    {'label': '2019', 'value':'2019'},
                                    ],
                        id='ipm-tahun-multidropdowneko',
                           multi=True,
                           value=['2018','2019','2020']),
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
                           id='ipm-kabupaten-multidropdowneko',
                           multi=True,
                           value=[1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17.,18,19,20,21,22,23,24 
]),
                         html.H5("GDP Regional Provinsi 2018", style={'textAlign': 'center'}),
                            dcc.Graph(id='ipmbareko')],
                          style={ 'width': '50%','display': 'inline-block','float': 'right','background': '#f9f9f9','box-shadow': '0 0 1px rgba(0,0,0,.2), 0 2px 4px rgba(0,0,0,.1)','border-radius': '5px','margin-bottom': '20px','text-shadow': '1px 1px 1px rgba(0,0,0,.1)'}),
            
            
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
    newfig.update_xaxes(categoryorder='total descending')
    return newfig 

@app.callback(
    dash.dependencies.Output('ipmbar','figure'),
    [dash.dependencies.Input('ipm-tahun-multidropdown','value'),
     dash.dependencies.Input('ipm-kabupaten-multidropdown','value')]
    )
       
# Update the histogram

def update_hist(name,kabupaten):
    dfbnbp = pd.read_csv('ipm.csv')
    dfbnbp =  dfbnbp[ dfbnbp['Kode'].isin(kabupaten)]
    #create selection for the dataset
    #untuk histogram feed to the graph
    dfbnbp['Tahun'] = dfbnbp.Tahun.astype(str)
    dfbnbp = dfbnbp[dfbnbp['Tahun'].isin(name)]
    ipmfig  = px.bar(dfbnbp,x='Provinsi',y='IPM',color="Tahun")
    ipmfig.update_layout(barmode='group')
    ipmfig.update_xaxes(categoryorder='total descending')
    return ipmfig 

@app.callback(
    dash.dependencies.Output('imgbelpenind','figure'),
    [dash.dependencies.Input('tahun-jenisbelanja','value')
     ]
    )       
# Update the histogram
def treemaps(tahun):
   bedahdatajenispenggunaan = pd.read_csv('bedahdataprovdashboard.csv')
   bedahdatajenispenggunaan=bedahdatajenispenggunaan.loc[bedahdatajenispenggunaan["Tahun"]==2018,:]
   bedahdatajenispenggunaan=bedahdatajenispenggunaan.loc[bedahdatajenispenggunaan["Bidang"]=="Pendidikan",:]
   #untuk lomba apbd
   bedahdatajenispenggunaan = pd.crosstab(bedahdatajenispenggunaan['Jenis Belanja'], columns="Nominal",values=bedahdatajenispenggunaan.Nominal, aggfunc='sum')
   bedahdatajenispenggunaan['percent'] = round(100*bedahdatajenispenggunaan.Nominal / sum(bedahdatajenispenggunaan.Nominal), 2)
   bedahdatajenispenggunaan['Jenis Belanja']=bedahdatajenispenggunaan.index
   if tahun==2019:
       bedahdatajenispenggunaan = pd.read_csv('bedahdataprovdashboard.csv')
       bedahdatajenispenggunaan=bedahdatajenispenggunaan.loc[bedahdatajenispenggunaan["Tahun"]==2019,:]
       bedahdatajenispenggunaan=bedahdatajenispenggunaan.loc[bedahdatajenispenggunaan["Bidang"]=="Pendidikan",:]
       #untuk lomba apbd
       bedahdatajenispenggunaan = pd.crosstab(bedahdatajenispenggunaan['Jenis Belanja'], columns="Nominal",values=bedahdatajenispenggunaan.Nominal, aggfunc='sum')
       bedahdatajenispenggunaan['percent'] = round(100*bedahdatajenispenggunaan.Nominal / sum(bedahdatajenispenggunaan.Nominal), 2)
       bedahdatajenispenggunaan['Jenis Belanja']=bedahdatajenispenggunaan.index
        # Return all the rows on initial load/no country selected.   
   fig = px.treemap(bedahdatajenispenggunaan, 
                 path=['Jenis Belanja','percent'], 
                 values='Nominal',
                )
   return fig 

@app.callback(
    dash.dependencies.Output('graptotalperbandingan','figure'),
    [dash.dependencies.Input('tahun-jenisbelanjaprov','value'),
     dash.dependencies.Input('kabupaten-multidropdown-pend','value')
     ]
    )       
# Update the histogram
def treemaps(tahun,prov):
   bedahdatajenispenggunaan = pd.read_csv('bedahdataprovdashboard.csv')
   bedahdatajenispenggunaan=bedahdatajenispenggunaan.loc[bedahdatajenispenggunaan["Tahun"]==tahun,:]
   bedahdatajenispenggunaan=bedahdatajenispenggunaan.loc[bedahdatajenispenggunaan["Bidang"]=="Pendidikan",:]
   bedahdatajenispenggunaan=bedahdatajenispenggunaan.loc[bedahdatajenispenggunaan["Provinsi"]==prov,:]
   #untuk lomba apbd
   bedahdatajenispenggunaan = pd.crosstab(bedahdatajenispenggunaan['Jenis Belanja'], columns="Nominal",values=bedahdatajenispenggunaan.Nominal, aggfunc='sum')
   bedahdatajenispenggunaan['percent'] = round(100*bedahdatajenispenggunaan.Nominal / sum(bedahdatajenispenggunaan.Nominal), 2)
   bedahdatajenispenggunaan['Jenis Belanja']=bedahdatajenispenggunaan.index  
   fig = px.treemap(bedahdatajenispenggunaan, 
                 path=['Jenis Belanja','percent'], 
                 values='Nominal',
                )
   return fig 

@app.callback(
    dash.dependencies.Output('eventhistogrameko','figure'),
    [dash.dependencies.Input('tahun-multidropdowneko','value'),
     dash.dependencies.Input('kabupaten-multidropdowneko','value')]
    )
       
# Update the histogram

def update_hist(name,kabupaten):
    dfbnbp = pd.read_csv('dashboard2Eko.csv')
    dfbnbp =  dfbnbp[ dfbnbp['Kode Provinsi'].isin(kabupaten)]
    #create selection for the dataset
    #untuk histogram feed to the graph
    totalbelanja=dfbnbp.groupby(['Nama Provinsi', 'Jenis Belanja','Tahun']).sum()[["Total Belanja"]].reset_index()
    totalbelanja['Tahun'] = totalbelanja.Tahun.astype(str)
    totalbelanja = totalbelanja[totalbelanja['Tahun'].isin(name)]
    newfig  = px.bar(totalbelanja,x='Nama Provinsi',y='Total Belanja',color="Tahun")
    newfig.update_layout(barmode='group')
    newfig.update_xaxes(categoryorder='total descending')
    return newfig 

@app.callback(
    dash.dependencies.Output('ipmbareko','figure'),
    [dash.dependencies.Input('ipm-tahun-multidropdowneko','value'),
     dash.dependencies.Input('ipm-kabupaten-multidropdowneko','value')]
    )
       
# Update the histogram

def update_hist(name,kabupaten):
    dfbnbp = pd.read_csv('GDPreg.csv')
    dfbnbp =  dfbnbp[ dfbnbp['Kode'].isin(kabupaten)]
    #create selection for the dataset
    #untuk histogram feed to the graph
    dfbnbp['Tahun'] = dfbnbp.Tahun.astype(str)
    dfbnbp = dfbnbp[dfbnbp['Tahun'].isin(name)]
    ipmfig  = px.bar(dfbnbp,x='Provinsi ',y='GDP',color="Tahun")
    ipmfig.update_layout(barmode='group')
    ipmfig.update_xaxes(categoryorder='total descending')
    return ipmfig 

if __name__ == '__main__':
    app.run_server(debug=True)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import median_absolute_error

def get_metrics(y_true, y_pred):
    '''
    Função para calcular as métricas de erro do modelo preditivo. 
    Sendo essas mean squared error, root mean squared error, mean absolute error, mean absolute percentage error e median absolute error.
    '''
    mse = mean_squared_error(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    mede = median_absolute_error(y_true, y_pred)
    return dict([('MSE', mse), ('RMSE', rmse), ('MAE', mae), ('MAPE', mape), ('MedE', mede)])

import plotly.graph_objects as go

def plot_results(df, y_true, y_pred, model):
    '''
    Função para plotar o comparativo entre os valores reais e os valores previstos pelo modelo.
    '''
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['2019-01':'2020-12'].index[-12:],y=y_pred[:,0],
                             mode='lines', name='Renovável - Previsto',
                             line=dict(color='darkolivegreen', width=2, dash='dash')))
    fig.add_trace(go.Scatter(x=df['2019-01':'2020-12'].index[-12:], y=y_true[:,0],
                             mode='lines', name='Renovável - Real',
                             line=dict(color='green', width=2)))
    fig.add_trace(go.Scatter(x=df['2019-01':'2020-12'].index[-12:], y=y_pred[:,1],
                             mode='lines', name='Não Renovável - Previsto',
                             line=dict(color='firebrick', width=2, dash='dash')))
    fig.add_trace(go.Scatter(x=df['2019-01':'2020-12'].index[-12:], y=y_true[:,1],
                         mode='lines', name='Não Renovável - Real',
                         line=dict(color='red', width=2)))
    fig.update_layout(title=str('Previsão da Geração de Energia Elétrica por Fonte no Brasil usando '+ model),
                      xaxis_title='Mês e Ano',
                      yaxis_title='Energia Gerada ((TWh/mês))')

    return fig.show()
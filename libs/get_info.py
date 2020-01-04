from libs import *


def get_description(df: pandas.DataFrame, id_cols='id'):
    """
        Usage Example:
            get_description(df, id_cols=Id_col)
    """
    if isinstance(id_cols, list):
        for col in id_cols:
            if col not in df.columns:
                raise KeyError('DataFrame df doesn`t contain `{col}` column!'.format(col=col))

    summary = (df[[i for i in df.columns if i not in id_cols]].describe().transpose().reset_index())

    summary = summary.rename(columns = {"index" : "feature"})
    summary = numpy.around(summary,3)

    val_lst = [summary['feature'], summary['count'],
               summary['mean'],summary['std'],
               summary['min'], summary['max'],
               summary['25%'], summary['50%'],
               summary['75%']]

    trace  = go.Table(header=dict(values=summary.columns.tolist(),
                                    line=dict(color = ['#506784']),
                                    fill=dict(color = ['#119DFF']),
                                   ),
                      cells=dict(values=val_lst,
                                    line=dict(color = ['#506784']),
                                    fill=dict(color = ["lightgrey",'#F5F8FF'])
                                   ),
                      columnwidth = [200,60,100,100,60,60,80,80,80])
    layout = go.Layout(dict(title = "Variable Description"))
    figure = go.Figure(data=[trace],layout=layout)
    py.iplot(figure)

    
from libs import *


def scatter_3d(df: pandas.DataFrame, x_col, y_col, z_col,
                traces, title=''):
    """
        Usage Example:
            scatter_3d(telcom, 'col1', 'col2', 'col3',
                        ({'name': '1', 'text': '', 'filter': telcom[taget_col] == 1},
                         {'name': '0', 'text': '', 'filter': telcom[taget_col] == 0}
                        ), title='title'
                    )
    """
    # traces = ({'name': '', 'text': '', 'filter': None}, {'name': '', 'text': '', 'filter': None})
    n = len(traces)
    colors = []
    color = cm.rainbow(numpy.linspace(0, 1, n))
    for i, c in zip(range(n), color):
        colors.append(c)

    data = [go.Scatter3d(x=df[x['filter']][x_col],
                        y=df[x['filter']][y_col],
                        z=df[x['filter']][z_col],
                        name=x['name'],
                        text=x['text'],
                        mode="markers",
                        marker=dict(size=1,color=c[idx])
                        ) for idx, x in enumerate(traces)]

    layout = go.Layout(dict(title=title,
                        scene=dict(camera=dict(up=dict(x= 0 , y=0, z=0),
                                                   center=dict(x=0, y=0, z=0),
                                                   eye=dict(x=1.25, y=1.25, z=1.25)),
                                     xaxis=dict(title="monthly charges",
                                                   gridcolor='rgb(255, 255, 255)',
                                                   zerolinecolor='rgb(255, 255, 255)',
                                                   showbackground=True,
                                                   backgroundcolor='rgb(230, 230,230)'),
                                     yaxis=dict(title="total charges",
                                                   gridcolor='rgb(255, 255, 255)',
                                                   zerolinecolor='rgb(255, 255, 255)',
                                                   showbackground=True,
                                                   backgroundcolor='rgb(230, 230,230)'
                                                  ),
                                     zaxis=dict(title="tenure",
                                                   gridcolor='rgb(255, 255, 255)',
                                                   zerolinecolor='rgb(255, 255, 255)',
                                                   showbackground=True,
                                                   backgroundcolor='rgb(230, 230,230)'
                                                  )
                                    ),
                                height=700,
                       )
                  )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)

def corr_heatmap(df, method='pearson', min_periods=1, colorscale="Viridis", abs=False):
    """
        Usage Example:
            corr_heatmap(df, abs=True)
    """
    # compute correlation
    correlation = df.corr(method=method, min_periods=min_periods)

    # trick labels
    matrix_cols = correlation.columns.tolist()

    # conver to array
    corr_array = numpy.array(correlation)

    if abs:
        corr_array = numpy.abs(corr_array)

    # Plotting
    trace = go.Heatmap(z=corr_array,
                        x=matrix_cols,
                        y=matrix_cols,
                        colorscale=colorscale,
                        colorbar=dict(title=f"{method} correlation coefficient", 
                                        titleside="right")
                        )

    layout = go.Layout(dict(title="Correlation Matrix for variables",
                            autosize=False,
                            height=720,
                            width=800,
                            margin=dict(r=0, l=210,
                                        t=25, b=210,
                                        ),
                            yaxis=dict(tickfont=dict(size=9)),
                            xaxis=dict(tickfont=dict(size=9))
                       )
                  )
    data = [trace]
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)

def __make_scatter_2d(data, target_col, id_col, target, color):
    tracer = go.Scatter(x=data[data[target_col] == target]["PC1"],
                        y=data[data[target_col] == target]["PC2"],
                        name=target,
                        mode="markers",
                        marker=dict(color=color,
                                      line=dict(width = .5),
                                      symbol= "diamond-open"),
                        text=("Id: " + data[data[target_col] == target][id_col])
                       )
    return tracer

def pca_2d(df, target_col, id_cols, title=''):
    """
        Usage Example:
            pca_2d(df, target_col, Id_col, title="title")
    """
    pca = PCA(n_components=2)

    X = df[[i for i in df.columns if i not in [id_cols] + [target_col]]]
    Y = df[[target_col] + [id_cols]]

    principal_components = pca.fit_transform(X)
    pca_data = pandas.DataFrame(principal_components, columns = ["PC1", "PC2"])
    pca_data = pca_data.merge(Y, left_index=True, right_index=True, how="left")
    pca_data[target_col] = pca_data[target_col].astype(str)

    layout = go.Layout(dict(title=title,
                        plot_bgcolor="rgb(243,243,243)",
                        paper_bgcolor="rgb(243,243,243)",
                        xaxis=dict(gridcolor='rgb(255, 255, 255)',
                                    title="principal component 1",
                                    zerolinewidth=1, ticklen=5, gridwidth=2),
                        yaxis=dict(gridcolor = 'rgb(255, 255, 255)',
                                    title = "principal component 2",
                                     zerolinewidth=1, ticklen=5, gridwidth=2),
                        height=600
                       )
                  )

    n = len(numpy.unique(pca_data[target_col]))
    colors = []
    color = cm.rainbow(numpy.linspace(0, 1, n))
    for i, c in zip(range(n), color):
        colors.append(c)

    data = [__make_scatter_2d(pca_data, target_col, id_cols, target, c[idx])
            for idx, target in enumerate(numpy.unique(pca_data[target_col]))]

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)

def pca_3d(df, target_col, id_cols, title=''):
    """
        Usage Example:
            pca_3d(df, target_col, Id_col, title="title")
    """
    pca = PCA(n_components=3)

    X = df[[i for i in df.columns if i not in [id_cols] + [target_col]]]
    Y = df[[target_col] + [id_cols]]

    principal_components = pca.fit_transform(X)
    pca_data = pandas.DataFrame(principal_components, columns = ["PC1", "PC2", "PC3"])
    pca_data = pca_data.merge(Y, left_index=True, right_index=True, how="left")
    pca_data[target_col] = pca_data[target_col].astype(str)

    layout = go.Layout(dict(title=title,
                        scene=dict(camera=dict(up=dict(x= 0 , y=0, z=0),
                                                   center=dict(x=0, y=0, z=0),
                                                   eye=dict(x=1.25, y=1.25, z=1.25)),
                                     xaxis=dict(title="monthly charges",
                                                   gridcolor='rgb(255, 255, 255)',
                                                   zerolinecolor='rgb(255, 255, 255)',
                                                   showbackground=True,
                                                   backgroundcolor='rgb(230, 230,230)'),
                                     yaxis=dict(title="total charges",
                                                   gridcolor='rgb(255, 255, 255)',
                                                   zerolinecolor='rgb(255, 255, 255)',
                                                   showbackground=True,
                                                   backgroundcolor='rgb(230, 230,230)'
                                                  ),
                                     zaxis=dict(title="tenure",
                                                   gridcolor='rgb(255, 255, 255)',
                                                   zerolinecolor='rgb(255, 255, 255)',
                                                   showbackground=True,
                                                   backgroundcolor='rgb(230, 230,230)'
                                                  )
                                    ),
                                height=700,
                       )
                  )

    n = len(numpy.unique(pca_data[target_col]))
    colors = []
    color = cm.rainbow(numpy.linspace(0, 1, n))
    for i, c in zip(range(n), color):
        colors.append(c)

    data = [go.Scatter3d(x=pca_data[pca_data[target_col] == x]["PC1"],
                    y=pca_data[pca_data[target_col] == x]["PC2"],
                    z=pca_data[pca_data[target_col] == x]["PC3"],
                    name=x,
                    text=("Id: " + pca_data[pca_data[target_col] == x][id_cols]),
                    mode="markers",
                    marker=dict(size=1,color=c[idx])
                    ) for idx, x in enumerate(numpy.unique(pca_data[target_col]))]

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)

def plot_radar(df, aggregate, target_col, title=''):
    """
        Usage Example:
            bi_cs = df.nunique()[df.nunique() == 2].keys()
            dat_rad = df[bi_cs]

            plot_radar(dat_rad, 1, target_col, "1 -  Customers")
            plot_radar(dat_rad, 0, target_col, "0 - Customers")
    """
    bi_cs = df.columns
    data_frame = df[df[target_col] == aggregate] 
    data_frame_x = data_frame[bi_cs].sum().reset_index()
    data_frame_x.columns = ["feature", "yes"]
    data_frame_x["no"] = data_frame.shape[0] - data_frame_x["yes"]
    data_frame_x = data_frame_x[data_frame_x["feature"] != target_col]
    
    #count of 1's(yes)
    trace1 = go.Scatterpolar(r=data_frame_x["yes"].values.tolist(),
                             theta=data_frame_x["feature"].tolist(),
                             fill="toself",
                             name="count of 1's",
                             mode="markers+lines",
                             marker=dict(size=5)
                            )
    #count of 0's(No)
    trace2 = go.Scatterpolar(r=data_frame_x["no"].values.tolist(),
                             theta=data_frame_x["feature"].tolist(),
                             fill="toself",
                             name="count of 0's",
                             mode="markers+lines",
                             marker=dict(size = 5)
                            ) 

    layout = go.Layout(dict(polar=dict(radialaxis=dict(visible=True,
                                                        side="counterclockwise",
                                                        showline=True,
                                                        linewidth=2,
                                                        tickwidth=2,
                                                        gridcolor="white",
                                                        gridwidth=2),
                                        angularaxis=dict(tickfont=dict(size=10),
                                                        layer="below traces"
                                                        ),
                                        bgcolor="rgb(243,243,243)",
                                        ),
                            paper_bgcolor="rgb(243,243,243)",
                            title=title,
                            height=700))
    
    data = [trace2, trace1]
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)


def corr_sns_heatmap(corr, annot=True, cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1):
    sns.heatmap(corr[(corr >= 0.5) | (corr <= -0.4)], 
                cmap=cmap, vmax=vmax, vmin=vmin, linewidths=linewidths,
                annot=annot, annot_kws={"size": 8}, square=True)

def __autolabel(arrayA):
    """
        Label each colored square with the corresponding data value. 
        If value > 20, the text is in black, else in white.
    """
    arrayA = numpy.array(arrayA)
    for i in range(arrayA.shape[0]):
        for j in range(arrayA.shape[1]):
                plt.text(j,i, "%.2f"%arrayA[i,j], ha='center', va='bottom',color='w')

def gt_matrix(df, num_cols, sz=16):
    a = []
    for i, c1 in enumerate(num_cols):
        b = [] 
        for j, c2 in enumerate(num_cols):
            mask = (~df[c1].isnull()) & (~df[c2].isnull())
            if i >= j:
                b.append((df.loc[mask,c1].values >= df.loc[mask, c2].values).mean())
            else:
                b.append((df.loc[mask, c1].values > df.loc[mask, c2].values).mean())

        a.append(b)

    plt.figure(figsize = (sz,sz))
    plt.imshow(a, interpolation = 'None')
    _ = plt.xticks(range(len(num_cols)),num_cols,rotation = 90)
    _ = plt.yticks(range(len(num_cols)),num_cols,rotation = 0)
    __autolabel(a)

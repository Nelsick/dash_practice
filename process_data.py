#En este scripts se definiran las funciones para procesar los datos

def per_canceled_booking(df):
    cancelation = ((df[df['booking_status']=='Canceled']['booking_status'].count() / df['booking_status'].count())*100).round(1)
    return cancelation

def booking_per_year_graf(df):
    booking = df.groupby(['arrival_year','arrival_month'])['booking_status'].count().reset_index()
    booking = booking.sort_values(by=['arrival_year','arrival_month'])
    return booking

def segment_type(df):
    segment = df.market_segment_type.value_counts().to_frame('segment_type_count').reset_index()
    return segment

def update_graph(df,value):
    data = df[df['arrival_year'] == value]
    fig = px.bar(
        data_frame=data,
        x='arrival_month',
        y='booking_status',
        color='arrival_year',
        markers=True)
    return fig

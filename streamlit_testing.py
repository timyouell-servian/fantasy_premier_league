import streamlit as st
import pandas as pd
import requests

base_url = 'https://fantasy.premierleague.com/api/'

st.set_page_config(page_title='Tims First Website', page_icon=':shark:', layout='wide')
st.title('Hello and welcome to Tim\'s first website!')
st.write('Please check back soon for updates and Fantasy Premier League Football tips and stats.')


st.sidebar.subheader('About')
st.sidebar.write("""This website is designed to help you analyse and
                 ultimately pick the best Fantasy Premier League Football
                 options for your team.""")
st.sidebar.write('[Github](https://github.com/TimYouell15)')

if st.button('Click me for a joke'):
	st.write('The change in weather here in Sydney has got me swapping from aerosol deodorant. Roll on next week.')
else:
	st.write('I promise it will be worth it')

def display_frame(df):
    '''display dataframe with all float columns rounded to 1 decimal place'''
    float_cols = df.select_dtypes(include='float64').columns.values
    st.dataframe(df.style.format(subset=float_cols, formatter='{:.1f}'))


def get_bootstrap_data(data_type):
    resp = requests.get(base_url + 'bootstrap-static/')
    if resp.status_code != 200:
        raise Exception('Response was status code ' + str(resp.status_code))
    data = resp.json()
    try:
        elements_data = pd.DataFrame(data[data_type])
        return elements_data
    except KeyError:
        print('Unable to reach bootstrap API successfully')


def get_manager_history_data(manager_id):
    manager_hist_url = base_url + 'entry/' + str(manager_id) + '/history/'
    resp = requests.get(manager_hist_url)
    if resp.status_code != 200:
        raise Exception('Response was status code ' + str(resp.status_code))
    json = resp.json()
    try:
        data = pd.DataFrame(json['current'])
        return data
    except KeyError:
        print('Unable to reach bootstrap API successfully')


# st.write please enter your FPL id below
#st. text input box
# is there a way to view total number of FPL players?
def get_total_fpl_players():
    base_resp = requests.get(base_url + 'bootstrap-static/')
    return base_resp.json()['total_players']


fpl_id = st.sidebar.text_input('Please enter your FPL ID:', '')


if fpl_id == '':
	st.write('')
else:
    try:
        fpl_id = int(fpl_id)
        total_players = get_total_fpl_players()
        if fpl_id <= total_players:
            st.sidebar.write('Displaying FPL 2022/23 Season Data for FPL ID: ' + str(fpl_id))
            manager_data = get_manager_history_data(fpl_id)
            display_frame(manager_data)
        else:
            st.sidebar.write('FPL ID is too high to be a valid ID. Please try again.')
            st.sidebar.write('The total number of FPL players is: ' + str(total_players))
    except ValueError:
        st.sidebar.write('Please enter a valid FPL ID.')







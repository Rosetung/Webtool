from statistics import mean
from tkinter import FLAT
from turtle import title
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from scipy.stats import pearsonr
from sklearn import linear_model, metrics
from sklearn.metrics import r2_score
from scipy import stats
import matplotlib.pyplot as plt
import time

st.set_page_config(layout="wide")
st.title('Design your flow panels!')

file = st.file_uploader('Upload your own FACS configuration in Excel format. If nothing is uploaded, Duke-NUS FACS configuration (BD LSRFortessa; 5 lasers) will be uploaded.')

if file is not None:
    flowcon_df = pd.read_excel(file)

else:
    flowcon_df = pd.read_csv('https://github.com/Rosetung/Try/files/9681067/Try1.csv')

st.markdown('*FACS machine configuration*')
st.write(flowcon_df)

df = flowcon_df.replace('NaN', np.nan)
dfd= [[y for y in x if pd.notna(y)] for x in df.values.tolist()]

flat_list = [item for sublist in dfd for item in sublist]

selected_no = st.selectbox('How many markers?', ('Please select','2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'))

if selected_no=='Please select':
    st.stop()

if selected_no=='2':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)


    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)


    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
    

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()

            list=[]
            for a in df_0:
                for b in df_1:
                    cc=[a, b]
                    if(len(set(cc)) == len(cc)):
                        list.append(cc)
            
            with st.spinner('🧑‍🔬 Wait for it...'):
                time.sleep(1)
            st.success('🎉 Done!')  
            
            #st.write(list)                    
            number=range(len(list))
            st.subheader('Here are your flow panel options!')
            
            for j in number:
                cc0=flowcon_df[list[j][0]].tolist()
                cc1=flowcon_df[list[j][1]].tolist()
                for i in color_0:
                    for ii in color_1:
                        if i in cc0:
                            if ii in cc1:
                                print('')
                                st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii)
        


if selected_no=='3':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)


    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

  

    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()

            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()
   


                list=[]
                for a in df_0:
                    for b in df_1:
                        for c in df_2:
                            cc=[a, b, c]
                            if(len(set(cc)) == len(cc)):
                                list.append(cc)

                with st.spinner('🧑‍🔬 Wait for it...'):
                    time.sleep(1)
                st.success('🎉 Done!') 

                #st.write(list)                    
                number=range(len(list))
                st.subheader('Here are your flow panel options!')
                
                for j in number:
                    cc0=flowcon_df[list[j][0]].tolist()
                    cc1=flowcon_df[list[j][1]].tolist()
                    cc2=flowcon_df[list[j][2]].tolist()
                    for i in color_0:
                        for ii in color_1:
                            for iii in color_2:
                                if i in cc0:
                                    if ii in cc1:
                                        if iii in cc2:
                                            print('')
                                            st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii)
                    


if selected_no=='4':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
   

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()

   
            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()
    

                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()

    
                    list=[]
                    for a in df_0:
                        for b in df_1:
                            for c in df_2:
                                for d in df_3:
                                    cc=[a, b, c, d]
                                    if(len(set(cc)) == len(cc)):
                                        list.append(cc)

                    with st.spinner('🧑‍🔬 Wait for it...'):
                        time.sleep(1)
                    st.success('🎉 Done!') 

                    #st.write(list)                    
                    number=range(len(list))
                    st.subheader('Here are your flow panel options!')
                    
                    for j in number:
                        cc0=flowcon_df[list[j][0]].tolist()
                        cc1=flowcon_df[list[j][1]].tolist()
                        cc2=flowcon_df[list[j][2]].tolist()
                        cc3=flowcon_df[list[j][3]].tolist()
                        for i in color_0:
                            for ii in color_1:
                                for iii in color_2:
                                    for iiii in color_3:
                                        if i in cc0:
                                            if ii in cc1:
                                                if iii in cc2:
                                                    if iiii in cc3:
                                                        print('')
                                                        st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iiii)
                        

if selected_no=='5':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
   

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()




            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()
  

                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()



                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()



                        list=[]
                        for a in df_0:
                            for b in df_1:
                                for c in df_2:
                                    for d in df_3:
                                        for e in df_4:
                                            cc=[a, b, c, d, e]
                                            if(len(set(cc)) == len(cc)):
                                                list.append(cc)
   
                        with st.spinner('🧑‍🔬 Wait for it...'):
                            time.sleep(1)
                        st.success('🎉 Done!')                     
                        #st.write(list)                    
                        number=range(len(list))
                        st.subheader('Here are your flow panel options!')
                        
                        for j in number:
                            cc0=flowcon_df[list[j][0]].tolist()
                            cc1=flowcon_df[list[j][1]].tolist()
                            cc2=flowcon_df[list[j][2]].tolist()
                            cc3=flowcon_df[list[j][3]].tolist()
                            cc4=flowcon_df[list[j][4]].tolist()

                            for i in color_0:
                                for ii in color_1:
                                    for iii in color_2:
                                        for iv in color_3:
                                            for v in color_4:
                                                if i in cc0:
                                                    if ii in cc1:
                                                        if iii in cc2:
                                                            if iv in cc3:
                                                                if v in cc4:
                                                                    print('')
                                                                    st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v)


if selected_no=='6':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
  

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()



            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()


                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()



                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()



                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()

                            list=[]
                            for a in df_0:
                                for b in df_1:
                                    for c in df_2:
                                        for d in df_3:
                                            for e in df_4:
                                                for f in df_5:
                                                    cc=[a, b, c, d, e, f]
                                                    if(len(set(cc)) == len(cc)):
                                                        list.append(cc)
                            with st.spinner('🧑‍🔬 Wait for it...'):
                                time.sleep(1)
                            st.success('🎉 Done!')                     
                            #st.write(list)                    
                            number=range(len(list))
                            st.subheader('Here are your flow panel options!')
                            
                            for j in number:
                                cc0=flowcon_df[list[j][0]].tolist()
                                cc1=flowcon_df[list[j][1]].tolist()
                                cc2=flowcon_df[list[j][2]].tolist()
                                cc3=flowcon_df[list[j][3]].tolist()
                                cc4=flowcon_df[list[j][4]].tolist()
                                cc5=flowcon_df[list[j][5]].tolist()

                                for i in color_0:
                                    for ii in color_1:
                                        for iii in color_2:
                                            for iv in color_3:
                                                for v in color_4:
                                                    for vi in color_5:
                                                        if i in cc0:
                                                            if ii in cc1:
                                                                if iii in cc2:
                                                                    if iv in cc3:
                                                                        if v in cc4:
                                                                            if vi in cc5:
                                                                                print('')
                                                                                st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi)


if selected_no=='7':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    title_6 = st.text_input('Marker', key=7)
    color_6=st.multiselect('Select fluorophores available for this marker', flat_list, key=25)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(title_6)!=0:
        col_6 = ', '.join(color_6)
        st.write(title_6 + ': ' + col_6)

    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
 

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()


            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()
  

                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()


                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()


                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()


                            if len(color_6)!=0:
                                df_6 = flowcon_df[flowcon_df.isin(color_6)]
                                df_6 = df_6.dropna(axis=1, how='all', inplace=False)
                                df_6.columns.tolist()


                            list=[]
                            for a in df_0:
                                for b in df_1:
                                    for c in df_2:
                                        for d in df_3:
                                            for e in df_4:
                                                for f in df_5:
                                                    for g in df_6:
                                                        cc=[a, b, c, d, e, f, g]
                                                        if(len(set(cc)) == len(cc)):
                                                            list.append(cc)

                            with st.spinner('🧑‍🔬 Wait for it...'):
                                time.sleep(1)
                            st.success('🎉 Done!')                     
                            #st.write(list)                    
                            number=range(len(list))
                            st.subheader('Here are your flow panel options!')
                            
                            for j in number:
                                cc0=flowcon_df[list[j][0]].tolist()
                                cc1=flowcon_df[list[j][1]].tolist()
                                cc2=flowcon_df[list[j][2]].tolist()
                                cc3=flowcon_df[list[j][3]].tolist()
                                cc4=flowcon_df[list[j][4]].tolist()
                                cc5=flowcon_df[list[j][5]].tolist()
                                cc6=flowcon_df[list[j][6]].tolist()

                                for i in color_0:
                                    for ii in color_1:
                                        for iii in color_2:
                                            for iv in color_3:
                                                for v in color_4:
                                                    for vi in color_5:
                                                        for vii in color_6:
                                                            if i in cc0:
                                                                if ii in cc1:
                                                                    if iii in cc2:
                                                                        if iv in cc3:
                                                                            if v in cc4:
                                                                                if vi in cc5:
                                                                                    if vii in cc6:
                                                                                        print('')
                                                                                        st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi+', '+ title_6 + ': ' + vii)

if selected_no=='8':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    title_6 = st.text_input('Marker', key=7)
    color_6=st.multiselect('Select fluorophores available for this marker', flat_list, key=25)

    title_7 = st.text_input('Marker', key=8)
    color_7=st.multiselect('Select fluorophores available for this marker', flat_list, key=26)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(title_6)!=0:
        col_6 = ', '.join(color_6)
        st.write(title_6 + ': ' + col_6)

    if len(title_7)!=0:
        col_7 = ', '.join(color_7)
        st.write(title_7 + ': ' + col_7)

    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
   

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()


            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()


                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()


                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()


                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()


                            if len(color_6)!=0:
                                df_6 = flowcon_df[flowcon_df.isin(color_6)]
                                df_6 = df_6.dropna(axis=1, how='all', inplace=False)
                                df_6.columns.tolist()


                                if len(color_7)!=0:
                                    df_7 = flowcon_df[flowcon_df.isin(color_7)]
                                    df_7 = df_7.dropna(axis=1, how='all', inplace=False)
                                    df_7.columns.tolist()


                                    list=[]
                                    for a in df_0:
                                        for b in df_1:
                                            for c in df_2:
                                                for d in df_3:
                                                    for e in df_4:
                                                        for f in df_5:
                                                            for g in df_6:
                                                                for h in df_7:
                                                                    cc=[a, b, c, d, e, f, g, h]
                                                                    if(len(set(cc)) == len(cc)):
                                                                        list.append(cc)

                                    with st.spinner('🧑‍🔬 Wait for it...'):
                                        time.sleep(1)
                                    st.success('🎉 Done!')                    
                                    #st.write(list)                    
                                    number=range(len(list))
                                    st.subheader('Here are your flow panel options!')
                                    
                                    for j in number:
                                        cc0=flowcon_df[list[j][0]].tolist()
                                        cc1=flowcon_df[list[j][1]].tolist()
                                        cc2=flowcon_df[list[j][2]].tolist()
                                        cc3=flowcon_df[list[j][3]].tolist()
                                        cc4=flowcon_df[list[j][4]].tolist()
                                        cc5=flowcon_df[list[j][5]].tolist()
                                        cc6=flowcon_df[list[j][6]].tolist()
                                        cc7=flowcon_df[list[j][7]].tolist()

                                        for i in color_0:
                                            for ii in color_1:
                                                for iii in color_2:
                                                    for iv in color_3:
                                                        for v in color_4:
                                                            for vi in color_5:
                                                                for vii in color_6:
                                                                    for viii in color_7:
                                                                        if i in cc0:
                                                                            if ii in cc1:
                                                                                if iii in cc2:
                                                                                    if iv in cc3:
                                                                                        if v in cc4:
                                                                                            if vi in cc5:
                                                                                                if vii in cc6:
                                                                                                    if viii in cc7:
                                                                                                        print('')
                                                                                                        st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi+', '+ title_6 + ': ' + vii+', '+ title_7 + ': ' + viii)


if selected_no=='9':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    title_6 = st.text_input('Marker', key=7)
    color_6=st.multiselect('Select fluorophores available for this marker', flat_list, key=25)

    title_7 = st.text_input('Marker', key=8)
    color_7=st.multiselect('Select fluorophores available for this marker', flat_list, key=26)

    title_8 = st.text_input('Marker', key=9)
    color_8=st.multiselect('Select fluorophores available for this marker', flat_list, key=27)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(title_6)!=0:
        col_6 = ', '.join(color_6)
        st.write(title_6 + ': ' + col_6)

    if len(title_7)!=0:
        col_7 = ', '.join(color_7)
        st.write(title_7 + ': ' + col_7)

    if len(title_8)!=0:
        col_8 = ', '.join(color_8)
        st.write(title_8 + ': ' + col_8)


    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()


        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()




            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()
  

                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()


                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()


                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()

                            if len(color_6)!=0:
                                df_6 = flowcon_df[flowcon_df.isin(color_6)]
                                df_6 = df_6.dropna(axis=1, how='all', inplace=False)
                                df_6.columns.tolist()


                                if len(color_7)!=0:
                                    df_7 = flowcon_df[flowcon_df.isin(color_7)]
                                    df_7 = df_7.dropna(axis=1, how='all', inplace=False)
                                    df_7.columns.tolist()


                                    if len(color_8)!=0:
                                        df_8 = flowcon_df[flowcon_df.isin(color_8)]
                                        df_8 = df_8.dropna(axis=1, how='all', inplace=False)
                                        df_8.columns.tolist()


                                        list=[]
                                        for a in df_0:
                                            for b in df_1:
                                                for c in df_2:
                                                    for d in df_3:
                                                        for e in df_4:
                                                            for f in df_5:
                                                                for g in df_6:
                                                                    for h in df_7:
                                                                        for k in df_8:
                                                                            cc=[a, b, c, d, e, f, g, h, k]
                                                                            if(len(set(cc)) == len(cc)):
                                                                                list.append(cc)

                                        with st.spinner('🧑‍🔬 Wait for it...'):
                                            time.sleep(1)
                                        st.success('🎉 Done!') 

                                        #st.write(list)                    
                                        number=range(len(list))
                                        st.subheader('Here are your flow panel options!')
                                        
                                        for j in number:
                                            cc0=flowcon_df[list[j][0]].tolist()
                                            cc1=flowcon_df[list[j][1]].tolist()
                                            cc2=flowcon_df[list[j][2]].tolist()
                                            cc3=flowcon_df[list[j][3]].tolist()
                                            cc4=flowcon_df[list[j][4]].tolist()
                                            cc5=flowcon_df[list[j][5]].tolist()
                                            cc6=flowcon_df[list[j][6]].tolist()
                                            cc7=flowcon_df[list[j][7]].tolist()
                                            cc8=flowcon_df[list[j][8]].tolist()

                                            for i in color_0:
                                                for ii in color_1:
                                                    for iii in color_2:
                                                        for iv in color_3:
                                                            for v in color_4:
                                                                for vi in color_5:
                                                                    for vii in color_6:
                                                                        for viii in color_7:
                                                                            for ix in color_8:
                                                                                if i in cc0:
                                                                                    if ii in cc1:
                                                                                        if iii in cc2:
                                                                                            if iv in cc3:
                                                                                                if v in cc4:
                                                                                                    if vi in cc5:
                                                                                                        if vii in cc6:
                                                                                                            if viii in cc7:
                                                                                                                if ix in cc8:
                                                                                                                    print('')
                                                                                                                    st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi+', '+ title_6 + ': ' + vii+', '+ title_7 + ': ' + viii+', '+ title_8 + ': ' + ix)

if selected_no=='10':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    title_6 = st.text_input('Marker', key=7)
    color_6=st.multiselect('Select fluorophores available for this marker', flat_list, key=25)

    title_7 = st.text_input('Marker', key=8)
    color_7=st.multiselect('Select fluorophores available for this marker', flat_list, key=26)

    title_8 = st.text_input('Marker', key=9)
    color_8=st.multiselect('Select fluorophores available for this marker', flat_list, key=27)

    title_9 = st.text_input('Marker', key=10)
    color_9=st.multiselect('Select fluorophores available for this marker', flat_list, key=28)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(title_6)!=0:
        col_6 = ', '.join(color_6)
        st.write(title_6 + ': ' + col_6)

    if len(title_7)!=0:
        col_7 = ', '.join(color_7)
        st.write(title_7 + ': ' + col_7)

    if len(title_8)!=0:
        col_8 = ', '.join(color_8)
        st.write(title_8 + ': ' + col_8)

    if len(title_9)!=0:
        col_9 = ', '.join(color_9)
        st.write(title_9 + ': ' + col_9)


    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()


        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()


            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()
    

                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()


                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()

                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()

                            if len(color_6)!=0:
                                df_6 = flowcon_df[flowcon_df.isin(color_6)]
                                df_6 = df_6.dropna(axis=1, how='all', inplace=False)
                                df_6.columns.tolist()

                                if len(color_7)!=0:
                                    df_7 = flowcon_df[flowcon_df.isin(color_7)]
                                    df_7 = df_7.dropna(axis=1, how='all', inplace=False)
                                    df_7.columns.tolist()

                                    if len(color_8)!=0:
                                        df_8 = flowcon_df[flowcon_df.isin(color_8)]
                                        df_8 = df_8.dropna(axis=1, how='all', inplace=False)
                                        df_8.columns.tolist()

                                        if len(color_9)!=0:
                                            df_9 = flowcon_df[flowcon_df.isin(color_9)]
                                            df_9 = df_9.dropna(axis=1, how='all', inplace=False)
                                            df_9.columns.tolist()


                                            list=[]
                                            for a in df_0:
                                                for b in df_1:
                                                    for c in df_2:
                                                        for d in df_3:
                                                            for e in df_4:
                                                                for f in df_5:
                                                                    for g in df_6:
                                                                        for h in df_7:
                                                                            for k in df_8:
                                                                                for l in df_9:
                                                                                    cc=[a, b, c, d, e, f, g, h, k, l]
                                                                                    if(len(set(cc)) == len(cc)):
                                                                                        list.append(cc)

                                            with st.spinner('🧑‍🔬 Wait for it...'):
                                                time.sleep(1)
                                            st.success('🎉 Done!') 

                                            #st.write(list)                    
                                            number=range(len(list))
                                            st.subheader('Here are your flow panel options!')
                                            
                                            for j in number:
                                                cc0=flowcon_df[list[j][0]].tolist()
                                                cc1=flowcon_df[list[j][1]].tolist()
                                                cc2=flowcon_df[list[j][2]].tolist()
                                                cc3=flowcon_df[list[j][3]].tolist()
                                                cc4=flowcon_df[list[j][4]].tolist()
                                                cc5=flowcon_df[list[j][5]].tolist()
                                                cc6=flowcon_df[list[j][6]].tolist()
                                                cc7=flowcon_df[list[j][7]].tolist()
                                                cc8=flowcon_df[list[j][8]].tolist()
                                                cc9=flowcon_df[list[j][9]].tolist()

                                                for i in color_0:
                                                    for ii in color_1:
                                                        for iii in color_2:
                                                            for iv in color_3:
                                                                for v in color_4:
                                                                    for vi in color_5:
                                                                        for vii in color_6:
                                                                            for viii in color_7:
                                                                                for ix in color_8:
                                                                                    for x in color_9:
                                                                                        if i in cc0:
                                                                                            if ii in cc1:
                                                                                                if iii in cc2:
                                                                                                    if iv in cc3:
                                                                                                        if v in cc4:
                                                                                                            if vi in cc5:
                                                                                                                if vii in cc6:
                                                                                                                    if viii in cc7:
                                                                                                                        if ix in cc8:
                                                                                                                            if x in cc9:
                                                                                                                                print('')
                                                                                                                                st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi+', '+ title_6 + ': ' + vii+', '+ title_7 + ': ' + viii+', '+ title_8 + ': ' + ix+', '+ title_9 + ': ' + x)


if selected_no=='11':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    title_6 = st.text_input('Marker', key=7)
    color_6=st.multiselect('Select fluorophores available for this marker', flat_list, key=25)

    title_7 = st.text_input('Marker', key=8)
    color_7=st.multiselect('Select fluorophores available for this marker', flat_list, key=26)

    title_8 = st.text_input('Marker', key=9)
    color_8=st.multiselect('Select fluorophores available for this marker', flat_list, key=27)

    title_9 = st.text_input('Marker', key=10)
    color_9=st.multiselect('Select fluorophores available for this marker', flat_list, key=28)

    title_10 = st.text_input('Marker', key=11)
    color_10=st.multiselect('Select fluorophores available for this marker', flat_list, key=29)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(title_6)!=0:
        col_6 = ', '.join(color_6)
        st.write(title_6 + ': ' + col_6)

    if len(title_7)!=0:
        col_7 = ', '.join(color_7)
        st.write(title_7 + ': ' + col_7)

    if len(title_8)!=0:
        col_8 = ', '.join(color_8)
        st.write(title_8 + ': ' + col_8)

    if len(title_9)!=0:
        col_9 = ', '.join(color_9)
        st.write(title_9 + ': ' + col_9)

    if len(title_10)!=0:
        col_10 = ', '.join(color_10)
        st.write(title_10 + ': ' + col_10)


    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()


        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()


            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()
  

                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()


                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()


                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()


                            if len(color_6)!=0:
                                df_6 = flowcon_df[flowcon_df.isin(color_6)]
                                df_6 = df_6.dropna(axis=1, how='all', inplace=False)
                                df_6.columns.tolist()


                                if len(color_7)!=0:
                                    df_7 = flowcon_df[flowcon_df.isin(color_7)]
                                    df_7 = df_7.dropna(axis=1, how='all', inplace=False)
                                    df_7.columns.tolist()


                                    if len(color_8)!=0:
                                        df_8 = flowcon_df[flowcon_df.isin(color_8)]
                                        df_8 = df_8.dropna(axis=1, how='all', inplace=False)
                                        df_8.columns.tolist()


                                        if len(color_9)!=0:
                                            df_9 = flowcon_df[flowcon_df.isin(color_9)]
                                            df_9 = df_9.dropna(axis=1, how='all', inplace=False)
                                            df_9.columns.tolist()


                                            if len(color_10)!=0:
                                                df_10 = flowcon_df[flowcon_df.isin(color_10)]
                                                df_10 = df_10.dropna(axis=1, how='all', inplace=False)
                                                df_10.columns.tolist()



                                                list=[]
                                                for a in df_0:
                                                    for b in df_1:
                                                        for c in df_2:
                                                            for d in df_3:
                                                                for e in df_4:
                                                                    for f in df_5:
                                                                        for g in df_6:
                                                                            for h in df_7:
                                                                                for k in df_8:
                                                                                    for l in df_9:
                                                                                        for m in df_10:
                                                                                            cc=[a, b, c, d, e, f, g, h, k, l, m]
                                                                                            if(len(set(cc)) == len(cc)):
                                                                                                list.append(cc)

                                                with st.spinner('🧑‍🔬 Wait for it...'):
                                                    time.sleep(1)
                                                st.success('🎉 Done!')                     
                                                #st.write(list)                    
                                                number=range(len(list))
                                                st.subheader('Here are your flow panel options!')
                                                
                                                for j in number:
                                                    cc0=flowcon_df[list[j][0]].tolist()
                                                    cc1=flowcon_df[list[j][1]].tolist()
                                                    cc2=flowcon_df[list[j][2]].tolist()
                                                    cc3=flowcon_df[list[j][3]].tolist()
                                                    cc4=flowcon_df[list[j][4]].tolist()
                                                    cc5=flowcon_df[list[j][5]].tolist()
                                                    cc6=flowcon_df[list[j][6]].tolist()
                                                    cc7=flowcon_df[list[j][7]].tolist()
                                                    cc8=flowcon_df[list[j][8]].tolist()
                                                    cc9=flowcon_df[list[j][9]].tolist()
                                                    cc10=flowcon_df[list[j][10]].tolist()

                                                    for i in color_0:
                                                        for ii in color_1:
                                                            for iii in color_2:
                                                                for iv in color_3:
                                                                    for v in color_4:
                                                                        for vi in color_5:
                                                                            for vii in color_6:
                                                                                for viii in color_7:
                                                                                    for ix in color_8:
                                                                                        for x in color_9:
                                                                                            for xi in color_10:
                                                                                                if i in cc0:
                                                                                                    if ii in cc1:
                                                                                                        if iii in cc2:
                                                                                                            if iv in cc3:
                                                                                                                if v in cc4:
                                                                                                                    if vi in cc5:
                                                                                                                        if vii in cc6:
                                                                                                                            if viii in cc7:
                                                                                                                                if ix in cc8:
                                                                                                                                    if x in cc9:
                                                                                                                                        if xi in cc10:
                                                                                                                                            print('')
                                                                                                                                            st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi+', '+ title_6 + ': ' + vii+', '+ title_7 + ': ' + viii+', '+ title_8 + ': ' + ix+', '+ title_9 + ': ' + x+', '+ title_10 + ': ' + xi)


if selected_no=='12':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    title_6 = st.text_input('Marker', key=7)
    color_6=st.multiselect('Select fluorophores available for this marker', flat_list, key=25)

    title_7 = st.text_input('Marker', key=8)
    color_7=st.multiselect('Select fluorophores available for this marker', flat_list, key=26)

    title_8 = st.text_input('Marker', key=9)
    color_8=st.multiselect('Select fluorophores available for this marker', flat_list, key=27)

    title_9 = st.text_input('Marker', key=10)
    color_9=st.multiselect('Select fluorophores available for this marker', flat_list, key=28)

    title_10 = st.text_input('Marker', key=11)
    color_10=st.multiselect('Select fluorophores available for this marker', flat_list, key=29)

    title_11 = st.text_input('Marker', key=12)
    color_11=st.multiselect('Select fluorophores available for this marker', flat_list, key=30)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(title_6)!=0:
        col_6 = ', '.join(color_6)
        st.write(title_6 + ': ' + col_6)

    if len(title_7)!=0:
        col_7 = ', '.join(color_7)
        st.write(title_7 + ': ' + col_7)

    if len(title_8)!=0:
        col_8 = ', '.join(color_8)
        st.write(title_8 + ': ' + col_8)

    if len(title_9)!=0:
        col_9 = ', '.join(color_9)
        st.write(title_9 + ': ' + col_9)

    if len(title_10)!=0:
        col_10 = ', '.join(color_10)
        st.write(title_10 + ': ' + col_10)

    if len(title_11)!=0:
        col_11 = ', '.join(color_11)
        st.write(title_11 + ': ' + col_11)


    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
  

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()



            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()


                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()


                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()


                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()


                            if len(color_6)!=0:
                                df_6 = flowcon_df[flowcon_df.isin(color_6)]
                                df_6 = df_6.dropna(axis=1, how='all', inplace=False)
                                df_6.columns.tolist()


                                if len(color_7)!=0:
                                    df_7 = flowcon_df[flowcon_df.isin(color_7)]
                                    df_7 = df_7.dropna(axis=1, how='all', inplace=False)
                                    df_7.columns.tolist()

                                    if len(color_8)!=0:
                                        df_8 = flowcon_df[flowcon_df.isin(color_8)]
                                        df_8 = df_8.dropna(axis=1, how='all', inplace=False)
                                        df_8.columns.tolist()

                                        if len(color_9)!=0:
                                            df_9 = flowcon_df[flowcon_df.isin(color_9)]
                                            df_9 = df_9.dropna(axis=1, how='all', inplace=False)
                                            df_9.columns.tolist()


                                            if len(color_10)!=0:
                                                df_10 = flowcon_df[flowcon_df.isin(color_10)]
                                                df_10 = df_10.dropna(axis=1, how='all', inplace=False)
                                                df_10.columns.tolist()


                                                if len(color_11)!=0:
                                                    df_11 = flowcon_df[flowcon_df.isin(color_11)]
                                                    df_11 = df_11.dropna(axis=1, how='all', inplace=False)
                                                    df_11.columns.tolist()


                                                    list=[]
                                                    for a in df_0:
                                                        for b in df_1:
                                                            for c in df_2:
                                                                for d in df_3:
                                                                    for e in df_4:
                                                                        for f in df_5:
                                                                            for g in df_6:
                                                                                for h in df_7:
                                                                                    for k in df_8:
                                                                                        for l in df_9:
                                                                                            for m in df_10:
                                                                                                for n in df_11:
                                                                                                    cc=[a, b, c, d, e, f, g, h, k, l, m, n]
                                                                                                    if(len(set(cc)) == len(cc)):
                                                                                                        list.append(cc)

                                                    with st.spinner('🧑‍🔬 Wait for it...'):
                                                        time.sleep(1)
                                                    st.success('🎉 Done!') 

                                                    #st.write(list)                    
                                                    number=range(len(list))
                                                    st.subheader('Here are your flow panel options!')
                                                    
                                                    for j in number:
                                                        cc0=flowcon_df[list[j][0]].tolist()
                                                        cc1=flowcon_df[list[j][1]].tolist()
                                                        cc2=flowcon_df[list[j][2]].tolist()
                                                        cc3=flowcon_df[list[j][3]].tolist()
                                                        cc4=flowcon_df[list[j][4]].tolist()
                                                        cc5=flowcon_df[list[j][5]].tolist()
                                                        cc6=flowcon_df[list[j][6]].tolist()
                                                        cc7=flowcon_df[list[j][7]].tolist()
                                                        cc8=flowcon_df[list[j][8]].tolist()
                                                        cc9=flowcon_df[list[j][9]].tolist()
                                                        cc10=flowcon_df[list[j][10]].tolist()
                                                        cc11=flowcon_df[list[j][11]].tolist()

                                                        for i in color_0:
                                                            for ii in color_1:
                                                                for iii in color_2:
                                                                    for iv in color_3:
                                                                        for v in color_4:
                                                                            for vi in color_5:
                                                                                for vii in color_6:
                                                                                    for viii in color_7:
                                                                                        for ix in color_8:
                                                                                            for x in color_9:
                                                                                                for xi in color_10:
                                                                                                    for xii in color_11:
                                                                                                        if i in cc0:
                                                                                                            if ii in cc1:
                                                                                                                if iii in cc2:
                                                                                                                    if iv in cc3:
                                                                                                                        if v in cc4:
                                                                                                                            if vi in cc5:
                                                                                                                                if vii in cc6:
                                                                                                                                    if viii in cc7:
                                                                                                                                        if ix in cc8:
                                                                                                                                            if x in cc9:
                                                                                                                                                if xi in cc10:
                                                                                                                                                    if xii in cc11:
                                                                                                                                                        print('')
                                                                                                                                                        st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi+', '+ title_6 + ': ' + vii+', '+ title_7 + ': ' + viii+', '+ title_8 + ': ' + ix+', '+ title_9 + ': ' + x+', '+ title_10 + ': ' + xi+', '+ title_11 + ': ' + xii)


if selected_no=='13':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    title_6 = st.text_input('Marker', key=7)
    color_6=st.multiselect('Select fluorophores available for this marker', flat_list, key=25)

    title_7 = st.text_input('Marker', key=8)
    color_7=st.multiselect('Select fluorophores available for this marker', flat_list, key=26)

    title_8 = st.text_input('Marker', key=9)
    color_8=st.multiselect('Select fluorophores available for this marker', flat_list, key=27)

    title_9 = st.text_input('Marker', key=10)
    color_9=st.multiselect('Select fluorophores available for this marker', flat_list, key=28)

    title_10 = st.text_input('Marker', key=11)
    color_10=st.multiselect('Select fluorophores available for this marker', flat_list, key=29)

    title_11 = st.text_input('Marker', key=12)
    color_11=st.multiselect('Select fluorophores available for this marker', flat_list, key=30)

    title_12 = st.text_input('Marker', key=13)
    color_12=st.multiselect('Select fluorophores available for this marker', flat_list, key=31)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(title_6)!=0:
        col_6 = ', '.join(color_6)
        st.write(title_6 + ': ' + col_6)

    if len(title_7)!=0:
        col_7 = ', '.join(color_7)
        st.write(title_7 + ': ' + col_7)

    if len(title_8)!=0:
        col_8 = ', '.join(color_8)
        st.write(title_8 + ': ' + col_8)

    if len(title_9)!=0:
        col_9 = ', '.join(color_9)
        st.write(title_9 + ': ' + col_9)

    if len(title_10)!=0:
        col_10 = ', '.join(color_10)
        st.write(title_10 + ': ' + col_10)

    if len(title_11)!=0:
        col_11 = ', '.join(color_11)
        st.write(title_11 + ': ' + col_11)

    if len(title_12)!=0:
        col_12 = ', '.join(color_12)
        st.write(title_12 + ': ' + col_12)


    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
   

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()


            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()

                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()


                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()


                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()



                            if len(color_6)!=0:
                                df_6 = flowcon_df[flowcon_df.isin(color_6)]
                                df_6 = df_6.dropna(axis=1, how='all', inplace=False)
                                df_6.columns.tolist()

  
                                if len(color_7)!=0:
                                    df_7 = flowcon_df[flowcon_df.isin(color_7)]
                                    df_7 = df_7.dropna(axis=1, how='all', inplace=False)
                                    df_7.columns.tolist()


                                    if len(color_8)!=0:
                                        df_8 = flowcon_df[flowcon_df.isin(color_8)]
                                        df_8 = df_8.dropna(axis=1, how='all', inplace=False)
                                        df_8.columns.tolist()


                                        if len(color_9)!=0:
                                            df_9 = flowcon_df[flowcon_df.isin(color_9)]
                                            df_9 = df_9.dropna(axis=1, how='all', inplace=False)
                                            df_9.columns.tolist()


                                            if len(color_10)!=0:
                                                df_10 = flowcon_df[flowcon_df.isin(color_10)]
                                                df_10 = df_10.dropna(axis=1, how='all', inplace=False)
                                                df_10.columns.tolist()


                                                if len(color_11)!=0:
                                                    df_11 = flowcon_df[flowcon_df.isin(color_11)]
                                                    df_11 = df_11.dropna(axis=1, how='all', inplace=False)
                                                    df_11.columns.tolist()


                                                    if len(color_12)!=0:
                                                        df_12 = flowcon_df[flowcon_df.isin(color_12)]
                                                        df_12 = df_12.dropna(axis=1, how='all', inplace=False)
                                                        df_12.columns.tolist()


                                                        list=[]
                                                        for a in df_0:
                                                            for b in df_1:
                                                                for c in df_2:
                                                                    for d in df_3:
                                                                        for e in df_4:
                                                                            for f in df_5:
                                                                                for g in df_6:
                                                                                    for h in df_7:
                                                                                        for k in df_8:
                                                                                            for l in df_9:
                                                                                                for m in df_10:
                                                                                                    for n in df_11:
                                                                                                        for o in df_12:
                                                                                                            cc=[a, b, c, d, e, f, g, h, k, l, m, n, o]
                                                                                                            if(len(set(cc)) == len(cc)):
                                                                                                                list.append(cc)

                                                        with st.spinner('🧑‍🔬 Wait for it...'):
                                                            time.sleep(1)
                                                        st.success('🎉 Done!')                     
                                                        #st.write(list)                    
                                                        number=range(len(list))
                                                        st.subheader('Here are your flow panel options!')
                                                        
                                                        for j in number:
                                                            cc0=flowcon_df[list[j][0]].tolist()
                                                            cc1=flowcon_df[list[j][1]].tolist()
                                                            cc2=flowcon_df[list[j][2]].tolist()
                                                            cc3=flowcon_df[list[j][3]].tolist()
                                                            cc4=flowcon_df[list[j][4]].tolist()
                                                            cc5=flowcon_df[list[j][5]].tolist()
                                                            cc6=flowcon_df[list[j][6]].tolist()
                                                            cc7=flowcon_df[list[j][7]].tolist()
                                                            cc8=flowcon_df[list[j][8]].tolist()
                                                            cc9=flowcon_df[list[j][9]].tolist()
                                                            cc10=flowcon_df[list[j][10]].tolist()
                                                            cc11=flowcon_df[list[j][11]].tolist()
                                                            cc12=flowcon_df[list[j][12]].tolist()

                                                            for i in color_0:
                                                                for ii in color_1:
                                                                    for iii in color_2:
                                                                        for iv in color_3:
                                                                            for v in color_4:
                                                                                for vi in color_5:
                                                                                    for vii in color_6:
                                                                                        for viii in color_7:
                                                                                            for ix in color_8:
                                                                                                for x in color_9:
                                                                                                    for xi in color_10:
                                                                                                        for xii in color_11:
                                                                                                            for xiii in color_12:
                                                                                                                if i in cc0:
                                                                                                                    if ii in cc1:
                                                                                                                        if iii in cc2:
                                                                                                                            if iv in cc3:
                                                                                                                                if v in cc4:
                                                                                                                                    if vi in cc5:
                                                                                                                                        if vii in cc6:
                                                                                                                                            if viii in cc7:
                                                                                                                                                if ix in cc8:
                                                                                                                                                    if x in cc9:
                                                                                                                                                        if xi in cc10:
                                                                                                                                                            if xii in cc11:
                                                                                                                                                                if xiii in cc12:
                                                                                                                                                                    print('')
                                                                                                                                                                    st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi+', '+ title_6 + ': ' + vii+', '+ title_7 + ': ' + viii+', '+ title_8 + ': ' + ix+', '+ title_9 + ': ' + x+', '+ title_10 + ': ' + xi+', '+ title_11 + ': ' + xii+', '+ title_12 + ': ' + xiii)



if selected_no=='14':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    title_6 = st.text_input('Marker', key=7)
    color_6=st.multiselect('Select fluorophores available for this marker', flat_list, key=25)

    title_7 = st.text_input('Marker', key=8)
    color_7=st.multiselect('Select fluorophores available for this marker', flat_list, key=26)

    title_8 = st.text_input('Marker', key=9)
    color_8=st.multiselect('Select fluorophores available for this marker', flat_list, key=27)

    title_9 = st.text_input('Marker', key=10)
    color_9=st.multiselect('Select fluorophores available for this marker', flat_list, key=28)

    title_10 = st.text_input('Marker', key=11)
    color_10=st.multiselect('Select fluorophores available for this marker', flat_list, key=29)

    title_11 = st.text_input('Marker', key=12)
    color_11=st.multiselect('Select fluorophores available for this marker', flat_list, key=30)

    title_12 = st.text_input('Marker', key=13)
    color_12=st.multiselect('Select fluorophores available for this marker', flat_list, key=31)

    title_13 = st.text_input('Marker', key=14)
    color_13=st.multiselect('Select fluorophores available for this marker', flat_list, key=32)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(title_6)!=0:
        col_6 = ', '.join(color_6)
        st.write(title_6 + ': ' + col_6)

    if len(title_7)!=0:
        col_7 = ', '.join(color_7)
        st.write(title_7 + ': ' + col_7)

    if len(title_8)!=0:
        col_8 = ', '.join(color_8)
        st.write(title_8 + ': ' + col_8)

    if len(title_9)!=0:
        col_9 = ', '.join(color_9)
        st.write(title_9 + ': ' + col_9)

    if len(title_10)!=0:
        col_10 = ', '.join(color_10)
        st.write(title_10 + ': ' + col_10)

    if len(title_11)!=0:
        col_11 = ', '.join(color_11)
        st.write(title_11 + ': ' + col_11)

    if len(title_12)!=0:
        col_12 = ', '.join(color_12)
        st.write(title_12 + ': ' + col_12)
    
    if len(title_13)!=0:
        col_13 = ', '.join(color_13)
        st.write(title_13 + ': ' + col_13)


    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
  

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()



            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()


                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()


                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()



                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()


                            if len(color_6)!=0:
                                df_6 = flowcon_df[flowcon_df.isin(color_6)]
                                df_6 = df_6.dropna(axis=1, how='all', inplace=False)
                                df_6.columns.tolist()


                                if len(color_7)!=0:
                                    df_7 = flowcon_df[flowcon_df.isin(color_7)]
                                    df_7 = df_7.dropna(axis=1, how='all', inplace=False)
                                    df_7.columns.tolist()


                                    if len(color_8)!=0:
                                        df_8 = flowcon_df[flowcon_df.isin(color_8)]
                                        df_8 = df_8.dropna(axis=1, how='all', inplace=False)
                                        df_8.columns.tolist()


                                        if len(color_9)!=0:
                                            df_9 = flowcon_df[flowcon_df.isin(color_9)]
                                            df_9 = df_9.dropna(axis=1, how='all', inplace=False)
                                            df_9.columns.tolist()


                                            if len(color_10)!=0:
                                                df_10 = flowcon_df[flowcon_df.isin(color_10)]
                                                df_10 = df_10.dropna(axis=1, how='all', inplace=False)
                                                df_10.columns.tolist()


                                                if len(color_11)!=0:
                                                    df_11 = flowcon_df[flowcon_df.isin(color_11)]
                                                    df_11 = df_11.dropna(axis=1, how='all', inplace=False)
                                                    df_11.columns.tolist()


                                                    if len(color_12)!=0:
                                                        df_12 = flowcon_df[flowcon_df.isin(color_12)]
                                                        df_12 = df_12.dropna(axis=1, how='all', inplace=False)
                                                        df_12.columns.tolist()



                                                        if len(color_13)!=0:
                                                            df_13 = flowcon_df[flowcon_df.isin(color_13)]
                                                            df_13 = df_13.dropna(axis=1, how='all', inplace=False)
                                                            df_13.columns.tolist()

 

                                                            list=[]
                                                            for a in df_0:
                                                                for b in df_1:
                                                                    for c in df_2:
                                                                        for d in df_3:
                                                                            for e in df_4:
                                                                                for f in df_5:
                                                                                    for g in df_6:
                                                                                        for h in df_7:
                                                                                            for k in df_8:
                                                                                                for l in df_9:
                                                                                                    for m in df_10:
                                                                                                        for n in df_11:
                                                                                                            for o in df_12:
                                                                                                                for p in df_13:
                                                                                                                    cc=[a, b, c, d, e, f, g, h, k, l, m, n, o, p]
                                                                                                                    if(len(set(cc)) == len(cc)):
                                                                                                                        list.append(cc)
                                                            with st.spinner('🧑‍🔬 Wait for it...'):
                                                                time.sleep(1)
                                                            st.success('🎉 Done!')                     
                                                            #st.write(list)                    
                                                            number=range(len(list))
                                                            st.subheader('Here are your flow panel options!')
                                                            
                                                            for j in number:
                                                                cc0=flowcon_df[list[j][0]].tolist()
                                                                cc1=flowcon_df[list[j][1]].tolist()
                                                                cc2=flowcon_df[list[j][2]].tolist()
                                                                cc3=flowcon_df[list[j][3]].tolist()
                                                                cc4=flowcon_df[list[j][4]].tolist()
                                                                cc5=flowcon_df[list[j][5]].tolist()
                                                                cc6=flowcon_df[list[j][6]].tolist()
                                                                cc7=flowcon_df[list[j][7]].tolist()
                                                                cc8=flowcon_df[list[j][8]].tolist()
                                                                cc9=flowcon_df[list[j][9]].tolist()
                                                                cc10=flowcon_df[list[j][10]].tolist()
                                                                cc11=flowcon_df[list[j][11]].tolist()
                                                                cc12=flowcon_df[list[j][12]].tolist()
                                                                cc13=flowcon_df[list[j][13]].tolist()

                                                                for i in color_0:
                                                                    for ii in color_1:
                                                                        for iii in color_2:
                                                                            for iv in color_3:
                                                                                for v in color_4:
                                                                                    for vi in color_5:
                                                                                        for vii in color_6:
                                                                                            for viii in color_7:
                                                                                                for ix in color_8:
                                                                                                    for x in color_9:
                                                                                                        for xi in color_10:
                                                                                                            for xii in color_11:
                                                                                                                for xiii in color_12:
                                                                                                                    for xiv in color_13:
                                                                                                                        if i in cc0:
                                                                                                                            if ii in cc1:
                                                                                                                                if iii in cc2:
                                                                                                                                    if iv in cc3:
                                                                                                                                        if v in cc4:
                                                                                                                                            if vi in cc5:
                                                                                                                                                if vii in cc6:
                                                                                                                                                    if viii in cc7:
                                                                                                                                                        if ix in cc8:
                                                                                                                                                            if x in cc9:
                                                                                                                                                                if xi in cc10:
                                                                                                                                                                    if xii in cc11:
                                                                                                                                                                        if xiii in cc12:
                                                                                                                                                                            if xiv in cc13:
                                                                                                                                                                                print('')
                                                                                                                                                                                st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi+', '+ title_6 + ': ' + vii+', '+ title_7 + ': ' + viii+', '+ title_8 + ': ' + ix+', '+ title_9 + ': ' + x+', '+ title_10 + ': ' + xi+', '+ title_11 + ': ' + xii+', '+ title_12 + ': ' + xiii+', '+ title_13 + ': ' + xiv)


if selected_no=='15':
    st.write('Please enter the name of each marker and select all fluorophores available for each marker ')
    title_0 = st.text_input('Marker', key=1)
    color_0=st.multiselect('Select fluorophores available for this marker', flat_list)

    title_1 = st.text_input('Marker', key=2)
    color_1=st.multiselect('Select fluorophores available for this marker', flat_list, key=20)

    title_2 = st.text_input('Marker', key=3)
    color_2=st.multiselect('Select fluorophores available for this marker', flat_list, key=21)

    title_3 = st.text_input('Marker', key=4)
    color_3=st.multiselect('Select fluorophores available for this marker', flat_list, key=22)

    title_4 = st.text_input('Marker', key=5)
    color_4=st.multiselect('Select fluorophores available for this marker', flat_list, key=23)

    title_5 = st.text_input('Marker', key=6)
    color_5=st.multiselect('Select fluorophores available for this marker', flat_list, key=24)

    title_6 = st.text_input('Marker', key=7)
    color_6=st.multiselect('Select fluorophores available for this marker', flat_list, key=25)

    title_7 = st.text_input('Marker', key=8)
    color_7=st.multiselect('Select fluorophores available for this marker', flat_list, key=26)

    title_8 = st.text_input('Marker', key=9)
    color_8=st.multiselect('Select fluorophores available for this marker', flat_list, key=27)

    title_9 = st.text_input('Marker', key=10)
    color_9=st.multiselect('Select fluorophores available for this marker', flat_list, key=28)

    title_10 = st.text_input('Marker', key=11)
    color_10=st.multiselect('Select fluorophores available for this marker', flat_list, key=29)

    title_11 = st.text_input('Marker', key=12)
    color_11=st.multiselect('Select fluorophores available for this marker', flat_list, key=30)

    title_12 = st.text_input('Marker', key=13)
    color_12=st.multiselect('Select fluorophores available for this marker', flat_list, key=31)

    title_13 = st.text_input('Marker', key=14)
    color_13=st.multiselect('Select fluorophores available for this marker', flat_list, key=32)

    title_14 = st.text_input('Marker', key=15)
    color_14=st.multiselect('Select fluorophores available for this marker', flat_list, key=33)

    st.subheader('''Overview of fluorophores you've selected for each marker''')
    if len(title_0)!=0:
        col_0 = ', '.join(color_0)
        st.write(title_0 + ': ' + col_0)

    if len(title_1)!=0:
        col_1 = ', '.join(color_1)
        st.write(title_1 + ': ' + col_1)

    if len(title_2)!=0:
        col_2 = ', '.join(color_2)
        st.write(title_2 + ': ' + col_2)

    if len(title_3)!=0:
        col_3 = ', '.join(color_3)
        st.write(title_3 + ': ' + col_3)

    if len(title_4)!=0:
        col_4 = ', '.join(color_4)
        st.write(title_4 + ': ' + col_4)

    if len(title_5)!=0:
        col_5 = ', '.join(color_5)
        st.write(title_5 + ': ' + col_5)

    if len(title_6)!=0:
        col_6 = ', '.join(color_6)
        st.write(title_6 + ': ' + col_6)

    if len(title_7)!=0:
        col_7 = ', '.join(color_7)
        st.write(title_7 + ': ' + col_7)

    if len(title_8)!=0:
        col_8 = ', '.join(color_8)
        st.write(title_8 + ': ' + col_8)

    if len(title_9)!=0:
        col_9 = ', '.join(color_9)
        st.write(title_9 + ': ' + col_9)

    if len(title_10)!=0:
        col_10 = ', '.join(color_10)
        st.write(title_10 + ': ' + col_10)

    if len(title_11)!=0:
        col_11 = ', '.join(color_11)
        st.write(title_11 + ': ' + col_11)

    if len(title_12)!=0:
        col_12 = ', '.join(color_12)
        st.write(title_12 + ': ' + col_12)
    
    if len(title_13)!=0:
        col_13 = ', '.join(color_13)
        st.write(title_13 + ': ' + col_13)

    if len(title_14)!=0:
        col_14 = ', '.join(color_14)
        st.write(title_14 + ': ' + col_14)


    if len(color_0)!=0:
        df_0 = flowcon_df[flowcon_df.isin(color_0)]
        df_0 = df_0.dropna(axis=1, how='all', inplace=False)
        df_0.columns.tolist()
  

        if len(color_1)!=0:
            df_1 = flowcon_df[flowcon_df.isin(color_1)]
            df_1 = df_1.dropna(axis=1, how='all', inplace=False)
            df_1.columns.tolist()



            if len(color_2)!=0:
                df_2 = flowcon_df[flowcon_df.isin(color_2)]
                df_2 = df_2.dropna(axis=1, how='all', inplace=False)
                df_2.columns.tolist()
   

                if len(color_3)!=0:
                    df_3 = flowcon_df[flowcon_df.isin(color_3)]
                    df_3 = df_3.dropna(axis=1, how='all', inplace=False)
                    df_3.columns.tolist()


                    if len(color_4)!=0:
                        df_4 = flowcon_df[flowcon_df.isin(color_4)]
                        df_4 = df_4.dropna(axis=1, how='all', inplace=False)
                        df_4.columns.tolist()


                        if len(color_5)!=0:
                            df_5 = flowcon_df[flowcon_df.isin(color_5)]
                            df_5 = df_5.dropna(axis=1, how='all', inplace=False)
                            df_5.columns.tolist()


                            if len(color_6)!=0:
                                df_6 = flowcon_df[flowcon_df.isin(color_6)]
                                df_6 = df_6.dropna(axis=1, how='all', inplace=False)
                                df_6.columns.tolist()

                                if len(color_7)!=0:
                                    df_7 = flowcon_df[flowcon_df.isin(color_7)]
                                    df_7 = df_7.dropna(axis=1, how='all', inplace=False)
                                    df_7.columns.tolist()


                                    if len(color_8)!=0:
                                        df_8 = flowcon_df[flowcon_df.isin(color_8)]
                                        df_8 = df_8.dropna(axis=1, how='all', inplace=False)
                                        df_8.columns.tolist()


                                        if len(color_9)!=0:
                                            df_9 = flowcon_df[flowcon_df.isin(color_9)]
                                            df_9 = df_9.dropna(axis=1, how='all', inplace=False)
                                            df_9.columns.tolist()


                                            if len(color_10)!=0:
                                                df_10 = flowcon_df[flowcon_df.isin(color_10)]
                                                df_10 = df_10.dropna(axis=1, how='all', inplace=False)
                                                df_10.columns.tolist()


                                                if len(color_11)!=0:
                                                    df_11 = flowcon_df[flowcon_df.isin(color_11)]
                                                    df_11 = df_11.dropna(axis=1, how='all', inplace=False)
                                                    df_11.columns.tolist()

                                                    if len(color_12)!=0:
                                                        df_12 = flowcon_df[flowcon_df.isin(color_12)]
                                                        df_12 = df_12.dropna(axis=1, how='all', inplace=False)
                                                        df_12.columns.tolist()


                                                        if len(color_13)!=0:
                                                            df_13 = flowcon_df[flowcon_df.isin(color_13)]
                                                            df_13 = df_13.dropna(axis=1, how='all', inplace=False)
                                                            df_13.columns.tolist()


                                                            if len(color_14)!=0:
                                                                df_14 = flowcon_df[flowcon_df.isin(color_14)]
                                                                df_14 = df_14.dropna(axis=1, how='all', inplace=False)
                                                                df_14.columns.tolist()



                                                                list=[]
                                                                for a in df_0:
                                                                    for b in df_1:
                                                                        for c in df_2:
                                                                            for d in df_3:
                                                                                for e in df_4:
                                                                                    for f in df_5:
                                                                                        for g in df_6:
                                                                                            for h in df_7:
                                                                                                for k in df_8:
                                                                                                    for l in df_9:
                                                                                                        for m in df_10:
                                                                                                            for n in df_11:
                                                                                                                for o in df_12:
                                                                                                                    for p in df_13:
                                                                                                                        for q in df_14:
                                                                                                                            cc=[a, b, c, d, e, f, g, h, k, l, m, n, o, p, q]
                                                                                                                            if(len(set(cc)) == len(cc)):
                                                                                                                                list.append(cc)
                                                                with st.spinner('🧑‍🔬 Wait for it...'):
                                                                    time.sleep(1)
                                                                st.success('🎉 Done!')                     
                                                                #st.write(list)                    
                                                                number=range(len(list))
                                                                st.subheader('Here are your flow panel options!')
                                                                
                                                                for j in number:
                                                                    cc0=flowcon_df[list[j][0]].tolist()
                                                                    cc1=flowcon_df[list[j][1]].tolist()
                                                                    cc2=flowcon_df[list[j][2]].tolist()
                                                                    cc3=flowcon_df[list[j][3]].tolist()
                                                                    cc4=flowcon_df[list[j][4]].tolist()
                                                                    cc5=flowcon_df[list[j][5]].tolist()
                                                                    cc6=flowcon_df[list[j][6]].tolist()
                                                                    cc7=flowcon_df[list[j][7]].tolist()
                                                                    cc8=flowcon_df[list[j][8]].tolist()
                                                                    cc9=flowcon_df[list[j][9]].tolist()
                                                                    cc10=flowcon_df[list[j][10]].tolist()
                                                                    cc11=flowcon_df[list[j][11]].tolist()
                                                                    cc12=flowcon_df[list[j][12]].tolist()
                                                                    cc13=flowcon_df[list[j][13]].tolist()
                                                                    cc14=flowcon_df[list[j][14]].tolist()

                                                                    for i in color_0:
                                                                        for ii in color_1:
                                                                            for iii in color_2:
                                                                                for iv in color_3:
                                                                                    for v in color_4:
                                                                                        for vi in color_5:
                                                                                            for vii in color_6:
                                                                                                for viii in color_7:
                                                                                                    for ix in color_8:
                                                                                                        for x in color_9:
                                                                                                            for xi in color_10:
                                                                                                                for xii in color_11:
                                                                                                                    for xiii in color_12:
                                                                                                                        for xiv in color_13:
                                                                                                                            for xv in color_14:
                                                                                                                                if i in cc0:
                                                                                                                                    if ii in cc1:
                                                                                                                                        if iii in cc2:
                                                                                                                                            if iv in cc3:
                                                                                                                                                if v in cc4:
                                                                                                                                                    if vi in cc5:
                                                                                                                                                        if vii in cc6:
                                                                                                                                                            if viii in cc7:
                                                                                                                                                                if ix in cc8:
                                                                                                                                                                    if x in cc9:
                                                                                                                                                                        if xi in cc10:
                                                                                                                                                                            if xii in cc11:
                                                                                                                                                                                if xiii in cc12:
                                                                                                                                                                                    if xiv in cc13:
                                                                                                                                                                                        if xv in cc14:
                                                                                                                                                                                            print('')
                                                                                                                                                                                            st.write('👉 '+title_0 + ': ' + i+', '+ title_1 + ': ' + ii+', '+ title_2 + ': ' + iii+', '+ title_3 + ': ' + iv+', '+ title_4 + ': ' + v+', '+ title_5 + ': ' + vi+', '+ title_6 + ': ' + vii+', '+ title_7 + ': ' + viii+', '+ title_8 + ': ' + ix+', '+ title_9 + ': ' + x+', '+ title_10 + ': ' + xi+', '+ title_11 + ': ' + xii+', '+ title_12 + ': ' + xiii+', '+ title_13 + ': ' + xiv+', '+ title_14 + ': ' + xv)




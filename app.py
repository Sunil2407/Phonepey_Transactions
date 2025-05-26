# Importing Libraries
import pandas as pd
import mysql.connector as mysql
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit as st
import seaborn as sns


#Streamlit App Configuration
st.set_page_config(page_title= "Phonepe Transaction",
                   page_icon= "random",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created by *sunil*!
                                        Data has been cloned from Phonepe Pulse Github Repo"""})

#Connecting to MySQL Database

mydb = mysql.connect(
  user  = "newuser",
  password = "Apps@5566",
  host = 'localhost',
  database = "phonepetransaction"
)

# Create a cursor()

cursor = mydb.cursor()

# Navigation Menu (Horizontal Tabs)
SELECT = option_menu(
    menu_title=None,
    options=["Promotion", "Basic insights", "Contact"],
    icons=["bar-chart", "toggles", "at"],
    default_index=2,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white", "size": "cover"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}
    }

)

#Promotion Tab Content
video_url = 'https://www.phonepe.com/webstatic/5988/videos/page/home-fast-secure-v3.mp4'

if SELECT == "Promotion":
    st.markdown("[PhonePe Website](https://www.phonepe.com/)", unsafe_allow_html=True)
    # Display the video
    st.video(video_url,format='video/mp4')



# Contact Tab – Your Profile
name = "Sunil Kumar G T"
mail = "sunilkumar14.gts@gmail.com"
profile_picture_url = "https://media.licdn.com/dms/image/v2/C5616AQHbp6bKjfjusA/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1662612557724?e=1752710400&v=beta&t=VbGz_nSKus5QM0akYhO-W4ZHe31WloXpKyHvw_5WjR4"  
linkedin_url = "https://in.linkedin.com/in/sunil-kumar-245312197"
github_url = "https://github.com/Sunil2407"

if SELECT == "Contact":
    col1, col2 = st.columns(2)

    # Display profile picture in the center column
    with col1:
        st.image(profile_picture_url, caption="My Profile Picture", use_column_width=True)

   
    # Right column with personal details
    with col2:
        st.title(name)
        st.title(mail)
        st.subheader("An Aspiring DATA-SCIENTIST.... !")

        # Social media links
        st.write(f"[LinkedIn]({linkedin_url})")
        st.write(f"[GitHub]({github_url})")




# Basic Insights Tab – Core Data Visualization

if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--", "Top 10 Transactions by Amount",
               "Bottom 10 Transactions by Amount",
               "Top 10 Mobile Brands by Average User Percentage",
               "Top 10 Districts by Transaction Count",
               "Yearly User Registrations per State",
               "Transaction Trends by Type (e.g., Recharge, Bill Payment, etc.)",
               "Top 10 transactions_type based on states and transaction_amount",
               "Total Insurance Amount and Policies per State"]
    select = st.selectbox("Select the option", options)

    if select == "Top 10 Transactions by Amount":
    
        # Execute the SQL query
        cursor.execute("""
            SELECT DISTINCT State, Transaction_amount, Year, Quarter 
            FROM toptransaction 
            ORDER BY Transaction_amount DESC 
            LIMIT 10;
        """)
        
        # Fetch data
        rows = cursor.fetchall()
        
        # Debug: show raw data
        st.write("Raw fetched rows:", rows)
        
        # Create DataFrame
        df = pd.DataFrame(rows, columns=['State', 'Transaction_Amount', 'Year', 'Quarter'])
        
        # Display the DataFrame
        st.write("Top 10 Transactions by Amount")
        st.dataframe(df)
        
        # Ensure numeric conversion
        df['Transaction_Amount'] = pd.to_numeric(df['Transaction_Amount'], errors='coerce')
        
        # Plotly Bar Chart
        fig = px.bar(df, 
                     x='State', 
                     y='Transaction_Amount', 
                     color='Year',
                     title='Top 10 Transactions by Amount',
                     labels={'Transaction_Amount': 'Transaction Amount'},
                     hover_data=['Quarter'])
        st.plotly_chart(fig)
        
        # Seaborn Chart
        plt.figure(figsize=(12, 6))
        sns.barplot(x='State', y='Transaction_Amount', hue='Year', data=df)
        plt.title('Top 10 Transactions by Amount')
        plt.xlabel('State')
        plt.ylabel('Transaction Amount')
        st.pyplot(plt)
    #_______________________________________________________________________________________            
    elif select == "Bottom 10 Transactions by Amount":
        # Execute SQL query
        cursor.execute("""
            SELECT State, Transaction_amount, Year, Quarter 
            FROM aggregatetransaction 
            ORDER BY Transaction_amount ASC 
            LIMIT 10;
        """)
    
        # Fetch data
        rows = cursor.fetchall()
    
        # Debug: show raw data
        st.write("Raw fetched rows:", rows)
    
        # Create DataFrame
        df = pd.DataFrame(rows, columns=['State', 'Transaction_Amount', 'Year', 'Quarter'])
    
        # Display the data in a table
        st.write("Bottom 10 Transactions by Amount")
        st.dataframe(df)
    
        # Ensure numeric data type
        df['Transaction_Amount'] = pd.to_numeric(df['Transaction_Amount'], errors='coerce')
    
        # Plotly Bar Chart
        fig = px.bar(df, 
                     x='State', 
                     y='Transaction_Amount', 
                     color='Year',
                     title='Bottom 10 Transactions by Amount',
                     labels={'Transaction_Amount': 'Transaction Amount'},
                     hover_data=['Quarter'])
        st.plotly_chart(fig)
    
        # Seaborn Bar Plot
        plt.figure(figsize=(12, 6))
        sns.barplot(x='State', y='Transaction_Amount', hue='Year', data=df)
        plt.title('Bottom 10 Transactions by Amount')
        plt.xlabel('State')
        plt.ylabel('Transaction Amount')
        st.pyplot(plt)
        
        

    #_______________________________________________________________________________________            
    elif select == "Top 10 Mobile Brands by Average User Percentage":
        
        # Execute SQL query
        cursor.execute("""
            SELECT Brand_Name, AVG(User_Percentage) AS Avg_Percentage 
            FROM aggregateusers 
            GROUP BY Brand_Name 
            ORDER BY Avg_Percentage DESC 
            LIMIT 10;
        """)
    
        # Fetch data
        rows = cursor.fetchall()
    
        # Debug: show raw data
        st.write("Raw fetched rows:", rows)
    
        # Create DataFrame
        df = pd.DataFrame(rows, columns=['Brand_Name', 'Avg_Percentage'])
    
        # Display the data
        st.write("Top 10 Mobile Brands by Average User Percentage")
        st.dataframe(df)
    
        # Ensure numeric type
        df['Avg_Percentage'] = pd.to_numeric(df['Avg_Percentage'], errors='coerce')
    
        # Plotly Bar Chart
        fig = px.bar(df, 
                     x='Brand_Name', 
                     y='Avg_Percentage',
                     title='Top 10 Mobile Brands by Average User Percentage',
                     labels={'Avg_Percentage': 'Average User Percentage'},
                     color='Avg_Percentage',
                     color_continuous_scale='Viridis')
        st.plotly_chart(fig)
    
        # Seaborn Bar Plot
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Brand_Name', y='Avg_Percentage', data=df, palette='viridis')
        plt.title('Top 10 Mobile Brands by Average User Percentage')
        plt.xlabel('Brand Name')
        plt.ylabel('Average User Percentage')
        plt.xticks(rotation=45)
        st.pyplot(plt)
    
    #_______________________________________________________________________________________
    elif select == "Top 10 Districts by Transaction Count":
        # Execute the query
        cursor.execute("""
            SELECT State, District,
                   SUM(Transaction_Count) AS Total_Transactions
            FROM toptransaction
            GROUP BY State, District
            ORDER BY Total_Transactions DESC
            LIMIT 10;
        """)
        
        # Fetch data
        rows = cursor.fetchall()
        
        # Debug: show raw data
        st.write("Raw fetched rows:", rows)
        
        # Create DataFrame
        df = pd.DataFrame(rows, columns=['State', 'District', 'Total_Transactions'])
    
        # Display the DataFrame
        st.write("Top 10 Districts by Transaction Count")
        st.dataframe(df)
    
        # Ensure numeric type
        df['Total_Transactions'] = pd.to_numeric(df['Total_Transactions'], errors='coerce')
    
        # Plotly visualization
        fig = px.bar(df, x='District', y='Total_Transactions', color='State',
                     title='Top 10 Districts by Transaction Count',
                     labels={'Total_Transactions': 'Transaction Count'})
        st.plotly_chart(fig)
    
        # Seaborn visualization
        plt.figure(figsize=(12, 6))
        sns.barplot(x='District', y='Total_Transactions', hue='State', data=df)
        plt.title('Top 10 Districts by Transaction Count')
        plt.xlabel('District')
        plt.ylabel('Transaction Count')
        st.pyplot(plt)
    
    #_______________________________________________________________________________________
    elif select == "Transaction Trends by Type (e.g., Recharge, Bill Payment, etc.)":
        cursor.execute(
            "SELECT distinct Transaction_type, Transaction_amount FROM aggregatetransaction GROUP BY Transaction_amount, Transaction_type;")
        df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_type', 'Transaction_amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Transaction Trends by Type (e.g., Recharge, Bill Payment, etc.)")
            fig = px.bar(df, x="Transaction_type", y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)
 #_______________________________________________________________________________________
    elif select == "Yearly User Registrations per State":
    # Execute the query
        cursor.execute("""
            SELECT 
                State,
                Year,
                SUM(User_Count) AS Yearly_Registrations
            FROM aggregateusers
            GROUP BY State, Year
            ORDER BY State, Year;
        """)
        
        # Fetch data
        rows = cursor.fetchall()
        
        # Debug print
        st.write("Raw fetched rows:", rows)
        
        # Create DataFrame
        df = pd.DataFrame(rows, columns=['State', 'Year', 'Yearly_Registrations'])
    
        # Display data
        st.write("Yearly User Registrations per State")
        st.dataframe(df)
    
        # Ensure numeric conversion
        df['Yearly_Registrations'] = pd.to_numeric(df['Yearly_Registrations'], errors='coerce')
    
        # Plotly visualization
        fig = px.bar(df, x='Year', y='Yearly_Registrations', color='State',
                     barmode='group',
                     title='Yearly User Registrations per State',
                     labels={'Yearly_Registrations': 'User Count'})
        st.plotly_chart(fig)
    
        # Seaborn visualization
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Year', y='Yearly_Registrations', hue='State', data=df)
        plt.title('Yearly User Registrations per State')
        plt.xlabel('Year')
        plt.ylabel('User Count')
        st.pyplot(plt)
    #_______________________________________________________________________________________
    elif select == "Top 10 transactions_type based on states and transaction_amount":
        cursor.execute(
            "SELECT DISTINCT State,Transaction_type,Transaction_amount FROM aggregatetransaction ORDER BY Transaction_amount DESC LIMIT 10;")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Transaction_type', 'Transaction_amount'])
        
        col1, col2 = st.columns(2)
        with col1:
           st.write(df)
        with col2:
            # Simple Bar Chart
            st.title("Top 10 transactions_type based on states and transaction_amount")
            fig = px.bar(df, x="State", y="Transaction_amount", color="Transaction_type", title="Top 10 transactions_type based on states and transaction_amount")
            st.plotly_chart(fig, use_container_width=True)
    #______________________________________________________________________________________
    elif select == "Total Insurance Amount and Policies per State":
        # Execute the SQL query
        cursor.execute("""
                SELECT State,
                       ROUND(SUM(Insurance_Amount)) AS Total_Insurance_Amount,
                       SUM(Insurance_Count) AS Total_Policies
                FROM aggregateinsurance
                GROUP BY State
                ORDER BY Total_Insurance_Amount DESC;
            """)
            
        # Fetch data
        rows = cursor.fetchall()
        
        # Show raw data for debugging
        st.write("Raw fetched rows:", rows)
    
        # Create DataFrame
        df = pd.DataFrame(rows, columns=['State', 'Total_Insurance_Amount', 'Total_Policies'])
    
        # Display DataFrame in Streamlit
        st.write("Total Insurance Amount and Policies per State")
        st.dataframe(df)
    
        # Ensure numeric types
        df['Total_Insurance_Amount'] = pd.to_numeric(df['Total_Insurance_Amount'], errors='coerce')
        df['Total_Policies'] = pd.to_numeric(df['Total_Policies'], errors='coerce')
    
        # Plotly Bar Chart for Total Insurance Amount
        fig1 = px.bar(df, x='State', y='Total_Insurance_Amount',
                      title='Total Insurance Amount by State',
                      labels={'Total_Insurance_Amount': 'Insurance Amount'},
                      color='Total_Insurance_Amount',
                      color_continuous_scale='Blues')
        st.plotly_chart(fig1)
    
        # Plotly Bar Chart for Total Policies
        fig2 = px.bar(df, x='State', y='Total_Policies',
                      title='Total Insurance Policies by State',
                      labels={'Total_Policies': 'Policy Count'},
                      color='Total_Policies',
                      color_continuous_scale='Purples')
        st.plotly_chart(fig2)
    
        # Seaborn Bar Plot (Optional)
        plt.figure(figsize=(12, 6))
        sns.barplot(x='State', y='Total_Insurance_Amount', data=df)
        plt.xticks(rotation=45)
        plt.title('Total Insurance Amount by State')
        plt.xlabel('State')
        plt.ylabel('Insurance Amount')
        st.pyplot(plt)
   
   
   
       
       
    

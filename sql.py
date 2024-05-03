from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
import sqlite3

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content([question, prompt[0]])
    return response.text

def read_sql_query(sql, db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = [
    """
        You are an expert in converting English questions to SQL code!
        The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
        SECTION \n\nFor example, \nExample 1 - How many entries of records are present?,
        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
        \nExample 2 - How many students study in Data Science class?,
        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT where CLASS="Data Science";
        also the sql code should not have in beginning or end and sql word in output
    """
]


st.set_page_config(page_title="I can Retriever Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("input: ", key="input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
#!/usr/bin/env python
# coding: utf-8

# In[1]:
import streamlit as st
import functions
import time

todos = functions.get_todos()
complete = functions.get_completed()

def add_todo():
    newtodo = st.session_state["new_todo"] + "\n"
    todos.append(newtodo)
    functions.write_file(todos,'todolist.txt')

st.title("Tappy")
st.subheader("- the only todo app you will need")
st.write('Keep track of your tasks')

#giveeachtodoauniquekeybyusingindex
for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key={i})
    #if checkbox = true
    if checkbox:
        complete.append(todos.pop(i))
        functions.write_complete(complete)
        functions.write_file(todos)
        del st.session_state[{i}]
        st.experimental_rerun()

st.text_input(label="", placeholder='Add new task',
              on_change=add_todo,key="new_todo")

st.write('Completed items:')
completed = st.empty()
for todo in complete:
    st.write('- ' + time.strftime('%d-%m-%Y')+ ' '+ todo)


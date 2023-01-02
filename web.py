import streamlit as st
import function as func

def add_todo():
    todo = st.session_state["todos"] +"\n"
    todos = func.gettodo()
    todos.append(todo)
    func.writetodo(todos)
    st.session_state["todos"]=" "

st.title("My Todo App")
st.subheader("made by rishabh sharawat")
st.write("simple write")
todos = func.gettodo()
for index,todo in enumerate (todos):
    check=st.checkbox(todo,key=todo)
    if check:
         todos.pop(index)
         func.writetodo(todos)
         del st.session_state[todo]
         st.experimental_rerun()


st.text_input(label=" ", placeholder="Add Todo",on_change= add_todo ,key="todos")

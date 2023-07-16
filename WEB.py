import streamlit as st
import functions



todos = functions.get()
def add():
    todo=st.session_state["new"]+"\n"
    todos.append(todo)
    functions.write(todos)


st.title("My Todo App")
st.subheader("Made by Pranav Sharma")
st.write("Your Todos")


for index,to in enumerate(todos):
    checkbox=st.checkbox(to,key=to)
    if checkbox:
        todos.pop(index)
        functions.write(todos)
        del st.session_state[to]
        st._rerun()

st.text_input(label="",placeholder="Add new Todo..",
              on_change=add, key="new")
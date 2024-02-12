import streamlit as st
import functions
todos = functions.get_car_name_func()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_car_name_func(todos)
    st.session_state["new_todo"] = ""


    print(todo)


st.title("My todo app")
st.subheader("this is my todo app")
st.write("this app is to increase my productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=f"{todo}-{index}")
    if checkbox:
        todos.pop(index)
        functions.write_car_name_func(todos)
        del st.session_state[f"{todo}-{index}"]
        st.rerun()



st.text_input(label="Enter something below:", placeholder="Add a new todo..",
              on_change=add_todo,key="new_todo")
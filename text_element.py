import streamlit as st
import os 


st.title("Simple Title")
st.header("This is a header")
st.subheader("Subheader")
st.markdown("This is _Markdown")
st.caption("small text")

code_sample = """
def sum(a,b):
  return a+b
"""
st.code(code_sample, language="python")
code_java = """
public static void main(String[] args){
  System.out.println("Hello Java");
}
"""
st.code(code_java, language="java")

st.button("Click me")

st.divider()

st.image(os.path.join(os.getcwd(), "static", "image.png"))

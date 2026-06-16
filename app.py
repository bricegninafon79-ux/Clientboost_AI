menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Sales Message", "Marketing Content", "Follow-Up", "Pricing"]
)

st.session_state.generated = False

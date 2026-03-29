import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Coffee Shop", layout="wide")

# -------------------------
# SESSION STATE (CART)
# -------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>
.stApp {
    background-color: #2b1a12;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    padding: 15px 40px;
    color: white;
}

/* Hero */
.title {
    font-size: 60px;
    font-weight: bold;
}
.yellow { color: #f4b400; }
.white { color: white; }

/* Cards */
.card {
    background-color: #3b2418;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    color: white;
}

/* Button */
.stButton>button {
    background-color: white;
    color: black;
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# NAVBAR
# -------------------------
st.markdown("""
<div class="navbar">
    <div><b>BREWLAB</b></div>
    <div>Home &nbsp;&nbsp; Menu &nbsp;&nbsp; Cart</div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# HERO SECTION
# -------------------------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    <div class="title">
        <span class="yellow">COFFEE</span><br>
        <span class="white">LIFE'S BEGINNING</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://images.pexels.com/photos/374885/pexels-photo-374885.jpeg")

# -------------------------
# MENU DATA
# -------------------------
menu = [
    {"name": "Espresso", "price": 2.5, "img": "https://images.pexels.com/photos/414645/pexels-photo-414645.jpeg"},
    {"name": "Latte", "price": 3.5, "img": "https://images.pexels.com/photos/312418/pexels-photo-312418.jpeg"},
    {"name": "Cappuccino", "price": 3.0, "img": "https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg"},
    {"name": "Americano", "price": 2.0, "img": "https://images.pexels.com/photos/374885/pexels-photo-374885.jpeg"}
]

# -------------------------
# MENU SECTION
# -------------------------
st.markdown("## ☕ Our Coffee")

cols = st.columns(4)

for i, item in enumerate(menu):
    with cols[i]:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.image(item["img"], use_container_width=True)
        st.markdown(f"### {item['name']}")
        st.write(f"${item['price']}")

        if st.button("Add to Cart", key=f"add_{i}"):
            st.session_state.cart.append(item)
            st.success(f"{item['name']} added!")

        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# CART SECTION
# -------------------------
st.markdown("## 🛒 Your Cart")

if not st.session_state.cart:
    st.warning("Cart is empty")
else:
    total = 0

    for i, item in enumerate(st.session_state.cart):
        col1, col2, col3 = st.columns([3,2,1])

        with col1:
            st.write(item["name"])

        with col2:
            st.write(f"${item['price']}")

        with col3:
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()

        total += item["price"]

    st.markdown(f"## 💰 Total: ${total}")

    if st.button("Checkout"):
        st.success("🎉 Order Confirmed!")
        st.session_state.cart.clear()
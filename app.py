import streamlit as st
import time

# ==========================================
# --- PAGE CONFIGURATION ---
# ==========================================
st.set_page_config(
    page_title="ClientBoost AI v2",
    page_icon="🚀",
    layout="centered"
)

# ==========================================
# --- INITIALIZE SESSION STATE ---
# ==========================================
if "step" not in st.session_state:
    st.session_state.step = 1
if "selected_pain" not in st.session_state:
    st.session_state.selected_pain = None
if "selected_plan" not in st.session_state:
    st.session_state.selected_plan = None
if "payment_done" not in st.session_state:
    st.session_state.payment_done = False

# ==========================================
# --- STEP 1: HOME & MOTIVATION ---
# ==========================================
if st.session_state.step == 1:
    st.title("🚀 ClientBoost AI v2")
    
    st.markdown("""
    ### Turn cold prospects into loyal customers.
    **ClientBoost AI** analyzes the specific pain points of your target audience to generate high-converting outreach messages and marketing copy. No more spending hours looking for the right words: our AI handles it for you.
    """)
    
    st.success("💡 *The success of a sale doesn't depend on what you sell, but on how you solve your customer's problem. Take action today!*")
    
    st.divider()
    
    if st.button("Start analyzing your business ➔", type="primary", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# ==========================================
# --- STEP 2: DIAGNOSTIC (PROBLEM SELECTION) ---
# ==========================================
elif st.session_state.step == 2:
    st.title("🎯 Step 2: What is your biggest challenge?")
    st.write("Select the primary problem your business currently faces to guide the AI.")
    
    pains = [
        "I can't seem to find qualified clients.",
        "My email conversion rate is too low.",
        "My sales pages are not converting enough.",
        "I spend too much time writing prospecting messages."
    ]
    
    default_index = pains.index(st.session_state.selected_pain) if st.session_state.selected_pain in pains else 0
    selected = st.radio("Choose your main challenge:", pains, index=default_index)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back to Home", use_container_width=True):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("Continue to Plans ➔", type="primary", use_container_width=True):
            st.session_state.selected_pain = selected
            st.session_state.step = 3
            st.rerun()

# ==========================================
# --- STEP 3: PLAN SELECTION & PAYMENT (PAYWALL) ---
# ==========================================
elif st.session_state.step == 3:
    st.title("💳 Step 3: Choose your plan")
    st.caption(f"🎯 Targeted Problem: {st.session_state.selected_pain}")
    st.info("Unlock access to AI content generation by choosing one of our plans below.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🥉 Basic")
        st.subheader("$9 / mo")
        st.write("• 5 generations / month")
        st.write("• Standard support")
        if st.button("Choose Basic", key="btn_basic", use_container_width=True):
            st.session_state.selected_plan = "Basic"
            st.session_state.payment_done = True
            
    with col2:
        st.markdown("### 🥈 Premium")
        st.subheader("$29 / mo")
        st.write("• Unlimited generations")
        st.write("• Access to new models")
        if st.button("🔥 Choose Premium", key="btn_premium", use_container_width=True):
            st.session_state.selected_plan = "Premium"
            st.session_state.payment_done = True
            
    with col3:
        st.markdown("### 🥇 Ultra")
        st.subheader("$49 / mo")
        st.write("• Team & Collaboration")
        st.write("• 24/7 VIP Support")
        if st.button("Choose Ultra", key="btn_ultra", use_container_width=True):
            st.session_state.selected_plan = "Ultra"
            st.session_state.payment_done = True

    st.divider()
    
    if st.session_state.payment_done:
        st.success(f"✅ Payment simulated successfully for the **{st.session_state.selected_plan}** plan!")
        if st.button("Access Product Description ➔", type="primary", use_container_width=True):
            st.session_state.step = 4
            st.rerun()
            
    if st.button("⬅ Back", key="back_to_2"):
        st.session_state.step = 2
        st.session_state.payment_done = False 
        st.rerun()

# ==========================================
# --- STEP 4: DESCRIPTION & CUSTOM GENERATION ---
# ==========================================
elif st.session_state.step == 4:
    st.title("✍️ Step 4: Create your campaign with AI")
    st.caption(f"Active Plan: **{st.session_state.selected_plan}** | Solving Problem: *{st.session_state.selected_pain}*")
    
    st.subheader("Describe your product or service")
    product_desc = st.text_area(
        "Briefly explain what you sell and who it is for:", 
        placeholder="E.g., An online course for freelancers who want to double their rates...",
        height=120
    )
    
    if st.button("✨ Generate My Marketing Copy", type="primary", use_container_width=True):
        if product_desc.strip() == "":
            st.warning("⚠️ Please enter a description before generating.")
        else:
            with st.spinner("🔮 AI is applying the best psychological strategy for your problem..."):
                time.sleep(2) 
                
                st.success("🎉 Here is the strategic solution generated by the AI:")
                
                # --- STRATEGIC LOGIC BASED ON THE CHOSEN PROBLEM ---
                if st.session_state.selected_pain == "I can't seem to find qualified clients.":
                    st.info("💡 **AI Strategy Activated:** Lead Generation & Qualification Framework.")
                    st.markdown(f"""
                    ### 🎯 Your Client Attraction Sequence
                    * **The Magnetic Hook:** \"Stop chasing window shoppers. If you are tired of spending hours on the phone with people who don't have the budget, here is how to flip the script.\"
                    * **The Value Angle:** Thanks to **{product_desc}**, you won't have to chase leads anymore: ideal clients will apply to work with you.
                    * **Immediate Action Plan:** Filter your requests from the very start with a quick 3-question qualification survey.
                    """)
                    
                elif st.session_state.selected_pain == "My email conversion rate is too low.":
                    st.info("💡 **AI Strategy Activated:** Curiosity Psychology & Follow-up (PAS Framework).")
                    st.markdown(f"""
                    ### 📧 Your High-Open-Rate Subject Lines & Email Structure
                    * **Recommended Subject Lines (Run an A/B test):** 
                      1. *« The invisible problem killing your results... »*
                      2. *« {product_desc} (What no one is telling you) »*
                    * **The Body Copy (Narrative Hook):** « Do your emails end up in the 'Promotions' tab or worse, get deleted within 2 seconds? That's because they lack dramatic tension. »
                    * **The Transition:** That is exactly why we built an approach around **{product_desc}** to rebuild that connection from the very first line.
                    """)
                    
                elif st.session_state.selected_pain == "My sales pages are not converting enough.":
                    st.info("💡 **AI Strategy Activated:** AIDA Restructuring (Attention, Interest, Desire, Action) + Friction Reduction.")
                    st.markdown(f"""
                    ### ⚡ Your Main Headline Structure (Hero Section)
                    * **The Hook Headline:** « Don't change your product. Change the story you tell on your page. »
                    * **The Subheadline:** Discover how **{product_desc}** eliminates your visitors' objections before they even reach the buy button.
                    * **Urgent Trust Element to Add:** Implement a 14-day \"Money-Back Guarantee\" right under your pricing to break down the final psychological barrier.
                    """)
                    
                elif st.session_state.selected_pain == "I spend too much time writing prospecting messages.":
                    st.info("💡 **AI Strategy Activated:** Automation & Ultra-short Script (Cold Outreach).")
                    st.markdown(f"""
                    ### ✉️ Your Direct Prospecting Script (LinkedIn / DM)
                    * **Golden Rule:** Under 150 words. Nobody reads walls of text.
                    * **Ready-to-send Message:**
                    > « Hello [First Name], I see you are scaling your business. Often, the most time-consuming part is finding the right messaging. We developed **{product_desc}** to automate this process while keeping it 100% human. Would a 2-minute demo catch your eye this week? »
                    """)

    st.divider()
    
    # --- FOOTER & AUTHOR SIGNATURE ---
    st.caption("Made with ❤️ by **kēllønę🔗💨**")
    
    if st.button("🔄 Restart From Beginning", key="reset_flow", use_container_width=True):
        st.session_state.step = 1
        st.session_state.selected_pain = None
        st.session_state.selected_plan = None
        st.session_state.payment_done = False
        st.rerun()
    

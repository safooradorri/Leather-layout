
import streamlit as st
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(page_title="بهینه‌سازی برش چرم")
st.title("ابزار بهینه‌سازی برش چرم برای کمربند")

st.sidebar.header("ورودی‌ها")
leather_length = st.sidebar.number_input("طول چرم (متر)", min_value=0.1, value=1.5, step=0.1)
leather_width = st.sidebar.number_input("عرض چرم (متر)", min_value=0.1, value=0.5, step=0.1)
belt_length = st.sidebar.number_input("طول کمربند (متر)", min_value=0.05, value=1.0, step=0.05)
belt_width = st.sidebar.number_input("عرض کمربند (متر)", min_value=0.01, value=0.05, step=0.01)

if st.sidebar.button("محاسبه و نمایش الگو"):
    leather_length_cm = leather_length * 100
    leather_width_cm = leather_width * 100
    belt_length_cm = belt_length * 100
    belt_width_cm = belt_width * 100

    belts_per_row = math.floor(leather_length_cm / belt_length_cm)
    rows = math.floor(leather_width_cm / belt_width_cm)
    total_belts = belts_per_row * rows

    used_area = total_belts * belt_length_cm * belt_width_cm
    total_area = leather_length_cm * leather_width_cm
    waste = total_area - used_area
    waste_percent = (waste / total_area) * 100

    st.success(f"تعداد کمربند قابل تولید: {total_belts}")
    st.info(f"ضایعات چرم: {waste_percent:.2f}%")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, leather_length_cm)
    ax.set_ylim(0, leather_width_cm)
    ax.set_title("چینش کمربندها روی چرم")
    ax.set_aspect('equal')

    for i in range(belts_per_row):
        for j in range(rows):
            rect = patches.Rectangle((i * belt_length_cm, j * belt_width_cm), belt_length_cm, belt_width_cm, linewidth=1, edgecolor='black', facecolor='saddlebrown')
            ax.add_patch(rect)

    st.pyplot(fig)

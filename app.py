import streamlit as st
import streamlit.components.v1 as components
import json

profiles = [
    {
        "id": 1,
        "name": "Ram Charan",
        "age": 38,
        "profession": "Actor & Entrepreneur",
        "interests": ["Dancing", "Horse Riding", "Philanthropy"],
        "gallery": ["https://www.telugu360.com/wp-content/uploads/2019/01/img_3539.jpg",
                    "https://th.bing.com/th/id/OSK.HERO7I7N5E_Qap6D6w4ctB-_qYOIa_g3duSGjdB-2_8XBwE?w=312&h=200&c=7&rs=1&o=6&dpr=1.3&pid=SANGAM",
                    "https://i.pinimg.com/736x/6e/a9/3f/6ea93fb2e9a523edb5c5ad9d21588771.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 2,
        "name": "Samantha Ruth",
        "age": 35,
        "profession": "Actress & Businesswoman",
        "interests": ["Yoga", "Traveling", "Animal Welfare"],
        "gallery": ["https://www.masala.com/cloud/2023/01/07/samantha_ruth_prabhu_1651131556235_1651131568960.jpg","https://th.bing.com/th/id/OIP.VrtSCm5Epk-D-Ux76GJs8wHaKa?w=208&h=293&c=7&r=0&o=5&cb=iwc2&dpr=1.3&pid=1.7","https://th.bing.com/th/id/OIP.hjS-6IwGyBvprJeXzdp2HwHaKM?w=208&h=286&c=7&r=0&o=5&cb=iwc2&dpr=1.3&pid=1.7"],
        "hasLikedYou": False
    },
    {
        "id": 3,
        "name": "Prabhas",
        "age": 43,
        "profession": "Actor",
        "interests": ["Bodybuilding", "Motorcycles", "Philanthropy"],
        "gallery": ["https://i.pinimg.com/736x/df/a6/07/dfa607d11a8e7f1a12ad361374131f94.jpg","https://i.pinimg.com/736x/50/26/0d/50260d895950667c5997930d1335b55b.jpg","https://i.pinimg.com/736x/36/30/30/363030c5d947bcd32dc24e0d71bfe908.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 4,
        "name": "Allu Arjun",
        "age": 41,
        "profession": "Actor, Dancer",
        "interests": ["Street Dance", "Fashion", "Charity Work"],
        "gallery": ["https://i.pinimg.com/736x/7b/47/11/7b4711b2a3fd733dda520c96874f8711.jpg","https://i.pinimg.com/736x/24/33/be/2433be168931c4f49231c4a60db06026.jpg","https://i.pinimg.com/736x/7d/37/97/7d37973dff97b2f3e1708b44bfafe527.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 5,
        "name": "Rashmika Mandanna",
        "age": 27,
        "profession": "Actress",
        "interests": ["Reading", "Cooking", "Social Media"],
        "gallery": ["https://tse3.mm.bing.net/th/id/OIP.0tKc3DqwwGpGjer45uJPmgHaFj?cb=iwc2&rs=1&pid=ImgDetMain","https://i.pinimg.com/736x/1c/f4/13/1cf413cd3f4fdf5cd3b9b7013ecdd56a.jpg","https://i.pinimg.com/736x/3e/90/d2/3e90d2d0b8b7ec56cb61988a3bd6acc8.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 6,
        "name": "N.T. Rama Rao Jr.",
        "age": 40,
        "profession": "Actor & Producer",
        "interests": ["Politics", "Cricket", "Fitness"],
        "gallery": ["https://img.mensxp.com/media/content/2022/Jan/19_61deb81182673.jpeg","https://i.pinimg.com/736x/5b/81/54/5b81545985a9027df4f55a8f6aad3f42.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 7,
        "name": "Pooja Hegde",
        "age": 32,
        "profession": "Actress & Model",
        "interests": ["Dancing", "Fashion Design", "Travel Vlogging"],
        "gallery": ["https://th.bing.com/th/id/OIP.pROIziBMf7wGDIXSkGLv8QHaJQ?w=208&h=260&c=7&r=0&o=5&cb=iwc2&dpr=1.3&pid=1.7","https://i.pinimg.com/736x/8f/e0/ef/8fe0ef712369883e691b44f13286ce41.jpg","https://i.pinimg.com/736x/b5/62/75/b56275484c99fbe88c0b5b41177d4357.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 8,
        "name": "Deepika Padukone",
        "age": 38,
        "profession": "Actress & Producer",
        "interests": ["Mental Health", "Traveling", "Dancing"],
        "gallery": ["https://th.bing.com/th/id/OSK.hX02dlzisMEP05l3zGOV-cLzkB8uTTr0DJy2X6FTLvc?w=200&h=200&c=7&rs=1&o=6&dpr=1.3&pid=SANGAM","https://i.pinimg.com/736x/72/15/50/7215505d0b071145703ccf4135be0d07.jpg"],
        "hasLikedYou": False
    },
    {
        "id": 9,
        "name": "Virat Kohli",
        "age": 36,
        "profession": "Cricketer & Entrepreneur",
        "interests": ["Fitness", "Cars", "Animal Welfare"],
        "gallery": ["https://i.pinimg.com/736x/e9/39/9a/e9399a266a22ea71db9794a69433faa8.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 10,
        "name": "Alia Bhatt",
        "age": 32,
        "profession": "Actress & Singer",
        "interests": ["Singing", "Writing", "Nature"],
        "gallery": ["https://th.bing.com/th/id/OSK.pW8G4FdYTLAkqmV_a3jzjooY8gZz29RItmSNlmnwJds?w=224&h=200&c=12&rs=1&o=6&dpr=1.3&pid=SANGAM","https://i.pinimg.com/736x/21/29/7a/21297a5420992bb436c6e94eb0b99029.jpg","https://i.pinimg.com/736x/24/58/00/245800117e9aafdc4cc6788989dc0739.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 11,
        "name": "Mahesh Babu",
        "age": 45,
        "profession": "Actor & Philanthropist",
        "interests": ["Health Initiatives", "Fitness", "Movies"],
        "gallery": ["https://i.pinimg.com/736x/1c/23/bb/1c23bb6b2a316db401837508198d6e7c.jpg",
                    "https://i.pinimg.com/736x/9b/14/45/9b1445763e31004ce012207696bf345d.jpg",
                    "https://i.pinimg.com/736x/14/18/4b/14184b36f7151f0668fa365c55b61204.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 12,
        "name": "Kriti Sanon",
        "age": 34,
        "profession": "Actress & Poet",
        "interests": ["Poetry", "Dancing", "Fashion"],
        "gallery": ["https://th.bing.com/th/id/OSK.1ymdqFRYcHYpHTUccQAORS5o_BZIj_73pbauXxiJkQo?w=224&h=200&c=12&rs=1&o=6&dpr=1.3&pid=SANGAM","https://i.pinimg.com/736x/ff/f8/8e/fff88e31667e244c2301a484135fbbbe.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 13,
        "name": "Hrithik Roshan",
        "age": 50,
        "profession": "Actor & Dancer",
        "interests": ["Workout", "Photography", "Adventure"],
        "gallery": ["https://th.bing.com/th/id/OIP.p-z7HFE4nE5zQWccL8iY5AHaFj?w=252&h=189&c=7&r=0&o=5&cb=iwc2&dpr=1.3&pid=1.7","https://i.pinimg.com/736x/66/8f/00/668f00782d609e2490e47ca22987c11d.jpg"],
        "hasLikedYou": False
    },
    {
        "id": 14,
        "name": "Nayanthara",
        "age": 39,
        "profession": "Actress & Entrepreneur",
        "interests": ["Interior Design", "Temple Visits", "Fitness"],
        "gallery": ["https://th.bing.com/th/id/OSK.HEROBgNSw6d0UDFsVMOGGBdh-MUjP-ENtZb6W-yD1Knp4zM?w=312&h=200&c=7&rs=1&o=6&dpr=1.3&pid=SANGAM","https://i.pinimg.com/736x/80/8f/0c/808f0c8fe6d7ea90635d699eac510c36.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 15,
        "name": "Ranveer Singh",
        "age": 39,
        "profession": "Actor & Performer",
        "interests": ["Fashion", "Rapping", "Collecting Sneakers"],
        "gallery": ["https://th.bing.com/th/id/OIP.He7SmDzn5ecsauAQFDMJzwHaEK?w=327&h=183&c=7&r=0&o=5&cb=iwc2&dpr=1.3&pid=1.7","https://i.pinimg.com/736x/9f/11/98/9f1198d1b64c3ab1a1df4f26060226db.jpg"],
        "hasLikedYou": True
    },
    {
        "id": 16,
        "name": "Kiara Advani",
        "age": 33,
        "profession": "Actress",
        "interests": ["Art", "Baking", "Spirituality"],
        "gallery": ["https://th.bing.com/th?id=OIF.B07pgrdflYfWDQcHCi%2blNw&w=305&h=180&c=7&r=0&o=5&cb=iwc2&dpr=1.3&pid=1.7","https://i.pinimg.com/736x/1c/c5/6d/1cc56d8f2cb9a9dd546e2bba02b67ab0.jpg"],
        "hasLikedYou": False
    },
    {
        "id": 17,
        "name": "Yash",
        "age": 38,
        "profession": "Actor",
        "interests": ["Fitness", "Motorbikes", "Nature Retreats"],
        "gallery": ["https://i.pinimg.com/736x/a2/03/f0/a203f00bafe49cbee77e453fdef354d5.jpg","https://i.pinimg.com/736x/84/4a/95/844a951999ba5f31e643033583646877.jpg"],
        "hasLikedYou": True
    }
]

# Initialize session state
if 'gender_preference' not in st.session_state:
    st.session_state.gender_preference = "Both"
if 'matches' not in st.session_state:
    st.session_state.matches = []
if 'all_viewed' not in st.session_state:
    st.session_state.all_viewed = False
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'current_image_index' not in st.session_state:
    st.session_state.current_image_index = 0

st.set_page_config(page_title="SaSu - Matchmaking App", layout="centered")
# Gender mapping
gender_map = {
    "Ram Charan": "Boy",
    "Prabhas": "Boy",
    "Allu Arjun": "Boy",
    "N.T. Rama Rao Jr.": "Boy",
    "Virat Kohli": "Boy",
    "Mahesh Babu": "Boy",
    "Hrithik Roshan": "Boy",
    "Ranveer Singh": "Boy",
    "Yash": "Boy",
    "Samantha Ruth": "Girl",
    "Rashmika Mandanna": "Girl",
    "Pooja Hegde": "Girl",
    "Deepika Padukone": "Girl",
    "Alia Bhatt": "Girl",
    "Kriti Sanon": "Girl",
    "Nayanthara": "Girl",
    "Kiara Advani": "Girl"
}

# Filter profiles based on gender preference
def get_filtered_profiles():
    if st.session_state.gender_preference == "Boy":
        return [p for p in profiles if gender_map.get(p["name"], "") == "Boy"]
    elif st.session_state.gender_preference == "Girl":
        return [p for p in profiles if gender_map.get(p["name"], "") == "Girl"]
    return profiles

# UI Components
st.markdown("""
<style>
    .profile-image {
        width: 100%;
        max-height: 400px;
        object-fit: contain;
        margin: 0 auto;
        display: block;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .gender-buttons {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-bottom: 15px;
    }
    
    .action-section {
        position: sticky;
        bottom: 0;
        background: white;
        padding: 15px 0;
        border-top: 1px solid #f0f0f0;
        margin-top: 20px;
    }
    
    .gallery-dots {
        display: flex;
        justify-content: center;
        margin: 10px 0;
    }
    .dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #ccc;
        margin: 0 5px;
    }
    .dot.active {
        background: #6a1b9a;
    }
    
    .profile-info {
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#6a1b9a; margin-bottom: 20px;">SaSu – Because Mom Knows Best</h1>', 
            unsafe_allow_html=True)

# Gender selection - buttons closer together
st.markdown('<div class="gender-buttons">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,1,1])
with col1: 
    if st.button("👦 Boys"):
        st.session_state.update({
            "gender_preference": "Boy",
            "all_viewed": False,
            "matches": [],
            "current_index": 0,
            "current_image_index": 0
        })
        st.rerun()
with col2: 
    if st.button("👧 Girls"):
        st.session_state.update({
            "gender_preference": "Girl",
            "all_viewed": False,
            "matches": [],
            "current_index": 0,
            "current_image_index": 0
        })
        st.rerun()
with col3: 
    if st.button("🤝 Both"):
        st.session_state.update({
            "gender_preference": "Both",
            "all_viewed": False,
            "matches": [],
            "current_index": 0,
            "current_image_index": 0
        })
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"<p style='text-align:center; color:#6a1b9a;'>Current selection: {st.session_state.gender_preference}</p>", 
            unsafe_allow_html=True)

# Get filtered profiles
filtered_profiles = get_filtered_profiles()

# Main profile display
if st.session_state.all_viewed:
    st.subheader("🌟 Potential Matches")
    if not st.session_state.matches:
        st.write("No matches found yet. Keep trying!")
    else:
        st.write("These families have shown interest in your child:")
        cols = st.columns(3)
        for idx, match in enumerate(st.session_state.matches):
            with cols[idx % 3]:
                st.image(match['gallery'][0], use_container_width=True)
                st.markdown(f"""
                **{match['name']}, {match['age']}**  
                *{match['profession']}*  
                Interests: {", ".join(match['interests'])}
                """)
    if st.button("Start Over"):
        st.session_state.update({
            "all_viewed": False,
            "matches": [],
            "current_index": 0,
            "current_image_index": 0
        })
        st.rerun()
else:
    if st.session_state.current_index >= len(filtered_profiles):
        st.session_state.all_viewed = True
        st.rerun()
    
    current_profile = filtered_profiles[st.session_state.current_index]
    
    # Perfectly sized profile image
    st.markdown(f"""
    <img src="{current_profile['gallery'][st.session_state.current_image_index]}" 
         class="profile-image" 
         alt="{current_profile['name']}'s profile photo">
    """, unsafe_allow_html=True)
    
    # Gallery dots
    dots_html = "<div class='gallery-dots'>"
    for i in range(len(current_profile['gallery'])):
        active = "active" if i == st.session_state.current_image_index else ""
        dots_html += f"<span class='dot {active}'></span>"
    dots_html += "</div>"
    st.markdown(dots_html, unsafe_allow_html=True)
    
    # Profile info
    st.markdown(f"""
    <div class="profile-info">
        <h3>{current_profile['name']}, {current_profile['age']}</h3>
        <p><em>{current_profile['profession']}</em></p>
        <p><strong>Interests:</strong> {", ".join(current_profile['interests'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Photo navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Previous Photo", use_container_width=True):
            st.session_state.current_image_index = (
                st.session_state.current_image_index - 1) % len(current_profile['gallery'])
            st.rerun()
    with col2:
        if st.button("Next Photo →", use_container_width=True):
            st.session_state.current_image_index = (
                st.session_state.current_image_index + 1) % len(current_profile['gallery'])
            st.rerun()
    
    # Action buttons - perfectly positioned
    st.markdown('<div class="action-section">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✖ Not Interested", use_container_width=True):
            st.session_state.current_index += 1
            st.session_state.current_image_index = 0
            if st.session_state.current_index >= len(filtered_profiles):
                st.session_state.all_viewed = True
            st.rerun()
    with col2:
        if st.button("❤ Interested", use_container_width=True, type="primary"):
            if current_profile['hasLikedYou']:
                st.session_state.matches.append(current_profile)
                st.success(f"Potential match! The family of {current_profile['name']} is also interested!")
            st.session_state.current_index += 1
            st.session_state.current_image_index = 0
            if st.session_state.current_index >= len(filtered_profiles):
                st.session_state.all_viewed = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
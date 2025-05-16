import streamlit as st
import streamlit.components.v1 as components
import json

if 'gender_preference' not in st.session_state:
    st.session_state.gender_preference = "Both"

# Full Profile List
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
        "gallery": ["https://studybymind.com/wp-content/uploads/2022/06/Yash-KGF-Actor-Biography-2.jpg","https://i.pinimg.com/736x/84/4a/95/844a951999ba5f31e643033583646877.jpg"],
        "hasLikedYou": True
    }

]


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

if st.session_state.gender_preference == "Boy":
    filtered_profiles = [p for p in profiles if gender_map.get(p["name"], "") == "Boy"]
elif st.session_state.gender_preference == "Girl":
    filtered_profiles = [p for p in profiles if gender_map.get(p["name"], "") == "Girl"]
else:
    filtered_profiles = profiles

js_profiles = json.dumps(filtered_profiles)

# App UI
st.set_page_config(page_title="SaSu - Matchmaking App", layout="centered")
st.markdown("""
    <h1 style="text-align:center; color:#6a1b9a;">SaSu – Because Mom Knows Best</h1>
    <style>
    .stButton > button {
        transition: all 0.3s ease;
        border: 2px solid #6a1b9a !important;
        color: #6a1b9a !important;
        background-color: white !important;
    }
    .stButton > button:focus {
        background-color: #6a1b9a !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Gender selection buttons
col1, col2, col3 = st.columns(3)
with col1: st.button("👦 Boy", on_click=lambda: st.session_state.update(gender_preference="Boy"))
with col2: st.button("👧 Girl", on_click=lambda: st.session_state.update(gender_preference="Girl"))
with col3: st.button("🤝 Both", on_click=lambda: st.session_state.update(gender_preference="Both"))

st.markdown(f"<p style='text-align:center; color:#6a1b9a;'>Current selection: {st.session_state.gender_preference}</p>", 
            unsafe_allow_html=True)

# HTML Component
components.html(f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    margin: 0;
    padding: 0;
    background-color: #f0f0f5;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}}

.wrapper {{
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 20px 0;
}}

.profile-card {{
    width: 350px;
    border-radius: 15px;
    background: #fff;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    overflow: hidden;
    margin: 0 auto;
}}

.gallery-container {{
    position: relative;
    height: 400px;
    overflow: visible;  /* CHANGED FROM hidden */
}}

.gallery-image {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: opacity 0.3s;
}}

.navigation-arrows {{
    position: absolute;
    top: 50%;
    width: 100%;
    transform: translateY(-50%);
    display: flex;
    justify-content: space-between;
    padding: 0 15px;
    box-sizing: border-box; /* Crucial fix */
}}

.arrow {{
    font-family: Arial, sans-serif; /* Better symbol rendering */
    font-size: 28px; /* Larger size */
    padding-bottom: 3px; /* Visual alignment */
}}


.dots-container {{
    position: absolute;
    bottom: 15px;
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 8px;
    z-index: 2;
}}

.dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(255,255,255,0.5);
    cursor: pointer;
    transition: all 0.3s;
}}

.dot.active {{
    background: white;
    transform: scale(1.2);
}}

.profile-info {{
    padding: 20px;
    text-align: center;
}}

.profile-info h2 {{
    margin: 0;
    color: #6a1b9a;
}}

.profile-info p {{
    margin: 5px 0 15px 0;
    color: #444;
}}

.interests {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
}}

.interest-tag {{
    background-color: #ba68c8;
    color: white;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 0.85em;
}}

.buttons {{
    text-align: center;
    margin: 15px 0;
}}

button {{
    font-size: 30px;
    background: none;
    border: none;
    margin: 0 25px;
    cursor: pointer;
}}

.match {{
    display: none;
    text-align: center;
    font-size: 18px;
    background: #c8e6c9;
    padding: 10px;
    margin: 10px 20px;
    border-radius: 12px;
    font-weight: bold;
    color: #2e7d32;
}}
.end-screen {{
    width: 100%;
    height: 100%;
    padding: 20px;
    text-align: center;
    display: none;
    flex-direction: column;
    align-items: center;
}}

.matches-container {{
    width: 100%;
    height: 80vh;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}}

.match-profile {{
    width: 250px;
    background: white;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    margin: 10px;
    flex-shrink: 0;
}}

.match-profile img {{
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 5px;
    margin-bottom: 10px;
}}
                

</style>
</head>
<body>
    <div class="wrapper">
        <div class="profile-card">
            <div class="gallery-container">
                <div class="navigation-arrows">
                    <div class="arrow" onclick="previousImage()">‹</div>
                    <div class="arrow" onclick="nextImage()">›</div>
                </div>
                <div class="dots-container" id="dots-container"></div>
                <img class="gallery-image" id="current-image" src="">
            </div>
            <div class="profile-info">
                <h2 id="profile-name"></h2>
                <p id="profile-profession"></p>
                <div class="interests" id="profile-interests"></div>
            </div>
            <div class="buttons">
                <button onclick="handleDislike()">👎</button>
                <button onclick="handleLike()">❤️</button>
            </div>
            <div class="match" id="match">🎉 It's a Match!</div>
        </div>
        <div class="end-screen" id="end-screen">
            <h2 style="color:#6a1b9a; margin-bottom: 30px;">🌟 Potential Matches 🌟</h2>
            <div class="matches-container" id="mutual-matches"></div>
        </div>
    </div>

<script>
const profiles = {js_profiles};
let currentIndex = 0;
let currentImageIndex = 0;
let viewedProfiles = new Set();
let userLikes = [];

function updateGallery() {{
    const profile = profiles[currentIndex];
    document.getElementById('current-image').src = profile.gallery[currentImageIndex];
    
    const dotsContainer = document.getElementById('dots-container');
    dotsContainer.innerHTML = profile.gallery.map((_, i) => 
        `<div class="dot ${{i === currentImageIndex ? 'active' : ''}}" 
              onclick="changeImage(${{i}})"></div>`
    ).join('');
}}

function loadProfile() {{
    currentImageIndex = 0;
    const profile = profiles[currentIndex];
    
    document.getElementById('current-image').src = profile.gallery[0];
    document.getElementById('profile-name').textContent = profile.name + ', ' + profile.age;
    document.getElementById('profile-profession').textContent = profile.profession;
    
    document.getElementById('profile-interests').innerHTML = 
        profile.interests.map(i => `<span class="interest-tag">${{i}}</span>`).join('');
    
    document.getElementById('match').style.display = 'none';
    updateGallery();
}}

function nextImage() {{
    currentImageIndex = (currentImageIndex + 1) % profiles[currentIndex].gallery.length;
    updateGallery();
}}

function previousImage() {{
    currentImageIndex = (currentImageIndex - 1 + profiles[currentIndex].gallery.length) % 
                       profiles[currentIndex].gallery.length;
    updateGallery();
}}

function changeImage(index) {{
    currentImageIndex = index;
    updateGallery();
}}

function handleLike() {{
    const profile = profiles[currentIndex];
    viewedProfiles.add(profile.id);
    userLikes.push(profile.id);
    
    if(profile.hasLikedYou) {{
        document.getElementById('match').style.display = 'block';
    }}
    currentIndex = (currentIndex + 1) % profiles.length;
    setTimeout(() => {{
        loadProfile();
        checkEnd();
    }}, 600);
}}

function handleDislike() {{
    const profile = profiles[currentIndex];
    viewedProfiles.add(profile.id);
    currentIndex = (currentIndex + 1) % profiles.length;
    loadProfile();
    checkEnd();
}}
function checkEnd() {{
    if (viewedProfiles.size >= profiles.length) {{
        document.querySelector('.profile-card').style.display = 'none';
        document.getElementById('end-screen').style.display = 'block';
        showMutualMatches();
    }}
}}

function showMutualMatches() {{
    const mutualMatches = profiles.filter(p => 
        p.hasLikedYou && userLikes.includes(p.id)
    );
    
    const container = document.getElementById('mutual-matches');
    container.innerHTML = mutualMatches.map(p => `
        <div class="match-profile">
            <img src="${{p.gallery[0]}}">
            <h3>${{p.name}}, ${{p.age}}</h3>
            <p>${{p.profession}}</p>
            <div class="interests" style="margin-top: 10px;">
                ${{p.interests.map(i => `<span class="interest-tag">${{i}}</span>`).join('')}}
            </div>
        </div>
    `).join('');
}}

loadProfile();
</script>
</body>
</html>
""", height=780, scrolling=False)
